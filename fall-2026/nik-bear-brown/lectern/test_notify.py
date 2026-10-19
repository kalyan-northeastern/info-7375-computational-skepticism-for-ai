#!/usr/bin/env python3
"""Tests for notify.py: what gets posted to the public channel, and what never does."""
import json, os, tempfile, unittest

import notify


def row(i, co="Anthropic", title="Educator", **kw):
    r = {"source": "greenhouse", "company": co, "source_id": str(i), "title": title, "location_text": "Remote",
         "url": f"https://jobs.example.com/{i}", "matched": {"role_title": ["educator"], "kept_because": "role word in title"}}
    r.update(kw)
    return r


class Notify(unittest.TestCase):
    def test_unwatched_companies_are_never_posted(self):
        rows, msgs = notify.build_messages([row(1), row(2, co="Stripe")], watched={"Anthropic"})
        self.assertEqual([r["company"] for r in rows], ["Anthropic"])
        self.assertNotIn("Stripe", "".join(msgs))

    def test_priority_companies_come_first(self):
        rows, _ = notify.build_messages([row(1, co="Replit"), row(2, co="Figma"), row(3, co="Anthropic")], {"Replit", "Figma", "Anthropic"})
        self.assertEqual([r["company"] for r in rows], ["Anthropic", "Figma", "Replit"])

    def test_already_posted_listings_are_skipped(self):
        rows, _ = notify.build_messages([row(1), row(2)], {"Anthropic"}, already={"greenhouse:1"})
        self.assertEqual([r["source_id"] for r in rows], ["2"])

    def test_long_lists_are_chunked_and_the_footer_ends_the_last(self):
        _, msgs = notify.build_messages([row(i, title="T" * 90) for i in range(40)], {"Anthropic"})
        self.assertGreater(len(msgs), 1)
        self.assertTrue(all(len(m) <= notify.MAX_CHUNK + 400 for m in msgs))
        self.assertTrue(msgs[-1].endswith(notify.FOOTER))

    def test_newly_watched_companies_are_marked_so_they_are_not_read_as_fresh(self):
        _, msgs = notify.build_messages([row(1, co="Replit")], {"Replit"}, first_time={"Replit"})
        self.assertIn("(newly watched)", msgs[0])

    def test_a_message_with_a_local_path_or_email_is_refused(self):
        self.assertFalse(notify.post("t", "see /Users/someone/file", send=False))
        self.assertFalse(notify.post("t", "write to a.b@example.com", send=True))

    def test_a_dry_run_records_nothing_as_posted(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "posted.json")
            n = notify.post_new([row(1)], {"Anthropic"}, set(), p, "run x", send=False)
            self.assertEqual(n, 0)
            self.assertFalse(os.path.exists(p))


if __name__ == "__main__":
    unittest.main()
