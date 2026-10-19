# nik-bear-brown

A place for the public work of Nik Bear Brown's examples — INFO 7375, Fall 2026.

> **This folder is the canonical master for a project live-coded in three classes.** The same job-search tool is built in Computational Skepticism, Branding and AI, and Prompt Engineering, with a different emphasis in each. Shared code and configuration are edited **here** and propagated with `./lectern/sync.sh`. Class-specific writing is never copied. The rule, the file lists, and the recovery procedure are in **[`SYNC.md`](SYNC.md)**.

## Executive summary

**What this is.** Professor Bear's worked examples for **INFO 7375 Computational Skepticism for AI**, Fall 2026, done the way students do them and logged the way students log them.

**What we are doing now: Assignment 2, the Boondoggle Report.** The assignment asks for an application to be specified with Gru (a design document from `/v0` through `/s1`, then a Boondoggle Score from `/claude`), followed by a reflection on which work belongs to Claude and which to the human. **The application Professor Bear is specifying is a downloadable version of Gru**: instead of a prompt pasted into a Claude Project, a set of skills and scripts that runs inside a repository someone has downloaded, and can read that repository's folders and files before asking any questions.

**A mistake, kept on the record.** The first Gru session (turns 00–13 in `03-week-2-boondoggle-report/gru-session/`) specified the **wrong application**: greenhouse-watch, a job-board watcher from Professor Bear's *other* class, Prompt Engineering. Claude Code picked it after reading that class's folder and assumed that was the work. The session is kept, not deleted, because the course log keeps mistakes.

**Where the real report stands.** A second Gru session, on the downloadable Gru, has confirmed `/v0` through `/v4` and passed the Phase 1 gate. `/s1` (components) is in progress. Claude Code typed Professor Bear's answers in that session and confirmed its gates for him; he has not reviewed them yet. Gru's section outputs are in [`FRICTIONAL.md`](FRICTIONAL.md), verbatim.

| Folder or file | What it is | Shared? |
|---|---|---|
| [`SYNC.md`](SYNC.md) | What is shared across the three classes, what is not, and how to propagate | the rule itself |
| [`lectern/`](lectern/) | **The tool, canonical here.** `collect.py` reads 18 job boards across three applicant-tracking systems and keeps the teaching-related postings; `sources.json` is the watch list, `keywords.json` the filter, `ATS.md` which system each company uses. `sync.sh` copies all four out | **shared** |
| [`facts/`](facts/) | The CV as structured facts, attested | **shared** |
| [`figma/`](figma/) | The first single-company iteration: saved board, scan, kept postings | **shared** |
| [`greenhouse-watch-demo/`](greenhouse-watch-demo/) | The Reallocation Engine's watcher run on one board | **shared** |
| [`assignment-3/`](assignment-3/) | Assignment 3, robustness and explanation: a probe runner that tries to break a result on purpose, and a check of whether a fluent explanation names the feature that actually moves the output | this class only |
| [`PLAN.md`](PLAN.md) | The map of all twelve Canvas assignments: what each requires, what exists, what is still to do, and the order of attack | this class only |
| [`01-…` to `12-…`](PLAN.md) | One numbered folder per Canvas assignment, each with a `PLAN.md`. Folder 03 is the Week 2 assignment: the brief, the reports so far, and every Gru turn verbatim (it was `boondoggle-report/` until 2026-10-18) | this class only |
| [`films/`](films/) | Layouts and evidence for films in the series *Professor Bear Does His Assignments* that this folder's work produces. First: `evaluating-the-rejections/`, the arithmetic of what a hundred clean reads can show, with the script that computes it | this class only |
| [`FRICTIONAL.md`](FRICTIONAL.md) | The process log: what was tried, what went wrong, who did what, and every push | **never copied** |
| [`CLAUDE.md`](CLAUDE.md) | Rules Claude Code follows in this folder | this class only |
