<!-- Source: Canvas export info7375-21966-st-computational-skepticism-sec-08-fall-2026-bos-1-tr-export.imscc, published assignment text. Due date converted from the export's UTC. -->

> **Canvas assignment · 25 points · due Sat Oct 10, 2026, 11:59 PM ET**

# The Reallocation Engine — Mode Design Assignment

**Total: 25 points**

- 15 points rubric
- 5 points in-class presentation (show and tell)
- 5 points relative quartile

------------------------------------------------------------------------

## Overview

The Reallocation Engine is a data and script system for helping international students and early-career technical workers cut through job-search noise. The core claim is that the problem isn't motivation — it's information asymmetry. Students can't easily see which companies have H-1B sponsorship history, which ones just got funded, or whether a posting is even still live. The engine combines three data layers to make those signals visible:

- **80 Days to Stay** — 30K+ companies mapped with SEC Form D funding signals and H-1B sponsorship history
- **Job-Ops** — ATS provider detection, job liveness checking, application tracking, and pipeline integrity scripts
- **The Cognitive Pivot** — BLS/O\*NET role-quality scoring built on the thesis that the labor-market premium is shifting toward verification, system judgment, and causal reasoning — work AI can't reliably do yet

The stack is Python + Node, with Greenhouse/Lever/Ashby scrapers, a Playwright liveness checker, and a compact SOC occupation table covering 1,000+ occupations with cognitive demand scores.

GitHub: [https://github.com/nikbearbrown/the-reallocation-engine/](https://github.com/nikbearbrown/the-reallocation-engine/)

------------------------------------------------------------------------

## The Assignment

Design a new **mode** for The Reallocation Engine that is relevant to your professional domain or career goals.

A mode is a student-facing operating recipe. It tells a student what data to check, which scripts to run, what the output should look like, and what to log. Modes use verified data and tested scripts first — they do not ask an LLM to guess when a dataset or script can answer the question.

Your mode should either:

- use existing repo data and scripts in a new workflow suited to your domain, or
- propose new data sources or commands the repo does not yet have, with a clear rationale for why they belong

You do not need to write working code. You need to design the workflow, specify what it does and does not verify, and explain why it matters for your specific situation.

------------------------------------------------------------------------

## What to Submit

### 1. Your Mode File (the deliverable)

Write a mode file in the style of the existing modes in `modes/`. It should include:

- a clear statement of what the mode does and when to use it
- what existing data sources or scripts it uses, with exact paths or commands where applicable
- what new data sources or commands you are proposing, if any, with a justification for each
- what the mode can and cannot verify — be explicit about gaps
- an output format (a table, a report template, a log entry)
- a log template for `modes/RUN_LOG.md`

The mode does not have to be implemented. It has to be honest — if a script doesn't exist yet, say so rather than pretending it does.

### 2. Domain Justification (one page or less)

Explain:

- who uses this mode and in what situation
- what information asymmetry it addresses — what can the student not easily see without it?
- how it connects to one or more of the three engine layers (80 Days, Job-Ops, Cognitive Pivot)
- what the failure modes are — what would this mode get wrong, and for whom would those errors be hardest to catch?

### 3. Worked Example

Run your mode (or a simulation of it) against at least one real or realistic scenario and show the output. Include:

- what inputs you used
- what the mode produced
- what was verified vs. inferred
- what you would change based on seeing the output

------------------------------------------------------------------------

## Rubric (15 points)

### Mode Design Quality — 6 points

| Points | Description |
|----|----|
| 5–6 | Mode is specific to a real domain or career situation. Data sources, commands, and output formats are named precisely. The boundary between verified and inferred is clearly drawn. Someone in this situation would immediately recognize the workflow. |
| 3–4 | Mode is reasonably specific but one or two sections are generic or could apply to any job-seeker. |
| 1–2 | Mode is vague, overly broad, or relies on prompting where a script or dataset could answer the question. |
| 0 | No mode submitted, or mode is entirely a prompting recipe with no data or script grounding. |

### Domain Justification — 5 points

| Points | Description |
|----|----|
| 4–5 | Identifies a specific information asymmetry. Connects clearly to at least one engine layer. Names 1–2 failure modes that are specific to the domain — not "the model might hallucinate" but the shape of the error that would be hardest for someone in this situation to catch. |
| 2–3 | Justification is present but generic. Failure modes are at a level that applies to any job-seeker. |
| 0–1 | Justification is absent or only restates the assignment description. |

### Worked Example — 4 points

| Points | Description |
|----|----|
| 3–4 | Output shown from a real or realistic scenario. Commentary names what was verified vs. inferred, what the mode missed, and what you would change. |
| 1–2 | Output present with minimal commentary, or commentary without a real output. |
| 0 | No worked example, or example is fabricated without acknowledgment. |

------------------------------------------------------------------------

## In-Class Presentation — 5 points

Five-minute show-and-tell. Walk the class through:

1.  what domain or situation you designed for
2.  what information asymmetry the mode addresses
3.  one concrete thing you learned from running (or simulating) it

No slides required. You may show your mode file directly.

------------------------------------------------------------------------

## Relative Quartile — 5 points

Assigned after all submissions are reviewed.

| Quartile   | Points |
|------------|--------|
| Top 25%    | 4–5    |
| Second 25% | 2–3    |
| Third 25%  | 1      |
| Bottom 25% | 0      |

The quartile score reflects overall quality relative to peers — specificity, honesty about what is and isn't verified, and evidence that you actually ran or simulated the workflow rather than described running it.

------------------------------------------------------------------------

## What "Specific Enough" Looks Like

| Too Generic | Specific Enough |
|----|----|
| Job-seeker in tech | International master's student in data science with OPT expiring in 8 months |
| Researcher | PhD student in biostatistics evaluating industry roles that sponsor H-1B for SOC 15-2041 |
| Business professional | MBA candidate targeting pre-Series B fintech companies with recent Form D filings |
| Engineer | Mechanical engineer on STEM OPT extension evaluating role resilience using BLS cognitive-demand scores |

The test: would a student in that exact situation immediately recognize the workflow as designed for them, or could it describe any international job-seeker?

------------------------------------------------------------------------

## Examples of Possible Modes

These are starting points, not requirements. Design for your own situation.

- `biotech.md` — evaluating roles at Form D-funded biotech companies using SOC codes for life sciences occupations and H-1B sponsorship history for those codes specifically
- `opt-countdown.md` — prioritizing applications by company sponsorship timeline compatibility given a specific OPT end date
- `cognitive-fit.md` — filtering roles by cognitive-pivot score to identify positions resilient to AI substitution in a target SOC group
- `salary-floor.md` — using BLS OEWS wage data and H-1B median salary fields to set a realistic salary floor before applying
- `startup-triage.md` — using Form D recency and funding amount to separate viable early-stage companies from funding-dry ghost employers

------------------------------------------------------------------------

## Honesty Rule

The engine's prime directive is: use collected data and tested scripts first. Use prompting only to explain, summarize, draft, or make bounded judgments after the relevant data has been checked.

Your mode should follow the same rule. If data is missing, say it is missing. If a script doesn't exist yet, propose it — don't pretend it runs. The best submissions will be the ones that are clearest about what the mode cannot do.
