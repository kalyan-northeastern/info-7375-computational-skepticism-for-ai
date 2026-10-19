<!-- Source: Canvas export info7375-21966-st-computational-skepticism-sec-08-fall-2026-bos-1-tr-export.imscc, assignment text as exported. Due date converted from the export's UTC. -->

> **Canvas assignment · 100 points · NOT PUBLISHED in Canvas yet · exported due date Mon Jul 27, 2026, 11:59 PM ET** (a summer 2026 date; reset it if this assignment is used this term)

# Assignment: The Reallocation Engine, Audited — Build a Useful Tool That Doubts Itself

**INFO 7375 — Computational Skepticism for AI** **Total Points: 100** (80 criterion-referenced core + 20 norm-referenced quality) **Due:** \[set on Canvas\] @ 11:59 PM **Submission:** GitHub repo (code + report) + video explainer (5–8 min) + Frictional Journal + AI Use Disclosure

> Tailoring note: this assignment references *The Reallocation Engine* as the domain text. Anchor your tool to a specific mechanism from the book (the chapter and page). Where this prompt speaks generally about "a reallocation," replace it with the book's specific engine for your chosen domain.

------------------------------------------------------------------------

## The Premise

A **reallocation engine** is any system that decides to move a scarce resource from where it is to where it "should" be — capital across a portfolio, compute across jobs, staff across shifts, inventory across warehouses, aid across regions, attention across a feed, credit across applicants. It ingests data, scores options, and outputs a **move**: take X from here, put it there.

This is the single most dangerous shape an AI system can take, and it is the exact failure the course is built to catch. A reallocation engine does not crash visibly. It produces a *plausible answer to the wrong question*: a statistically valid recommendation on a causally incoherent claim, a bias-amplifying reallocation deployed by someone with the skill to build it and the wrong framework to question it. And unlike a classifier that only labels, a reallocation engine **acts on the world** — it moves the resource — so its errors are not abstract. Someone loses the staff, the capital, the credit, the aid.

Your job is to build a genuinely useful reallocation tool **and** to wrap it in the skeptical machinery that makes it trustworthy — a tool that knows what it cannot know, communicates its uncertainty honestly, and **stops and asks a human before it moves anything that matters.**

The build is Tier 1 work — the tools are good at it, delegate freely. The validation is Tier 4 and Tier 5 work — supervising the tool, formulating the right question, distinguishing correlation from causation, knowing when the output is wrong. That validation is what this course is for, and it is the primary object of assessment here.

------------------------------------------------------------------------

## Choose Your Domain

Pick one resource and one reallocation decision you can defend with domain knowledge:

- **Capital / budget** — reallocate spend across campaigns, projects, or line items
- **Compute / infrastructure** — reallocate jobs, cache, or capacity across nodes
- **People / time** — reallocate staff, shifts, reviewers, or effort across tasks
- **Inventory / supply** — reallocate stock, beds, or bandwidth across sites
- **Attention / ranking** — reallocate feed slots, recommendations, or triage priority
- **Access / eligibility** — reallocate credit, aid, admissions, or interventions across people

The last two categories touch people's outcomes directly. If you choose them, the bias audit and the hard-stop gate below carry more weight — and so does your accountability for getting them right.

Your data can be a real public dataset (Kaggle, Data.gov, HuggingFace, an org's open data) or a carefully documented synthetic set — but if synthetic, you must state what real-world structure it does and does not capture. **Quality over volume: a small, clean, well-understood dataset beats a large opaque one.**

------------------------------------------------------------------------

## Deliverables

1.  **A working tool** — runs, ingests data, and outputs a reallocation recommendation with an uncertainty estimate. Not a notebook of disconnected cells; a thing a person could actually run.
2.  **A validation report** (PDF or Markdown in the repo) documenting the seven skeptical checks below.
3.  **A video explainer** (5–8 min) — the argument for a non-specialist: what it reallocates, the most surprising failure you found, and what a deployer needs to know that the accuracy number alone would not tell them. (*Unreal Reels* optional; any clear video tool is fine.)
4.  **The Frictional Journal** — a timestamped prediction *before* you built, and a reflection *immediately after*. (Required — see below.)
5.  **The AI Use Disclosure** block, including a specific "What the AI could not do." (Required.)

------------------------------------------------------------------------

## Core Components (80 points)

### 1. The Working Reallocation Tool — 12 points

Build the engine. It must (a) ingest your dataset, (b) produce a concrete reallocation recommendation (move quantity Q of the resource from A to B), and (c) attach an explicit **uncertainty** to that recommendation (not just a point decision). State the objective it optimizes in one plain sentence — and name what that objective leaves out.

- *Good looks like:* a runnable tool, a clear reallocation output, an honest objective statement.
- *Grading:* 12 = runs cleanly, real recommendation, uncertainty attached; 8 = runs, recommendation present but uncertainty thin; 5 = fragile or notebook-only; 3 = doesn't run as a tool.

### 2. Data Validation & the GIGO Gate — 10 points

Before the tool is allowed to reallocate anything, the data must pass a gate. Run a skeptical EDA: what does this dataset assume that isn't true? Define a **quality standard a human could check** (e.g., "every record has a timestamp, a source, and a non-null resource value; the measurement protocol did not change mid-collection"). Document what fails the gate and what you do about it.

- *Good looks like:* named hidden assumptions, a checkable gate, documented rejections.
- *Grading:* rewards finding the failure the dataset was designed (or happened) to hide — not a clean-looking table with no interrogation.

### 3. Bias Audit (data → output) — 10 points

Trace bias from data collection through to the reallocation. Who is systematically advantaged or starved by this engine, and where does that enter — the sampling, the labels, the objective, the feedback loop? Apply at least one quantitative fairness metric and evaluate **two competing fairness definitions**, documenting the tradeoff (you cannot satisfy all of them; say which you chose and what it costs). Identify the **highest-leverage intervention point.**

- *Good looks like:* bias traced to a specific mechanism, two fairness definitions in tension, an honest tradeoff, a named leverage point.

### 4. Explainability & Its Critique — 10 points

Produce an explanation of your engine's recommendations (SHAP, LIME, counterfactual explanations, or an equivalent). Then **critique it**: find at least one case where the explanation is *technically accurate and practically misleading* — where what the explanation shows and what your domain knowledge requires come apart. The gap is the point, not the plot.

- *Good looks like:* a real explanation + a specific, named case where it lies by omission.

### 5. Causal & Counterfactual Reasoning — Pearl's Three Rungs — 15 points

This is the heart of the assignment and the highest-weighted component. A reallocation is a *causal* claim: "moving the resource to B will produce a better outcome." Prove you know the difference between correlation and that claim.

- **Rung 1 — Observation:** what does the data show *correlates* with a good outcome?
- **Rung 2 — Intervention:** what would change *if you actually reallocated*? Is your engine optimizing an interventional quantity or just an observational one? Name the confounders that could make the correlation vanish under intervention.
- **Rung 3 — Counterfactual:** for one specific past case, what *would have happened* had the engine reallocated differently? State the assumptions that counterfactual rests on. Then answer plainly: **does your engine reallocate on correlation dressed as causation?** Most do. Honesty about that scores higher than a false claim of causal validity.
- *Grading:* 15 = all three rungs, confounders named, an honest verdict on the causal status of the engine; 11 = rungs present but intervention/counterfactual thin; 8 = observation only, causation assumed; ≤5 = correlation reported as cause with no interrogation.

### 6. Adversarial Robustness & Fragility — 8 points

Find where the recommendation breaks. Design a small, realistic perturbation — a distribution shift, a plausible data error, a gamed input — and document the conditions under which the engine flips its reallocation or fails. A resource-moving tool that flips under a perturbation a human wouldn't notice is not "understanding" anything.

- *Good looks like:* a specific perturbation, the failure condition documented, honest limits.

### 7. Delegation Map + the Hard-Stop Gate — 10 points

Draw the delegation map: for every component, **what does the tool decide, what do you decide, and what is the explicit handoff where your judgment overrides the output?** Then implement — or, if out of scope, precisely specify — the **HARD STOP**: the engine may recommend a reallocation, but it must **stop and require explicit human approval before executing any move that spends money, commits a resource, or changes a person's access.** Name which of these it would do, and why the gate is non-negotiable there. (Reallocation without a hard stop is how an accountable tool becomes an unaccountable one; "it ran unattended and moved the budget" is exactly the failure this gate prevents.)

- *Good looks like:* a real delegation map with a named override point, and a hard-stop gate on every resource-moving action with a stated response (approve / flag / block) and who resolves it.

### Uncertainty Communication (woven through, checked in the report and video)

Across the report and the video, communicate what the engine knows and what it doesn't **without overstating or understating confidence.** A visualization that includes the uncertainty, a plain sentence a non-specialist would trust, and an explicit "here is where I would not trust this tool." This is assessed as part of components 1, 4, and the video's clarity.

------------------------------------------------------------------------

## Required Gates (not graded for points, but gating — see deductions)

### Frictional Journal

- **Before you begin:** a timestamped prediction — what you expect the hardest failure to be, how causally valid you expect the engine to turn out, and your confidence (as a number).
- **Immediately after:** a reflection — what actually happened, where your prediction was wrong, and what that says about your calibration. This is the frictional record; it is how the course tracks whether you are getting better at knowing what you know.

### AI Use Disclosure (required on every submission)

``` code-block__code
AI USE DISCLOSURE
Tool(s) used:
Portions assisted:
How used:
What I changed:
What the AI could not do: [a SPECIFIC judgment call that required your values, domain
  knowledge, or accountability — a concrete instance, not a category claim]
```

The final field must name something concrete and Tier-4/5. Not "AI can't understand context." Something like: *"The model recommended reallocating budget toward the channel with the highest observed ROI, but that ROI was confounded by seasonality it had no way to see — I know Q4 spend always over-performs because I ran last year's campaign. The correlation it optimized would not survive the intervention."* That is the irreducibly human part, and finding it is the assignment.

------------------------------------------------------------------------

## Grading Rubric

| Component | Points |
|----|----|
| 1\. Working reallocation tool | 12 |
| 2\. Data validation & GIGO gate | 10 |
| 3\. Bias audit (data → output) | 10 |
| 4\. Explainability & its critique | 10 |
| 5\. Causal & counterfactual reasoning (Pearl's three rungs) | 15 |
| 6\. Adversarial robustness & fragility | 8 |
| 7\. Delegation map + hard-stop gate | 10 |
| Uncertainty communication (woven through 1/4/video) | 5 |
| **Core total** | **80** |
| **Quality score** (norm-referenced — iteration, domain judgment, validation rigor vs. the cohort) | **20** |
| **Total** | **100** |

**Quality score (20, norm-referenced):** graded relative to the cohort. Work that shows real iteration, genuine domain judgment, and validation rigor scores at the top; minimal engagement scores at the bottom. You can reach 80 on the core rubric alone. The 20 rewards going further — the skeptical check nobody else thought to run, the causal honesty nobody else had the nerve to state, the hard-stop design that would actually survive deployment.

**Automatic deductions:**

- Missing Frictional Journal (prediction or reflection): **−10**
- Missing or category-only AI Use Disclosure ("What the AI could not do" not specific): **−10**
- Missing video explainer: **−10**
- Tool doesn't run / not reproducible from the repo: **−15**
- Engine reallocates a real resource with no hard-stop gate and no justification for its absence: **−15**
- Causal claim asserted with zero interrogation (correlation reported as cause): **−10**
- Late without prior communication: not graded (per syllabus); flagged late with notice: −5%/day.

------------------------------------------------------------------------

## What NOT to Do

- Ship a model that reports accuracy and calls it validated. Accuracy is not trust.
- Claim causal validity because the correlation is strong. Name the confounders or say you can't.
- Hide the failure. The most surprising failure you found is the most valuable thing you'll submit.
- Chase data volume. 200 clean, understood records beat 200,000 opaque ones.
- Let the engine move a resource unattended. If it spends, commits, or changes access — it stops and asks. Every time.
- Fake the "What the AI could not do" field with a category claim. Name the specific instance.

------------------------------------------------------------------------

## Submission Requirements

Submit to Canvas by the deadline:

1.  **GitHub repo link** — runnable tool + the validation report (README explains how to run it).
2.  **Video explainer** (5–8 min) — unlisted link or file; the non-specialist argument.
3.  **Frictional Journal** — prediction (timestamped before) + reflection (after), in the repo or PDF.
4.  **AI Use Disclosure** block — on the report, "What the AI could not do" specific and Tier-4/5.

File naming: `LastName_FirstName_ReallocationEngine.[pdf|md]` for the report; repo link and video link in the Canvas submission comment.

------------------------------------------------------------------------

## Resources

- *The Reallocation Engine* — the domain text; anchor your engine to a specific chapter mechanism.
- *Computational Skepticism for AI* (Brown) — the validation methodology; Pearl's ladder (Wks 3/13), GIGO/EDA (Wk 4), explainability (Wk 5), bias (Wk 6), adversarial (Wk 7), delegation/trust (Wk 10).
- Pearl, *The Book of Why* — the three rungs (excerpts on Canvas).
- Fairness metrics: `fairlearn`, `aif360`. Explainability: `shap`, `lime`.
- *Unreal Reels* (optional) — for the video explainer.
- Claude / ChatGPT / Gemini — required, per the Generative AI Policy. Use one to draft the tool and the first-pass validation, then find the load-bearing thing it got confidently wrong. That gap is the grade.
