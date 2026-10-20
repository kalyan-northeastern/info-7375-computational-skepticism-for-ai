#!/usr/bin/env python3
"""Tests for run_daily.py --text-out: the ad text is kept, it is resumable, and the monitor is unchanged."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import json, os, tempfile, unittest

from collectors import run_daily, monitor


class Stub:
    calls = 0

    @staticmethod
    def collect():
        return ([{"job_id": str(i), "title": f"Role {i}", "locations": "Remote", "url": f"https://x/{i}", "posted_at": None}
                 for i in range(3)], 3)

    @staticmethod
    def fetch_description(j):
        Stub.calls += 1
        return f"text of {j['job_id']}"


class TextOut(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = os.path.join(self.tmp.name, "m.db")
        self.out = os.path.join(self.tmp.name, "text")
        run_daily.COLLECTORS["stub"] = Stub
        Stub.calls = 0

    def tearDown(self):
        run_daily.COLLECTORS.pop("stub", None)
        self.tmp.cleanup()

    def lines(self):
        with open(os.path.join(self.out, "stub.jsonl"), encoding="utf-8") as f:
            return [json.loads(x) for x in f if x.strip()]

    def test_text_is_kept_for_every_job_and_the_monitor_still_stores_only_a_hash(self):
        # the --only choices come from COLLECTORS at parse time, so "stub" is accepted here
        run_daily.main(["--db", self.db, "--only", "stub", "--text-out", self.out])
        got = self.lines()
        self.assertEqual([r["job_id"] for r in got], ["0", "1", "2"])
        self.assertEqual(got[1]["description"], "text of 1")
        db = monitor.open_db(self.db)
        self.assertEqual(db.execute("select count(*), sum(desc_hash is not null) from jobs").fetchone(), (3, 3))

    def test_a_second_run_does_not_fetch_text_again(self):
        run_daily.main(["--db", self.db, "--only", "stub", "--text-out", self.out])
        first = Stub.calls
        run_daily.main(["--db", self.db, "--only", "stub", "--text-out", self.out])
        self.assertEqual(Stub.calls, first)
        self.assertEqual(len(self.lines()), 3)

    def test_known_jobs_get_their_text_when_the_file_is_missing_it(self):
        run_daily.main(["--db", self.db, "--only", "stub"])                  # monitor has the jobs, no text saved
        before = Stub.calls
        run_daily.main(["--db", self.db, "--only", "stub", "--text-out", self.out])
        self.assertEqual(Stub.calls - before, 3)                              # fetched again, because the text was never kept
        self.assertEqual(len(self.lines()), 3)


if __name__ == "__main__":
    unittest.main()
