#!/usr/bin/env python3
"""Tests for publish_delta.py: classification, the unavailable-source rule, state timing, and the commit guard."""
import os as _os, sys as _sys
for _p in (_os.path.dirname(_os.path.abspath(__file__)), _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))):
    if _os.path.exists(_os.path.join(_p, "lectern_paths.py")):
        _sys.path.insert(0, _p)
        break
import lectern_paths as lp   # where things are: see lectern_paths.py
import json, os, tempfile, unittest

import publish_delta as pd


def rec(sid, title="Educator", company="Acme", **kw):
    r = {"source": "greenhouse", "company": company, "source_id": sid, "title": title,
         "url": f"https://x/{sid}", "location_text": "Remote", "department": "Ed", "date_posted": "2026-10-01",
         "matched": {"role_title": ["educator"], "kept_because": "role word in title"}, "text": "ad " + sid}
    r.update(kw)
    return r


def make_run(root, date, kept, all_extra=(), sources=None):
    d = os.path.join(root, date)
    os.makedirs(d)
    sources = sources or [{"company": "Acme", "provider": "greenhouse", "status": "ok", "postings": len(kept)}]
    with open(os.path.join(d, f"jobs-of-interest-{date}.json"), "w") as f:
        json.dump({"sources": sources, "records": kept}, f)
    allr = [{**{k: v for k, v in r.items() if k not in ("text", "matched")}, "kept": True} for r in kept] + list(all_extra)
    with open(os.path.join(d, f"all-jobs-{date}.json"), "w") as f:
        json.dump({"sources": sources, "records": allr}, f)
    return d


class DeltaTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def delta(self, first, second):
        make_run(self.root, "2026-10-01", first)
        d2 = make_run(self.root, "2026-10-02", second[0], second[1] if len(second) > 1 else (), second[2] if len(second) > 2 else None)
        base, _ = pd.baseline_from_runs(self.root, "2026-10-02")
        return pd.diff(base, pd.load_run(d2))

    def test_new_changed_gone_and_unchanged(self):
        new, changed, gone = self.delta([rec("1"), rec("2"), rec("3", title="Old title")],
                                        [[rec("1"), rec("3", title="New title"), rec("4")]])
        self.assertEqual([r["source_id"] for r in new], ["4"])
        self.assertEqual([r["source_id"] for r in changed], ["3"])
        self.assertEqual(changed[0]["changes"][0]["field"], "title")
        self.assertEqual([r["source_id"] for r in gone], ["2"])
        self.assertEqual(gone[0]["why"], "no longer on the board")

    def test_gone_but_still_on_board_says_the_filter_dropped_it(self):
        _, _, gone = self.delta([rec("1")], [[], [{"source": "greenhouse", "company": "Acme", "source_id": "1",
                                                   "title": "Educator", "kept": False, "reject_reason": "no-keyword-match"}]])
        self.assertIn("no longer kept by the filter: no-keyword-match", gone[0]["why"])

    def test_unavailable_source_is_unknown_not_gone(self):
        src = [{"company": "Acme", "provider": "greenhouse", "status": "unavailable", "reason": "HTTP 404"}]
        _, _, gone = self.delta([rec("1")], [[rec("9", company="Other")], (), src])
        self.assertTrue(gone[0]["why"].startswith("unknown: source unavailable"))

    def test_ad_text_change_is_reported_without_storing_the_text(self):
        _, changed, _ = self.delta([rec("1")], [[rec("1", text="a different ad")]])
        self.assertEqual(changed[0]["changes"][0]["field"], "ad text")
        self.assertIsNone(changed[0]["changes"][0]["before"])
        self.assertNotIn("text", pd.slim(rec("1")))

    def test_state_only_keeps_rows_of_unreadable_sources(self):
        make_run(self.root, "2026-10-01", [rec("1"), rec("2", company="Down")],
                 sources=[{"company": "Acme", "status": "ok"}, {"company": "Down", "status": "ok"}])
        base, _ = pd.baseline_from_runs(self.root, "2026-10-02")
        d2 = make_run(self.root, "2026-10-02", [rec("1")], sources=[{"company": "Acme", "status": "ok"},
                                                                      {"company": "Down", "status": "unavailable"}])
        path = pd.write_state(self.root, pd.load_run(d2), base)
        keys = set(json.load(open(path))["candidates"])
        self.assertEqual(keys, {"greenhouse:1", "greenhouse:2"})

    def test_a_new_filter_key_is_not_reported_as_a_change(self):
        old = rec("1")
        newer = rec("1", matched={**old["matched"], "connector": None, "materials": None, "title_only": False})
        self.assertEqual(pd.fingerprint(pd.slim(old)), pd.fingerprint(pd.slim(newer)))
        changed_words = rec("1", matched={"role_title": ["educator", "instructor"], "kept_because": "role word in title"})
        self.assertNotEqual(pd.fingerprint(pd.slim(old)), pd.fingerprint(pd.slim(changed_words)))

    def test_full_snapshots_are_never_committable(self):
        for bad in ("runs/2026-10-18/all-jobs-2026-10-18.json", "runs/2026-10-18/jobs-of-interest-2026-10-18.csv",
                    "runs/2026-10-18/raw/greenhouse-x.json", "monitor.db", "runs/2026-10-18/quality-report-2026-10-18.md"):
            self.assertTrue(pd.NEVER_COMMIT.search(bad), bad)
        for ok in ("runs/2026-10-18/delta-2026-10-18.md", "runs/published-state.json"):
            self.assertFalse(pd.NEVER_COMMIT.search(ok), ok)


if __name__ == "__main__":
    unittest.main()
