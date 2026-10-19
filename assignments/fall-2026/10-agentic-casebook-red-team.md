<!-- Source: Canvas export info7375-21966-st-computational-skepticism-sec-08-fall-2026-bos-1-tr-export.imscc, assignment text as exported. Due date converted from the export's UTC. -->

> **Canvas assignment · 100 points · NOT PUBLISHED in Canvas yet · exported due date Wed Aug 5, 2026, 11:59 PM ET** (a summer 2026 date; reset it if this assignment is used this term)

# Assignment — The Agentic Casebook: Red-Team One System (100 points)

**INFO 7375 · Computational Skepticism for AI** **Type:** AUDIT (take a system that already exists and trace where it breaks and who owns the break) **Choose-your-focus:** you pick the system, and you pick **three** of the book's thirteen skeptical lenses to turn on it.

> *"Skepticism is easy when something looks suspicious. The skill is doing it when the output looks right."* — Introduction
>
> This is the AUDIT half of the course's core skill. Its twin is *Build It, Then Break It* (the BUILD assignment), where you turn the same instruments on something you made. Here you turn them on something already running in the world.

------------------------------------------------------------------------

## What you are doing

You will choose **one real agentic AI system** — the book calls it your **Pebble** — and red-team it, producing a **casebook**: a small, evidence-backed collection of the ways it can fail, written the way security researchers write up the systems they break. You do not need to have built the system. You need to be able to observe it, feed it inputs, and check its outputs *against the world* rather than against its own report.

You will not audit the whole book's worth of lenses. You will **choose three** chapters' instruments and apply each one, deliberately, to your Pebble. The grade is not on how many failures you find. It is on the honesty of your method: did you **write down what you expected before you looked**, did you check the **world** and not just the **artifact**, and can you **name who owns each break**.

------------------------------------------------------------------------

## Step 1 — Choose your Pebble and write the System Dossier (10 pts)

Pick an agentic AI system — ideally one with real consequences when it fails. It must be:

- **Agentic** — it takes actions through tools (sends mail, edits files, calls APIs, moves money, files tickets, posts content), not just a chatbot that only talks.
- **Accessible** — you can run it, instrument it, or study it from solid public documentation.
- **Meaningful blast radius** — a wrong action has real consequences (a deletion, a disclosure, a purchase, a denied application).
- **Safe and ethical to poke** — sandboxed, your own, or a documented public case. Do not attack systems you are not authorized to test. A well-documented published failure (e.g. an *Agents of Chaos* case) is a legitimate Pebble.
- **Right-sized** — small enough to study across three lenses, rich enough to produce **5–11 distinct failure cases**.

Write a one-page **System Dossier** and pin it to the front of your casebook: system name, architecture in two sentences, its **tool surface** (what actions it can actually take), deployment context, a candidate failure mode you already suspect, and your access constraints.

*Examples of acceptable Pebbles:* an email or calendar agent you can sandbox; a customer-support agent; a coding agent with shell/file access; a retrieval agent that acts on what it finds; a documented public agent failure you reconstruct from primary sources.

------------------------------------------------------------------------

## Step 2 — Lock your prediction (the method, not a step) (built into every case)

Before you observe the system on a given probe, **write and date what you expect to happen.** The book calls this the prediction-lock, and it is the difference between skepticism and hindsight. A case where the system did what you predicted is still a case; a case where it surprised you is a better one — but only if the prediction was on the record *first*. Ungrounded "I knew it would do that" earns nothing.

------------------------------------------------------------------------

## Step 3 — Choose THREE lenses and apply each one (45 pts — 15 each)

Pick **three** of the following. Each names the actual instrument from its chapter; applying the instrument correctly to *your* Pebble is what earns the points. For each lens you produce **one case** (using the case template in Step 4) plus the short analysis the lens calls for.

| \# | Lens (chapter) | The instrument you apply | The case it produces |
|----|----|----|----|
| A | **Probability & base rates (Ch 2)** | Find the system's confidence number and the real **base rate**; run **Bayes** on one flag; state the **Popperian falsification condition**. | A confident number priced against its base rate — is the certainty earned? |
| B | **Data validation (Ch 3)** | Reconstruct the **epistemic frame** of the data the system reads (six-step procedure; "why exactly N rows?"; what is *not* in the data — MCAR/MAR/**MNAR**). | A silent structural assumption in the system's data that procedural EDA would miss. |
| C | **Robustness (Ch 4)** | Run a small **probe suite** (prompt sensitivity, authority escalation, proxy-feature, tool-surface, distribution-shift); frame failures as **non-robust features** ("robust against *what*?"), open the **Rung-3 counterfactual**. | A perturbation that breaks it, and what the break reveals about the proxy it learned. |
| D | **Explainability (Ch 5)** | Collect request vs. the agent's **self-explanation** vs. its **actual tool calls** vs. ground-truth state over 5–10 tasks; classify each mismatch **technically-wrong / technically-accurate-but-practically-misleading / properly-calibrated**. | A gap between what the system *says it did* and what it *did*. |
| E | **Bias & leverage (Ch 6)** | Draw the causal graph from world to outcome; walk the **ten bias mechanisms**; run a **leverage analysis** to locate where the bias lives and **name the owner** of that node. | The single highest-leverage place the bias enters — rarely the model. |
| F | **Fairness (Ch 7)** | Instantiate two conflicting definitions (**demographic parity / equalized odds / calibration parity**) on the system's population; show the **impossibility** on its own numbers; write a **defended choice** and name who should have decided. | A values decision the system made silently, surfaced and put on the record. |
| G | **Agentic false-success (Ch 8)** | Catch a **false success report** — the agent says done; you check world state and it isn't; write the **stop / gating condition** ("you broke my toy" test). | The report-vs-world gap that defines agentic failure. |
| H | **Delegation (Ch 9)** | Build the 8-item **delegation map** for one workflow the system runs; find one **handoff condition** that is not testable ("looks good" is not a handoff condition) and rewrite it so a non-author could check it. | An untestable handoff where the system's word is taken on trust. |
| I | **Honest visualization (Ch 10)** | Take one chart the system (or its dashboard) produces; audit it against the **nine-item deceptive-visualization catalog**; flag the two highest-risk encoding choices and rebuild the honest version. | A misleading output-layer encoding — a validation failure where the user actually looks. |
| J | **Uncertainty & verbs (Ch 11)** | Run a **verb audit** of the system's claims against the taxonomy (*hypothesize → suggest → observe → find → show → demonstrate → conclude → prove*); mark every over-reach and rewrite the five worst with the licensed verb. | A claim whose verb outruns its evidence. |

**Rule for all lenses:** apply the four classical moves at least once across your three cases — **Descartes** (enumerate how the confident sentence could be false), **Hume** (is this confidence about the world or only about the record so far?), **Popper** (state, in advance, what would count as failure), **Plato** (name the artifact, name the world, interrogate the relationship). Label each move where you use it.

------------------------------------------------------------------------

## Step 4 — Write each case on the standard template

Every case in your casebook uses these fields:

``` code-block__code
Case ID:
Lens applied (chapter):
Input (what you gave it):
Prediction-lock (dated, written BEFORE you observed):
Action the system took:
Reported outcome (the artifact):
Actual outcome (the world):
Which supervisory capacity failed:  [PA / PF / TO / IJ / EI]
Evidence (logs, screenshots, world-state check):
Severity:
```

The **five supervisory capacities** you choose from in that field: **\[PA\]** Plausibility Auditing, **\[PF\]** Problem Formulation, **\[TO\]** Tool Orchestration, **\[IJ\]** Interpretive Judgment, **\[EI\]** Executive Integration.

------------------------------------------------------------------------

## Step 5 — The accountability attestation (15 pts)

Write the four-part attestation for your audit (Ch 12). This is graded harder than the cases, because it is where most audits get lazy:

1.  **What you tested** — the probes you ran and what you actually observed.
2.  **What you did NOT test** — an honest list. *"An empty result set is the new 'it works.'"* Force at least three things you did not or could not check.
3.  **Who clears which gate** — for this system in its real deployment, name which party is answerable for which category of failure (owner / non-owner user / model provider / framework developer / deploying org). A responsibility that is everyone's is no one's.
4.  **Verbs calibrated** — confirm your own claims in this report are pitched at licensed verbs.

------------------------------------------------------------------------

## Step 6 — The go/no-go memo (10 pts)

One page (Ch 13). Headline recommendation with a **calibrated verb**: **deploy / modify / defer / refuse** — for a *named* use. Then: the deployments where it works, the ones where it must not be used, the ones where more work could change the answer, the **named human owner**, and a **stop condition**. If your Pebble is a public case, write the memo the deploying org *should have* written before shipping.

------------------------------------------------------------------------

## Step 7 — Assemble the casebook

Deliver a small casebook:

- `00-dossier.md` — the System Dossier.
- One file per case (5–11 cases; at minimum the three from your chosen lenses, but strong submissions find more while running them).
- `failure-statistics.md` — a table: count of cases per lens, per supervisory capacity, and a fundamental-vs-contingent tally (a **fundamental** failure is one the architecture cannot fix without redesign; a **contingent** one is a bug or config).
- `attestation.md` and `go-no-go.md`.
- A one-paragraph **"what would change my mind"** honesty note.

------------------------------------------------------------------------

## Grading (100 points)

| Component | Pts | What earns full marks |
|----|----|----|
| System Dossier + Pebble selection | 10 | A genuinely agentic system with real blast radius; tool surface named precisely; a defensible candidate failure mode. |
| Three chosen lenses correctly applied | 45 | Each instrument used *as the chapter defines it* — not name-dropped — on your own system, each with a dated prediction-lock and a real world-state check. 15 each. |
| The four classical moves, labeled | 10 | All four appear at least once, each doing real work (not decoration), correctly labeled. |
| Accountability attestation | 15 | A real "what I did NOT test" list (≥3), and responsibility distributed to *named* parties, not diffused. |
| Go/no-go memo | 10 | A calibrated verb tied to a named use, a named owner, and a testable stop condition. |
| Honesty: prediction-vs-result gaps | 10 | Predictions were on the record first; surprises are reported as surprises, not rewritten. A wrong prediction honestly logged scores higher than a vague right one. |

**Honesty floor (applies across the rubric):** a fabricated case, a screenshot that doesn't show what you claim, or an "actual outcome" you asserted without checking the world is not a deduction — it is a zero on that case, because it is the exact failure this course exists to catch. Checking the *artifact* and reporting it as the *world* is the error, not a shortcut around it.

**Optional relative-quartile overlay (course tradition):** if your section grades on the honesty quartile, the strongest casebooks are the ones clearest about what they could *not* test and least eager to claim a clean result. Evidence you actually ran the probes — real logs, real world-state checks — outranks the number of failures found.

------------------------------------------------------------------------

## Notes on scope and honesty

- **You are auditing, not redesigning.** "The agent is given. Do not propose a redesign." Your job is to find where it breaks and who owns the break — proposing a validation-scope change is welcome; rebuilding the system is out of scope.
- **The artifact is not the world.** Every "actual outcome" must be a check against reality — the server state, the sent folder, the actual file, the real record — not the system's own success message.
- **Undefended gaps are where the patients die.** The point of the "what I did NOT test" list is that the unchecked path is exactly where the real failure will come from.
