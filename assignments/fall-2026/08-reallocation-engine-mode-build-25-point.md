<!-- Source: Canvas export info7375-21966-st-computational-skepticism-sec-08-fall-2026-bos-1-tr-export.imscc, assignment text as exported. Due date converted from the export's UTC. -->

> **Canvas assignment · 25 points · NOT PUBLISHED in Canvas yet · exported due date Fri Jul 17, 2026, 11:59 PM ET** (a summer 2026 date; reset it if this assignment is used this term)

The Reallocation Engine — Mode Build Assignment (25-Point Version)

Total: 25 points

20 points — rubric (Mode Design 8 · Domain Justification 7 · Worked Run 5) 5 points (20%) — Explainer Video (qualitative)

This is a lighter-weight variant of the 100-point Mode Build Assignment. The difference: in-class, live presentation is replaced by a short explainer video. Everything else about the standard — build something that runs, verify it, be honest about what it can't do — still applies. Nothing has to be perfect. It has to be honest, and it has to have actually run.

Overview

The Reallocation Engine is an evidence-first system for international students and early-career technical workers. The core claim is that the job-search problem is not motivation — it is information asymmetry. You cannot easily see which companies have H-1B sponsorship history, which just filed a Form D, whether a posting is even still live, or whether a role is the kind of work AI is about to commoditize. The engine makes those signals visible across three layers:

80 Days to Stay — 30K+ companies mapped with SEC Form D funding signals and H-1B sponsorship history. Job-Ops — ATS provider detection, posting liveness checking, application tracking, pipeline-integrity scripts. The Cognitive Pivot — BLS/O\*NET role-quality scoring on the thesis that the labor premium is shifting toward verification, system judgment, and causal reasoning — work AI cannot yet do reliably.

The repository is governed by SNICKERDOODLE.md (the constitution) and indexed by DOMAIN.md. Read both before you start. The prime directive: use verified local data and tested scripts first; use an LLM only to explain, summarize, draft, or make bounded judgments after the data has been checked. Your mode follows the same rule.

GitHub: [https://github.com/nikbearbrown/the-reallocation-engine/](https://github.com/nikbearbrown/the-reallocation-engine/)

The Assignment

Design and run a new mode for The Reallocation Engine that is relevant to your professional domain or career goals.

A mode (the repo calls these recipes — they live in recipes/, e.g. case-ds-faang-opt-runway.md) is a student-facing operating recipe. It declares what data to check, which scripts to run, what the output should look like, and what to log. Modes check verified data and tested scripts first; they do not ask an LLM to guess when a dataset or script can answer the question.

Your mode must either:

use existing repo data and scripts in a new workflow suited to your domain, or propose new data sources or commands the repo does not yet have, with a clear rationale for why they belong.

You must run at least one real, tested script from the repo against real data and show the output. You do not have to implement every script your mode proposes — but the mode must be grounded in commands that actually exist and that you actually ran. Where a script does not yet exist, you mark it with a typed \[TODO\] (see the lifecycle section) and label its output as proposed, never as if it ran.

Before You Start: Get the Engine Running Clone the repo and install: npm install. Read SNICKERDOODLE.md, DOMAIN.md, AGENTS.md, and recipes/README.md. Confirm the toolchain works — run the conformance check: npm run verify. Try a real, side-effect-free run so you have something to anchor your mode to. Any of these work today: npm run ats:scan -- --dry-run \# ATS provider detection / scan, no writes npm run ats:liveness -- \<job-url\> \# posting liveness — a GATE, not a vote npm run score \# BLS/O\*NET role-quality scorer npm run resumes:pdf -- --all \# render resumes (reads private/, writes back to private/) python3 scripts/sec/refresh-recent-sec-quarters.py \# SEC Form D refresh Capture the real terminal output — you will need it for the Worked Run and the video.

Personal data stays private. Your real résumé, application tracker, contacts, and outcomes live in private/ and data/ats/ (gitignored). You may read them locally, but never copy, paraphrase, or commit personal data into a tracked file, a report, a log, or the video. If you generate an artifact from private data, write it back into private/. npm run doctor enforces this.

What to Submit

1.  Your Mode File (the primary deliverable)

Write a mode file in the style of the recipes in recipes/. Name it for your situation (e.g. case-biostat-h1b-soc-15-2041.md). It must include:

Status frontmatter following the recipe lifecycle (see below). Be honest about which stage you actually reached. Purpose — what the mode does and exactly when to use it. Source Inventory — what existing data sources or scripts it uses, with exact paths or commands (data/80-days-to-stay/…, data/BLS/…, npm run …, scripts/…). Proposed additions — any new data sources or commands, each with a justification for why it belongs, marked with a typed \[TODO\]. Phase gates — the hard stops a human must clear, each with a testable condition. Liveness and visa timeline are gates, not votes. What it can and cannot verify — drawn explicitly. This boundary is the heart of the grade. Output Contract — an agent log (JSON) and a human report (Markdown table or template). One artifact cannot serve both readers (P5). Stop conditions — when the mode must refuse to produce a score rather than guess. A log template for logs/RUN_LOG.md.

2.  Domain Justification (one page or less)

Explain:

Who uses this mode and in what exact situation. What information asymmetry it addresses — what can this person not easily see without it? How it connects to one or more engine layers (80 Days, Job-Ops, Cognitive Pivot). Failure modes — name 1–2 errors specific to your domain. Not "the model might hallucinate," but the shape of the error and, critically, for whom it would be hardest to catch.

3.  Worked Run (real execution + verification + reflection)

Run your mode — or the parts of it that exist — against at least one real or realistic scenario, and show the actual output. Include:

Inputs you used (anonymized if drawn from private data). Commands you ran, verbatim, and their real terminal output (paste it; don't describe it). Verified vs. inferred — a line-by-line split of what the data/scripts established versus what you or an LLM judged. Verification — how you confirmed the output was real: re-ran with --dry-run, parsed the JSON, cross-checked a count against the source, deliberately tried to break it (see the Attestation format). Reflection — what went well, what the mode got wrong or missed, and your next steps. Nothing is perfect; say where yours isn't.

4.  A RUN_LOG entry

Append a real entry to logs/RUN_LOG.md (or include it in your submission) recording the run: date, mode, inputs, outputs, result, open issues. No secrets, no personal contact details, no private application notes.

5.  Explainer Video (5 points, 20% — replaces in-class presentation)

A short video (3–5 minutes) walking through your mode. No slides required — screen-record your mode file and terminal directly. It must cover:

the domain or situation you designed for, the information asymmetry the mode addresses, one concrete thing you learned from running (or failing to run) it, one honest limitation — something it cannot verify, at least one unscripted, uncut segment showing a live terminal run — not a narrated screenshot, not an edited-together highlight reel. This is the part that proves you can operate the mode, not just describe it.

Upload the video file or an unlisted link (no public posting of private data) with your submission.

Recipe Lifecycle (be honest about where you landed)

Your status frontmatter is a claim, and per the constitution every claim needs evidence. Editing the status without the evidence is a violation, not a promotion.

DRAFT ──► SPECIFIED ──► RUNNABLE-SAMPLE ──► RUNNABLE-LIVE ──► VERIFIED

yaml

``` code-block__code
---
status: DRAFT          # DRAFT | SPECIFIED | RUNNABLE-SAMPLE | RUNNABLE-LIVE | VERIFIED
todos_open: 0
last_gate: null
attestation: null
recipe_version: 0.1.0
---
```

A mode honestly marked RUNNABLE-SAMPLE with one real run and a clear-eyed list of what it cannot do will score higher than one marked VERIFIED with no evidence. The honesty rule is graded, not decorative.

Attestation (include in your Worked Run)

markdown

``` code-block__code
## Attestation
- Recipe: <name> v<version>
- By: <name> · <date>

### Tested
| Ran | Saw | Expected |
|---|---|---|
| <command or action> | <observed result> | <expected result> |
| <at least one deliberate attempt to break it> | ... | ... |

### Did not test
- <honest list — an empty one is the new "it works">

### Broke during testing, fixed
- <what failed, what changed, where>
```

How to Submit

Submit both:

A zip upload (to the course LMS) named reallocation-\<yourname\>-mode.zip, containing: your mode file, the one-page domain justification, the worked-run write-up with pasted real output and attestation, your RUN_LOG.md entry, the explainer video file or an unlisted link, any new/edited scripts or sample data (no personal data — scrub private/ and data/ats/).

A GitHub pull request to nikbearbrown/the-reallocation-engine: fork the repo, create a branch mode/\<yourname\>-\<domain\>, add your mode file under recipes/, your justification and worked run under assignments/submissions/\<yourname\>/, run npm run verify and npm run doctor before pushing — a PR that fails conformance or leaks private data is not yet gradeable, open the PR with a title naming your domain and the lifecycle stage you reached.

The zip is your submission of record; the PR is the proof it runs in the real tree.

Rubric (25 points)

Mode Design Quality — 8 points

| Points | Description |
|----|----|
| 7–8 | Mode is specific to a real domain or career situation. Data sources, commands, gates, and output formats are named precisely and the named commands actually exist. The boundary between verified and inferred is clearly drawn. The mode ran. Someone in this situation would immediately recognize the workflow. |
| 4–6 | Reasonably specific, runs, but one or two sections are generic or could apply to any job-seeker, or the verified/inferred line is fuzzy in places. |
| 2–3 | Vague, overly broad, or leans on prompting where a script or dataset could answer; or never actually ran. |
| 0–1 | No mode, or an entirely prompt-based recipe with no data or script grounding. |

Domain Justification — 7 points

| Points | Description |
|----|----|
| 6–7 | Identifies a specific information asymmetry. Connects clearly to at least one engine layer. Names 1–2 failure modes specific to the domain — the shape of the error and who would struggle most to catch it. |
| 3–5 | Present but generic. Failure modes apply to any job-seeker. |
| 0–2 | Absent or only restates the assignment. |

Worked Run — 5 points

| Points | Description |
|----|----|
| 5 | Real command output from a real or realistic scenario, pasted not described. Verified-vs-inferred split is explicit. Attestation includes a deliberate break attempt. Reflection names what went well, what the mode missed, and concrete next steps. |
| 3–4 | Output present with thin verification, or reflection without a real run, or a missing break attempt. |
| 1–2 | Output described but not shown, or no reflection. |
| 0 | No worked run, or output fabricated without acknowledgment. |

Explainer Video — 5 points (20%, qualitative)

| Points | Description |
|----|----|
| 5 | Clear domain, the asymmetry lands, includes a genuine unscripted terminal segment, names a real limitation, holds to 3–5 minutes. |
| 3–4 | Covers the material but generic, over time, or the "live" segment is clearly edited/scripted. |
| 1–2 | Video present but thin — restates the mode file with no new insight. |
| 0 | Absent, or only restates the assignment. |

What "Specific Enough" Looks Like

| Too Generic | Specific Enough |
|----|----|
| Job-seeker in tech | International master's student in data science, OPT expiring in 8 months |
| Researcher | PhD student in biostatistics evaluating industry roles that sponsor H-1B for SOC 15-2041 |
| Business professional | MBA candidate targeting pre-Series B fintech companies with recent Form D filings |
| Engineer | Mechanical engineer on STEM OPT extension scoring role resilience with BLS cognitive-demand scores |

The test: would a student in that exact situation immediately recognize the workflow as built for them, or could it describe any international job-seeker?

Examples of Possible Modes

Starting points, not requirements — design for your own situation:

biotech.md — roles at Form D-funded biotech firms, scored with life-sciences SOC codes and H-1B history for those codes specifically. opt-countdown.md — prioritizing applications by company sponsorship timeline against a specific OPT end date. cognitive-fit.md — filtering roles by cognitive-pivot score to find positions resilient to AI substitution in a target SOC group. salary-floor.md — using BLS OEWS wage data and H-1B median-salary fields to set a realistic salary floor before applying. startup-triage.md — using Form D recency and amount to separate viable early-stage firms from funding-dry ghost employers.

The Honesty Rule

The engine's prime directive: use collected data and tested scripts first; use prompting only to explain, summarize, draft, or make bounded judgments after the relevant data has been checked. Your mode follows the same rule. If data is missing, say it is missing. If a script doesn't exist yet, propose it with a typed \[TODO\] — don't pretend it runs. The best submissions, on paper and on video, are the ones clearest about what the mode cannot do.
