# One-call judge (Pydantic AI)

## Executive summary

**What this is.** A parallel version of Lectern, built to find out what One-call judge (Pydantic AI) does that the plain Python does not, and what it costs. Replace the keyword filter with one structured model call returning a typed {keep, family, reason}, run over the postings the keyword filter already judged, and compare. The false-friend words that tripped the first filter are the adversarial set. **Why it is here.** Each version moves one thing (see `../PLAN.md`); this one's job is rung 1 (rung 1) of the ladder. **Where it stands.** Not started. Nothing in this folder has been built or run.

## What it reads (one source of truth)

- **The targets:** `../../config/targets.json`, read directly and never copied. Which companies, schools and research groups to look at, and which have been removed and why, are decided there and only there.
- **The rules:** `../../config/keywords.json` for the strict run; `../../../06-setup-exercise-personal-layer/search/profile.yml` for a loose run (what an honest educational AI advocate would fit).
- **Never edits** either file. A company this version finds is written to `proposed-targets.jsonl` here, each with a link to a public page that backs the claim; a person promotes it.

## What it owns

How it collects (it may collect its own data, so the way it reads a board can be compared with the Python's), how it judges, where its state lives, and how it is scheduled: the model call and its typed output; the rules are `config/keywords.json`, read, not copied.

## What it writes

The standard run format (`runs/DATE/all-jobs-DATE.json` and `jobs-of-interest-DATE.json`, checked by `../../compare/check_run_format.py`) and an append-only log in `../../logs/judge-pydantic-ai/`. It is compared with the reference run by `../../compare/compare_runs.py`.

## How it is judged

Oracle: Agreement with the keyword filter; the disagreements read by hand. The same columns as every version are in `../PLAN.md`: broken-source test, what it found, Discord precision, log against outside evidence, heartbeat, where the rules live, unattended completion, cost and time, time to first working version.

## To do

Everything. First: make it write the standard run format on one day's boards, then run `../../compare/compare_runs.py` against that day's Python run.
