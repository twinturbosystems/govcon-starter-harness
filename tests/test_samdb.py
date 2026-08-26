import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("samdb", ROOT / "tools" / "samdb.py")
samdb = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(samdb)


def notice(notice_id, posted="2026-08-25", **extra):
    value = {
        "noticeId": notice_id,
        "title": "Offline fixture notice " + notice_id,
        "postedDate": posted,
        "active": "Yes",
        "naicsCode": "541519",
    }
    value.update(extra)
    return value


def network_args(db_path, fixture, **overrides):
    values = {
        "db": str(db_path),
        "profile": None,
        "naics": ["541519"],
        "set_aside": [],
        "daily_limit": 10,
        "timeout": 1,
        "fixture": None if fixture is None else str(fixture),
        "notice_type": None,
    }
    values.update(overrides)
    return SimpleNamespace(**values)


class SamDbTests(unittest.TestCase):
    def test_rolling_call_count_excludes_old_and_fixture_rows(self):
        conn = samdb.open_db(":memory:")
        fixed = samdb.datetime(2026, 8, 26, 12, 0, 0, tzinfo=samdb.timezone.utc)
        rows = [
            ("2026-08-25T11:59:59Z", "ok"),
            ("2026-08-25T12:00:00Z", "ok"),
            ("2026-08-26T11:59:59Z", "http_error"),
            ("2026-08-26T11:59:59Z", "fixture"),
        ]
        for called_utc, outcome in rows:
            conn.execute(
                "INSERT INTO api_calls "
                "(called_utc, call_date, endpoint, params, http_status, records, outcome) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (called_utc, called_utc[:10], "offline", "{}", 200, 0, outcome))
        conn.commit()

        with mock.patch.object(samdb, "now_utc", return_value=fixed):
            count = samdb.calls_last_24_hours(conn)
        conn.close()

        self.assertEqual(count, 2)

    def test_daily_limit_must_be_positive(self):
        with tempfile.TemporaryDirectory() as temp:
            args = network_args(
                Path(temp) / "sam.db", None, daily_limit=0,
                overlap_days=7, first_run_days=7)

            with self.assertRaises(samdb.KitError) as caught:
                samdb.cmd_sync(args)

            self.assertEqual(caught.exception.code, 2)
            self.assertIn("at least 1", caught.exception.message)
            self.assertFalse((Path(temp) / "sam.db").exists())

        parser = samdb.build_parser()
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
            parser.parse_args(["sync", "--daily-limit", "0"])
        self.assertEqual(caught.exception.code, 2)

    def test_pagination_uses_zero_based_page_indexes(self):
        calls = []
        pages = [
            {"totalRecords": 3, "opportunitiesData": [notice("A"), notice("B")]},
            {"totalRecords": 3, "opportunitiesData": [notice("C")]},
        ]

        def fake_get(conn, url, params, key, timeout, fixture, page_index):
            calls.append((params["offset"], page_index))
            return pages[page_index]

        args = SimpleNamespace(timeout=1, fixture=None, notice_type=None)
        conn = samdb.open_db(":memory:")
        with mock.patch.object(samdb, "MAX_RECORDS_PER_CALL", 2), \
                mock.patch.object(samdb, "api_get", side_effect=fake_get):
            records, used, next_page, complete = samdb.pull_window(
                conn, "key", "541519", "", samdb.parse_date("2026-08-25"),
                samdb.parse_date("2026-08-25"), 10, args)
        conn.close()

        self.assertEqual(calls, [("0", 0), ("1", 1)])
        self.assertEqual([row["noticeId"] for row in records], ["A", "B", "C"])
        self.assertEqual((used, next_page, complete), (2, 2, True))

    def test_normalize_accepts_current_and_older_set_aside_fields(self):
        current = samdb.normalize(notice(
            "CURRENT", setAsideCode="SDVOSBC",
            setAside="Service-Disabled Veteran-Owned Small Business"))
        older = samdb.normalize(notice(
            "OLDER", typeOfSetAside="WOSB",
            typeOfSetAsideDescription="Women-Owned Small Business"))

        self.assertEqual(
            (current["set_aside_code"], current["set_aside_description"]),
            ("SDVOSBC", "Service-Disabled Veteran-Owned Small Business"))
        self.assertEqual(
            (older["set_aside_code"], older["set_aside_description"]),
            ("WOSB", "Women-Owned Small Business"))

    def test_sync_keeps_complete_pages_on_429_without_advancing_freshness(self):
        with tempfile.TemporaryDirectory() as temp:
            temp_path = Path(temp)
            fixture = temp_path / "fixture"
            fixture.mkdir()
            (fixture / "page-0.json").write_text(json.dumps({
                "totalRecords": 2,
                "opportunitiesData": [notice("KEPT")],
            }), encoding="utf-8")
            (fixture / "page-1.json").write_text(json.dumps({
                "__http_status": 429,
                "message": "offline quota rehearsal",
            }), encoding="utf-8")
            db_path = temp_path / "sam.db"
            conn = samdb.open_db(str(db_path))
            samdb.set_state(conn, "last_sync_utc", "2026-08-20T12:00:00Z")
            samdb.set_state(conn, "last_sync_window_to", "2026-08-20")
            conn.commit()
            conn.close()

            args = network_args(
                db_path, fixture, overlap_days=7, first_run_days=7)
            output = io.StringIO()
            with mock.patch.object(samdb, "MAX_RECORDS_PER_CALL", 1), \
                    contextlib.redirect_stdout(output):
                result = samdb.cmd_sync(args)

            conn = samdb.open_db(str(db_path), create=False)
            stored = conn.execute("SELECT COUNT(*) AS n FROM opportunities").fetchone()["n"]
            coverage = conn.execute("SELECT COUNT(*) AS n FROM coverage").fetchone()["n"]
            self.assertEqual(result, 3)
            self.assertEqual(stored, 1)
            self.assertEqual(coverage, 0)
            self.assertEqual(samdb.get_state(conn, "last_sync_utc"),
                             "2026-08-20T12:00:00Z")
            self.assertEqual(samdb.get_state(conn, "last_sync_status"), "incomplete")
            self.assertEqual(samdb.get_state(conn, "last_sync_attempt_calls"), "2")
            conn.close()

            rendered = output.getvalue()
            self.assertIn("Request attempts in this run: 2", rendered)
            self.assertIn("API calls from this folder in the last 24 hours: 0", rendered)
            self.assertIn("Retained 1 notice(s)", rendered)
            self.assertIn("not recorded as full coverage", rendered)

    def test_sync_local_budget_exhaustion_is_incomplete_and_nonzero(self):
        with tempfile.TemporaryDirectory() as temp:
            db_path = Path(temp) / "sam.db"
            args = network_args(
                db_path, None, naics=["541519", "541611"], daily_limit=1,
                overlap_days=7, first_run_days=7)
            output = io.StringIO()
            pulled = ([notice("FIRST")], 1, 1, True)

            with mock.patch.object(samdb, "load_key", return_value="offline-key"), \
                    mock.patch.object(samdb, "pull_window", return_value=pulled), \
                    contextlib.redirect_stdout(output):
                result = samdb.cmd_sync(args)

            conn = samdb.open_db(str(db_path), create=False)
            self.assertEqual(result, 3)
            self.assertEqual(samdb.get_state(conn, "last_sync_status"), "incomplete")
            self.assertIsNone(samdb.get_state(conn, "last_sync_utc"))
            self.assertEqual(samdb.get_state(conn, "last_sync_attempt_calls"), "1")
            self.assertEqual(
                conn.execute("SELECT COUNT(*) AS n FROM opportunities").fetchone()["n"], 1)
            conn.close()
            self.assertIn("24-hour call budget is spent", output.getvalue())
            self.assertIn("Request attempts in this run: 1", output.getvalue())

    def test_backfill_resumes_refused_page_and_records_only_completed_coverage(self):
        with tempfile.TemporaryDirectory() as temp:
            temp_path = Path(temp)
            fixture = temp_path / "fixture"
            fixture.mkdir()
            (fixture / "page-0.json").write_text(json.dumps({
                "totalRecords": 2,
                "opportunitiesData": [notice("PAGE0")],
            }), encoding="utf-8")
            page_one = fixture / "page-1.json"
            page_one.write_text(json.dumps({
                "__http_status": 429,
                "message": "offline quota rehearsal",
            }), encoding="utf-8")
            db_path = temp_path / "sam.db"
            today = samdb.today_utc()
            args = network_args(
                db_path, fixture, since=today, months=12.0, chunk_days=90,
                reset=False, plan_only=False)

            first_output = io.StringIO()
            with mock.patch.object(samdb, "MAX_RECORDS_PER_CALL", 1), \
                    contextlib.redirect_stdout(first_output):
                first_result = samdb.cmd_backfill(args)

            conn = samdb.open_db(str(db_path), create=False)
            cursor = json.loads(samdb.get_state(conn, "backfill_cursor"))
            self.assertEqual(first_result, 3)
            self.assertEqual(cursor, {"index": 0, "offset": 1})
            self.assertEqual(
                conn.execute("SELECT COUNT(*) AS n FROM opportunities").fetchone()["n"], 1)
            self.assertEqual(
                conn.execute("SELECT COUNT(*) AS n FROM coverage").fetchone()["n"], 0)
            conn.close()

            page_one.write_text(json.dumps({
                "totalRecords": 2,
                "opportunitiesData": [notice("PAGE1")],
            }), encoding="utf-8")
            second_output = io.StringIO()
            with mock.patch.object(samdb, "MAX_RECORDS_PER_CALL", 1), \
                    contextlib.redirect_stdout(second_output):
                second_result = samdb.cmd_backfill(args)

            conn = samdb.open_db(str(db_path), create=False)
            cursor = json.loads(samdb.get_state(conn, "backfill_cursor"))
            self.assertEqual(second_result, 0)
            self.assertEqual(cursor, {"index": 1, "offset": 0})
            self.assertEqual(
                conn.execute("SELECT COUNT(*) AS n FROM opportunities").fetchone()["n"], 2)
            self.assertEqual(
                conn.execute("SELECT COUNT(*) AS n FROM coverage").fetchone()["n"], 1)
            conn.close()
            self.assertIn("API page index 1", first_output.getvalue())
            self.assertIn("Backfill is complete", second_output.getvalue())

    def test_backfill_local_budget_exhaustion_is_incomplete_and_nonzero(self):
        with tempfile.TemporaryDirectory() as temp:
            db_path = Path(temp) / "sam.db"
            start = (samdb.parse_date(samdb.today_utc()) - samdb.timedelta(days=1)).isoformat()
            args = network_args(
                db_path, None, since=start, months=12.0, chunk_days=1,
                reset=False, plan_only=False, daily_limit=1)
            output = io.StringIO()
            pulled = ([notice("FIRST")], 1, 1, True)

            with mock.patch.object(samdb, "load_key", return_value="offline-key"), \
                    mock.patch.object(samdb, "pull_window", return_value=pulled), \
                    contextlib.redirect_stdout(output):
                result = samdb.cmd_backfill(args)

            conn = samdb.open_db(str(db_path), create=False)
            cursor = json.loads(samdb.get_state(conn, "backfill_cursor"))
            self.assertEqual(result, 3)
            self.assertEqual(cursor, {"index": 1, "offset": 0})
            self.assertEqual(samdb.get_state(conn, "last_backfill_status"), "incomplete")
            self.assertIsNone(samdb.get_state(conn, "last_backfill_utc"))
            self.assertEqual(
                conn.execute("SELECT COUNT(*) AS n FROM coverage").fetchone()["n"], 1)
            conn.close()
            self.assertIn("Completed chunks: 1 of 2", output.getvalue())
            self.assertIn("Backfill is not finished", output.getvalue())


if __name__ == "__main__":
    unittest.main()
