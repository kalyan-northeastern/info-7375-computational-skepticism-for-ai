# Week 2 — The Boondoggle Report
**Application:** Lectern
**Course:** Computational Skepticism for AI
**Date:** 2026-10-11

---

# Part 1 — The SDD
# /v0 — Problem Formulation Gate
**Date:** 2026-10-11
**Mode:** interactive

---

## Question 1 — Ecosystem

**Gru:** What ecosystem or platform does this proposal live inside? Two sentences maximum. This is context — not the proposal itself.

**Fellow:** The public job-board APIs of ten companies selling AI to universities (Greenhouse, Ashby, SmartRecruiters, plus custom career-page APIs at Google, Amazon, Microsoft, and Meta). The postings are public; no authentication exists or is used. The operator is a single researcher running a daily monitoring routine from a Linux VM, with outputs pushed to GitHub.

## Question 2 — Existing components touched

**Gru:** What already exists inside that ecosystem that this proposal touches, depends on, or extends? Name the specific components, not the general system.

**Fellow:**
- Greenhouse Boards API (`boards-api.greenhouse.io`) — Anthropic, Figma, Miro
- Ashby API (`api.ashbyhq.com`) — OpenAI, Notion
- SmartRecruiters API — Canva
- Google Careers search (server-rendered HTML, query params)
- Amazon Jobs search JSON endpoint (`amazon.jobs/en/search.json`)
- Microsoft Careers PCSX search API (`apply.careers.microsoft.com`)
- Meta Careers (Playwright/GraphQL — exists in code, unrunnable from this environment)

## Question 3 — The one sentence

**Gru:** In one sentence — what are you proposing to ADD? Not what problem exists. What is the new thing? Format: "[THING] is a [WHAT] inserted [WHERE] that produces [OUTPUT]."

**Fellow (first attempt):** "A system to monitor job boards for teaching-related postings at AI companies."

**Gru — PUSHBACK:** That's a goal, not a thing. "A system to monitor" names what you want, not what you're building. What is the component? What does it take in, what does it produce, where does it sit? The sentence must name the thing, the insertion point, and the output — or we have no foundation.

**Fellow (second attempt):** "Lectern is a scheduled collection-and-diff pipeline inserted between ten companies' public job-board APIs and a SQLite state store that produces daily new/closed posting diffs with trust-scored run health and teaching-relevance filtering."

**Gru:** That names the thing (Lectern), the insertion point (between the board APIs and the SQLite store), and the output (daily diffs, trust scores, relevance filtering). One question before I accept it: "teaching-relevance filtering" — is that a keyword filter or a judgment? Name it precisely or it becomes a weasel word in every downstream section.

**Fellow:** Keyword filter. A fixed keyword set matched against title and description text. No ML, no judgment. The filter's output is "kept for review," not "is teaching-related" — the human makes that call.

**Gru:** Accepted, with that correction recorded. The sentence stands as:

---

## V0 SUMMARY

**Ecosystem:** The public job-board APIs of ten companies selling AI to universities (Anthropic, Figma, OpenAI, Google, Notion, Meta, Microsoft, Amazon/AWS, Canva, Miro), accessed without authentication from a Linux VM by a single researcher-operator, with outputs pushed to GitHub.

**Existing components touched:** Greenhouse Boards API (Anthropic, Figma, Miro); Ashby API (OpenAI, Notion); SmartRecruiters API (Canva); Google Careers server-rendered search; Amazon Jobs search JSON endpoint; Microsoft Careers PCSX search API; Meta Careers GraphQL (in code, unrunnable from this environment).

**Proposal:** Lectern is a scheduled collection-and-diff pipeline inserted between ten companies' public job-board APIs and a SQLite state store that produces daily new/closed posting diffs with trust-scored run health and keyword-based teaching-relevance filtering (candidates kept for human review, not auto-classified).

**Confirmed by fellow:** yes — 2026-10-11. Proceed to /v1.
# /v1 — Problem Intake
**Date:** 2026-10-11
**Prerequisite:** /v0 confirmed

---

## Intake answers

**1. Name of the system:** Lectern

**2. Problem (one sentence):** The education-AI advocate role Bear wants almost never gets posted, so there is no direct job signal to watch — but the hiring patterns of companies selling AI to universities are observable evidence of where their institutional attention is going.

**3. Who has this problem:** Bear, an independent AI-education consultant. Current workflow: manually checking ten companies' career pages for teaching-related roles, which is infeasible daily across ~17,000 postings. What breaks: without systematic collection, a newly posted education/advocate/enablement role — the trigger for a pitch — is found by luck or not at all, and there is no historical record of what appeared and disappeared.

**4. What does Lectern give that manual checking does not:** A complete daily inventory with identity. Every posting gets a source-native ID; the system remembers what it has seen, so "new since yesterday" and "closed after two consecutive absences" are computed, not eyeballed. The keyword filter reduces ~17,000 postings to ~60 candidates for human review.

**5. Category:** Scheduled data-collection and change-detection pipeline. Not a job board, not a recommender, not an analytics dashboard.

**6. Deployment target and why:** A single Linux VM (the operator's personal compute), cron-triggered or manually triggered. No multi-user service, no hosted infrastructure — because the only consumer is the operator, and the blast radius of a failure is one missed day of data.

**7. Build scale:** Solo developer, already built over ~1 week. Maintenance: minutes per day (trigger the recipe, read the report).

**8. Three systems relied on — and the specific capability each must integrate with:**
- The ten companies' public board APIs — the listing inventory itself (title, location, description URL, source-native ID).
- SQLite — durable state: jobs table (first_seen/last_seen), runs table (fetched/reported/trusted per run).
- GitHub — the shared surface: dated run outputs and logs pushed daily so the work is visible off-VM.

**9. One system explicitly NOT replicated:** A general job aggregator (Indeed, LinkedIn). Rejected: apply-side affordances, relevance ranking, user accounts. Lectern never helps anyone apply to a job; it reads listings as evidence of company interest, which is a different instrument pointed at the same data.

---

## Problem Summary

Lectern is a scheduled collection-and-diff pipeline for a single researcher-operator, that solves the unobservability of hiring-pattern signals at ten AI companies selling to universities through daily source-native-ID-tracked collection with trust-scored runs. It occupies the space between a manual bookmark-checking routine and a commercial sales-intelligence feed, and it succeeds when the operator can name, for any given day, exactly which postings are new, which closed, and whether the collection itself is trustworthy — without re-reading seventeen thousand listings.

**Gru:** That summary could still describe a generic change-detection service. The one question that makes it specific: what does "trust-scored" mean here, in one mechanism?

**Fellow:** A run is trusted only if it fetched ≥90% of the source-reported total AND ≥70% of the previous trusted run's count; a job is closed only after missing from two consecutive trusted runs. Untrusted runs update what they saw but never close jobs.

**Gru:** Recorded. That mechanism is the system's identity — it goes into /v2 as a principle, not just a detail.

---

## Biggest unresolved question

Whether the Meta collector can ever run from this environment (Chromium's network tunnel is blocked by the egress proxy) — and if not, whether Meta stays in the watch list as an unwired aspiration or is dropped from the /v0 proposal's "ten companies" claim. The proposal currently overclaims by one.

---

## Required personal addition (after /v1 Problem Summary)

# Required addition after /v1 — DRAFT FOR BEAR (rewrite in your own voice)

> **[DRAFT — replace with your own words before submitting]**
> Gru's pushback changed two things about how I understood the problem. First, at /v0, my "system to monitor job boards for teaching-related postings" was sent back as a goal rather than a thing — and then the follow-up question, whether the relevance filtering was keyword matching or judgment, forced the distinction the whole project depends on: the filter produces *candidates for review*, not *teaching-related postings*. I had been using those interchangeably in my own head. Second, at /v1, being asked what "trust-scored" meant "in one mechanism" turned a vague virtue word into the 90%/70%/two-miss rule — which then became a /v2 principle rather than an implementation detail. The pattern in both cases: I arrived describing what I wanted to be true, and Gru held the line until I stated what the system actually does. If Gru had accepted the first formulations, the SDD would have documented my intentions instead of my pipeline.
# /v2 — Architecture Principles
**Date:** 2026-10-11
**Prerequisite:** /v1 confirmed

---

## Principle 1 — Source-native identity

**Commitment:** Every posting is identified by the source's own ID (Greenhouse job ID, Ashby posting ID, Amazon ICIMS ID). Never a title hash, never a generated key.

**Honors:** A re-run of the same board produces the same IDs; diffs are computed on identity, not fuzzy matching.
**Violates:** Hashing title+location as the key — two postings with the same title at different offices collide, and a reworded title looks like a new job.
**Failure state if ignored:** New/closed diffs become noise; the operator cannot trust "14 new" to mean 14 new postings.

## Principle 2 — Trust is a claim about the run, not the world

**Commitment:** Every run states a falsifiable claim about its own completeness (fetched ≥90% of source-reported total AND ≥70% of the previous trusted run). A run that fails the claim is recorded as untrusted: it updates what it saw, but it never closes jobs.

**Honors:** The October 9 Microsoft pull (1,746 of 2,414 reported) was recorded, kept its partial data, and closed nothing.
**Violates:** Treating any completed fetch as authoritative — a throttled run would mass-"close" hundreds of live postings.
**Failure state if ignored:** A single bad run deletes the historical record it was supposed to extend. The diff becomes a measure of collection failure, not hiring change.

## Principle 3 — Two misses before burial

**Commitment:** A job is marked closed only after it is absent from two consecutive trusted runs. One absence is a data point; two is a pattern.

**Honors:** A posting missing from one run due to a transient API gap stays open; genuinely removed postings close within two days.
**Violates:** Closing on first absence — transient failures (the Microsoft throttle bucket, a Greenhouse 500) would generate false "closed" events daily.
**Failure state if ignored:** The operator chases ghosts — "closed" postings that reappear tomorrow, destroying confidence in the diff.

## Principle 4 — No credentials, no login, no exceptions

**Commitment:** All collection uses unauthenticated public endpoints. If a source requires login, it is not collected — it is recorded as unreachable and the proposal's company count is reduced.

**Honors:** Greenhouse, Ashby, SmartRecruiters, Google, Amazon, Microsoft PCSX — all public.
**Violates:** Adding a session cookie to reach a gated board — creates a credential to protect, a terms-of-service question, and a failure mode (session expiry) with no operator to notice it promptly.
**Failure state if ignored:** The pipeline silently depends on a login session; when it expires, runs fail in ways that look like "no new jobs" rather than "collection broken."

---

## Principle Collision Test

**Gru:** Principles 2 and 4 are on a collision course, and it's already live. Principle 4 says collect only what's public; Principle 2 says don't trust incomplete runs. Microsoft's API is public but throttles this VM's IP aggressively — so you get runs that are public-but-incomplete, failing Principle 2's 90% bar repeatedly. Three dead retries. Which principle is PRIMARY when they conflict — do you keep hammering a throttling endpoint (straining Principle 4's "respect the source" spirit), or do you accept untrusted partial data indefinitely (hollowing out Principle 2)?

**Fellow:** Principle 2 is primary. An untrusted run that records what it saw is honest; a forced complete run against a throttling source risks getting the IP blocked entirely, which would violate Principle 4's deeper intent (don't jeopardize access). The collision resolves as: keep collecting what the source gives, mark it untrusted, and carry the caveat. The evening retry uses backoff and detachment, not aggression.

**Gru:** Recorded. Principle 2 primary over Principle 4's completeness implications. Note the asymmetry: Principle 4 constrains *method* (no login), Principle 2 constrains *interpretation* (don't overclaim). They collide only on effort, not on ethics — that's why the resolution holds.

Second collision, latent: Principle 1 (source-native IDs) vs. the real world — what happens when a company migrates ATS (e.g., Ashby → Greenhouse) and every ID changes overnight? The diff would report thousands of "new" and thousands of "closed" simultaneously.

**Fellow:** Logged as an open question. No migration has been observed. If it happens, the correct response is a declared re-baselining run, not silent ID remapping — remapping would violate Principle 1's spirit (identity comes from the source, not from our matching cleverness).

**Gru:** Good. That goes in the Open Questions Log (/p5) when we get there. Principles locked.
# /v3 — Core User Flows
**Date:** 2026-10-11
**Prerequisite:** /v2 principles locked

---

## PRIMARY FLOW — the daily recipe (happy path)

1. Operator triggers the recipe (types "run daily recipe").
2. For each of the 6 ATS boards: `collect.py` fetches all postings via the board API, paginating to the source-reported total. Each posting is stored with its source-native ID, title, locations, URL, posted date, and description.
3. Keyword filter runs against title + description: matches are written to `jobs-of-interest-{date}.json/.csv`; everything goes to `all-jobs-{date}.json/.csv`.
4. For Google, Amazon, Microsoft: `run_daily.py` fetches listings into the SQLite monitor. Each run records fetched count, source-reported total, and the trust verdict (≥90% of reported AND ≥70% of previous trusted run).
5. Monitor diffs source-native IDs against prior state: unseen IDs get `first_seen` (and descriptions fetched only for these); IDs absent from two consecutive trusted runs are marked closed.
6. One health line per source is printed: fetched, reported, new, closed, trusted.
7. Dated outputs and the run log are pushed to GitHub.
8. Operator reads the report: new postings of interest, closed postings, and any untrusted runs needing attention.

**Gru:** Step 2 says "paginating to the source-reported total." What does the collector do when the source-reported total is itself suspect — Amazon reporting exactly 10,000? "Paginate to the total" assumes the total is honest.

**Fellow:** It doesn't assume honesty; it assumes the total is the source's claim. The trust rule (Principle 2) measures fetched *against the claimed total* — so if the source caps at 10,000, a 10,000-fetch run is "trusted" relative to the claim, and the cap question is carried as a known unknown, not resolved. The flow records the claim; it doesn't validate it.

**Gru:** Acceptable — but that means Principle 2's trust is trust-relative-to-the-source's-claim, not trust-about-the-world. Say that in /s1 when you document the monitor. Continue.

## INTEGRATION FLOW — system to system

| Touchpoint | Protocol | Data exchanged | Failure owner |
|---|---|---|---|
| Greenhouse Boards API | HTTPS JSON, no auth | Job list + detail per board (Anthropic, Figma, Miro) | Source (rate limit/deprecation); operator on contract change |
| Ashby API | HTTPS JSON, no auth | Postings (OpenAI, Notion) | Source |
| SmartRecruiters API | HTTPS JSON, no auth | Postings (Canva) | Source |
| Google Careers | HTTPS HTML scrape, query params | Server-rendered listing cards | Operator (markup change breaks parsing) |
| Amazon Jobs | HTTPS JSON (`search.json`) | Posting records, `hits` total | Source |
| Microsoft PCSX | HTTPS JSON | Search results pages | Shared: source throttles; operator backs off |
| Meta Careers | Playwright + GraphQL | — (no data; tunnel blocked) | Environment (documented, not retried blindly) |
| SQLite (local) | File | jobs + runs tables | Operator (backup = GitHub push of outputs, not the DB) |
| GitHub | HTTPS API | Dated outputs, logs | Operator |

**Failure behavior:** A single source failing does not block the others — each collector runs independently, and the recipe reports per-source health. A source that fails three consecutive days gets flagged in the report; it is not silently dropped from the watch list.

## ADMINISTRATIVE FLOW — operator path

- **Configure:** Edit `sources.json` (boards), `keywords.json` (filter terms), or collector parameters. No UI; the config files are the interface.
- **Monitor:** Read the daily health lines. `trusted=no` on any source means "yesterday's diff for this source is provisional."
- **Maintain:** When a collector breaks (markup change, API deprecation), fix the collector, note it in the run log. The SQLite DB is never edited by hand — corrections go through re-runs.
- **Recover:** If the DB is lost, the dated GitHub outputs contain every run's postings; state can be rebuilt by re-ingesting them. The DB is a working store, not the archive — the archive is Git.

---

## Flow Honesty Test

**Gru:** If this flow were a command-line prototype with no UI, no branding, no secondary features — just the collectors, the SQLite diff, and a printed report — would it solve the stated problem?

**Fellow:** Yes. That *is* the system. There is no UI, no branding, no secondary features. The prototype and the product are the same thing — which is either admirable scope discipline or an admission that this never needed to be more than scripts. For one operator watching ten boards, scripts are the correct scope.

**Gru:** Recorded. That answer also bounds /p1 later: anything that isn't the collectors, the diff, or the report needs to justify itself against this test.
# /v4 — User and Business Needs
**Date:** 2026-10-11
**Prerequisite:** /v3 flows documented

---

## Needs

**N1 — Daily new-posting awareness (User)**
Bear must be able to list every posting that appeared since the previous run, without re-reading the full inventory.
*Pass/fail:* The daily report's "new" list, intersected with a manual spot-check of one board, contains no posting the board shows as new that the report omits.

**N2 — Reliable closure detection (User)**
Bear must be able to distinguish a posting that was actually removed from one that was merely missed by a bad fetch.
*Pass/fail:* No posting is reported closed unless it was absent from two consecutive trusted runs (verifiable in the runs table).

**N3 — Collection honesty (User)**
Bear must be able to tell, for each source each day, whether the collection itself succeeded — not just how many postings it returned.
*Pass/fail:* Every run row carries fetched, reported, and trusted; a run with fetched < 90% of reported is never labeled trusted.

**N4 — Teaching-signal triage (User)**
Bear must be able to review the day's teaching-relevant candidates in under 15 minutes.
*Pass/fail:* The keyword filter reduces the daily inventory (~17,000 postings) to a candidate list small enough to read in one sitting (observed: ~57–60). The list is candidates for review, not classifications — Bear makes the relevance call.

**N5 — Historical continuity (User)**
Bear must be able to answer "when did this posting first appear?" for any posting in the inventory.
*Pass/fail:* Every job row carries first_seen; a query for any known posting returns a date matching the dated output file in which it first appeared.

**N6 — Off-VM visibility (Operator)**
Bear must be able to see every run's outputs without access to the VM.
*Pass/fail:* Dated JSON/CSV outputs and the run log are pushed to GitHub daily; nothing the operator needs lives only on the VM.

**N7 — Independent verifiability (Business)**
A third party (e.g., a Claude Code session on a fresh clone) must be able to verify the system's claims from the committed artifacts alone.
*Pass/fail:* The state-check procedure (fresh clone → run the four verification prompts) reproduces the reported counts from committed files without needing the VM's database.

**N8 — Bounded blast radius (Business)**
A failure in any one source's collector must not corrupt another source's data or the historical record.
*Pass/fail:* Each collector writes only its own source's rows; the trust rule prevents untrusted runs from closing jobs; verified by the October 9 Microsoft partial pull (1,746/2,414) closing zero jobs.

---

**Gru:** N4's pass/fail says "~57–60" candidates. That's an observation, not a test. What if the keyword set drifts and the list grows to 400 — does N4 fail? Name the actual threshold or admit the need is "small enough to read," which is a judgment, not a test.

**Fellow:** It's a judgment bounded by time: "reviewable in under 15 minutes." If the list grows past what 15 minutes covers, the need fails and the keyword set gets tightened. The number isn't the test; the timebox is.

**Gru:** Accepted — but write that. "Under 15 minutes of operator review" is the testable form.

**Gru:** N7 is the most interesting need here and the least typical. You're requiring that the system be verifiable by a *different AI* from its artifacts. Most SDDs would call that out of scope. Why is it a Need and not a nice-to-have?

**Fellow:** Because the system's output is evidence for claims Bear makes publicly (in the course, in the brief, potentially to vendors). If the counts can't be independently reproduced, they're assertions, not evidence. For a skepticism course's instrument, verifiability isn't polish — it's the product.

**Gru:** Recorded. That justification also answers Prompt D's "why verification matters" before you've written it. Phase 1 gate: problem summary confirmed, principles locked, primary flow documented, needs written and mapped. Confirm to proceed to systems and architecture.

**Fellow:** Confirmed.
# /s1 — Core Component Documentation
**Date:** 2026-10-11
**Prerequisite:** Phase 1 gate confirmed (/v1–/v4)

---

## C1 — ATS board collector (`lectern/collect.py`)

**Maps to:** N1 (new-posting awareness), N5 (historical continuity), N6 (off-VM visibility)
**Problem it solves:** Six of the ten boards speak standard ATS APIs; without a unified pull, the operator would query three different API shapes by hand.
**How it works:** Reads `sources.json` (board list); for each board, paginates the board API to the reported total; stores each posting with source-native ID, title, locations, URL, posted_at, description. Writes dated `all-jobs-{date}.json/.csv`. Throttles with jitter between requests; no auth.
**Inputs:** `sources.json`, board API responses.
**Outputs:** Dated JSON/CSV per run; per-posting records with native IDs.
**Error signals:** HTTP errors, pagination shortfall vs. reported total → logged, run continues to next board.
**Retry behavior:** None within a run; the next daily run re-pulls. Idempotent (same IDs).
**Principle alignment:** P1 (native IDs as keys), P4 (no auth).
**Flow placement:** Primary flow step 2.
**Edge cases:**
1. Board migrates ATS (IDs change en masse) → diff explodes; declared re-baseline required (open question, /v2).
2. Board API deprecates a field (e.g., `posted_at` disappears) → record stored without it; no failure, but N5 weakens for that board.
3. Reported total is 0 (board emptied or API error) → 0 fetched of 0 reported; logged, not trusted as "no jobs."
**Scope boundary:** Does not diff, does not score trust, does not filter. It collects. The monitor and the filter are separate components.

## C2 — Keyword relevance filter (`keywords.json` + filter stage)

**Maps to:** N4 (teaching-signal triage)
**Problem it solves:** ~17,000 postings/day is unreadable; ~60 candidates is reviewable in 15 minutes.
**How it works:** Fixed keyword set (teaching, education, enablement, training, academy, advocate, curriculum, faculty, student, learning) matched case-insensitively against title + description. Matches → `jobs-of-interest-{date}.json/.csv`. No scoring, no ranking, no ML.
**Inputs:** `all-jobs-{date}.json`, `keywords.json`.
**Outputs:** Candidate list (~57–60/day observed).
**Principle alignment:** P2-adjacent — the filter makes no truth claim; output is labeled "candidates for review," never "teaching-related postings."
**Flow placement:** Primary flow step 3.
**Edge cases:**
1. Keyword set too broad (e.g., "learning" matches "machine learning" everywhere) → candidate list balloons past the 15-minute review budget; N4 fails → tighten the set.
2. A genuinely relevant posting uses none of the keywords ("DevRel for EDU") → missed; accepted as filter recall limit, not a bug. The full inventory remains searchable.
3. Description fetch failed for a posting → matched on title only; flagged in output.
**Scope boundary:** Does not classify, does not rank, does not learn. The relevance judgment is the human's (N4's 15-minute review).

## C3 — Custom collectors (`collectors/google.py`, `amazon.py`, `microsoft.py`)

**Maps to:** N1, N3 (collection honesty), N5
**Problem it solves:** Three boards have no standard ATS API; each needs a bespoke fetch (Google: HTML scrape; Amazon: search JSON; Microsoft: PCSX JSON).
**How it works:** Each returns `(jobs, reported_total)` with source-native IDs. Pagination walks to the reported total with per-request throttling and jitter. Checkpoint file per collector allows resume after interruption.
**Inputs:** Board endpoints; checkpoint files.
**Outputs:** Job records into the monitor's SQLite store; per-run (fetched, reported, trusted).
**Error signals:** HTTP 429/500, connection resets → backoff with cooldown; checkpoint preserved.
**Retry behavior:** Resume from checkpoint on next invocation; wrap-around pagination converges to full coverage across invocations.
**Principle alignment:** P1 (native IDs), P2 (trust claim per run), P4 (no auth; throttle respect).
**Flow placement:** Primary flow step 4.
**Edge cases:**
1. Throttle bucket (Microsoft, observed Oct 9–11) → partial pulls marked untrusted; checkpoint resumes; no job closures from untrusted runs.
2. Source-reported total is a round cap (Amazon: exactly 10,000) → trust computed against the claimed total; the cap question carried as known unknown.
3. Markup/API contract change (Google HTML) → parser breaks loudly (exception, not silent empty) → operator fixes the collector.
**Scope boundary:** Does not interpret postings, does not filter. Collection only.

## C4 — Meta collector (`collectors/meta.py`)

**Maps to:** —

**Gru — FLAG:** This component maps to no Need. It produces no data: Chromium's network tunnel is blocked by the egress proxy, so it has never completed a run, and it is not wired into `run_daily.py`. Per behavioral rule 1, I am naming this before documenting it further: C4 is an unwired aspiration, not a component. It stays in the codebase as a stub; it does not appear in any flow, and the /v0 proposal's "ten companies" currently overclaims by one. Either the environment changes or the proposal drops to nine. Documented here so the gap is visible, not hidden.

**Fellow:** Acknowledged. The /v1 open question stands: Meta stays in the watch list as intent, but no claim about Meta data is made anywhere until a run completes.

## C5 — Monitor (`collectors/monitor.py`)

**Maps to:** N1, N2 (closure detection), N3, N5, N8 (blast radius)
**Problem it solves:** Collection without memory is just downloading. The monitor is the system's memory: what was seen, when, and whether the seeing was trustworthy.
**How it works:** SQLite with `jobs` (source-native ID, company, title, locations, url, first_seen, last_seen, status) and `runs` (company, run_at, fetched, reported_total, trusted) tables. New IDs → `first_seen`, descriptions fetched only for unseen IDs. Recurring IDs → `last_seen` updated. IDs absent from two consecutive trusted runs → status closed. Trust per run: fetched ≥90% of reported AND ≥70% of previous trusted run. Untrusted runs update sightings but never close.
**Inputs:** Collector outputs (jobs + reported totals).
**Outputs:** Health line per source (fetched, reported, new, closed, trusted); the diff the operator reads.
**Principle alignment:** P2 (the trust claim, implemented), P3 (two misses), P1 (native-ID keying).
**Flow placement:** Primary flow steps 4–6.
**Edge cases:**
1. First-ever run (no previous trusted run) → the 70% clause has no baseline; trust falls back to the 90% clause alone, flagged as provisional.
2. Source total drops legitimately (mass layoff postings removed) → fetched may fall below 70% of previous trusted run → run marked untrusted even though the data is real; operator judgment required to re-baseline.
3. DB lost → rebuild from dated GitHub outputs (the archive); first_seen dates recoverable to day precision.
**Scope boundary:** Does not fetch, does not filter, does not push. It remembers and judges runs. Trust here is trust-relative-to-the-source's-claim (per /v3), not trust-about-the-world.

## C6 — Runner (`collectors/run_daily.py`)

**Maps to:** N1, N6
**Problem it solves:** The collectors and the monitor are libraries; something must invoke them in the right order and report.
**How it works:** CLI entry (`--only google|amazon|microsoft`, or all). Invokes each collector, feeds results to the monitor, prints health lines. Designed to run detached (`setsid nohup`) so session death doesn't kill a long pull.
**Principle alignment:** P2 (reports trust per source); the detached-launch pattern exists because three Microsoft runs died mid-session.
**Flow placement:** Primary flow steps 4–6 (orchestration).
**Edge cases:**
1. Session killed mid-run → checkpoint files preserve progress; next invocation resumes.
2. One collector throws → others still run; the failure is reported per-source, not as a global abort.
3. Launched during a throttle bucket → 429s, backoff, checkpoint; run may complete untrusted rather than not at all.
**Scope boundary:** No collection logic, no trust logic, no filtering. Orchestration and reporting only.

## C7 — GitHub delivery (push of dated outputs + logs)

**Maps to:** N6 (off-VM visibility), N7 (independent verifiability)
**Problem it solves:** The VM is invisible to everyone including the operator's other machines; without delivery, the work might as well not exist.
**How it works:** After each run, dated JSON/CSV outputs and the run log are committed and pushed to `fall-2026/nik-bear-brown/lectern/` in the course repo. The SQLite DB itself is not committed (working store, not archive).
**Principle alignment:** N7's verifiability — a fresh clone plus the four verification prompts reproduces the counts.
**Flow placement:** Primary flow step 7.
**Edge cases:**
1. Push fails (network) → outputs remain on VM; next run's push includes them; no data loss, delayed visibility.
2. Output files grow large (descriptions for thousands of postings) → JSON per run, not appended; old runs are history, not baggage.
3. Sensitive data in a posting (rare; public boards) → boards are public by design; nothing private to leak.
**Scope boundary:** Delivery only. Not a backup system, not a dashboard, not a website.

---

**Gru:** Every component maps to a Need except C4, which is flagged, not documented. Phase 2 gate will come after /s4 in a full SDD; for this assignment the required sections stop at /s1. Proceed to /claude when ready.
# /claude — Boondoggle Score
**Date:** 2026-10-11
**System:** Lectern
**SDD Completion:** /v0–/v1–/v2–/v3–/v4–/s1 (C4 flagged unwired; /s2–/p5 not run)
**Team Claude fluency:** Level III (orchestrate multiple Claude contexts / Claude Code)
**Deployment target:** Single Linux VM, operator-triggered, GitHub as shared surface

---

## PHASE LEGEND
F = Foundation · C = Core System Skeleton · I = Integration Layer · B = Full Feature Build · H = Hardening · R = Release

---

### STEP 1 · PHASE F · HUMAN TASK
**LABOR:** Human
**SUPERVISORY CAPACITY:** [PF] — Problem Formulation. Deciding that the thing being built is a collection-and-diff pipeline reading listings as company-interest evidence — not a job board, not an aggregator — before Claude sees any technical context. This framing determines every downstream component boundary; Claude cannot choose it.
**ACTION:** Write the /v0 one-sentence proposal in the "[THING] is a [WHAT] inserted [WHERE] that produces [OUTPUT]" format. Confirm it names the thing, not the problem. Do not proceed until the sentence survives the "could this describe ten systems?" test.

---

### STEP 2 · PHASE F · CLAUDE TASK
**LABOR:** Claude
**CONTEXT REQUIRED:** The /v0 sentence and the ten-company watch list. No code yet.
**PROMPT:**
"""
You are scaffolding a Python project called lectern. Create the repository layout: lectern/collect.py, lectern/collectors/{google,amazon,microsoft,meta,monitor}.py, lectern/sources.json, lectern/keywords.json, lectern/sync.sh, lectern/runs/. Write sources.json with the 10 companies mapped to their board types (greenhouse/ashby/smartrecruiters/custom) and API base URLs where known: Greenhouse boards-api.greenhouse.io, Ashby api.ashbyhq.com, SmartRecruiters api.smartrecruiters.com. Leave custom collectors' endpoint fields empty with a comment naming what goes there. Do NOT write any collector logic yet — layout and config skeleton only.
"""
**EXPECTED OUTPUT:** Directory tree with empty module stubs and a valid sources.json with all 10 companies.
**HANDOFF CONDITION:** Every file in the layout exists; sources.json parses as JSON and lists exactly 10 companies with board types; no collector logic present (scaffolding only).
**DEPENDENCY:** Step 1.

---

### STEP 3 · PHASE F · HUMAN TASK
**LABOR:** Human
**SUPERVISORY CAPACITY:** [PF] — Problem Formulation. Deciding the trust rule's exact thresholds (≥90% of reported, ≥70% of previous trusted, two-miss close) and writing them as falsifiable claims. The numbers are judgment about how much collection failure is tolerable before the diff becomes untrustworthy; no dataset tells Claude these values.
**ACTION:** Write the trust rule as three testable sentences in /v2. For each threshold, write one sentence justifying why that number and not 10 points higher or lower. If you cannot justify a number, mark it provisional and name what evidence would change it.

---

### STEP 4 · PHASE C · CLAUDE TASK
**LABOR:** Claude
**CONTEXT REQUIRED:** Steps 1–3. The trust rule text. SQLite available.
**PROMPT:**
"""
In lectern/collectors/monitor.py, implement a SQLite store with two tables. jobs: job_id TEXT PRIMARY KEY (source-native ID, never generated), company TEXT, title TEXT, locations TEXT, url TEXT, posted_at TEXT, description TEXT, first_seen TEXT, last_seen TEXT, status TEXT DEFAULT 'open'. runs: id INTEGER PRIMARY KEY AUTOINCREMENT, company TEXT, run_at TEXT, fetched INTEGER, reported_total INTEGER, trusted INTEGER. Implement record_run(company, jobs, reported_total): insert/update job rows (new IDs get first_seen=now, recurring get last_seen=now), compute trusted as (fetched >= 0.9*reported_total AND fetched >= 0.7*previous_trusted_fetched) with previous_trusted_fetched=0 allowed on first run, insert the run row, then mark jobs closed only if trusted=1 AND the job was absent from this run and the previous trusted run. Return (new_count, closed_count, trusted). Do not implement fetching — only the store and the trust/diff logic.
"""
**EXPECTED OUTPUT:** monitor.py with the schema and record_run implementing the exact rule, including the two-miss close and the untrusted-run-never-closes behavior.
**HANDOFF CONDITION:** A stubbed test passes: feed run 1 (100/100), run 2 (50/100, untrusted), run 3 (95/100, trusted) — assert run 2 closed zero jobs and run 3 closed only jobs absent from both run 1 and run 3.
**DEPENDENCY:** Steps 1–3.

---

### STEP 5 · PHASE C · HUMAN TASK
**LABOR:** Human
**SUPERVISORY CAPACITY:** [PA] — Plausibility Auditing. Reading Claude's monitor.py for the specific failure the stubbed test doesn't cover: what happens when reported_total is 0, when fetched exceeds reported, when the source's "total" is a cap. Hearing the wrong note before running it.
**ACTION:** Review monitor.py against these three cases: (a) reported_total=0 → trusted must be 0, not a division error; (b) fetched > reported_total → trusted=1 only if the 70% clause also passes, and log a warning; (c) Amazon's exact-10,000 cap → trust is relative to the claim, document that in a code comment. Fix or direct Claude to fix any case that fails.

---

### STEP 6 · PHASE C · CLAUDE TASK
**LABOR:** Claude
**CONTEXT REQUIRED:** Steps 1–5. Greenhouse API docs pattern (boards-api.greenhouse.io/v1/boards/{token}/jobs).
**PROMPT:**
"""
In lectern/collect.py, implement fetch_board(board_token): GET https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs, paginate if the API paginates, return a list of dicts with keys job_id (str, the 'id' field), title, locations (join location names), url (absolute_url), posted_at, description (fetch per-job only if a fetch_description flag is true; default false). Throttle 1 request/second with jitter. Never log in, never send credentials. Return (jobs, reported_total) where reported_total is len(jobs) for Greenhouse (it returns all). Write a main that reads lectern/sources.json, fetches all greenhouse boards, and writes lectern/runs/{date}/all-jobs-{date}.json.
"""
**EXPECTED OUTPUT:** collect.py fetching Greenhouse boards end-to-end, writing dated JSON.
**HANDOFF CONDITION:** Running against the real Figma board returns >100 postings, every record has a non-empty string job_id, and no two records share a job_id.
**DEPENDENCY:** Steps 1–5.

---

### STEP 7 · PHASE C · HUMAN TASK
**LABOR:** Human
**SUPERVISORY CAPACITY:** [TO] — Tool Orchestration. Deciding the build order: Ashby and SmartRecruiters collectors before or after the custom scrapers? The decision: standard APIs first (they're predictable), custom scrapers second (each is its own risk), because a working 6-board pipeline delivers value while the bespoke three are being fought.
**ACTION:** Sequence the remaining collector work: Ashby + SmartRecruiters (one Claude task), then Google, then Amazon, then Microsoft, then Meta-last (known environment block). Write the sequence down; do not let implementation order be accidental.

---

### STEP 8 · PHASE C · CLAUDE TASK
**LABOR:** Claude
**CONTEXT REQUIRED:** Steps 1–7, collect.py as the pattern to follow.
**PROMPT:**
"""
Extend lectern/collect.py with fetch_ashby(org) using https://api.ashbyhq.com/posting-api/job-board/{org} and fetch_smartrecruiters(company) using the SmartRecruiters public API. Both return (jobs, reported_total) with the same record keys as the Greenhouse fetcher: job_id (source-native, string), title, locations, url, posted_at, description (not fetched by default). Same throttle discipline. Wire all three into main so one invocation pulls all 6 boards. Keep per-board failures isolated: if one board errors, log it and continue to the next.
"""
**EXPECTED OUTPUT:** 6-board collection in one run.
**HANDOFF CONDITION:** One run returns postings from all 6 boards (Anthropic, Figma, Miro, OpenAI, Notion, Canva), each record keyed by a non-empty source-native job_id, and a simulated failure of one board (bad token) does not abort the other five.
**DEPENDENCY:** Steps 1–7.

---

### STEP 9 · PHASE I · CLAUDE TASK
**LABOR:** Claude
**CONTEXT REQUIRED:** Steps 1–8. Google Careers search URL pattern.
**PROMPT:**
"""
In lectern/collectors/google.py, implement fetch_google(): request the Google Careers search page with query parameters, parse the server-rendered listing cards (title, location, job ID from the card link), paginate through all result pages. Return (jobs, reported_total) with source-native job IDs. Throttle politely (2+ seconds between pages, jitter). If the markup doesn't match expectations, raise a descriptive exception — never silently return an empty list.
"""
**EXPECTED OUTPUT:** google.py returning Google postings with native IDs.
**HANDOFF CONDITION:** A live run returns >3,000 postings and the reported total matches the page count the site displays; a deliberately broken CSS selector raises an exception rather than returning [].
**DEPENDENCY:** Steps 1–8.

---

### STEP 10 · PHASE I · HUMAN TASK
**LABOR:** Human
**SUPERVISORY CAPACITY:** [PA] — Plausibility Auditing. The scraper's most dangerous failure is silent: returning 200 postings when the site shows 3,345, because pagination broke on page 3. No test catches this except a human comparing the fetched count to the site's own displayed total.
**ACTION:** Run google.py live. Compare fetched count to the total the Google Careers page displays. If they differ by more than 2%, do not accept the output — direct Claude to fix pagination. This check is not automatable with confidence; it requires eyes on the source.

---

### STEP 11 · PHASE I · CLAUDE TASK
**LABOR:** Claude
**CONTEXT REQUIRED:** Steps 1–10. Amazon Jobs search.json endpoint pattern.
**PROMPT:**
"""
In lectern/collectors/amazon.py, implement fetch_amazon(): GET https://www.amazon.jobs/en/search.json with base_query, country, result_limit=100, and offset pagination. Walk offsets until jobs returned < result_limit or offset exceeds the reported hits. Return (jobs, reported_total) where reported_total is the 'hits' field. Source-native ID is the job's ICIMS ID. Throttle 1/sec with jitter. IMPORTANT: verify pagination reaches the real total — do not stop at the first page and declare success. If hits is exactly 10000, log a warning that the total may be a source-side cap.
"""
**EXPECTED OUTPUT:** amazon.py with full pagination and the cap warning.
**HANDOFF CONDITION:** A live run fetches ≥99% of the reported hits value, and the log contains the cap warning when hits == 10000.
**DEPENDENCY:** Steps 1–10.

---

### STEP 12 · PHASE I · CLAUDE TASK
**LABOR:** Claude
**CONTEXT REQUIRED:** Steps 1–11. Microsoft PCSX search API pattern.
**PROMPT:**
"""
In lectern/collectors/microsoft.py, implement fetch_microsoft(): query the Microsoft Careers PCSX search API with pagination (start/num), throttle to ~1 request per 6 seconds with jitter and 5-minute cooldowns on HTTP 429. Maintain a checkpoint file recording the last completed offset so an interrupted run resumes rather than restarts. Return (jobs, reported_total). On repeated 429s, back off — never hammer the endpoint.
"""
**EXPECTED OUTPUT:** microsoft.py with throttling, cooldowns, and checkpoint resume.
**HANDOFF CONDITION:** An interrupted run (kill at ~40%) resumed from the checkpoint completes without re-fetching completed offsets; three consecutive 429s trigger a cooldown, not a retry storm.
**DEPENDENCY:** Steps 1–11.

---

### STEP 13 · PHASE I · HUMAN TASK
**LABOR:** Human
**SUPERVISORY CAPACITY:** [IJ] — Interpretive Judgment. Deciding what the Microsoft throttle situation *means* for the system's claims. The collector works; the environment throttles it. The judgment: partial data marked untrusted is honest, and the caveat travels with every count. Claude cannot decide how much uncertainty the operator's public claims can carry.
**ACTION:** Write the standing rule: Microsoft counts are reported with their trust verdict attached, always. No bare "Microsoft: 1,746 postings" without "untrusted." Add this to the run-report format.

---

### STEP 14 · PHASE B · CLAUDE TASK
**LABOR:** Claude
**CONTEXT REQUIRED:** Steps 1–13. The keyword list: teaching, education, enablement, training, academy, advocate, curriculum, faculty, student, learning.
**PROMPT:**
"""
Add a filter stage to lectern/collect.py: after collection, match each posting's title and description case-insensitively against lectern/keywords.json. Write matches to lectern/runs/{date}/jobs-of-interest-{date}.json (same record format). The output file header must state 'candidates for human review — not classifications.' Do not score, rank, or dedupe beyond source-native ID. Report kept/rejected counts.
"""
**EXPECTED OUTPUT:** Filter stage writing jobs-of-interest files with the disclaimer.
**HANDOFF CONDITION:** On the 2026-10-08 inventory, the filter keeps 50–70 postings (order of magnitude check), every kept posting contains a keyword in title or description, and the file header carries the disclaimer.
**DEPENDENCY:** Steps 1–13.

---

### STEP 15 · PHASE B · HUMAN TASK
**LABOR:** Human
**SUPERVISORY CAPACITY:** [PA] — Plausibility Auditing. The keyword "learning" will match every "machine learning" posting at these AI companies — potentially hundreds of false positives that drown the 15-minute review budget. Claude implemented the match correctly; the *set* is the risk.
**ACTION:** Run the filter on a full inventory. Read the kept list. For each keyword, count its contribution to false positives. Remove or scope any keyword whose noise exceeds its signal ("learning" → require word-boundary or drop). The 15-minute review budget (N4) is the test.

---

### STEP 16 · PHASE B · CLAUDE TASK
**LABOR:** Claude
**CONTEXT REQUIRED:** Steps 1–15. collectors/run_daily.py as orchestrator.
**PROMPT:**
"""
In lectern/collectors/run_daily.py, implement main(): for each of google/amazon/microsoft, call the collector, feed (jobs, reported_total) into monitor.record_run, collect the (new, closed, trusted) results, and print one health line per source: 'company fetched=X reported=Y new=A closed=B trusted=yes/no'. Support --only <company>. Wrap each collector call so one company's exception is caught, logged, and does not abort the others. Exit 0 unless all three failed.
"""
**EXPECTED OUTPUT:** run_daily.py orchestrating the three custom collectors with per-source isolation and health lines.
**HANDOFF CONDITION:** With microsoft's collector stubbed to raise, the run still completes google and amazon and prints three health lines including microsoft's failure.
**DEPENDENCY:** Steps 1–15.

---

### STEP 17 · PHASE B · HUMAN TASK
**LABOR:** Human
**SUPERVISORY CAPACITY:** [TO] — Tool Orchestration. The description-fetch policy: descriptions are fetched only for unseen IDs. This is a politeness and efficiency decision (don't re-fetch 17,000 descriptions daily), but it means description text is frozen at first sight — a posting whose description is later edited keeps the stale text. Claude would default to either always-fetch (hammering) or never-update (stale).
**ACTION:** Decide and document: descriptions fetched once at first_seen; re-fetch only if the title changes (title change = possible reposting). Write this as a code comment in monitor.py and a line in /s1.

---

### STEP 18 · PHASE H · CLAUDE TASK
**LABOR:** Claude
**CONTEXT REQUIRED:** Steps 1–17. The GitHub repo and the dated outputs.
**PROMPT:**
"""
Write lectern/sync.sh: after a run, git add lectern/runs/{date}/ and the run log, commit with message 'lectern run {date}: {total} postings, {kept} kept', push to origin main. The script must refuse to run if there are uncommitted changes unrelated to today's run (check git status first). Print the commit hash on success.
"""
**EXPECTED OUTPUT:** sync.sh with the safety check.
**HANDOFF CONDITION:** Dry-run against a test repo: with a stray uncommitted file present, the script refuses; with a clean tree, it commits and pushes exactly today's outputs.
**DEPENDENCY:** Steps 1–17.

---

### STEP 19 · PHASE H · HUMAN TASK
**LABOR:** Human
**SUPERVISORY CAPACITY:** [EI] — Executive Integration. Holding the whole system in view: the collectors work, the monitor judges, the filter triages, the runner orchestrates, the push delivers. The integration question: what does the operator actually read each morning, and does every component's output reach that reading? A gap here (e.g., trust verdicts printed but not pushed) is invisible to every component-level test.
**ACTION:** Run the full recipe end-to-end on a live day. Read the output as the operator. Verify: health lines for all sources, new/closed lists, trust verdicts, candidate list, everything pushed to GitHub. Fix any output that exists on the VM but never reaches the operator's eyes.

---

### STEP 20 · PHASE R · CLAUDE TASK
**LABOR:** Claude
**CONTEXT REQUIRED:** Steps 1–19. The full SDD.
**PROMPT:**
"""
Write the four verification prompts for independent checking (to be run by a fresh Claude Code session on a clean clone): (1) state check — verify committed run files exist and HEAD matches origin/main; (2) evidence summary — reproduce the posting counts from committed JSON without the database; (3) demand signal — list the kept teaching-candidate postings with IDs and titles; (4) feedback loop — confirm the trust rule implementation in monitor.py matches the /v2 principles. Each prompt must be runnable with no VM access and no database.
"""
**EXPECTED OUTPUT:** Four prompts, each self-contained.
**HANDOFF CONDITION:** A second Claude session (fresh context, repo clone only) executes all four and reproduces the reported counts — this is N7, tested.
**DEPENDENCY:** Steps 1–19.

---

### STEP 21 · PHASE R · HUMAN TASK
**LABOR:** Human
**SUPERVISORY CAPACITY:** [IJ] — Interpretive Judgment. The system's outputs are evidence for public claims (course, brief, vendor conversations). The judgment: what the counts do and do not establish — a listing is evidence of hiring interest, not of honesty about teaching; the filter finds candidates, not proof. Signing the release means standing behind these claim limits.
**ACTION:** Write the claim-limits paragraph (what a posting demonstrates vs. what it doesn't). Attach it to the release. Do not ship the system without it — an instrument without stated limits is a rhetorical weapon, not a research tool.

---

## SCORE SUMMARY

**Total steps:** 21
**Claude tasks:** 11 (52%)
**Human tasks:** 10 (48%)

**CRITICAL PATH:** 1 → 3 → 4 → 5 → 6 → 8 → 14 → 15 → 19 → 21. The trust rule (3) gates the monitor (4); the monitor's audit (5) gates all collectors; the filter's human audit (15) gates the release (21). Any delay in the trust-rule formulation cascades through everything — it is the system's load-bearing judgment.

**HIGHEST-RISK HANDOFFS:**
1. **Step 3 → Step 4 (trust thresholds → monitor implementation).** Risk: Claude implements the numbers exactly as specified, but the *numbers themselves* are wrong — 90% too lax (throttled runs trusted, mass false closures) or the two-miss rule too strict (real closures take a week to register). The failure mode is silent: the code is correct and the judgments are bad. Mitigation: the human justifies each threshold in writing (Step 3's action) before implementation.
2. **Step 14 → Step 15 (filter implementation → keyword audit).** Risk: the filter works as specified and floods the operator — "learning" matching hundreds of ML postings blows the 15-minute review budget, and the operator stops reading the list, silently discarding N4. The failure looks like success (the list is produced daily). Mitigation: the human reads the actual kept list (Step 15), not the kept count.
3. **Step 11's cap warning → operator's public claims.** Risk: Amazon reports exactly 10,000, the run is "trusted" relative to the claim, and the operator cites "10,000 postings collected" as a world-fact rather than a source-claim-fact. The handoff condition (log the warning) exists; the risk is that no human reads the log. Mitigation: Step 13's standing rule — trust verdicts attached to every count, always.

**SUPERVISORY CAPACITY DISTRIBUTION:**
[PA] Plausibility Auditing: 3 steps (5, 10, 15)
[PF] Problem Formulation: 2 steps (1, 3)
[TO] Tool Orchestration: 2 steps (7, 17)
[IJ] Interpretive Judgment: 2 steps (13, 21)
[EI] Executive Integration: 1 step (19)

No capacity appears zero times. [EI] appears once — flagged: executive integration is the capacity this build leans on least, which is expected for a single-operator pipeline with no multi-thread orchestration, but Step 19 is load-bearing precisely because no other step checks the whole.

**WHAT IS MISSING FROM THIS SCORE:**
- C4 (Meta collector) has no steps: it is unwired and unrunnable from this environment. When the network block lifts, add: Claude task (Playwright collector), human [PA] audit (verify listings against the live site), human [TO] decision (wire into run_daily or keep separate).
- /s2–/s4, /d1–/d3, /p1–/p5 were not run for this assignment; a production SDD would add API contract documentation (/d2) for the three custom collectors and a risk register (/p4) naming ATS migration as the top risk.
- The score covers the build, not the operation: no steps for the daily recipe's ongoing execution, which is correct — boondoggling scores the build; the recipe is the operator's practice.

---

# Part 2 — Boondoggle Reflection
**System:** Lectern
**Word count:** ~720

---

## Prompt A — The Split

The distribution: [PA] Plausibility Auditing leads with 3 steps, [PF], [TO], and [IJ] tie at 2 each, and [EI] Executive Integration trails with 1. No capacity is zero, so there's no flag to address — but the shape is the finding.

Lectern is a pipeline whose every intermediate product looks correct. Parsed listings look like listings. A filter match looks like relevance. A trust verdict looks like rigor. The dominant human labor is therefore hearing the wrong note in data that presents itself as right: the scraper that silently returns 200 of 3,345 postings (Step 10), the keyword "learning" matching every machine-learning role (Step 15), the monitor code that handles every case except reported_total=0 (Step 5). None of these failures look like failures. That's what the PA-heavy distribution says about this application: it is a system where the most expensive judgment is not deciding what to build but noticing when the built thing is quietly wrong.

[EI] appears once because Lectern is a single-operator linear pipeline — there are no concurrent Claude threads to hold toward a unified goal. That absence is a genuine property of the build, not a gap: Step 19 exists precisely because integration-by-inspection is the only integration this system gets.

## Prompt B — The Hardest Handoff

The most convincing is Handoff 1: the trust thresholds (Step 3) into the monitor implementation (Step 4). Here's the concrete failure. An engineer takes the Boondoggle Score, pastes the Step 4 prompt, and Claude produces a flawless monitor.py — the stubbed test passes, the two-miss rule works, untrusted runs close nothing. The engineer accepts it. What they accepted without noticing: the *numbers*. Ninety percent, seventy percent, two misses — Claude implemented them exactly as specified, and the specification was never justified. Six months later a throttled run fetches 91% of a source whose reported total was itself depressed by the throttle; the run is trusted; 400 live postings are mass-closed in one diff. The operator's "closed" list is garbage, and worse, the operator learns not to trust the diff at all — the instrument is intact and its credibility is destroyed.

The skeptical move that catches this is Popper's asymmetry, applied at the handoff. The stubbed test passing is a white swan: it confirms the implementation matches the spec, and it adds zero guarantee that the spec's numbers are right. The question the engineer should have asked is the black-swan question: "What single run would prove these thresholds wrong?" — and then run that scenario (a 91%-of-a-depressed-total fetch) before accepting the handoff. Verification of the implementation is cheap; falsification of the thresholds is the work, and it was skipped because the code looked done.

## Prompt C — Where Gru Was Right and Where I Disagreed

Gru's labor heuristics assign "transforming data from one format to another" to Claude, and the keyword filter looks like exactly that: a fixed term list matched against text, a mechanical transformation of the inventory into a candidate list. By the heuristic, Claude should own both the matching *and* the term selection — suggest keywords, tune for precision and recall, iterate.

I disagree on the term selection, and the frame the assignment offers is exactly right: this is mechanical execution versus judgment about whether the specification is correct. Claude can execute the match flawlessly and can even propose statistically sensible terms. What it cannot do is know what the candidate list is *for*. The list exists so Bear can spot the trigger for a specific pitch — an education-advocate role at a company selling AI to universities. "Teaching-related" in the abstract would include K-12 curriculum jobs, corporate L&D roles, and ed-tech marketing positions, all of which the filter should exclude even though a generic relevance judgment would keep them. The keyword set encodes Bear's intent, not the English language's semantics. Tuning it is interpretive judgment ([IJ]): supplying the meaning the output must serve, which Claude cannot supply because the meaning lives in Bear's plans, not in the data. Gru was right that the matching is Claude's work. The specification of what counts as a match was never delegable.

## Prompt D — The Solve-Verify Asymmetry Applied

Step 10: the human verification of the Google scraper's pagination. Claude produces a paginating scraper in about five minutes — request the search page, parse the cards, follow the next-page links, return (jobs, reported_total). The production cost is trivial. The verification is where the asymmetry bites: the human must open the live Google Careers page, note the total it displays, run the scraper, and compare. If the numbers differ, the diagnosis branches — pagination drift (the "next" link changed), a markup change (cards restructured), or throttling (pages silently truncated) — and each demands a different fix, each requiring familiarity with how that specific source behaves. None of this is in the prompt Claude received. It can't be; it's knowledge of the world, not the specification.

A team that skipped this verification would ship a collector that returns 200 postings while the site shows 3,345 — and the failure is silent, because 200 well-formed records look exactly like a complete result. Discovery timeline: weeks at best, when someone notices the "new" list for Google has been suspiciously empty; potentially never, because nothing errors and the health line prints a number. This is the asymmetry in its purest form in this build: production cost five minutes, verification cost an hour of domain-grounded attention, and the cost of skipping verification is unbounded — every downstream claim about Google hiring patterns quietly rests on 6% of the data.
