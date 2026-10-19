<!-- Source: Canvas export info7375-21966-st-computational-skepticism-sec-08-fall-2026-bos-1-tr-export.imscc, assignment text as exported. Due date converted from the export's UTC. -->

> **Canvas assignment · 100 points · NOT PUBLISHED in Canvas yet · exported due date Sun Aug 9, 2026, 11:59 PM ET** (a summer 2026 date; reset it if this assignment is used this term)

# Assignment — Build It, Then Break It: A Skeptic's Portfolio (100 points)

**INFO 7375 · Computational Skepticism for AI** **Type:** BUILD (make something, then hunt for where you let a mistake in) **Choose-your-focus:** you pick what you build, and you pick **two** of the book's skeptical instruments to turn on your own work.

> *"a BUILD, where you make something and hunt for where you let a mistake in."* — Introduction
>
> This is the BUILD half of the course's core skill, and it is harder than the AUDIT, for one reason: you will defend your own fluency. The model you trained, the chart you made, the dataset you cleaned — each arrives looking right *to you*, because you made it. The assignment is to break it anyway.

------------------------------------------------------------------------

## What you are doing

You will **build one small, real artifact** and then turn the course's skeptical instruments on it — not on someone else's system, on **yours**. The whole difficulty is that a builder is the least reliable auditor of their own build, exactly the way a model is the least reliable judge of its own output. The grade rewards the moment you find where *you* let the mistake in and say so on the record.

You choose the build. You choose **two** instruments (three if you want the stretch — see the note). Keep the artifact small enough that you can actually run the instruments end to end; a toy classifier you fully understand beats a large model you can only gesture at.

------------------------------------------------------------------------

## Step 1 — Choose and build your artifact (20 pts)

Pick one. Keep it small, real, and yours.

- **A small model / classifier** — train something modest on real data (tabular, text, or image). You need to be able to get predictions *and* confidence out of it.
- **A dataset you assemble** — collect/clean a real dataset from raw sources, with joins and decisions a reader can't see from the finished file.
- **A dashboard / visualization** — turn a real finding into charts an audience would act on.
- **An agent recipe / small tool** — a scripted tool that takes an action and reports an outcome.
- **A prompt-based system** — a structured prompt or small LLM pipeline that produces a decision or a classification you can test.

Deliverable for this step: the working artifact, plus a half-page **build note** — what it does, what data or inputs it uses, and the one decision you were least sure about while making it. (That decision is usually where the mistake is; you are pre-registering the suspect.)

------------------------------------------------------------------------

## Step 2 — Lock predictions before you probe (built into every instrument)

Before you run each instrument on your own work, **write and date what you expect it to reveal.** You will be tempted to skip this because you *made the thing* and think you know. That confidence is precisely what the prediction-lock is testing. A surprise you predicted against is worth more than a confirmation you assumed.

------------------------------------------------------------------------

## Step 3 — Choose TWO instruments and apply each to YOUR build (25 pts each = 50)

Pick **two**. Each names the real technique from its chapter. Apply it to your own artifact and report what it exposes — especially what it exposes that you did not want to find.

| Instrument (chapter) | What you actually do to your own build |
|----|----|
| **Calibration (Ch 2 + Ch 11)** | Make your artifact emit its own confidence. Bin predictions by stated confidence, plot the **reliability diagram** against the diagonal, compute **Brier score** and **ECE**, fit **temperature scaling**, then re-plot on a **shifted** slice of data and report what moved. Catch the decorative number. |
| **Robustness probe (Ch 4)** | Write a small **probe suite** (≥3 probes: perturbation, proxy-feature, distribution-shift, and — for agents/prompts — authority-escalation or tool-surface). Run it; for each break, apply **features-not-bugs** framing: name the proxy your build learned, the human-relevant feature it *should* use, and what the gap says. Deliver a **robustness profile** (a table: robust against *what*, residual risk, monitoring), not a single number. |
| **Data-frame audit (Ch 3)** | Write a **datasheet** for the data behind your build (Gebru's questions, adapted), run the **six-step epistemic-frame reconstruction**, produce the **structural-assumptions table** (sampling / time-window / label-proxy / MNAR / feature-engineering / boundary), and trace one row end to end. Then plant-and-find: name a hidden failure procedural EDA would miss in *your* data. |
| **Bias & fairness (Ch 6 + Ch 7)** | Draw the causal graph from world to your artifact's output; run a **leverage analysis** to find where bias enters. Then compute at least two of **demographic parity / equalized odds / calibration parity** across a group in your data, show they **cannot all hold** (the impossibility, on your own numbers), and write a **defended choice** with a monitoring plan — or a defended "not applicable, here is why." |
| **Honest visualization (Ch 10)** | Build the **honest** version of your finding *and* a **deliberately misleading** version from the *same numbers* (no fabricated data — the misleading power must come only from encoding choices: truncated axes, aggregation that hides a distribution, cherry-picked window, color asymmetry). Put them side by side and write what each choice did. The misleading chart is for-your-eyes-only; the report ships the *comparison*. |
| **Uncertainty & verbs (Ch 11)** | Write up your build's central finding in the **three-layer document** (plain summary / technical / reproducibility appendix), then run a **verb audit** on your own plain-language claims against the taxonomy (*hypothesize → … → prove*), mark every over-reach you made, and rewrite them at the licensed verb. Say, explicitly, **what would change your mind**. |

Apply the **four classical moves** at least once across your two instruments, labeled where used: Descartes (how could my confident sentence be false?), Hume (is my confidence about the world or only about my sample?), Popper (what did I decide, in advance, would count as my build failing?), Plato (name the artifact I made, the world it claims to describe, and the relationship between them).

------------------------------------------------------------------------

## Step 4 — The confession: where I let the mistake in (15 pts)

This is the heart of the BUILD. In a page, write the **single place you let a mistake into your own work** — a leaked feature, an optimistic label, a chart choice that flattered the result, a confidence number you never checked, a join that silently dropped a subgroup. Not a hypothetical; the real one your instruments (or the process of running them) surfaced. Name:

- what the mistake was,
- **why you wanted to believe the version that contained it** (the fluency you were defending),
- how an instrument caught it (or how you caught it while running one),
- what you changed, and what residual risk remains.

A submission that reports "no mistakes found" is either not looking hard enough or not being honest, and is graded as such. Every real build has one. The skill is finding yours.

------------------------------------------------------------------------

## Step 5 — Assemble the skeptic's portfolio

Deliver:

- The **artifact** (code / dataset / dashboard / tool / prompt system) with a short run/repro note.
- The **build note** (Step 1) with your pre-registered suspect decision.
- Two **instrument reports** (Step 3), each with its dated prediction-lock, method, result, and the labeled classical moves.
- The **confession** (Step 4).
- A closing **"what would change my mind" / "still puzzling"** note.

------------------------------------------------------------------------

## Grading (100 points)

| Component | Pts | What earns full marks |
|----|----|----|
| The build | 20 | A working, real artifact you fully understand, with a build note that pre-registers the decision you were least sure of. |
| Instrument 1 applied to your own work | 25 | The technique run *correctly and fully* (e.g. an actual reliability diagram + ECE + a shifted-distribution re-plot, not a sentence about calibration), with a dated prediction-lock. |
| Instrument 2 applied to your own work | 25 | Same bar, second instrument. |
| The confession | 15 | A *real* mistake, named honestly, with the fluency you were defending made explicit and the fix + residual risk stated. |
| Prediction-locks + change-of-mind | 10 | Predictions on the record before probing; surprises reported as surprises. |
| Three-layer / reproducibility | 5 | A reader can rerun the core result; claims pitched at licensed verbs. |

**The stretch (optional, no extra points, stronger portfolio):** apply a **third** instrument. It does not raise the ceiling on the rubric, but a three-instrument portfolio is a materially stronger artifact to show an employer, and sections grading on the honesty quartile weight demonstrated range.

**Honesty floor:** fabricated results, a "reliability diagram" that isn't computed from real predictions, or a misleading chart built by changing the numbers (rather than the encoding) is a zero on that component. The misleading-visualization exercise specifically requires that **the deception come only from design choices on honest data** — inventing numbers misses the entire point.

------------------------------------------------------------------------

## Why this is the harder half

In the AUDIT assignment, the system's failures are someone else's; you are a hostile outside reader and that is a comfortable posture. Here the failures are yours, and the instruments will find things you would rather not have found. That discomfort is the assignment. The professional skill this course certifies is not "can you criticize an AI system" — it is "can you doubt your **own** output at the exact moment it looks most finished." Build something. Then break it. Then tell the truth about the break.
