# 02 · Filter

**What it does.** Takes the collected postings, drops repeats of the same (source, id), marks any posting with no title, link or parseable date, and applies the keyword rules: keep on a role word in the title, enough topic words in the body, evidence that the job makes teaching materials for a named audience, or an account or partnership title whose body names higher education. Every posting leaves with a decision and a reason.

**Output (one item):** `{date, keywords_version, sources, watched, counts: {postings_fetched, postings_unique, kept, rejected: {reason: n}}, records: [...]}`, each record with `kept`, `matched` (the words and which rule) and `reject_reason`.

**Python counterpart:** `judge()` and the per-posting checks in `collect.py`. **Logic:** `shared/lib/judge.js`. **Rules:** `shared/keywords.json` (v0.5.2), copied from the Python master; the rules are never edited in the workflow.

**Tested.** Headless: all 12 synthetic records identical to the Python's, covering all four keep rules and the reject reasons (no keyword, one topic word, no link, no date, duplicate). Real data: **all 2,465 postings from the 2026-10-18 run identical** to the Python on every field, keep decision and matched words (81 kept by each).

**Limits.** A filter agreement says the port is faithful, not that the filter is right: the rules' own measured weaknesses (see `keywords.json`) carry over unchanged.
