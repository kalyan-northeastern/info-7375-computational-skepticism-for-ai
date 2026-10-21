# PROJECT-BRIEF — PM Sponsor Check (working title)

Kalyan Venkata Swamy Karnati · INFO 7375 · Fall 2026 · Final project pitch

## 1. What is it?
A source-grounded triage tool that tells an early-career international product manager which health-tech employers have public evidence of sponsoring H-1B visas for *product managers*, not just for engineers, and labels every answer as record or inference.
When it is done it will exist as a GitHub repository: a recipe (agent file + human card), a Python scan script, a labelled test set, and an evaluation log, contributed as a recipe to the Reallocation Engine.

## 2. Why would anyone care?
The usual sponsorship check answers "does this company sponsor anyone?" An early-career PM needs "does this company sponsor PMs, and is the posting open to me?" On my 2026-10-09 run, only 9 of 352 possible health sponsors listed a PM title among their top sponsored job titles, and none of those titles was entry level; a health-category filter would have missed 64 sponsoring companies filed under technology and other categories (38 Other Technology, 25 Other, 1 Computers).
Alternatives I looked at: (1) the Reallocation Engine's existing sponsorship evidence and role scorer (`scripts/score/role-scorer.mjs`), run on 2026-10-09; (2) Built In Boston job listings for Cohere Health PM roles, checked on 2026-10-09. What mine does that they do not: the engine's scorer rates each company's sponsorship as one tier (e.g. "Likely") and never asks whether PMs were sponsored, and in run 1 it reported postings nobody had checked as "liveness 1 [record]"; in run 2, after the labels were fixed, the two roles I could not check still ranked above the ones I had; Built In Boston still showed copies of Cohere PM roles marked "removed" while the live role sat on Cohere's own job board. Mine flags PM-specific title evidence separately and will not mark a role "Apply" until the posting has been checked on the company's own board.

## 3. Who opens it, and what do they do?
Target role: associate / entry-level product manager in health tech.
Reader: a hiring manager for a PM or product-operations role. In the first sixty seconds they open the human card, see the verify / cannot-verify list, and open one run log showing a gate catching a real error.

## 4. What does it prove about me?
Verification and source grounding (every field labelled record, your-input, or model-inference), evaluation (precision measured against an evidence-checked test set), and agent loops with human gates (no decision is final until a named human logs it).
Evidence: the 2026-10-09 run logs, the 64 keyword matches reviewed with evidence, and the scorer bug found in run 1 (missing liveness was reported as "checked"). A reviewer could fairly conclude I can find where a data pipeline misleads. They could not conclude it is production-ready.

## 5. In, out, first
In: health-tech PM roles, H-1B sponsorship evidence, posting liveness, SOC choice made by the student.
Out: it will not say which occupation code an employer will file, and it will not give immigration advice.
First: a tightened health-keyword filter scored against the 64 reviewed rows. Someone would know it ran because the eval log will show precision before (52/64, 81%) and after, with the command that produced it.

## 6. What could sink it?
The full DOL LCA disclosure data, which is the only way to confirm PM sponsorship beyond a truncated top-titles list, is large and its job titles are inconsistent. If I cannot ingest and match it in time, I will limit the lookup to the most recent fiscal year DOL has published, for employers in Massachusetts only, and say so in the eval log.

## 7. Why this project?
A mix. Existing skill on show: product management in health tech, from my PM internship at Andor Health (January–August 2026). I will not show any internal Andor Health work; the public evidence I can point to is coursework I made myself in health-tech product thinking: the `healthtech-pm-sponsor-triage` recipe and worked example submitted on 2026-10-09, and my Week 1 explainer film on Popper's demarcation, which rewrites a product claim with a metric, a threshold, and a window. New skills I am learning: Python data pipelines, building labelled test sets, and writing verification gates for agent output.

## Exists today (made 2026-10-09, can be shown)
- Recipe and human card `healthtech-pm-sponsor-triage` (v0.1.0, DRAFT)
- Prototype script `pm_title_scan.py`, run once on the repo's 80 Days and BLS data
- Shortlist CSV (352 rows), SOC candidate table (7 rows), two scorer reports, run log
- 64 keyword-lane matches reviewed with evidence (12 rejected)

## Will exist
- Tightened keyword filter with a measured precision change
- DOL LCA title lookup for PM sponsorship evidence
- A rule enforced in code: no Apply without a checked liveness result
- Evaluation log and a README a stranger can follow