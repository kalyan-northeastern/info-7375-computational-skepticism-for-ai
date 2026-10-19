#!/usr/bin/env python3
"""Tests for churn.py: flow, re-post detection, and the untrusted-read rule."""
import unittest

import churn


def rec(i, title="Educator", co="Acme", posted="2026-09-01", loc="Remote", dept="Ed"):
    return {"source": "greenhouse", "company": co, "source_id": str(i), "title": title, "location_text": loc,
            "department": dept, "date_posted": posted}


def snap(date, recs, ok=("Acme",)):
    return {"date": date, "path": f"all-jobs-{date}.json", "ok": set(ok), "recs": {churn.key_of(r): r for r in recs}}


class ChurnTests(unittest.TestCase):
    def test_new_closed_and_repost(self):
        a = snap("2026-10-01", [rec(1), rec(2, title="Writer"), rec(3, title="Analyst")])
        b = snap("2026-10-11", [rec(1), rec(4, title="Writer"), rec(5, title="Brand new")])
        f = churn.flow(a, b)
        r = f["rows"][0]
        self.assertEqual((r["closed"], r["new"], r["repost_like"]), (2, 2, 1))      # 2 and 3 gone; 4 is 2 re-posted
        self.assertEqual(f["totals"]["closed"], 2)
        self.assertTrue(r["trusted"])

    def test_a_board_that_comes_back_empty_is_not_counted_as_closings(self):
        a = snap("2026-10-01", [rec(i) for i in range(27)], ok=("Webflow", "Acme"))
        for r in a["recs"].values():
            r["company"] = "Webflow"
        b = snap("2026-10-11", [], ok=("Webflow", "Acme"))
        f = churn.flow(a, b)
        self.assertFalse(f["rows"][0]["trusted"])
        self.assertEqual(f["totals"]["closed"], 0)
        self.assertEqual(f["totals"]["boards"], 0)

    def test_same_job_under_a_new_post_id_is_counted_by_job_id(self):
        def r(i, ref, title):
            x = rec(i, title=title)
            x["job_ref"] = ref
            return x
        a = snap("2026-10-01", [r(1, "J1", "Teacher"), r(2, "J2", "Analyst"), r(3, "J3", "Writer")])
        b = snap("2026-10-11", [r(1, "J1", "Teacher"), r(9, "J2", "Analyst II"), r(4, "J4", "New")])
        row = churn.flow(a, b)["rows"][0]
        self.assertEqual(row["new_post_same_job"], 1)       # post 9 is job J2 under a new post id (the title changed, so title matching misses it)
        self.assertEqual((row["jobs_closed"], row["jobs_opened"]), (1, 1))   # J3 gone, J4 new
        self.assertEqual(row["repost_like"], 0)

    def test_a_tiny_board_is_not_flagged_for_a_few_extra_postings(self):
        a = snap("2026-10-01", [rec(i, title=f"t{i}") for i in range(6)])
        b = snap("2026-10-11", [rec(i, title=f"t{i}") for i in range(10)])
        self.assertTrue(churn.flow(a, b)["rows"][0]["trusted"])

    def test_same_title_open_under_several_ids_is_counted(self):
        a = snap("2026-10-01", [rec(1)])
        b = snap("2026-10-11", [rec(1), rec(2), rec(3)])
        self.assertEqual(churn.flow(a, b)["rows"][0]["same_title_open_under_many_ids"], 2)

    def test_age_and_the_reset_date_flag(self):
        s = snap("2026-10-18", [rec(i, posted="2026-10-10") for i in range(25)])
        row = churn.age_table(s)[0]
        self.assertEqual(row["median_days"], 8)
        self.assertTrue(row["date_looks_reset"])
        old = snap("2026-10-18", [rec(i, posted="2026-01-01") for i in range(25)])
        self.assertFalse(churn.age_table(old)[0]["date_looks_reset"])
        self.assertEqual(churn.age_table(old)[0]["over_180"], 25)

    def test_implied_days_open_follows_littles_law(self):
        a = snap("2026-10-01", [rec(i, title=f"t{i}") for i in range(100)])
        b = snap("2026-10-11", [rec(i, title=f"t{i}") for i in range(10, 110)])   # 10 closed, 10 new in 10 days
        r = churn.flow(a, b)["rows"][0]
        self.assertEqual(r["implied_mean_days_open"], 100)          # stock 100, 1 closing per day
        self.assertTrue(r["roughly_steady"])


if __name__ == "__main__":
    unittest.main()
