# Lectern history: what was added when, and why

## Executive summary

**What this is.** A day-by-day record of how the Lectern folder was built up: what was added each day, what changed, and the reason. **Why read it.** The folder looks like a pile of scripts because it grew one need at a time, and the order of those needs is the explanation: first a collector and a filter, then audits of the filter, then a ranking of companies, then a way to publish only what changed, then posting, then measuring whether the jobs turn over. **What it shows.** In about three weeks the project went from one collector to a pipeline with seven steps, and almost every step was added because the step before it produced a number that could not yet be trusted. This file is a companion to `../FRICTIONAL.md`, which tells the same story from the author's side; this one stays with what changed in this folder.

## How to keep this file

Add an entry whenever something in `lectern/` is added, changed or removed: the date, what, and why, in the same change. Source for the past entries: `git log` for this folder and the entries in `../FRICTIONAL.md`. Dates are commit dates. Write what happened, including what failed; never write a result nobody ran.

## How it was built up, in order

1. **A collector and a filter** (2026-09-26): read the boards, keep what looks like teaching.
2. **Audits of the filter** (09-26): sample the rejects, then audit by job function.
3. **A different question** (09-26): rank companies by whether they want this work, not postings by fit.
4. **More sources** (10-08): the big four, which have no simple feed.
5. **Publish only what changed** (10-18): new, changed, gone, against a remembered state.
6. **Do the jobs turn over?** (10-18): churn.
7. **Beyond job boards** (10-18): business-school faculty listings.
8. **Posting** (10-19): new listings go to Discord on their own; lab pages for a person to look at.
9. **Other forms** (10-19 on): the same pipeline as n8n workflows, tested against this one; a CrewAI form planned.

## Before this folder

The collector existed before this folder did. According to the 2026-09-26 entry in the log, the Branding and AI class folder already held the collector, the watch list, the filter, the applicant-tracking notes and the CV facts; this folder, named master that day, started with none of it. Earlier single-company versions are in `../greenhouse-watch-demo/` (the Reallocation Engine's watcher run on one board, begun 2026-09-24) and `../figma/` (the first single-company iteration: a saved board, a scan, the kept postings).

## 2026-09-26: the folder is made the master, and the filter is audited

- **Added:** `collect.py`, `keywords.json`, `sources.json`, `ATS.md` and `sync.sh` (the folder becomes the master for three classes; the copy mechanism is `sync.sh`, which also has a `--check` mode that changes nothing).
- **Added:** `audit_rejects.py`, a reproducible random sample of the 3,358 rejected postings (seed recorded). **Why:** nobody had looked at what the filter threw away. **Found:** an audit aimed at missed jobs found the opposite problem: `education` was in 618 of 618 Anthropic postings (a salary footer), and the topic-word rule was keeping recruiters.
- **Added:** `audit_titles.py` and `title_families.json`. **Why:** reading postings is the wrong unit; there are far fewer job functions than postings. **Found:** 18 families cover everything, and the audit's own first pass was wrong: it counted "training" as a teaching word, but at an AI company it means training a model. The error was reported, not quietly fixed.
- **Changed:** `keywords.json` to v0.4.0 and `title_families.json`. **Why:** the target became "makes the materials", in any kind of company, whatever it is called. A two-part body rule (a make-materials phrase and a named audience, both required) was built, failed twice on measurement, and was cut down; every cut phrase is recorded in the file with the count that cut it. A posting for a Learning Experiences Creator had been rejected for the want of one word. Result: 97 kept of 3,446.
- **Added:** `demand_report.py`. **Why:** the unit of analysis was wrong; a posting is evidence that a company decided the work is worth paying for, so the report ranks companies on five kinds of evidence. **Found:** Google's absence from the table was an artefact (no public feed), not a lack of demand; a person reading its careers site found 20 education roles on the first page. That check, its URL and its date went into `sources.json`.
- **Evidence:** the five 2026-09-26 entries in `../FRICTIONAL.md`.

## 2026-10-07: the first real sync

- **Changed:** `sync.sh`'s shared list gained `demand_report.py`. **Why:** the file had been added on 09-26 and never reached Prompt Engineering, because a new shared file is not shared until it is in the list. `sync.sh` was run for real for the first time.
- **Evidence:** the 2026-10-07 entry in `../FRICTIONAL.md`.

## 2026-10-08: more sources

- **Added:** `collectors/` (Google, Amazon, Microsoft, Meta; a shared monitor and a daily runner) and the first dated run, `runs/2026-10-08/`. **Why:** those four employers have no simple public job feed; they need their own collectors, which take hours.
- **Changed:** the Microsoft collector was slowed to about one request every six seconds, because its site throttles hard.

## 2026-10-18: a publishing step, a turnover measure, and a faculty reader

- **Added:** `publish_delta.py`, `runs/published-state.json` and the first delta (`runs/2026-10-18/`: 42 new, 7 changed, 9 gone). **Why:** only what changed since the last published run should be published, not everything. A source that could not be read today never closes a posting; it is "unknown".
- **Added:** `churn.py`. **Why:** are these real jobs that turn over, or postings that sit there? It measures age, flow between snapshots and re-posts. Closed is not hired.
- **Added:** `faculty_feed.py` and `faculty_config.json`. **Why:** business-school faculty roles that mention AI. The universities' own job systems mostly cannot be read by script, so it reads the Chronicle of Higher Education and Inside Higher Ed keyword feeds. First run: 1,727 items read, 14 matched, 0 errors. It was first built in a private folder with alerts to a private channel, an assumption of the assistant's that was corrected: the channel is meant to be public.
- **Changed:** `keywords.json` (v0.5.1, v0.5.2): a connector rule for roles that own a big institutional relationship, an account or partnership word in the title and a higher-education institution in the body, widened the same day to marketing, adoption and enterprise-account titles. Each addition was measured against the corpus first; a miscount of one role family (27 against 38) was found and corrected on the record.
- **Changed:** `sources.json`: Stripe and Writer came off the watch list, at Professor Bear's word; the reason first recorded was wrong and was corrected to his own (not directly applicable to improving education through AI, not a judgment that they are bad). Watch list: 16 boards.
- **Added:** `test_publish_delta.py`, `test_churn.py`, `test_connector_rule.py`; `.gitignore` (full snapshots and raw payloads stay local). `sync.sh` gained `collectors/` and `publish_delta.py`.
- **Ran:** a collection of 17 of 18 boards (HubSpot returned HTTP 404): 3,243 postings, 88 kept. A bug in `publish_delta.py` showed up the same day: it reported 47 postings as "changed" only because the filter had started writing a new field; fixed, with a test.
- **Evidence:** the two 2026-10-18 entries in `../FRICTIONAL.md`.

## 2026-10-19: posting, labs, and a second form

- **Added:** `notify.py`, `daily.sh`, `test_notify.py`, `test_run_daily.py`. **Why:** a standing rule, said with some frustration that it was not being done: new possible listings are posted to the public Discord channel automatically. The instruction had been given and never written into the pipeline; it now is (`daily.sh`, `CLAUDE.md` Rule 4). Only watched companies are posted, most-wanted first, nothing twice, and a message with a path or email address is refused.
- **Changed:** `collectors/run_daily.py` gained `--text-out`, because the first Google run kept only hashes of the ad text. Microsoft returned HTTP 429 and remains unread.
- **Changed:** `faculty_config.json`: Brown and eight more business schools; 21 schools in all.
- **Added:** `post_labs()` in `notify.py`, its tests and `CLAUDE.md` Rule 5. **Why:** the part-time research search. Lab and research-group pages that look like great fits are posted for Professor Bear to look at, and nothing is approached before he has. Only the lab's public name, institution, link and its own words are ever read; people, emails and phone numbers cannot reach a post.
- **Changed:** `sources.json`: Replit came off the watch list, at his word: it is AI but not educational AI, and the role he read there is entry-level. Watch list: 15 boards. `sync.sh` gained `--only <word>` so one class can be synced.
- **Outside this folder, the same day:** the pipeline rebuilt as five n8n workflows and tested against this Python (`../lectern-n8n/`), and a student's version of the lab search that led to checking lab funding against the NIH and NSF award databases (`../lab-outreach/`).
- **Evidence:** the 2026-10-18 entry (which carries the 10-19 work) in `../FRICTIONAL.md`.

## 2026-10-20: this folder is explained

- **Added:** `README.md` (what each file is, the pipeline, what is shared, what is not here) and this file. **Why:** a visitor to the folder on GitHub saw a flat pile of scripts with no map. The honest answer to "why is it organised like this" was that it was not organised, it accumulated; the layout stays as it is for now (moving files means re-syncing three repositories), and the README is the map.
- **Added beside this folder:** `../lectern-n8n/`, a copy of the n8n form, so the Python and n8n versions can be read side by side.
