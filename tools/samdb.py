#!/usr/bin/env python3
"""
samdb.py, the local opportunity database for the GovCon Starter Kit.

Why this exists. The SAM.gov Get Opportunities API is rate limited hard. The published
non-federal tiers are 10 requests in 24 hours without an entity role and 1,000 requests in
24 hours with one. Searching live against the lower tier is not workable, so this script
keeps a local copy: one small sync, then search offline as often as you like.

What it is not. It mirrors opportunity NOTICES. It does not download attachments,
statements of work, or amendment documents. Those still come from SAM.gov itself.

Design constraints, on purpose:
  - Python 3 standard library only. No pip install. The audience is not technical.
  - One SQLite file at data/sam.db. No server.
  - The SAM.gov public API key is loaded inside this process, from company/.env.local, and is
    never written to the database, to a log, to a filename, or to standard output.
  - Every SQL statement is parameterised. Search terms come from user input.

Commands:
  init      create the database and the schema
  status    what is in the database, how old it is, and what it covers
  sync      pull what is new since the last successful sync, one or two calls on a normal day
  backfill  resumable historical load, chunked and rate aware
  search    search the local database, no network call, ever
  changes   what changed, which is the thing the API itself cannot give you
  describe  fetch the full description text for one notice, one API call

Run any command with -h for its options.
"""

from __future__ import print_function

import sys

if sys.version_info < (3, 8):
    print("This script needs Python 3.8 or newer. You are running "
          + ".".join(str(n) for n in sys.version_info[:3]) + ".")
    print("Next action: install Python 3 from https://www.python.org/downloads/ "
          "and run this command again.")
    sys.exit(2)

import argparse
import hashlib
import json
import os
import re
import sqlite3
import stat
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

API_SEARCH = "https://api.sam.gov/opportunities/v2/search"
API_DESCRIPTION = "https://api.sam.gov/prod/opportunities/v1/noticedesc"

# The API caps a single call at 1,000 records and caps postedFrom to postedTo at one year.
MAX_RECORDS_PER_CALL = 1000
MAX_WINDOW_DAYS = 365

# Fields compared between one sync and the next. A change in any of these is a real change
# in the notice, and each one gets a row in the changes table.
TRACKED_FIELDS = [
    "solicitation_number",
    "title",
    "agency_path",
    "naics",
    "classification_code",
    "set_aside_code",
    "set_aside_description",
    "notice_type",
    "base_type",
    "posted_date",
    "response_deadline_raw",
    "archive_type",
    "archive_date",
    "active",
    "pop_city",
    "pop_state",
    "pop_zip",
    "pop_country",
    "contract_type",
    "award_number",
    "award_amount",
    "award_date",
    "awardee_name",
    "link",
]

# Columns written on every upsert, tracked plus derived.
DERIVED_FIELDS = [
    "department",
    "sub_agency",
    "office",
    "response_deadline_date",
    "response_deadline_time",
    "response_deadline_zone",
    "description_url",
]

CHANGE_KIND = {
    "response_deadline_raw": "deadline_moved",
    "set_aside_code": "set_aside_changed",
    "set_aside_description": "set_aside_changed",
    "notice_type": "type_changed",
    "base_type": "type_changed",
    "naics": "naics_changed",
    "title": "title_changed",
    "pop_city": "place_changed",
    "pop_state": "place_changed",
    "pop_zip": "place_changed",
    "pop_country": "place_changed",
    "award_number": "award_recorded",
    "award_amount": "award_recorded",
    "award_date": "award_recorded",
    "awardee_name": "award_recorded",
    "link": "link_changed",
    "archive_type": "archive_changed",
    "archive_date": "archive_changed",
    "posted_date": "reposted",
}

KIND_LABEL = {
    "new": "new notices",
    "deadline_moved": "response deadline changed",
    "set_aside_changed": "set-aside changed",
    "cancelled": "cancelled or made inactive",
    "reappeared": "made active again",
    "type_changed": "notice type changed",
    "naics_changed": "NAICS changed",
    "title_changed": "title changed",
    "place_changed": "place of performance changed",
    "award_recorded": "award recorded",
    "link_changed": "link changed",
    "archive_changed": "archive date or type changed",
    "reposted": "posted date changed",
    "field_changed": "other field changed",
}

SCHEMA = """
CREATE TABLE IF NOT EXISTS opportunities (
    notice_id               TEXT PRIMARY KEY,
    solicitation_number     TEXT,
    title                   TEXT,
    agency_path             TEXT,
    department              TEXT,
    sub_agency              TEXT,
    office                  TEXT,
    naics                   TEXT,
    classification_code     TEXT,
    set_aside_code          TEXT,
    set_aside_description   TEXT,
    notice_type             TEXT,
    base_type               TEXT,
    posted_date             TEXT,
    response_deadline_raw   TEXT,
    response_deadline_date  TEXT,
    response_deadline_time  TEXT,
    response_deadline_zone  TEXT,
    archive_type            TEXT,
    archive_date            TEXT,
    active                  TEXT,
    pop_city                TEXT,
    pop_state               TEXT,
    pop_zip                 TEXT,
    pop_country             TEXT,
    contract_type           TEXT,
    award_number            TEXT,
    award_amount            TEXT,
    award_date              TEXT,
    awardee_name            TEXT,
    link                    TEXT,
    description_url         TEXT,
    description             TEXT,
    description_fetched_utc TEXT,
    first_seen_utc          TEXT NOT NULL,
    last_seen_utc           TEXT NOT NULL,
    last_changed_utc        TEXT,
    content_hash            TEXT NOT NULL,
    raw_json                TEXT
);

CREATE INDEX IF NOT EXISTS idx_opp_naics    ON opportunities (naics);
CREATE INDEX IF NOT EXISTS idx_opp_deadline ON opportunities (response_deadline_date);
CREATE INDEX IF NOT EXISTS idx_opp_posted   ON opportunities (posted_date);
CREATE INDEX IF NOT EXISTS idx_opp_setaside ON opportunities (set_aside_code);
CREATE INDEX IF NOT EXISTS idx_opp_state    ON opportunities (pop_state);

-- What each notice looked like on each sync date. content_hash is written every time the
-- notice is seen. payload holds the full picture only when it differs from the previous
-- snapshot, so a year of daily syncs does not turn into a gigabyte of identical copies.
-- To read a notice as it stood on a date, take the most recent snapshot on or before that
-- date whose payload is not null.
CREATE TABLE IF NOT EXISTS snapshots (
    snapshot_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    notice_id     TEXT NOT NULL,
    sync_date     TEXT NOT NULL,
    captured_utc  TEXT NOT NULL,
    content_hash  TEXT NOT NULL,
    payload       TEXT,
    UNIQUE (notice_id, sync_date)
);

CREATE INDEX IF NOT EXISTS idx_snap_notice ON snapshots (notice_id, sync_date);

-- The change history. The API only ever returns the latest active version of a notice, so
-- nobody calling it can see what moved. Because this database snapshots on every sync, it
-- accumulates the history the API cannot give you.
CREATE TABLE IF NOT EXISTS changes (
    change_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    notice_id     TEXT NOT NULL,
    detected_utc  TEXT NOT NULL,
    sync_date     TEXT NOT NULL,
    kind          TEXT NOT NULL,
    field         TEXT,
    old_value     TEXT,
    new_value     TEXT
);

CREATE INDEX IF NOT EXISTS idx_changes_notice ON changes (notice_id);
CREATE INDEX IF NOT EXISTS idx_changes_date   ON changes (sync_date);
CREATE INDEX IF NOT EXISTS idx_changes_kind   ON changes (kind);

-- The last successful sync window, the last run time, and the saved backfill plan.
CREATE TABLE IF NOT EXISTS sync_state (
    key          TEXT PRIMARY KEY,
    value        TEXT NOT NULL,
    updated_utc  TEXT NOT NULL
);

-- What the database actually knows about. Coverage equals whatever filters were synced.
CREATE TABLE IF NOT EXISTS coverage (
    filter_kind      TEXT NOT NULL,
    filter_value     TEXT NOT NULL,
    earliest_posted  TEXT,
    latest_posted    TEXT,
    last_synced_utc  TEXT,
    PRIMARY KEY (filter_kind, filter_value)
);

-- Every API call this folder made, so the rate limit can be reported honestly. The URL and
-- the parameters are stored with the api_key removed before they reach this table.
CREATE TABLE IF NOT EXISTS api_calls (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    called_utc   TEXT NOT NULL,
    call_date    TEXT NOT NULL,
    endpoint     TEXT NOT NULL,
    params       TEXT NOT NULL,
    http_status  INTEGER,
    records      INTEGER,
    outcome      TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_calls_date ON api_calls (call_date, outcome);
"""


class KitError(Exception):
    """An error with one clear next action for the user."""

    def __init__(self, message, next_action=None, code=1):
        Exception.__init__(self, message)
        self.message = message
        self.next_action = next_action
        self.code = code


class RateLimited(KitError):
    """A refused request, plus any complete pages already read by the current pull."""

    def __init__(self, message, next_action=None, code=3):
        KitError.__init__(self, message, next_action, code)
        self.records = []
        self.calls_used = 0
        self.next_offset = 0


# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------

def require_positive_daily_limit(args):
    if args.daily_limit < 1:
        raise KitError(
            "--daily-limit must be at least 1.",
            "Run the command again with --daily-limit 10, or with the positive limit "
            "shown for your SAM.gov API key.",
            code=2)


def positive_int(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return number

def now_utc():
    return datetime.now(timezone.utc)


def now_utc_iso():
    return now_utc().strftime("%Y-%m-%dT%H:%M:%SZ")


def today_utc():
    return now_utc().strftime("%Y-%m-%d")


def parse_date(text):
    return datetime.strptime(text, "%Y-%m-%d").date()


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def default_db_path():
    return os.path.join(repo_root(), "data", "sam.db")


def mmddyyyy(d):
    return d.strftime("%m/%d/%Y")


def scrub(text, key):
    """Remove the api key from anything about to be printed or stored."""
    if not text:
        return text
    text = str(text)
    if key:
        text = text.replace(key, "REDACTED")
    # Belt and braces: strip any api_key parameter that got into a string another way.
    text = re.sub(r"(api_key=)[^&\s\"']+", r"\1REDACTED", text)
    return text


def redact_params(params):
    out = {}
    for name, value in params.items():
        if name.lower() in ("api_key", "apikey"):
            continue
        out[name] = value
    return out


def say(line=""):
    sys.stdout.write(line + "\n")


# ---------------------------------------------------------------------------
# the key
# ---------------------------------------------------------------------------

def load_key(root):
    """Read SAM_API_KEY from company/.env.local. Returns the key or raises.

    The key is returned into this process only. It is never printed, never stored, and
    never passed to anything that writes to disk.
    """
    path = os.path.join(root, "company", ".env.local")
    if not os.path.exists(path):
        raise KitError(
            "No SAM.gov public API key file exists at company/.env.local, so there is "
            "nothing to call the API with.",
            "Sign in at https://sam.gov, open Account Details, request a Public API Key, copy "
            "company/.env.local.example to company/.env.local, and paste the key after "
            "SAM_API_KEY= . Then run this again.",
            code=4,
        )
    key = ""
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            line = line.strip()
            if line.startswith("#") or "=" not in line:
                continue
            name, _, value = line.partition("=")
            if name.strip() == "SAM_API_KEY":
                key = value.strip().strip('"').strip("'")
    if not key:
        raise KitError(
            "company/.env.local exists but SAM_API_KEY is empty.",
            "Open company/.env.local in a text editor and paste your key after "
            "SAM_API_KEY= , with no quotes and no spaces. Then run this again.",
            code=4,
        )
    return key


# ---------------------------------------------------------------------------
# database
# ---------------------------------------------------------------------------

def set_restrictive_permissions(path):
    """Owner read and write only, where the platform supports it.

    Returns a plain sentence describing exactly what was done, so the kit can report it
    rather than claim it.
    """
    try:
        os.chmod(path, stat.S_IRUSR | stat.S_IWUSR)
    except OSError as exc:
        return "Could not set file permissions on " + path + ": " + str(exc)
    if os.name == "nt":
        return ("File permissions: os.chmod was called with owner read and write. On Windows "
                "that only controls the read-only attribute; access is governed by the folder "
                "ACL, so the file is as private as the folder you unzipped. To lock it "
                "further, use icacls yourself.")
    mode = stat.S_IMODE(os.stat(path).st_mode)
    return "File permissions: set to %o, owner read and write only." % mode


def open_db(path, create=True):
    folder = os.path.dirname(os.path.abspath(path))
    if create and folder and not os.path.isdir(folder):
        os.makedirs(folder)
    existed = os.path.exists(path)
    if not existed and not create:
        raise KitError(
            "No local database at " + path + " yet.",
            "Run /sync to build it, or /backfill to load history first.",
            code=5,
        )
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    conn.commit()
    if not existed:
        set_restrictive_permissions(path)
    return conn


def get_state(conn, key, default=None):
    row = conn.execute("SELECT value FROM sync_state WHERE key = ?", (key,)).fetchone()
    return row["value"] if row else default


def set_state(conn, key, value):
    conn.execute(
        "INSERT INTO sync_state (key, value, updated_utc) VALUES (?, ?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value = excluded.value, "
        "updated_utc = excluded.updated_utc",
        (key, str(value), now_utc_iso()),
    )


def calls_last_24_hours(conn):
    cutoff = (now_utc() - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")
    row = conn.execute(
        "SELECT COUNT(*) AS n FROM api_calls WHERE called_utc >= ? AND outcome != 'fixture'",
        (cutoff,),
    ).fetchone()
    return int(row["n"])


def record_call(conn, endpoint, params, status, records, outcome):
    conn.execute(
        "INSERT INTO api_calls (called_utc, call_date, endpoint, params, http_status, "
        "records, outcome) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (now_utc_iso(), today_utc(), endpoint,
         json.dumps(redact_params(params), sort_keys=True), status, records, outcome),
    )


def note_coverage(conn, kind, value, posted_from, posted_to):
    row = conn.execute(
        "SELECT earliest_posted, latest_posted FROM coverage WHERE filter_kind = ? "
        "AND filter_value = ?", (kind, value)).fetchone()
    earliest = posted_from
    latest = posted_to
    if row:
        if row["earliest_posted"] and row["earliest_posted"] < earliest:
            earliest = row["earliest_posted"]
        if row["latest_posted"] and row["latest_posted"] > latest:
            latest = row["latest_posted"]
    conn.execute(
        "INSERT INTO coverage (filter_kind, filter_value, earliest_posted, latest_posted, "
        "last_synced_utc) VALUES (?, ?, ?, ?, ?) "
        "ON CONFLICT(filter_kind, filter_value) DO UPDATE SET "
        "earliest_posted = excluded.earliest_posted, latest_posted = excluded.latest_posted, "
        "last_synced_utc = excluded.last_synced_utc",
        (kind, value, earliest, latest, now_utc_iso()),
    )


def note_completed_query_coverage(conn, naics, set_aside, posted_from, posted_to):
    """Record only a filter combination whose entire date window finished."""
    if set_aside:
        note_coverage(conn, "query", "NAICS %s; set-aside %s" % (naics, set_aside),
                      posted_from, posted_to)
    else:
        note_coverage(conn, "naics", naics, posted_from, posted_to)


# ---------------------------------------------------------------------------
# the profile
# ---------------------------------------------------------------------------

def parse_profile(root, path=None):
    """Pull the NAICS codes, and set-aside codes if the owner listed them, from the profile.

    NAICS codes are read from the first column of the NAICS table. Set-aside API codes are
    read only from an explicit line, because the profile states set-aside status in prose and
    guessing an API code from prose is how a search quietly returns the wrong thing.
    """
    profile_path = path or os.path.join(root, "company", "profile.md")
    if not os.path.exists(profile_path):
        return {"path": profile_path, "exists": False, "naics": [], "set_asides": []}
    with open(profile_path, "r", encoding="utf-8", errors="replace") as handle:
        text = handle.read()

    naics = []
    for line in text.splitlines():
        match = re.match(r"^\s*\|\s*(\d{6})\s*\|", line)
        if match and match.group(1) not in naics:
            naics.append(match.group(1))

    set_asides = []
    for line in text.splitlines():
        match = re.match(r"^\s*SAM set-aside codes:\s*(.+)$", line, re.IGNORECASE)
        if match:
            for token in re.split(r"[,\s]+", match.group(1)):
                token = token.strip().upper()
                if token and token not in set_asides:
                    set_asides.append(token)
    return {"path": profile_path, "exists": True, "naics": naics, "set_asides": set_asides}


# ---------------------------------------------------------------------------
# the API
# ---------------------------------------------------------------------------

def read_fixture(fixture, page_index):
    """Read a canned response instead of calling the API.

    A fixture is either a single JSON file or a folder holding page-0.json, page-1.json and
    so on. A fixture may carry "__http_status" to rehearse an error, for example a 429, so
    the rate limit path can be proved without a key and without a live call.
    """
    if os.path.isdir(fixture):
        candidate = os.path.join(fixture, "page-%d.json" % page_index)
        if not os.path.exists(candidate):
            raise KitError(
                "Fixture folder " + fixture + " has no page-%d.json ." % page_index,
                "Add that file, or lower the number of pages the fixture is meant to serve.",
            )
        path = candidate
    else:
        path = fixture
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def api_get(conn, url, params, key, timeout=60, fixture=None, page_index=0):
    """One API call. Returns the parsed JSON body.

    Never retries. On a rate limit or a quota error it raises RateLimited with what the API
    actually said, and the caller stops.
    """
    endpoint = url
    if fixture:
        body = read_fixture(fixture, page_index)
        status = int(body.pop("__http_status", 200))
        if status != 200:
            record_call(conn, endpoint, params, status, 0, "fixture")
            conn.commit()
            raise_for_status(status, body, conn, endpoint, params, fixture=True)
        record_call(conn, endpoint, params, status, len(body.get("opportunitiesData") or []),
                    "fixture")
        conn.commit()
        return body

    query = dict(params)
    query["api_key"] = key
    full = url + "?" + urllib.parse.urlencode(query)
    request = urllib.request.Request(full, headers={
        "Accept": "application/json",
        "User-Agent": "govcon-starter-kit-samdb/1.0",
    })
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8", errors="replace")
            body = json.loads(raw) if raw.strip() else {}
            record_call(conn, endpoint, params, response.status,
                        len(body.get("opportunitiesData") or []), "ok")
            conn.commit()
            return body
    except urllib.error.HTTPError as exc:
        raw = ""
        try:
            raw = exc.read().decode("utf-8", errors="replace")
        except Exception:
            pass
        try:
            body = json.loads(raw) if raw.strip() else {}
        except ValueError:
            body = {"message": raw[:500]}
        record_call(conn, endpoint, params, exc.code, 0, "http_error")
        conn.commit()
        raise_for_status(exc.code, body, conn, endpoint, params, key=key)
    except urllib.error.URLError as exc:
        record_call(conn, endpoint, params, None, 0, "network_error")
        conn.commit()
        raise KitError(
            "Could not reach the SAM.gov API: " + scrub(str(exc.reason), key),
            "Check that this machine is online, then run the command again. Nothing was "
            "lost; the database still holds everything from earlier runs.",
            code=6,
        )
    except ValueError as exc:
        record_call(conn, endpoint, params, 200, 0, "bad_json")
        conn.commit()
        raise KitError(
            "The API replied with something that is not JSON: " + scrub(str(exc), key),
            "Run the command again once. If it repeats, check "
            "https://open.gsa.gov/api/get-opportunities-public-api/ for a change to the API.",
            code=6,
        )


def error_text(body):
    if not isinstance(body, dict):
        return str(body)[:400]
    error = body.get("error")
    if isinstance(error, dict):
        return "%s: %s" % (error.get("code", "error"), error.get("message", ""))
    for field in ("errorMessage", "message", "description", "detail"):
        if body.get(field):
            return str(body[field])[:400]
    return json.dumps(body)[:400]


def raise_for_status(status, body, conn, endpoint, params, key=None, fixture=False):
    detail = scrub(error_text(body), key)
    used = calls_last_24_hours(conn)
    if status == 429 or "RATE_LIMIT" in detail.upper() or "OVER_RATE" in detail.upper():
        raise RateLimited(
            "Rate limit reached. The API refused the call with HTTP %d and said: %s"
            % (status, detail),
            "Stop here. This folder has made %d API calls in the last 24 hours. This command "
            "does not retry. Backfill saves the refused page index. Sync keeps complete "
            "pages and safely repeats the unfinished filter window after the limit resets."
            % used,
            code=3,
        )
    if status in (401, 403):
        raise KitError(
            "The API rejected the key with HTTP %d and said: %s" % (status, detail),
            "Sign in at https://sam.gov, open Account Details, and check the Public API Key "
            "copied into company/.env.local. Keep spaces out of the value and do not paste "
            "the key into the chat.",
            code=4,
        )
    if status == 400:
        raise KitError(
            "The API rejected the request with HTTP 400 and said: %s" % detail,
            "One of the parameter names or values is wrong. Open "
            "https://open.gsa.gov/api/get-opportunities-public-api/ , compare the parameter "
            "names it lists today, and say plainly what changed.",
            code=6,
        )
    raise KitError(
        "The API returned HTTP %d and said: %s" % (status, detail),
        "Run the command again once. If it repeats, check "
        "https://open.gsa.gov/api/get-opportunities-public-api/ for a service notice.",
        code=6,
    )


# ---------------------------------------------------------------------------
# normalising one notice
# ---------------------------------------------------------------------------

def split_deadline(raw):
    """Split the stated deadline into date, time, and zone, without converting anything.

    Time zone conversion is not done here on purpose. The kit states a deadline exactly as
    the notice states it, and the owner confirms it on SAM.gov before bidding.
    """
    if not raw:
        return "", "", ""
    text = str(raw).strip()
    match = re.match(
        r"^(\d{4}-\d{2}-\d{2})[T ](\d{2}:\d{2}(?::\d{2})?)\s*([+-]\d{2}:?\d{2}|Z)?$", text)
    if match:
        return match.group(1), match.group(2), (match.group(3) or "")
    match = re.match(r"^(\d{4}-\d{2}-\d{2})$", text)
    if match:
        return match.group(1), "", ""
    return "", "", ""


def first_str(value, prefer=("code", "value", "name")):
    """Flatten one of the API's nested value shapes into a plain string.

    prefer decides which key wins. A place of performance city is wanted by name, a state by
    its two-letter code, so the caller says which.
    """
    if value is None:
        return ""
    if isinstance(value, list):
        for item in value:
            if isinstance(item, dict):
                for field in prefer:
                    if item.get(field):
                        return str(item[field])
            elif item:
                return str(item)
        return ""
    if isinstance(value, dict):
        for field in prefer:
            if value.get(field):
                return str(value[field])
        return ""
    return str(value)


def normalize(record):
    """Turn one API record into the columns this database keeps."""
    pop = record.get("placeOfPerformance") or {}
    award = record.get("award") or {}
    awardee = award.get("awardee") or {}

    path = record.get("fullParentPathName") or ""
    parts = [p.strip() for p in path.split(".") if p.strip()]
    department = parts[0] if parts else ""
    sub_agency = parts[1] if len(parts) > 1 else ""
    office = parts[-1] if len(parts) > 2 else ""

    naics = first_str(record.get("naicsCode"))
    if not naics:
        naics = first_str(record.get("naicsCodes"))

    deadline_raw = record.get("responseDeadLine") or ""
    d_date, d_time, d_zone = split_deadline(deadline_raw)

    description = record.get("description") or ""
    description_url = description if str(description).startswith("http") else ""

    row = {
        "notice_id": str(record.get("noticeId") or "").strip(),
        "solicitation_number": str(record.get("solicitationNumber") or ""),
        "title": str(record.get("title") or ""),
        "agency_path": path,
        "department": department,
        "sub_agency": sub_agency,
        "office": office,
        "naics": naics,
        "classification_code": str(record.get("classificationCode") or ""),
        # The current response table uses setAsideCode and setAside. Older examples and
        # stored fixtures use typeOfSetAside and typeOfSetAsideDescription. Accept both.
        "set_aside_code": str(record.get("setAsideCode") or
                              record.get("typeOfSetAside") or ""),
        "set_aside_description": str(record.get("setAside") or
                                     record.get("typeOfSetAsideDescription") or ""),
        "notice_type": str(record.get("type") or ""),
        "base_type": str(record.get("baseType") or ""),
        "posted_date": str(record.get("postedDate") or "")[:10],
        "response_deadline_raw": str(deadline_raw),
        "response_deadline_date": d_date,
        "response_deadline_time": d_time,
        "response_deadline_zone": d_zone,
        "archive_type": str(record.get("archiveType") or ""),
        "archive_date": str(record.get("archiveDate") or "")[:10],
        "active": str(record.get("active") or ""),
        "pop_city": first_str(pop.get("city"), prefer=("name", "value", "code")),
        "pop_state": first_str(pop.get("state"), prefer=("code", "value", "name")),
        "pop_zip": str(pop.get("zip") or ""),
        "pop_country": first_str(pop.get("country"), prefer=("code", "name", "value")),
        # The notice summary rarely states the contract type. It is kept where SAM gives it
        # and left empty otherwise, rather than inferred.
        "contract_type": str(record.get("contractType") or award.get("type") or ""),
        "award_number": str(award.get("number") or ""),
        "award_amount": str(award.get("amount") or ""),
        "award_date": str(award.get("date") or "")[:10],
        "awardee_name": str(awardee.get("name") or ""),
        "link": str(record.get("uiLink") or ""),
        "description_url": description_url,
    }
    return row


def content_hash(row):
    payload = json.dumps({field: row.get(field, "") for field in TRACKED_FIELDS},
                         sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def classify(field, old, new):
    if field == "active":
        if (old or "").lower().startswith("y") and (new or "").lower().startswith("n"):
            return "cancelled"
        if (old or "").lower().startswith("n") and (new or "").lower().startswith("y"):
            return "reappeared"
        return "field_changed"
    if field == "title":
        was = bool(re.search(r"cancel", old or "", re.IGNORECASE))
        now = bool(re.search(r"cancel", new or "", re.IGNORECASE))
        if now and not was:
            return "cancelled"
    return CHANGE_KIND.get(field, "field_changed")


def upsert(conn, row, raw_record, sync_date):
    """Insert or update one notice. Returns the list of change rows written."""
    notice_id = row["notice_id"]
    if not notice_id:
        return []
    digest = content_hash(row)
    stamp = now_utc_iso()
    existing = conn.execute(
        "SELECT * FROM opportunities WHERE notice_id = ?", (notice_id,)).fetchone()

    written = []
    if existing is None:
        columns = ["notice_id"] + TRACKED_FIELDS + DERIVED_FIELDS + [
            "first_seen_utc", "last_seen_utc", "last_changed_utc", "content_hash", "raw_json"]
        values = [row.get(name, "") for name in columns[:-5]]
        values += [stamp, stamp, stamp, digest,
                   json.dumps(raw_record, sort_keys=True, ensure_ascii=False)]
        placeholders = ",".join("?" * len(columns))
        conn.execute(
            "INSERT INTO opportunities (%s) VALUES (%s)" % (",".join(columns), placeholders),
            values)
        conn.execute(
            "INSERT INTO changes (notice_id, detected_utc, sync_date, kind, field, "
            "old_value, new_value) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (notice_id, stamp, sync_date, "new", None, None, row.get("title", "")))
        written.append({"kind": "new", "field": None, "old": None,
                        "new": row.get("title", ""), "notice_id": notice_id})
        write_snapshot(conn, notice_id, sync_date, digest, row, force_payload=True)
        return written

    if existing["content_hash"] == digest:
        conn.execute("UPDATE opportunities SET last_seen_utc = ? WHERE notice_id = ?",
                     (stamp, notice_id))
        write_snapshot(conn, notice_id, sync_date, digest, row, force_payload=False)
        return written

    for field in TRACKED_FIELDS:
        old = existing[field] if field in existing.keys() else None
        new = row.get(field, "")
        if (old or "") == (new or ""):
            continue
        kind = classify(field, old, new)
        conn.execute(
            "INSERT INTO changes (notice_id, detected_utc, sync_date, kind, field, "
            "old_value, new_value) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (notice_id, stamp, sync_date, kind, field, old, new))
        written.append({"kind": kind, "field": field, "old": old, "new": new,
                        "notice_id": notice_id})

    assignments = ", ".join("%s = ?" % name for name in TRACKED_FIELDS + DERIVED_FIELDS)
    values = [row.get(name, "") for name in TRACKED_FIELDS + DERIVED_FIELDS]
    values += [stamp, stamp, digest,
               json.dumps(raw_record, sort_keys=True, ensure_ascii=False), notice_id]
    conn.execute(
        "UPDATE opportunities SET " + assignments +
        ", last_seen_utc = ?, last_changed_utc = ?, content_hash = ?, raw_json = ? "
        "WHERE notice_id = ?", values)
    write_snapshot(conn, notice_id, sync_date, digest, row, force_payload=True)
    return written


def write_snapshot(conn, notice_id, sync_date, digest, row, force_payload):
    previous = conn.execute(
        "SELECT content_hash FROM snapshots WHERE notice_id = ? ORDER BY sync_date DESC, "
        "snapshot_id DESC LIMIT 1", (notice_id,)).fetchone()
    changed = force_payload or previous is None or previous["content_hash"] != digest
    payload = json.dumps({f: row.get(f, "") for f in TRACKED_FIELDS + DERIVED_FIELDS},
                         sort_keys=True, ensure_ascii=False) if changed else None
    conn.execute(
        "INSERT INTO snapshots (notice_id, sync_date, captured_utc, content_hash, payload) "
        "VALUES (?, ?, ?, ?, ?) ON CONFLICT(notice_id, sync_date) DO UPDATE SET "
        "content_hash = excluded.content_hash, "
        "payload = COALESCE(excluded.payload, snapshots.payload)",
        (notice_id, sync_date, now_utc_iso(), digest, payload))


# ---------------------------------------------------------------------------
# paging
# ---------------------------------------------------------------------------

def pull_window(conn, key, naics, set_aside, date_from, date_to, budget, args,
                start_offset=0):
    """Read one NAICS and date window, paging until it is exhausted or the budget runs out.

    Returns (records, calls_used, next_offset, complete).
    """
    records = []
    calls = 0
    offset = start_offset
    complete = False
    page_index = start_offset

    while True:
        if calls >= budget:
            break
        params = {
            "postedFrom": mmddyyyy(date_from),
            "postedTo": mmddyyyy(date_to),
            "limit": str(MAX_RECORDS_PER_CALL),
            "offset": str(offset),
        }
        if naics:
            params["ncode"] = naics
        if set_aside:
            params["typeOfSetAside"] = set_aside
        if args.notice_type:
            params["ptype"] = args.notice_type

        try:
            body = api_get(conn, API_SEARCH, params, key, timeout=args.timeout,
                           fixture=args.fixture, page_index=page_index)
        except RateLimited as exc:
            # The refused request is a real request attempt. Attach the successful pages so
            # the caller can persist them before it records the resume position.
            exc.records = list(records)
            exc.calls_used = calls + 1
            exc.next_offset = offset
            raise
        calls += 1
        page_index += 1
        page = body.get("opportunitiesData") or []
        total = int(body.get("totalRecords") or 0)
        records.extend(page)
        offset += 1
        if (not page or len(page) < MAX_RECORDS_PER_CALL or
                (total and offset * MAX_RECORDS_PER_CALL >= total)):
            complete = True
            break
    return records, calls, offset, complete


def apply_records(conn, records, sync_date):
    changes = []
    seen = 0
    for record in records:
        row = normalize(record)
        if not row["notice_id"]:
            continue
        seen += 1
        changes.extend(upsert(conn, row, record, sync_date))
    conn.commit()
    return seen, changes


# ---------------------------------------------------------------------------
# reporting helpers
# ---------------------------------------------------------------------------

def staleness(conn):
    last = get_state(conn, "last_sync_utc")
    if not last:
        return None, None
    try:
        when = datetime.strptime(last, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return last, None
    days = max(0, (now_utc() - when).days)
    return last, days


def coverage_lines(conn):
    rows = conn.execute(
        "SELECT filter_kind, filter_value, earliest_posted, latest_posted FROM coverage "
        "ORDER BY filter_kind, filter_value").fetchall()
    lines = []
    for row in rows:
        label = "NAICS" if row["filter_kind"] == "naics" else row["filter_kind"].title()
        lines.append("  %s %s, notices posted %s to %s" % (
            label, row["filter_value"], row["earliest_posted"] or "unknown",
            row["latest_posted"] or "unknown"))
    return lines


def freshness_banner(conn):
    last, days = staleness(conn)
    lines = []
    if last is None:
        lines.append("Local database: never synced. Everything below came from somewhere "
                     "other than a sync.")
    else:
        lines.append("Local database last synced %s, %s day(s) ago." % (last, days))
        if days is not None and days >= 3:
            lines.append("That is stale. Run /sync before you rely on any deadline below.")
    if get_state(conn, "last_sync_status") == "incomplete":
        attempt = get_state(conn, "last_sync_attempt_utc", "time not recorded")
        lines.append("The most recent sync attempt at %s did not finish. Complete pages were "
                     "kept, but they did not advance freshness or completed coverage."
                     % attempt)
    covered = coverage_lines(conn)
    if covered:
        lines.append("Completed coverage only. Partial pages may be stored, but do not extend "
                     "these ranges:")
        lines.extend(covered)
    else:
        lines.append("Coverage: nothing recorded yet.")
    return lines


CONFIRM_LINE = ("Confirm every deadline on SAM.gov itself before you rely on it to bid. This "
                "is a local mirror of notices, it can be stale, and SAM.gov is the "
                "authoritative record.")

FIXTURE_BANNER = ("Rehearsal against a local fixture file. No API call was made, nothing "
                  "counted against your 24-hour budget, and none of this came from SAM.gov.")

NOT_ATTACHMENTS_LINE = ("This database holds notices only. Attachments, statements of work, "
                        "and amendment documents are not here and still come from SAM.gov.")


# ---------------------------------------------------------------------------
# commands
# ---------------------------------------------------------------------------

def cmd_init(args):
    path = args.db
    conn = open_db(path)
    note = set_restrictive_permissions(path)
    say("Database ready at " + path)
    say(note)
    say("Tables: opportunities, snapshots, changes, sync_state, coverage, api_calls.")
    say("Next action: run /backfill to load history, or /sync to pull the last few days.")
    conn.close()
    return 0


def cmd_status(args):
    conn = open_db(args.db)
    path = os.path.abspath(args.db)
    size = os.path.getsize(path) if os.path.exists(path) else 0
    total = conn.execute("SELECT COUNT(*) AS n FROM opportunities").fetchone()["n"]
    active = conn.execute(
        "SELECT COUNT(*) AS n FROM opportunities WHERE LOWER(active) LIKE 'y%'"
    ).fetchone()["n"]
    snaps = conn.execute("SELECT COUNT(*) AS n FROM snapshots").fetchone()["n"]
    changed = conn.execute("SELECT COUNT(*) AS n FROM changes").fetchone()["n"]

    say("Local opportunity database")
    say("  File: " + path)
    say("  Size: %.1f KB" % (size / 1024.0))
    say("  Notices: %d, of which %d are marked active by SAM" % (total, active))
    say("  Snapshots: %d" % snaps)
    say("  Recorded changes: %d" % changed)
    say("")
    for line in freshness_banner(conn):
        say("  " + line)
    say("")
    say("  API calls made from this folder in the last 24 hours: %d"
        % calls_last_24_hours(conn))
    say("  That count is what this database recorded. It cannot see calls made with the "
        "same key from anywhere else.")

    plan_json = get_state(conn, "backfill_plan")
    if plan_json:
        plan = json.loads(plan_json)
        cursor = json.loads(get_state(conn, "backfill_cursor", '{"index": 0, "offset": 0}'))
        done = cursor.get("index", 0)
        say("  Backfill: chunk %d of %d done." % (done, len(plan)))
        if done < len(plan) and cursor.get("offset", 0):
            say("  Current chunk resumes at API page index %d." % cursor["offset"])
        if done >= len(plan):
            say("  Backfill is complete.")
    else:
        say("  Backfill: not started.")
    say("")
    say("  " + NOT_ATTACHMENTS_LINE)
    say("  " + CONFIRM_LINE)
    conn.close()
    return 0


def resolve_naics(conn, args, root):
    if args.naics:
        return list(args.naics)
    profile = parse_profile(root, args.profile)
    if profile["naics"]:
        return profile["naics"]
    if not profile["exists"]:
        raise KitError(
            "No NAICS codes to sync, and no company/profile.md to read them from.",
            "Run /setup-profile to build the profile, or pass the codes yourself with "
            "--naics 541519 --naics 541512 .",
            code=5,
        )
    raise KitError(
        "company/profile.md exists but no NAICS codes were found in it.",
        "Add your NAICS codes to the NAICS table in company/profile.md, or pass them with "
        "--naics 541519 .",
        code=5,
    )


def resolve_set_asides(args, root):
    if args.set_aside:
        return list(args.set_aside)
    profile = parse_profile(root, args.profile)
    return list(profile["set_asides"])


def cmd_sync(args):
    require_positive_daily_limit(args)
    root = repo_root()
    conn = open_db(args.db)
    naics_codes = resolve_naics(conn, args, root)
    set_asides = resolve_set_asides(args, root)
    sync_date = today_utc()

    last_to = get_state(conn, "last_sync_window_to")
    if last_to:
        start = parse_date(last_to) - timedelta(days=args.overlap_days)
    else:
        start = parse_date(sync_date) - timedelta(days=args.first_run_days)
    end = parse_date(sync_date)
    if (end - start).days > MAX_WINDOW_DAYS:
        start = end - timedelta(days=MAX_WINDOW_DAYS)

    combos = []
    for code in naics_codes:
        if set_asides:
            for set_aside in set_asides:
                combos.append((code, set_aside))
        else:
            combos.append((code, ""))

    used_recently = calls_last_24_hours(conn)
    budget = max(0, args.daily_limit - used_recently)
    if not args.fixture and budget <= 0:
        say("Nothing was called. This folder has already made %d API calls in the last 24 "
            "hours, which is the limit you told it about (%d)."
            % (used_recently, args.daily_limit))
        say("Next action: run /sync after the oldest call leaves the 24-hour window. The "
            "database still holds everything from earlier runs.")
        conn.close()
        return 3

    say("Sync window: notices posted %s to %s." % (start.isoformat(), end.isoformat()))
    say("Filters: NAICS " + ", ".join(naics_codes) +
        ("; set-aside " + ", ".join(set_asides) if set_asides else
         "; no set-aside filter, so every set-aside under those NAICS codes is pulled and "
         "the filtering happens locally at search time"))
    say("Planned calls: at least %d, one per filter combination, plus one more for each "
        "1,000 records beyond the first in any combination." % len(combos))
    if set_asides:
        say("Filtering by set-aside at the API costs one call per NAICS code per set-aside, "
            "so %d codes and %d set-asides is %d calls. Dropping the set-aside filter would "
            "cost %d calls and cover more, because every set-aside under those codes would "
            "come down and the filtering would happen locally at search time."
            % (len(naics_codes), len(set_asides), len(combos), len(naics_codes)))
    if args.fixture:
        say(FIXTURE_BANNER)
    say("")

    # The key is loaded only once there is real work to do, so an exhausted budget never
    # touches company/.env.local.
    key = "" if args.fixture else load_key(root)

    total_calls = 0
    total_records = 0
    all_changes = []
    completed_all = True
    rate_limited = False

    for code, set_aside in combos:
        if not args.fixture and total_calls >= budget:
            completed_all = False
            say("Stopped before NAICS %s: the 24-hour call budget is spent." % code)
            break
        try:
            records, calls, _, complete = pull_window(
                conn, key, code, set_aside, start, end,
                budget - total_calls if not args.fixture else 99, args)
        except RateLimited as exc:
            rate_limited = True
            completed_all = False
            total_calls += exc.calls_used
            seen, changes = apply_records(conn, exc.records, sync_date)
            total_records += seen
            all_changes.extend(changes)
            conn.commit()
            say(exc.message)
            if seen:
                say("Retained %d notice(s) from complete pages before the refused page. "
                    "That partial window is not recorded as full coverage." % seen)
            say(exc.next_action)
            break
        total_calls += calls
        seen, changes = apply_records(conn, records, sync_date)
        total_records += seen
        all_changes.extend(changes)
        if complete:
            note_completed_query_coverage(conn, code, set_aside, start.isoformat(),
                                          end.isoformat())
        if not complete:
            completed_all = False

    attempt_utc = now_utc_iso()
    set_state(conn, "last_sync_attempt_utc", attempt_utc)
    set_state(conn, "last_sync_attempt_calls", total_calls)
    if completed_all:
        set_state(conn, "last_sync_utc", attempt_utc)
        set_state(conn, "last_sync_calls", total_calls)
        set_state(conn, "last_sync_window_from", start.isoformat())
        set_state(conn, "last_sync_window_to", end.isoformat())
        set_state(conn, "last_sync_status", "complete")
    else:
        set_state(conn, "last_sync_status", "incomplete")
    conn.commit()

    say("")
    say("Request attempts in this run: %d. API calls from this folder in the last 24 hours: "
        "%d." % (total_calls, calls_last_24_hours(conn)))
    say("Notices read: %d." % total_records)
    report_changes(all_changes, conn)

    if completed_all:
        say("")
        say("The sync window is saved, so the next run starts from %s." % end.isoformat())
    else:
        say("")
        say("The sync did not finish, so the saved window was left where it was and nothing "
            "will be skipped next time.")
        if not rate_limited:
            say("Next action: run /sync after the 24-hour request window resets.")
    say("")
    say(NOT_ATTACHMENTS_LINE)
    say(CONFIRM_LINE)
    conn.close()
    return 0 if completed_all else 3


def report_changes(changes, conn):
    say("")
    if not changes:
        say("Nothing changed since the last sync.")
        return
    grouped = {}
    for change in changes:
        grouped.setdefault(change["kind"], []).append(change)
    order = ["new", "deadline_moved", "cancelled", "set_aside_changed", "type_changed",
             "reappeared", "naics_changed", "title_changed", "place_changed",
             "award_recorded", "archive_changed", "reposted", "link_changed",
             "field_changed"]
    say("What changed since last time:")
    for kind in order:
        items = grouped.get(kind)
        if not items:
            continue
        say("  %s: %d" % (KIND_LABEL.get(kind, kind), len(items)))
        for item in items[:10]:
            title = title_for(conn, item["notice_id"])
            if kind == "new":
                say("    %s  %s" % (item["notice_id"], title))
            else:
                say("    %s  %s" % (item["notice_id"], title))
                say("      %s: %s -> %s" % (item["field"], item["old"] or "empty",
                                            item["new"] or "empty"))
        if len(items) > 10:
            say("    and %d more, see /find-opps or the changes command" % (len(items) - 10))


def title_for(conn, notice_id):
    row = conn.execute("SELECT title FROM opportunities WHERE notice_id = ?",
                       (notice_id,)).fetchone()
    return row["title"] if row else ""


def build_backfill_plan(naics_codes, set_asides, start, end, chunk_days):
    plan = []
    combos = []
    for code in naics_codes:
        if set_asides:
            for set_aside in set_asides:
                combos.append((code, set_aside))
        else:
            combos.append((code, ""))
    for code, set_aside in combos:
        cursor = start
        while cursor <= end:
            stop = min(cursor + timedelta(days=chunk_days - 1), end)
            plan.append({"naics": code, "set_aside": set_aside,
                         "from": cursor.isoformat(), "to": stop.isoformat()})
            cursor = stop + timedelta(days=1)
    return plan


def cmd_backfill(args):
    require_positive_daily_limit(args)
    root = repo_root()
    conn = open_db(args.db)
    naics_codes = resolve_naics(conn, args, root)
    set_asides = resolve_set_asides(args, root)
    sync_date = today_utc()
    end = parse_date(sync_date)

    plan_json = get_state(conn, "backfill_plan")
    cursor = json.loads(get_state(conn, "backfill_cursor", '{"index": 0, "offset": 0}'))

    if args.reset or not plan_json:
        if args.since:
            start = parse_date(args.since)
        else:
            start = end - timedelta(days=int(round(args.months * 30.44)))
        if (end - start).days > MAX_WINDOW_DAYS * 5:
            raise KitError(
                "That is a very long backfill.",
                "Pick a shorter period with --months, for example --months 12 .")
        chunk = min(args.chunk_days, MAX_WINDOW_DAYS)
        plan = build_backfill_plan(naics_codes, set_asides, start, end, chunk)
        set_state(conn, "backfill_plan", json.dumps(plan))
        set_state(conn, "backfill_from", start.isoformat())
        set_state(conn, "backfill_to", end.isoformat())
        cursor = {"index": 0, "offset": 0}
        set_state(conn, "backfill_cursor", json.dumps(cursor))
        conn.commit()
    else:
        plan = json.loads(plan_json)

    remaining = len(plan) - cursor.get("index", 0)
    if remaining <= 0:
        say("Backfill is already complete. %d chunks were loaded, covering %s to %s."
            % (len(plan), get_state(conn, "backfill_from", "unknown"),
               get_state(conn, "backfill_to", "unknown")))
        say("Next action: run /sync each day from now on.")
        conn.close()
        return 0

    used_recently = calls_last_24_hours(conn)
    budget = max(0, args.daily_limit - used_recently)
    days_needed = (remaining + args.daily_limit - 1) // args.daily_limit

    say("Backfill plan")
    say("  Period: %s to %s" % (get_state(conn, "backfill_from", "unknown"),
                                get_state(conn, "backfill_to", "unknown")))
    say("  Filters: NAICS " + ", ".join(naics_codes) +
        ("; set-aside " + ", ".join(set_asides) if set_asides else "; no set-aside filter"))
    say("  Chunks: %d in total, %d still to do, %d done."
        % (len(plan), remaining, cursor.get("index", 0)))
    if set_asides:
        say("  Filtering by set-aside at the API multiplies the chunk count by the number of "
            "set-asides. Without that filter this plan would be %d chunks and would cover "
            "every set-aside under those NAICS codes."
            % (len(plan) // max(1, len(set_asides))))
    say("  Each chunk is at least one API call. A chunk holding more than 1,000 records "
        "needs one extra call per further 1,000.")
    say("  Your stated 24-hour limit is %d calls, and this folder made %d in the last "
        "24 hours." % (args.daily_limit, used_recently))
    say("  At that limit this backfill takes at least %d more 24-hour request window(s), "
        "and longer if chunks need extra pages." % days_needed)
    say("")

    if args.fixture:
        say("  " + FIXTURE_BANNER)

    if args.plan_only:
        say("Nothing was called. This was the plan only.")
        say("Next action: run /backfill without --plan-only when you are happy with the cost.")
        conn.close()
        return 0

    if not args.fixture and budget <= 0:
        say("Nothing was called. The 24-hour budget of %d calls is already spent."
            % args.daily_limit)
        say("Next action: run /backfill after the oldest call leaves the 24-hour window. It "
            "resumes at chunk %d of %d." % (cursor.get("index", 0) + 1, len(plan)))
        conn.close()
        return 3

    # The key is loaded only once there is real work to do, so an exhausted budget never
    # touches company/.env.local.
    key = "" if args.fixture else load_key(root)

    calls_used = 0
    total_records = 0
    all_changes = []
    rate_limited = False

    while cursor["index"] < len(plan):
        if not args.fixture and calls_used >= budget:
            break
        chunk = plan[cursor["index"]]
        try:
            records, calls, next_offset, complete = pull_window(
                conn, key, chunk["naics"], chunk["set_aside"],
                parse_date(chunk["from"]), parse_date(chunk["to"]),
                (budget - calls_used) if not args.fixture else 99, args,
                start_offset=cursor.get("offset", 0))
        except RateLimited as exc:
            rate_limited = True
            calls_used += exc.calls_used
            seen, changes = apply_records(conn, exc.records, sync_date)
            total_records += seen
            all_changes.extend(changes)
            cursor = {"index": cursor["index"], "offset": exc.next_offset}
            set_state(conn, "backfill_cursor", json.dumps(cursor))
            conn.commit()
            say(exc.message)
            if seen:
                say("Retained %d notice(s) from complete pages before the refused page. "
                    "This unfinished chunk is not recorded as full coverage." % seen)
            say(exc.next_action)
            break
        calls_used += calls
        seen, changes = apply_records(conn, records, sync_date)
        total_records += seen
        all_changes.extend(changes)
        if complete:
            note_completed_query_coverage(conn, chunk["naics"], chunk["set_aside"],
                                          chunk["from"], chunk["to"])
            cursor = {"index": cursor["index"] + 1, "offset": 0}
        else:
            cursor = {"index": cursor["index"], "offset": next_offset}
        set_state(conn, "backfill_cursor", json.dumps(cursor))
        conn.commit()

    attempt_utc = now_utc_iso()
    set_state(conn, "last_backfill_attempt_utc", attempt_utc)
    set_state(conn, "last_backfill_status",
              "complete" if cursor["index"] >= len(plan) else "incomplete")
    if cursor["index"] >= len(plan):
        set_state(conn, "last_backfill_utc", attempt_utc)
    conn.commit()

    done = cursor["index"]
    say("")
    say("Request attempts in this run: %d. API calls from this folder in the last 24 hours: "
        "%d." % (calls_used, calls_last_24_hours(conn)))
    say("Notices read: %d." % total_records)
    say("Completed chunks: %d of %d." % (done, len(plan)))
    if done < len(plan):
        say("Current chunk resumes at API page index %d." % cursor.get("offset", 0))
    report_changes(all_changes, conn)
    if done >= len(plan):
        say("")
        say("Backfill is complete. Next action: run /sync each day from now on.")
    else:
        say("")
        say("Backfill is not finished. Next action: run /backfill after the request limit "
            "resets. It resumes at chunk %d, API page index %d."
            % (done + 1, cursor.get("offset", 0)))
    say("")
    say(NOT_ATTACHMENTS_LINE)
    say(CONFIRM_LINE)
    conn.close()
    return 0 if done >= len(plan) else 3


def cmd_search(args):
    root = repo_root()
    conn = open_db(args.db, create=False)

    where = []
    params = []

    naics = list(args.naics or [])
    if args.from_profile and not naics:
        profile = parse_profile(root, args.profile)
        naics = profile["naics"]
        if not naics:
            say("No NAICS codes were found in %s, so the search was not narrowed by NAICS."
                % profile["path"])
            say("Next action: run /setup-profile to build the profile, or pass the codes with "
                "--naics 541519 .")
            say("")
    if naics:
        # Only question marks are placed into the SQL text here. Every value stays a bound
        # parameter, so a search term can never become SQL.
        where.append("naics IN (" + ",".join("?" * len(naics)) + ")")
        params.extend(naics)

    if args.set_aside:
        clauses = []
        for value in args.set_aside:
            clauses.append("(UPPER(set_aside_code) = ? OR "
                           "LOWER(set_aside_description) LIKE ?)")
            params.append(value.upper())
            params.append("%" + value.lower() + "%")
        where.append("(" + " OR ".join(clauses) + ")")

    if args.state:
        where.append("UPPER(pop_state) IN (" + ",".join("?" * len(args.state)) + ")")
        params.extend([s.upper() for s in args.state])

    if args.agency:
        where.append("LOWER(agency_path) LIKE ?")
        params.append("%" + args.agency.lower() + "%")

    for word in (args.keyword or []):
        where.append("(LOWER(title) LIKE ? OR LOWER(COALESCE(description, '')) LIKE ? "
                     "OR LOWER(COALESCE(solicitation_number, '')) LIKE ?)")
        needle = "%" + word.lower() + "%"
        params.extend([needle, needle, needle])

    if args.notice_type_filter:
        clauses = []
        for value in args.notice_type_filter:
            clauses.append("LOWER(notice_type) LIKE ?")
            params.append("%" + value.lower() + "%")
        where.append("(" + " OR ".join(clauses) + ")")

    if args.posted_since:
        where.append("posted_date >= ?")
        params.append(args.posted_since)

    if args.deadline_before:
        where.append("response_deadline_date <> '' AND response_deadline_date <= ?")
        params.append(args.deadline_before)

    if args.min_days is not None:
        cutoff = (now_utc().date() + timedelta(days=args.min_days)).isoformat()
        where.append("(response_deadline_date = '' OR response_deadline_date >= ?)")
        params.append(cutoff)

    if not args.include_inactive:
        where.append("LOWER(COALESCE(active, '')) LIKE 'y%'")

    if args.changed_since:
        where.append("notice_id IN (SELECT notice_id FROM changes WHERE sync_date >= ? "
                     "AND kind != 'new')")
        params.append(args.changed_since)

    if args.notice_id:
        where.append("notice_id = ?")
        params.append(args.notice_id)

    sql = "SELECT * FROM opportunities"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += (" ORDER BY CASE WHEN response_deadline_date = '' THEN 1 ELSE 0 END, "
            "response_deadline_date ASC, posted_date DESC LIMIT ?")
    params.append(args.limit)

    rows = conn.execute(sql, params).fetchall()
    total = conn.execute("SELECT COUNT(*) AS n FROM opportunities").fetchone()["n"]

    if args.json:
        payload = {
            "generated_utc": now_utc_iso(),
            "last_sync_utc": get_state(conn, "last_sync_utc"),
            "last_sync_attempt_utc": get_state(conn, "last_sync_attempt_utc"),
            "last_sync_status": get_state(conn, "last_sync_status"),
            "days_since_sync": staleness(conn)[1],
            "database_notices": total,
            "coverage": [dict(r) for r in conn.execute(
                "SELECT * FROM coverage ORDER BY filter_kind, filter_value").fetchall()],
            "results": [],
            "notes": [NOT_ATTACHMENTS_LINE, CONFIRM_LINE],
        }
        for row in rows:
            item = dict(row)
            item.pop("raw_json", None)
            item["changes"] = [dict(c) for c in conn.execute(
                "SELECT sync_date, kind, field, old_value, new_value FROM changes "
                "WHERE notice_id = ? AND kind != 'new' ORDER BY change_id DESC LIMIT 5",
                (row["notice_id"],)).fetchall()]
            payload["results"].append(item)
        say(json.dumps(payload, indent=2, ensure_ascii=False))
        conn.close()
        return 0

    for line in freshness_banner(conn):
        say(line)
    say("")
    say("Local search, no network call was made. %d of %d notices in the database matched."
        % (len(rows), total))
    say("")

    if not rows:
        say("Nothing matched.")
        say("Next action: loosen one filter, for example drop the state or widen the posted "
            "date, or run /sync if the database looks stale above.")
        say("")
        say(CONFIRM_LINE)
        conn.close()
        return 0

    for index, row in enumerate(rows, start=1):
        say("%d. %s" % (index, row["title"] or "no title stated"))
        say("   Notice ID: %s   Solicitation: %s"
            % (row["notice_id"], row["solicitation_number"] or "not stated"))
        say("   Agency: %s" % (row["agency_path"] or "not stated"))
        say("   NAICS: %s   Set-aside: %s   Notice type: %s"
            % (row["naics"] or "not stated",
               row["set_aside_description"] or row["set_aside_code"] or "none stated",
               row["notice_type"] or "not stated"))
        say("   Posted: %s   Response deadline as SAM stated it: %s"
            % (row["posted_date"] or "not stated",
               row["response_deadline_raw"] or "not stated"))
        if row["response_deadline_date"]:
            say("     which is date %s, time %s, zone %s, copied exactly and not converted"
                % (row["response_deadline_date"],
                   row["response_deadline_time"] or "not stated",
                   row["response_deadline_zone"] or "not stated"))
        place = ", ".join(p for p in [row["pop_city"], row["pop_state"], row["pop_zip"],
                                      row["pop_country"]] if p)
        say("   Place of performance: %s" % (place or "not stated"))
        say("   Contract type: %s" % (row["contract_type"] or "not stated in the notice"))
        say("   Active per SAM: %s   Link: %s"
            % (row["active"] or "not stated", row["link"] or "not stated"))
        say("   First seen in this database: %s   Last seen: %s"
            % (row["first_seen_utc"], row["last_seen_utc"]))
        history = conn.execute(
            "SELECT sync_date, kind, field, old_value, new_value FROM changes "
            "WHERE notice_id = ? AND kind != 'new' ORDER BY change_id DESC LIMIT 5",
            (row["notice_id"],)).fetchall()
        if history:
            say("   Change history, which the API itself cannot give you:")
            for change in history:
                say("     %s  %s: %s -> %s"
                    % (change["sync_date"], KIND_LABEL.get(change["kind"], change["kind"]),
                       change["old_value"] or "empty", change["new_value"] or "empty"))
        else:
            say("   Change history: nothing has changed since this database first saw it.")
        say("")

    say(NOT_ATTACHMENTS_LINE)
    say(CONFIRM_LINE)
    conn.close()
    return 0


def cmd_changes(args):
    conn = open_db(args.db, create=False)
    where = ["1 = 1"]
    params = []
    if args.since:
        where.append("c.sync_date >= ?")
        params.append(args.since)
    if args.notice_id:
        where.append("c.notice_id = ?")
        params.append(args.notice_id)
    if args.kind:
        where.append("c.kind IN (" + ",".join("?" * len(args.kind)) + ")")
        params.extend(args.kind)

    sql = ("SELECT c.*, o.title, o.solicitation_number, o.link FROM changes c "
           "LEFT JOIN opportunities o ON o.notice_id = c.notice_id WHERE "
           + " AND ".join(where) + " ORDER BY c.change_id DESC LIMIT ?")
    params.append(args.limit)
    rows = conn.execute(sql, params).fetchall()

    if args.json:
        say(json.dumps({"generated_utc": now_utc_iso(),
                        "changes": [dict(r) for r in rows],
                        "notes": [CONFIRM_LINE]}, indent=2, ensure_ascii=False))
        conn.close()
        return 0

    for line in freshness_banner(conn):
        say(line)
    say("")
    say("Change history. The SAM.gov API only ever returns the latest active version of a "
        "notice, so this history exists only because this database took a snapshot on each "
        "sync. Nothing here came from the API in one call.")
    say("")
    if not rows:
        say("No changes recorded for that filter.")
        conn.close()
        return 0
    for row in rows:
        label = ("first seen in this database" if row["kind"] == "new"
                 else KIND_LABEL.get(row["kind"], row["kind"]))
        say("%s  %s" % (row["sync_date"], label))
        say("   %s  %s" % (row["notice_id"], row["title"] or "title not stored"))
        if row["field"]:
            say("   %s: %s -> %s" % (row["field"], row["old_value"] or "empty",
                                     row["new_value"] or "empty"))
        if row["link"]:
            say("   %s" % row["link"])
        say("")
    say(CONFIRM_LINE)
    conn.close()
    return 0


def strip_html(text):
    text = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<")
    text = text.replace("&gt;", ">").replace("&quot;", '"').replace("&#39;", "'")
    return re.sub(r"\s+", " ", text).strip()


def cmd_describe(args):
    root = repo_root()
    conn = open_db(args.db, create=False)
    row = conn.execute("SELECT notice_id, title, description_url FROM opportunities "
                       "WHERE notice_id = ?", (args.notice_id,)).fetchone()
    if row is None:
        raise KitError(
            "No notice with id " + args.notice_id + " in the local database.",
            "Run a search first to confirm the notice id, or run /sync if the notice is "
            "newer than your last sync.",
            code=5,
        )
    used_recently = calls_last_24_hours(conn)
    if not args.fixture and used_recently >= args.daily_limit:
        say("Nothing was called. This folder has used %d of its %d API calls in the last "
            "24 hours." % (used_recently, args.daily_limit))
        say("Next action: run this again after the oldest call leaves the 24-hour window.")
        conn.close()
        return 3

    key = "" if args.fixture else load_key(root)
    params = {"noticeid": args.notice_id}
    body = api_get(conn, API_DESCRIPTION, params, key, timeout=args.timeout,
                   fixture=args.fixture)
    text = body.get("description") or body.get("body") or ""
    clean = strip_html(str(text))
    conn.execute("UPDATE opportunities SET description = ?, description_fetched_utc = ? "
                 "WHERE notice_id = ?", (clean, now_utc_iso(), args.notice_id))
    conn.commit()
    say("Description stored for %s, %d characters." % (args.notice_id, len(clean)))
    say("That cost one API call. Calls from this folder in the last 24 hours: %d."
        % calls_last_24_hours(conn))
    say("")
    say(clean[:2000] + (" ..." if len(clean) > 2000 else ""))
    say("")
    say(NOT_ATTACHMENTS_LINE)
    conn.close()
    return 0


# ---------------------------------------------------------------------------
# argument parsing
# ---------------------------------------------------------------------------

def add_common(parser):
    parser.add_argument("--db", default=default_db_path(),
                        help="path to the SQLite file, default data/sam.db")
    parser.add_argument("--profile", default=None,
                        help="path to the profile, default company/profile.md")


def add_network(parser):
    parser.add_argument("--daily-limit", type=positive_int, default=10,
                        help="API calls your account is allowed in 24 hours. 10 is the "
                             "no-role tier, 1000 if you hold a role on an entity "
                             "registration. Default 10, the safe assumption.")
    parser.add_argument("--timeout", type=int, default=60, help="seconds per call")
    parser.add_argument("--fixture", default=None,
                        help="read a canned JSON response instead of calling the API. A file "
                             "or a folder of page-0.json, page-1.json and so on. Use it to "
                             "rehearse a sync offline with no key and no network call.")
    parser.add_argument("--notice-type", default=None,
                        help="restrict the API pull to one notice type code, for example o "
                             "for solicitation")


def build_parser():
    parser = argparse.ArgumentParser(
        prog="samdb.py",
        description="Local opportunity database for the GovCon Starter Kit. Syncs SAM.gov "
                    "notices once a day and then searches offline.")
    subs = parser.add_subparsers(dest="command")

    p_init = subs.add_parser("init", help="create the database and schema")
    add_common(p_init)
    p_init.set_defaults(func=cmd_init)

    p_status = subs.add_parser("status", help="what is in the database and how old it is")
    add_common(p_status)
    p_status.set_defaults(func=cmd_status)

    p_sync = subs.add_parser("sync", help="pull what is new since the last successful sync")
    add_common(p_sync)
    add_network(p_sync)
    p_sync.add_argument("--naics", action="append", default=[],
                        help="NAICS code, repeatable. Default: read from the profile.")
    p_sync.add_argument("--set-aside", action="append", default=[],
                        help="typeOfSetAside code, repeatable. Default: no set-aside filter, "
                             "which costs fewer calls and covers more.")
    p_sync.add_argument("--overlap-days", type=int, default=7,
                        help="how far back before the last sync to look again, so a change "
                             "to a recent notice is caught. Default 7.")
    p_sync.add_argument("--first-run-days", type=int, default=7,
                        help="window to use when there has never been a sync. Default 7.")
    p_sync.set_defaults(func=cmd_sync)

    p_back = subs.add_parser("backfill", help="resumable historical load")
    add_common(p_back)
    add_network(p_back)
    p_back.add_argument("--naics", action="append", default=[])
    p_back.add_argument("--set-aside", action="append", default=[])
    p_back.add_argument("--months", type=float, default=12.0,
                        help="how far back to go, default 12 months")
    p_back.add_argument("--since", default=None, help="start date, YYYY-MM-DD")
    p_back.add_argument("--chunk-days", type=int, default=90,
                        help="days per chunk, default 90. The API caps a window at 365 days.")
    p_back.add_argument("--reset", action="store_true",
                        help="throw away the saved plan and build a new one")
    p_back.add_argument("--plan-only", action="store_true",
                        help="print the plan and the day estimate, make no call")
    p_back.set_defaults(func=cmd_backfill)

    p_search = subs.add_parser("search", help="search the local database, no network call")
    add_common(p_search)
    p_search.add_argument("--naics", action="append", default=[])
    p_search.add_argument("--from-profile", action="store_true",
                          help="take the NAICS codes from company/profile.md")
    p_search.add_argument("--set-aside", action="append", default=[])
    p_search.add_argument("--state", action="append", default=[])
    p_search.add_argument("--agency", default=None)
    p_search.add_argument("--keyword", action="append", default=[])
    p_search.add_argument("--notice-type-filter", action="append", default=[],
                          help="match against the stored notice type text")
    p_search.add_argument("--posted-since", default=None)
    p_search.add_argument("--deadline-before", default=None)
    p_search.add_argument("--min-days", type=int, default=None,
                          help="only notices whose deadline is at least this many days out")
    p_search.add_argument("--include-inactive", action="store_true")
    p_search.add_argument("--changed-since", default=None,
                          help="only notices that changed on or after this sync date")
    p_search.add_argument("--notice-id", default=None)
    p_search.add_argument("--limit", type=int, default=25)
    p_search.add_argument("--json", action="store_true")
    p_search.set_defaults(func=cmd_search)

    p_changes = subs.add_parser("changes", help="what changed, and when")
    add_common(p_changes)
    p_changes.add_argument("--since", default=None, help="sync date, YYYY-MM-DD")
    p_changes.add_argument("--notice-id", default=None)
    p_changes.add_argument("--kind", action="append", default=[])
    p_changes.add_argument("--limit", type=int, default=50)
    p_changes.add_argument("--json", action="store_true")
    p_changes.set_defaults(func=cmd_changes)

    p_desc = subs.add_parser("describe", help="fetch one notice description, one API call")
    add_common(p_desc)
    add_network(p_desc)
    p_desc.add_argument("--notice-id", required=True)
    p_desc.set_defaults(func=cmd_describe)

    return parser


def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "command", None):
        parser.print_help()
        return 0
    try:
        return args.func(args)
    except KitError as exc:
        say(exc.message)
        if exc.next_action:
            say("Next action: " + exc.next_action)
        return exc.code
    except sqlite3.Error as exc:
        say("The local database refused the operation: " + str(exc))
        say("Next action: run the status command. If the file is damaged, delete "
            "data/sam.db and run /backfill again; nothing in it is authoritative.")
        return 7


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
