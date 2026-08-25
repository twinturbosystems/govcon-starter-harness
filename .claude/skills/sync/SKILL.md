---
name: sync
description: Refresh the local opportunity database in data/sam.db with one small pull from the SAM.gov Get Opportunities API, then report what changed since last time: new notices, deadlines that moved, set-asides that changed, notices amended or cancelled. Uses one or two API calls on a normal day, which is what makes the kit usable inside a 10 calls per day rate limit. Use when the user asks to refresh, update, check for new opportunities, or when /find-opps says the local data is stale.
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
argument-hint: [optional: nothing, or a NAICS code to sync on its own, or "plan" to see the calls it would make]
---

# Sync the local opportunity database

Pull what is new from SAM.gov into `data/sam.db`, then say what changed. This is the only job in the kit that calls the API on a normal day, and it is meant to run once.

## Why this job exists, say it once if the user asks

The SAM.gov Get Opportunities API is rate limited hard. Per the GSA IAE System Account User Guide, a non-federal user with no role on an entity registration gets 10 requests per day. A user with a role on an entity registration gets 1,000 per day. Searching live against 10 calls a day is not workable, so the kit keeps its own copy: one small sync, then unlimited local searching.

## Input

$ARGUMENTS:

- empty: sync every NAICS code in `company/profile.md`
- a NAICS code: sync that one code only, which costs one call
- `plan`: say what it would call and stop, making no call at all

## Step 1, check Python 3 is there

The database tool is a single Python file, `tools/samdb.py`, written against the Python 3 standard library only. Nothing is installed, no package manager is involved.

Run one command to find the interpreter:

```bash
python3 --version || python --version || py -3 --version
```

On Windows, `python3` often opens the Microsoft Store instead of running anything. If that happens, use `python` or `py -3`. Use whichever of the three answered with a version number, in every command below.

If none of them works, give one next action and stop:

> Python 3 is not installed on this computer. Install it from https://www.python.org/downloads/ , then run `/sync` again. On Windows, tick "Add python.exe to PATH" on the first screen of the installer.

Do not paste a wall of alternatives, and do not offer to install it yourself.

## Step 2, check the key exists

The API needs a free key from api.data.gov, kept in `company/.env.local`. If that file does not exist, say this and stop:

1. Go to https://api.data.gov/signup/ . It is free, it takes about a minute, and the key arrives by email.
2. In this folder, copy the example file: `cp company/.env.local.example company/.env.local`
3. Open `company/.env.local` in a text editor and paste the key after `SAM_API_KEY=`.
4. Save it. That file is gitignored, so it stays on your machine.
5. Run `/sync` again.

Never ask the user to paste the key into the chat. Never read `company/.env.local` into the conversation. Never print it, echo it, or write it anywhere. The tool loads it inside its own process and never stores it.

## Step 3, say what the sync will do, then run it

Read `company/profile.md` and state the filters in two or three lines before running anything: the NAICS codes, the set-aside filter if the profile lists API codes for one, and roughly how many calls this will cost. One call per NAICS code is normal.

Then run it:

```bash
python3 tools/samdb.py sync --daily-limit 10
```

Replace `python3` with whichever interpreter answered in step 1.

`--daily-limit` is what you tell the tool your account is allowed per day. Leave it at 10 unless the user says they hold a role on an entity registration, in which case use `--daily-limit 1000`. The tool counts the calls it has made today and refuses to start one that would go past the limit, rather than finding out by being refused.

Useful variations, all of them optional:

```bash
python3 tools/samdb.py sync --naics 541519                 one code only, one call
python3 tools/samdb.py sync --overlap-days 14              look further back for amendments
python3 tools/samdb.py sync --set-aside SBA --set-aside SDVOSBC   filter at the API
python3 tools/samdb.py status                              what is in the database now
```

## Step 4, what the sync actually does

Explain it in plain words if the user asks, and do not overstate it.

1. It works out the window. It pulls notices posted from the day of the last successful sync, minus a seven day overlap, up to today. The overlap is there because the public search filters on the posted date and does not offer a modified date filter, so a recent notice that was amended is caught by looking back over the last week again.
2. It calls the API once per NAICS code, asking for up to 1,000 records. If a day genuinely holds more than 1,000 records for one code, it pages with an offset and each page is one more call.
3. It normalises each notice into the fields the kit uses, and computes a fingerprint of the fields that matter.
4. New notice ids are inserted. Existing ones are compared field by field against what the database already held, and every difference is written into the change history with the old value, the new value, and the date it was noticed.
5. It writes a snapshot row for every notice it saw, so the database records what each notice looked like on each sync date. The full picture is stored only when something changed, so a year of daily syncs stays small.
6. It saves the window and the run time. If the run did not finish, the saved window is left where it was, so the next run covers the gap rather than skipping it.

## Step 5, report what changed

The tool prints the change report. Lead with it, do not repeat it line for line, and put the ones that change a bid decision first:

1. Deadlines that moved. Say the old and the new, exactly as SAM stated them, with the time and the time zone, and never convert a time zone.
2. Notices cancelled or made inactive.
3. Set-asides that changed. A set-aside changing from SDVOSB to total small business, or the other way, changes who can bid, so it is never a footnote.
4. Amendments and corrections, which show up as a notice type change, a title change, or a change to the solicitation number.
5. New notices, with a count and the ones that match the profile named.

If any of those touches an opportunity that already has a file in `pipeline/`, update that file's log section with the change and the date, and say which files you updated.

Finish with one line pointing at `/find-opps` to search what just arrived.

## Step 6, when the rate limit stops it

The tool never retries against a rate limit. If it reports one, repeat what it said and stop:

- what happened, in one line, with the HTTP status and the message the API gave
- how many calls this folder has made today
- that nothing was lost and the saved position is written down
- one next action: run `/sync` again tomorrow

Do not run it again in the same session to see if it works now. Retrying against a rate limit spends tomorrow's budget as well.

Two honest limits on the call count. It counts what this folder recorded, so it cannot see calls made with the same key from another folder or another tool. And the provider decides when the count resets, not this kit.

## What this job does not do

- It does not download attachments, statements of work, or amendment documents. It mirrors notices. The documents still come from SAM.gov itself, and `/compliance-matrix` needs the real document.
- It does not fetch the full description text of a notice by default, because each description is another API call against the same daily budget. The tool stores the description link. To pull one description, run `python3 tools/samdb.py describe --notice-id <id>` and say that it cost one call.
- It does not make the local copy authoritative. Confirm every deadline on SAM.gov before bidding.
- It does not know about anything outside the filters it synced. If two NAICS codes were synced, the database knows two NAICS codes. Say that rather than implying the database is complete.

## Rules

- Never print, echo, repeat, or log the api.data.gov key, and never write it into any file.
- Never invent a notice, a deadline, a set-aside, or a change. Everything reported here comes out of the database, and the database comes from the API.
- Never state a response deadline without the time and the time zone as SAM stated them, and never convert a time zone.
- Never say a sync succeeded when the tool reported an incomplete run.
- Never loop the sync to get more data in one day.

## Rehearsing it without a key

The tool can read a canned JSON file instead of calling the API, which is how the sync path was tested on a machine with no key:

```bash
python3 tools/samdb.py sync --naics 541519 --fixture path/to/fixture-folder
```

A fixture folder holds `page-0.json`, `page-1.json` and so on, each shaped like a real API response. Every run against a fixture says plainly that it was a rehearsal, makes no call, and counts nothing against the budget. Offer this only when someone wants to see the mechanics before signing up for a key.
