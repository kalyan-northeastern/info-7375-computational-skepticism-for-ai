# CrewAI Crew

## Executive summary

**What this is.** A parallel version of Lectern, built to find out what CrewAI Crew does that the plain Python does not, and what it costs. Role-based agents deciding the flow (a Scout that reads the boards, a Judge that keeps or rejects, an Editor that writes the post). It will not match the Python, and how far it misses is the lesson. **Why it is here.** Each version moves one thing (see `../PLAN.md`); this one's job is rung 3 of the ladder. **Where it stands.** Not started. Nothing in this folder has been built or run.

## What it reads (one source of truth)

- **The targets:** `../../config/targets.json`, read directly and never copied. Which companies, schools and research groups to look at, and which have been removed and why, are decided there and only there.
- **The rules:** `../../config/keywords.json` for the strict run; `../../../06-setup-exercise-personal-layer/search/profile.yml` for a loose run (what an honest educational AI advocate would fit).
- **Never edits** either file. A company this version finds is written to `proposed-targets.jsonl` here, each with a link to a public page that backs the claim; a person promotes it.

## What it owns

How it collects (it may collect its own data, so the way it reads a board can be compared with the Python's), how it judges, where its state lives, and how it is scheduled: the roles, their prompts and how they hand work to each other.

## What it writes

The standard run format (`runs/DATE/all-jobs-DATE.json` and `jobs-of-interest-DATE.json`, checked by `../../compare/check_run_format.py`) and an append-only log in `../../logs/crewai-crew/`. It is compared with the reference run by `../../compare/compare_runs.py`.

## How it is judged

Oracle: Agreement, plus the broken-source test and invariant tests. The same columns as every version are in `../PLAN.md`: broken-source test, what it found, Discord precision, log against outside evidence, heartbeat, where the rules live, unattended completion, cost and time, time to first working version.

## To do

Everything. First: make it write the standard run format on one day's boards, then run `../../compare/compare_runs.py` against that day's Python run.
