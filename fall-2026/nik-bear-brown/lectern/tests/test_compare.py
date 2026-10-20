#!/usr/bin/env python3
"""Tests for compare/: the run-format check, the run comparison and the heartbeat."""
import json, os, sys, tempfile, unittest

for _p in (os.path.dirname(os.path.abspath(__file__)), os.path.dirname(os.path.dirname(os.path.abspath(__file__)))):
    if os.path.exists(os.path.join(_p, "lectern_paths.py")):
        sys.path.insert(0, _p)
        break
import lectern_paths as lp
sys.path.insert(0, os.path.join(lp.ROOT, "compare"))
import check_run_format as crf, compare_runs as cr, heartbeat as hb


def rec(i, kept, **kw):
    r = {"source": "greenhouse", "company": "X", "source_id": str(i), "title": "T", "url": "https://x/" + str(i), "date_posted": "2026-10-01", "kept": kept, "matched": {} if kept else None}
    r.update(kw); return r


def write_run(folder, all_recs, kept_recs):
    os.makedirs(folder, exist_ok=True)
    json.dump({"records": all_recs}, open(os.path.join(folder, "all-jobs-2026-10-20.json"), "w"))
    json.dump({"records": kept_recs}, open(os.path.join(folder, "jobs-of-interest-2026-10-20.json"), "w"))


class Compare(unittest.TestCase):
    def test_the_real_run_in_this_repository_passes_the_format_check(self):
        run = os.path.join(lp.RUNS, "2026-10-18")
        if not os.path.isdir(run):
            self.skipTest("no tracked run folder")
        problems, seen = crf.check_run(run)
        self.assertEqual(problems, [])

    def test_a_missing_field_and_a_wrong_type_are_reported(self):
        with tempfile.TemporaryDirectory() as d:
            bad = rec(1, True); del bad["url"]
            wrong = rec(2, False); wrong["kept"] = "yes"
            write_run(d, [bad, wrong], [dict(rec(1, True), matched="no")])
            problems, _ = crf.check_run(d)
            self.assertTrue(any("missing 'url'" in p for p in problems))
            self.assertTrue(any("'kept' is str" in p for p in problems))
            self.assertTrue(any("'matched' is str" in p for p in problems))

    def test_a_folder_without_the_files_is_a_problem_not_a_pass(self):
        with tempfile.TemporaryDirectory() as d:
            problems, _ = crf.check_run(d)
            self.assertEqual(len(problems), 2)

    def test_agreement_counts_both_sets_and_the_disagreements(self):
        ref = {("greenhouse", str(i)): rec(i, i < 3) for i in range(6)}
        other = {("greenhouse", str(i)): rec(i, i in (0, 1, 4)) for i in range(1, 8)}
        c = cr.compare(ref, other)
        self.assertEqual((c["both"], len(c["only_reference"]), len(c["only_form"])), (5, 1, 2))
        self.assertEqual([k[1] for k in c["disagree"]], ["2", "4"])
        self.assertEqual(c["agreement_rate"], 0.6)

    def test_the_report_opens_with_a_summary_and_calls_disagreements_questions(self):
        ref = {("g", "1"): rec(1, True, source="g")}; other = {("g", "1"): rec(1, False, source="g")}
        text = cr.report(cr.compare(ref, other), ref, other)
        self.assertIn("## Executive summary", text.split("\n\n")[1] + "\n\n" + text.split("\n\n")[2])
        self.assertIn("question", text)

    def test_the_heartbeat_names_a_tool_that_left_no_log_today(self):
        with tempfile.TemporaryDirectory() as d:
            for t, has in (("muse", True), ("grok-bot", False)):
                os.makedirs(os.path.join(d, t))
                if has:
                    open(os.path.join(d, t, "run-2026-10-21.md"), "w").write("x")
            self.assertEqual(hb.missing(d, "2026-10-21"), ["grok-bot"])
            self.assertEqual(hb.missing(d, "2026-10-21", ["muse", "dots"]), ["dots"])


if __name__ == "__main__":
    unittest.main()
