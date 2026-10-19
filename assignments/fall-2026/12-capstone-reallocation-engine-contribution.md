<!-- Source: Canvas export info7375-21966-st-computational-skepticism-sec-08-fall-2026-bos-1-tr-export.imscc, assignment text as exported. Due date converted from the export's UTC. -->

> **Canvas assignment · 250 points · NOT PUBLISHED in Canvas yet · exported due date Sun Aug 16, 2026, 11:59 PM ET** (a summer 2026 date; reset it if this assignment is used this term)

# Capstone — A Working Professional Contribution to the Reallocation Engine (250 points)

**Companion project for *The Reallocation Engine* · final project** **Type:** a real, mergeable contribution to a live evidence-first system — built to the standard a working professional would ship, not a class exercise thrown away after grading. **Choose-your-focus:** you pick the contribution. It must clear the book's quality bar and solve a real gap the book names. **Deliverables:** the contribution (code + recipe/card) · a verified-data attestation · an honest run · a GitHub PR to the real repo · a **portfolio piece** you can show an employer · an **explainer video**.

> *"Can the model verify this against reality, or only against itself? If only against itself, it's yours."* — Ch 16, The Build and the Honest Run
>
> This is the project that turns the course's skepticism into a résumé line. You are not writing about the engine. You are adding something to it that runs, that a maintainer could merge, and that a hiring manager could open.

------------------------------------------------------------------------

## The engine (one paragraph, so the contribution lands in the right place)

The Reallocation Engine is an evidence-first job-search system that fights **information asymmetry** for international students and early-career technical workers. Its floor is the **verified-data contract**: *"Run the script and read the audit before you prompt. Never invent a count, a rate, or a coverage number."* Its components are the SEC Form D funding detector, the 80-Days sponsorship scorer, ATS detection + liveness, BLS/O\*NET role quality, the visa-timeline gate, the Bayesian role scorer, the OPT framing generator, the ATS-safe résumé renderer, the recipe runtime, and the pipeline tracker with its **skip-rate** metric (a healthy run *skips ≥50%* — skipping is a successful outcome). Governance lives in `SNICKERDOODLE.md`, `DOMAIN.md`, `DATA_CONTRACT.md`, and `recipes/_shared.md`. Repo: `github.com/nikbearbrown/the-reallocation-engine/`.

------------------------------------------------------------------------

## Step 1 — Choose your contribution (and clear the bar before you start)

Pick **one** real contribution. The book names these gaps directly; any of them is fair game, and you may propose your own if it clears the same bar. Each entry says which chapters it satisfies.

**Data connectors (the most-named openings)**

- **A new ATS provider connector** — Workday, iCIMS, SmartRecruiters, embedded-Greenhouse, or an Ashby variant (Ch 8 ships only Greenhouse/Lever/Ashby). Must be **zero-token**, write to the unified postings schema, and **separate EMPTY from ERROR**.
- **An entity-resolution / employer-name-matching module** (Ch 5, 7) — normalize punctuation, case, and legal suffixes to join DOL ↔ USCIS ↔ SEC names. Must emit **before/after join-coverage counts** and a sample of rescued rows, and must never enable fuzzy matching without a human sign-off. This one directly flips artifact-"Unknown" sponsorship tiers into real ones.
- **An H-1B lottery-calendar / USCIS processing-time connector** feeding the visa-timeline gate's `expected_time_to_start` (Ch 10).
- **A local/metro wage-adjustment layer** over BLS OEWS national numbers (Ch 9 flags this gap explicitly).

**Scorers & validation harnesses**

- **A gate-behavior unit-test harness** (Ch 11, 16) — prove liveness and timeline **zero** the composite, catching the *gate-as-vote* bug that is the capstone's named build failure. High value, tight scope.
- **An automated ATS paste-test / parse harness** (Ch 13) — programmatic PDF text extraction with per-field PASS/FAIL for name, titles, dates, headings; optional multi-parser comparison.
- **A calibration-curve harness** for the sponsorship scorer (Ch 5) — "has anyone checked this scorer's calibration curve?"
- **A provenance inspector** (Ch 14) certifying each recipe run finding-grade vs. judgment-grade, or a **recipe↔card drift checker** (Ch 4).
- **A "one-question test" / verb-taxonomy output linter** (Ch 3, 5) — flag unsourced sentences and over-warranted verbs in engine outputs.

**Modes, ledgers, dashboards**

- **A fourth verify pipeline** or a **draft recipe promoted to runnable** (`apply`, `followup`, `interview-prep`, … are scaffolds awaiting real scripts).
- **An override ledger + weights-profile switcher** (Ch 11) — domestic vs. international binding-constraint profiles; overrides logged with the private fact that justified them.
- **A skip-rate / allocation dashboard** (Ch 15) read against the ≥50% target with sample-size caveats, or a **ghost-job prevalence dataset + visualization** (Ch 8) — both must respect the `data/ats/` privacy rule.

**The bar every contribution must clear (from Ch 16 + Appendix 98) — read this before you commit to one:**

1.  **Every number traces to a record** (or is explicitly labeled *model-judgment* / *your-input*).
2.  It ships as a **two-customer pair**: an AI recipe with the nine required sections **and** a human `.card.md` with **≥4 named failure modes** including drift and contract-violation.
3.  It declares its **phase gates, each with a failure path** — *"if a gate has no failure path, it is not a gate, it is decoration."*
4.  It writes an **audit** and a **`RUN_LOG.md`** entry.
5.  It prefers **"not implemented yet"** to fabrication.
6.  It keeps **`data/ats/` and all private data uncommitted**, and **never self-certifies honesty** — a human signs the attestation.
7.  A contribution that produces **finding-shaped output with no script behind it** is, by the book's own definition, the failure the engine exists to prevent — and is graded as such.

If your chosen contribution can't meet all seven, pick a smaller one that can. A tight, correct gate-behavior harness is worth more than an ambitious connector that fabricates coverage.

------------------------------------------------------------------------

## Step 2 — Build the contribution (code + the two-customer pair) (90 pts)

Build it into the real repo's structure (`scripts/` lowercase, `recipes/`, `data/`, `reports/`, `output/` for generated artifacts). The contribution is judged as a working professional's, on three axes:

- **It works (60).** The code runs, does what it claims, and clears its own **testable handoff conditions** — *"The scan returns real postings with provenance,"* never *"it looks done."* If it's a connector, it pulls real feeds and separates EMPTY from ERROR. If it's a harness, it actually fails on the bug it targets and passes when fixed. If it's an entity-resolver, it reports real before/after coverage on real data.
- **The two-customer pair (30).** An **AI recipe** (complete, explicit, imperative, read-first order, verbatim commands, stop conditions, log template — the **nine required sections**: executive summary, required reads, phase gates, primary stored tools *or* "no stored script exists," workflow, output contract, verification checks, logging rules, stop conditions) **and** a human **`.card.md`** (purpose, what it can/can't verify, dependencies, annotated commands, what it produces, **≥4 failure modes** including **drift** and **contract-violation**). Update both in the same commit.

------------------------------------------------------------------------

## Step 3 — The verified-data attestation (35 pts)

Prove the contract holds for your contribution:

- **The verified-vs-inferred boundary table** — the book's "Give to AI / Keep for yourself" split, applied to your component: every field/number your contribution emits, labeled *record* / *script-output* / *local-evidence* / *external-source* / *model-inference* / *your-input* / *missing*.
- **Every number traces.** For each figure your component reports (a coverage count, a rate, a score, a PASS/FAIL), name the script and the record it came from. If a number is a model judgment, it is labeled as one, not printed as a fact.
- **The ethics gate, passing (Ch 16):** (a) **Privacy** — no `data/ats/` or private file staged for commit; `npm run doctor` clean. (b) **Honesty** — nothing your component generates misrepresents status or invents a metric. *If either fails, the run does not happen.* Show the gate passing.

------------------------------------------------------------------------

## Step 4 — The honest run (35 pts)

Run your contribution for real and report it the way Ch 16 requires:

- **Plausibility audit before you trust the output** — sanity-check a batch. Does a ~0 sponsorship collapse the composite? Does a role past the OPT window get gated, not merely down-weighted? Catch the failure that *"ran, looked reasonable, and was wrong in exactly the way fluency hides."*
- **Real terminal output, pasted, not described** — the actual commands and their actual output.
- **A deliberate break attempt** — try to make your own contribution produce a wrong answer (a fuzzy-match false join, a ghost posting scored live, a gate that behaves like a vote). Report what you found. *The break attempt is worth more than a clean run.*
- **The metric readout, if your component touches decisions** — e.g. the **skip rate** in its working range, coverage before/after, parse PASS-rate, calibration error.
- **A "what the machine could not know" account** — the honest close: the judgment your contribution cannot make, the record it cannot see, the human call it hands back.

------------------------------------------------------------------------

## Step 5 — The GitHub PR (25 pts)

Ship it where a maintainer would review it:

- **Fork** the repo; branch `contrib/<name>-<component>`.
- Contribution code under `scripts/` + `recipes/`; docs/audit under the right folder; nothing generated committed as source of truth.
- **Run `npm run verify` and `npm run doctor` before you push.** A PR that fails conformance or leaks private data **is not gradeable** — the same bar the engine holds every run to.
- **No PII, no `data/ats/` contents.**
- PR description names: the gap it closes, the chapters it satisfies, the verified-vs-inferred boundary, and the one limitation it cannot verify.

Submit the PR link. (If the upstream repo doesn't accept external PRs, submit the PR against your own fork with the full diff and a maintainer-ready description — the discipline, not the merge, is what's graded.)

------------------------------------------------------------------------

## Step 6 — The portfolio piece (35 pts)

The artifact you show an employer. A professional case study (2–4 pages or a clean single-page site), written for a technical hiring manager, not for the grader:

- **The problem** — the specific information asymmetry your contribution attacks, for a specific person.
- **What you built** — the component, in plain professional language, with the architecture in a diagram or a few sentences.
- **The measurable improvement** — the number that makes it real: join-coverage before/after, artifact- Unknowns rescued, skip-rate moved into range, parse PASS-rate, calibration error reduced, a bug the harness now catches. One honest metric beats three vague claims.
- **Verified vs. inferred** — the boundary, stated plainly, because *that* is the professional signal: you know what your system does and does not know.
- **The failure modes and the one limitation it cannot verify** — naming what it can't do is the strongest thing on the page.
- **A demo** — a short screen capture, a linked PR, or a runnable snippet. Something a reader can open.

Portfolio-grade writing: calibrated verbs, no fabricated metrics, no `[ASK ME]` placeholders left in. This is the piece that outlives the course.

------------------------------------------------------------------------

## Step 7 — The explainer video (20 pts)

3–6 minutes. Its graded core is **at least one unscripted, uncut segment showing a live terminal run** — the real command, the real output appearing in real time, no cut inside the take. Arc:

- The domain and the asymmetry (~45s).
- **The uncut live run** — your contribution executing (or `npm run verify && doctor`), on a **fictional scenario and public example data — never real PII on screen**. If it errors on camera, **leave it in and narrate the fix**; that is the most honest footage you can submit.
- **One thing you learned** from running or failing to run it, and **one honest limitation** it cannot verify.

You may build the video with the brutalist explainer pipeline (the same one used for the 25-point progress report), but the uncut run must be real screen capture, not a slide of pasted output.

------------------------------------------------------------------------

## Grading (250 points)

| Component | Pts | What earns full marks |
|----|----|----|
| Contribution works | 60 | Runs, does what it claims, clears its testable handoff conditions; connectors separate EMPTY from ERROR; harnesses fail on the target bug and pass when fixed. |
| Two-customer pair | 30 | AI recipe with all nine sections + human card with ≥4 failure modes incl. drift and contract-violation; both updated together. |
| Verified-data attestation | 35 | Every emitted number traces to a record or is labeled a judgment; the verified/inferred boundary table is complete; the privacy + honesty ethics gate is shown passing. |
| The honest run | 35 | Real pasted output, a real plausibility audit, a real break attempt, the relevant metric readout, and a genuine "what the machine could not know" account. |
| GitHub PR | 25 | Forks and branches correctly; `verify` + `doctor` clean; no PII; a maintainer-ready description naming the gap and the limitation. |
| Portfolio piece | 35 | Employer-ready: the problem, the build, **one honest measurable improvement**, the verified/inferred line, the failure modes, and an openable demo. |
| Explainer video | 20 | 3–6 min with a real uncut live-terminal-run segment; one lesson, one honest limitation; no real PII on screen. |
| Honesty overlay | 10 | Nothing self-certified; verbs calibrated throughout; a fabricated metric or a finding with no script behind it forfeits this and caps the run/attestation components. |

**The zero condition (non-negotiable, from the verified-data contract):** any number your contribution prints that did not come from a record and is not labeled as a judgment — an invented coverage rate, a fabricated liveness call, a made-up calibration figure — is not a deduction. It is the exact failure the engine exists to prevent, and it caps the affected components at zero. *"Prefer 'not implemented yet' over pretending the system can do more than it can verify."*

------------------------------------------------------------------------

## How this connects to the rest of the course

The two 100-point Computational-Skepticism assignments teach the instruments — auditing a system you didn't build, and breaking one you did. This capstone is where those instruments earn money: a real contribution to a live system, attested to the verified-data contract, run honestly, and packaged as something a professional would ship and a hiring manager would open. The **25-point progress report** (the brutalist-explainer milestone) sits between kickoff and this final submission — it is your `/v0` gate, your phase-gate plan, and your first honest run, on the record, before the full build is due.
