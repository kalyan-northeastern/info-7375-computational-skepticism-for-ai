#!/usr/bin/env python3
"""Tests for collectors/biolabs.py with canned pages: no network."""
import io, os, sys, unittest, urllib.error

for _p in (os.path.dirname(os.path.abspath(__file__)), os.path.dirname(os.path.dirname(os.path.abspath(__file__)))):
    if os.path.exists(os.path.join(_p, "lectern_paths.py")):
        sys.path.insert(0, _p)
        break
import lectern_paths as lp
from collectors import biolabs as b

SEED = """<html><body><a href="/labs/smith-lab?utm_source=x#top">Smith Lab</a><a href="/donate/now">Donate to the lab fund</a>
<a href="https://mychart.example.edu/MyChart/">Patient group portal</a><a href="/about">About the labs</a><a href="/files/x.pdf">Lab handbook</a>
<a href="https://other.org/lab">Other Lab</a><a href="mailto:a@b.org">Lab contact</a><a href="/groups/genomics">Genomics Group</a></body></html>"""
LAB = """<html><head><meta name="description" content="We study single-cell RNA-seq and build Nextflow pipelines on HPC."></head><body><p>Short.</p>
<a href="/people">People</a><a href="mailto:pi@example.edu?subject=hi">email</a><p>Text with [at] and (dot) obfuscation: nobody at example dot org.</p></body></html>"""


class FakeResp:
    def __init__(self, body, status=200, ctype="text/html"):
        self.body, self.status, self.headers = body.encode(), status, {"Content-Type": ctype}
    def read(self): return self.body
    def __enter__(self): return self
    def __exit__(self, *a): return False


def opener(pages, robots="User-agent: *\nAllow: /\n"):
    calls = []
    def f(req, timeout=0):
        url = req.full_url
        calls.append((url, req.get_header("User-agent")))
        if url.endswith("/robots.txt"):
            if robots is None:
                raise urllib.error.HTTPError(url, 404, "nf", {}, io.BytesIO(b""))
            return FakeResp(robots, ctype="text/plain")
        if url in pages:
            return FakeResp(pages[url])
        raise urllib.error.HTTPError(url, 404, "nf", {}, io.BytesIO(b"<a href='/trap'>lab trap link</a>"))
    f.calls = calls
    return f


class Biolabs(unittest.TestCase):
    def test_canonical_url_drops_fragments_and_tracking_and_rewrites_the_childrens_host(self):
        self.assertEqual(b.canonical_url("https://x.edu/labs/a?utm_source=z&keep=1#top"), "https://x.edu/labs/a?keep=1")
        self.assertIn("research.childrenshospital.org/research-units/", b.canonical_url("https://www.childrenshospital.org/research-units/x"))

    def test_harvest_keeps_lab_links_and_drops_portals_fundraising_pdfs_mailto_and_other_organisations(self):
        r = b.Reader(delay=0, opener=opener({"https://labs.example.edu/dir": SEED}))
        status, labs = b.harvest(r, "https://labs.example.edu/dir", 50)
        urls = [u for _, u in labs]
        self.assertEqual(urls, ["https://labs.example.edu/labs/smith-lab", "https://labs.example.edu/groups/genomics"])

    def test_data_signal_counts_whole_words_only(self):
        n, hits = b.data_signal("We use scRNA-seq, single-cell methods, HPC and a bam file; also whpc and gambam do not count.")
        self.assertEqual(hits, ["bam", "hpc", "scrna-seq", "single-cell"])

    def test_a_disallowed_page_is_not_fetched_and_is_recorded_as_blocked(self):
        o = opener({"https://labs.example.edu/labs/x": LAB}, robots="User-agent: *\nDisallow: /labs/\n")
        rec = b.read_lab(b.Reader(delay=0, opener=o), "X Lab", "https://labs.example.edu/labs/x", "seed")
        self.assertEqual(rec["status"], "blocked_by_robots")
        self.assertFalse([c for c in o.calls if c[0].endswith("/labs/x")])

    def test_an_unreadable_robots_file_means_do_not_read(self):
        def broken(req, timeout=0):
            if req.full_url.endswith("/robots.txt"):
                raise urllib.error.HTTPError(req.full_url, 403, "no", {}, io.BytesIO(b""))
            return FakeResp(LAB)
        rec = b.read_lab(b.Reader(delay=0, opener=broken), "X", "https://labs.example.edu/a", "s")
        self.assertEqual(rec["status"], "blocked_by_robots")

    def test_the_user_agent_says_what_it_is_and_an_error_page_is_never_parsed_for_links(self):
        o = opener({})
        r = b.Reader(delay=0, opener=o)
        status, labs = b.harvest(r, "https://labs.example.edu/gone", 10)
        self.assertEqual((status, labs), ("404", []))
        self.assertTrue(all("lectern-biolabs" in ua for _, ua in o.calls))

    def test_a_lab_record_has_the_pages_own_words_a_score_and_only_published_mailto_links(self):
        o = opener({"https://labs.example.edu/a": LAB, "https://labs.example.edu/people": "<a href='mailto:pi2@example.edu'>x</a>"})
        rec = b.read_lab(b.Reader(delay=0, opener=o), "A", "https://labs.example.edu/a", "s")
        self.assertEqual(rec["what_the_lab_says_verbatim"], "We study single-cell RNA-seq and build Nextflow pipelines on HPC.")
        self.assertEqual(rec["matched"], ["hpc", "nextflow", "rna-seq", "single-cell"])
        self.assertEqual(rec["published_mailto"], ["pi2@example.edu", "pi@example.edu"])      # the obfuscated text was NOT decoded
        self.assertEqual(rec["people_page_url"], "https://labs.example.edu/people")

    def test_the_verbatim_field_is_at_most_300_characters(self):
        long = "<p>" + "word " * 200 + "</p>"
        rec = b.read_lab(b.Reader(delay=0, opener=opener({"https://labs.example.edu/a": "<html>" + long + "</html>"})), "A", "https://labs.example.edu/a", "s", with_people=False)
        self.assertLessEqual(len(rec["what_the_lab_says_verbatim"]), 300)


if __name__ == "__main__":
    unittest.main()
