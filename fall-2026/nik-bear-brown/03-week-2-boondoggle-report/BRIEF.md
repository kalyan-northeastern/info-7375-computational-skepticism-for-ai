# The brief — Week 2 Assignment: The Boondoggle Report

## Executive summary

**What this is.** The assignment brief Professor Bear is working through in this folder, kept here exactly as issued so a reader can check the report against what was asked.

**Why read it.** Every part of [`README.md`](README.md) answers one of the requirements below. The rubric at the bottom is the standard the finished report will be held to.

**What it asks for.** Use Gru to write a Software Design Document for a small real app (`/v0` through `/s1`), generate the Boondoggle Score (`/claude`), and write a 600–900-word reflection on where human judgment can and cannot be replaced.

---

**Computational Skepticism for AI · 25 points**

### Overview

You will use Gru — a software design documentation system built on the Irreducibly Human curriculum — to specify a small application and generate a full Boondoggle Score. Then you will write a short structured reflection on what the process revealed about where human judgment is and is not replaceable.

This assignment has two purposes. The first is operational: you need to be able to specify precisely before you can evaluate precisely, and specifying with Gru is the fastest way to develop that muscle. The second is analytical: the Boondoggle Score forces an explicit answer to the question this course is organized around — which cognitive work belongs to the human, and why? — before we have worked through the technical machinery that answers it formally.

By the end of this assignment, you should be able to describe the solve-verify asymmetry in terms of a specific project you built yourself.

Gru: https://www.nikbearbrown.com/tools/gru-tool

**Access Gru:** Set up a Claude Project using the Gru system prompt (provided in course materials). Alternatively, paste the system prompt at the start of a new Claude conversation and type /help to confirm it is running correctly.

### The Application

Specify a small, real app — something you could plausibly build in a few weeks with a collaborator, in a domain you know something about. It does not need to be original. It does not need to be ambitious. It needs to be specific enough that every component can be named and every task can be assigned.

Good candidates:

- A personal finance tracker that flags unusual spending patterns
- A research paper annotation tool with citation verification
- A scheduling system for a small clinic or tutoring service
- A content moderation dashboard for a small online community
- An automated test generator for a specific codebase you work with
- A calibration tracking tool for forecasting questions (meta-appropriate for this course)

Avoid:

- "An AI assistant for X" — too broad until you name what the AI does specifically
- Applications where your domain knowledge is thin — the assignment will expose that gap
- Applications so simple they have only two or three components — the Boondoggle Score will be uninformative

If you are unsure whether your application is appropriately scoped, run /v0 in Gru and see whether it pushes back. If Gru's /v0 gate stops you cold, that is the assignment working. Work through the pushback.

### Required Deliverables

#### Part 1 — The SDD (Software Design Document) · 15 points

Complete the following Gru commands in order. Each produces a section of the SDD.

| Command | What it produces | Required? |
|---|---|---|
| /v0 | Problem formulation gate — the one-sentence naming of the thing | Yes |
| /v1 | Problem intake — problem summary, comparable systems, success condition | Yes |
| /v2 | Architecture principles — 3–4 non-negotiable design commitments | Yes |
| /v3 | Core user flows — primary, integration, and administrative flows | Yes |
| /v4 | User and business needs — 5–8 testable need statements | Yes |
| /s1 | Core component documentation | Yes |
| /claude | Boondoggle Score — the full sequenced human/AI task split | Yes |
| Any additional section (/s2, /d1, /p4, etc.) | Extended architecture detail | Optional — encouraged |

Submit the complete SDD output as produced by Gru. Do not edit or clean up Gru's output for cosmetic reasons. Errors, flags, and pushback that Gru generated are part of the submission — they are evidence that the tool was working.

**One required addition you write yourself:** After the /v1 Problem Summary Gru produces, add a paragraph (3–5 sentences, in your own voice) explaining what Gru's pushback or refinement process changed about how you understood the problem. If Gru accepted your first formulation without pushback, explain why you think that happened — was the formulation genuinely tight, or did you get lucky?

#### Part 2 — The Boondoggle Reflection · 10 points

Write 600–900 words responding to the following four prompts. These are analytical prompts, not personal journal prompts. Cite your own Boondoggle Score for evidence — quote specific steps and handoff conditions where relevant.

**Prompt A — The Split (150–200 words).** Look at your Boondoggle Score's SUPERVISORY CAPACITY DISTRIBUTION table. Which capacity appears most often? Which appears least? What does the distribution tell you about the nature of your application — specifically, which kind of human judgment it most heavily depends on? If any capacity appears zero times, address Gru's flag directly: what does the absence mean, and is it a gap in the score or a genuine property of this particular build?

**Prompt B — The Hardest Handoff (150–200 words).** Gru names 2–3 HIGHEST-RISK HANDOFFS in the score summary. Choose the one you find most convincing. Describe, in concrete terms, what an engineer who failed that handoff would do — what they would accept from Claude that they should not have accepted, and what the downstream consequence would be. Connect this to one of the four skeptical moves from Chapter 1: which move, applied at that handoff, would catch the failure?

**Prompt C — Where Gru Was Right and Where You Disagreed (150–200 words).** Identify one place where Gru assigned a task to Claude that you believe should have been a human task — or vice versa. Argue your position. Use the distinction between mechanical execution of a specified task and judgment about whether the specification is correct as your frame. If you agreed with every assignment Gru made, say so and explain why the score was unusually well-calibrated for your application.

**Prompt D — The Solve-Verify Asymmetry Applied (150–200 words).** The course's central structural observation: producing AI output is cheap; verifying AI output is expensive. Find the single step in your Boondoggle Score where verification is most expensive relative to production — where the human task following a Claude task requires the most domain knowledge or takes the most time. Describe what a team that skipped that verification step would likely ship, and how long it would probably take before they found out.

### Grading Rubric

#### Part 1 — The SDD · 15 points

| Criterion | Points | What earns full credit |
|---|---:|---|
| Problem formulation | 3 | /v0 output names the thing being built (not the problem it solves), the insertion point, and the output. The one-sentence format is present and specific. |
| Problem intake and principles | 3 | /v1 produces a Problem Summary that could distinguish this system from a generic description. /v2 produces 3–4 principles with the collision test completed. |
| Flows and needs | 3 | /v3 primary flow is concrete at every step (no "the system processes the request"). /v4 needs are testable — each has an identifiable pass/fail condition. |
| Component documentation | 3 | /s1 documents each component with inputs, outputs, edge cases, and scope boundary. No component is documented without mapping to a Need. |
| Boondoggle Score | 3 | /claude produces a score with: labeled supervisory capacities on every human step, copy-pasteable prompts on every Claude step, testable handoff conditions on every Claude step, and a score summary including the distribution table. |

Partial credit: An SDD that reaches /s1 but has a weak /v0 formulation will be graded on what is there, but the weakness propagates — a vague problem statement usually means vague component boundaries. Gru's pushback that you overrode or dismissed will be noted.

What earns zero on the SDD: An SDD that reads as though the student handed Gru a paragraph description and accepted the first output without engaging the phase gates. The submitted output should show evidence of iteration — second attempts, corrected formulations, resolved pushback.

#### Part 2 — The Boondoggle Reflection · 10 points

| Criterion | Points | What earns full credit |
|---|---:|---|
| Prompt A: Capacity distribution analysis | 2.5 | Names the distribution, connects it to a specific property of the application domain, and addresses any zero-count capacity flags specifically. |
| Prompt B: Hardest handoff diagnosis | 2.5 | Describes a concrete failure scenario (not "the engineer might miss something"), names a specific downstream consequence, and connects accurately to one of the four skeptical moves. |
| Prompt C: Assignment disagreement | 2.5 | Takes a position, names the specific step, and argues using the mechanical-execution vs. judgment-about-specification distinction rather than general intuition. |
| Prompt D: Solve-verify asymmetry applied | 2.5 | Identifies a specific step (not a general observation), describes what would ship without verification, and gives a plausible estimate of discovery timeline with reasoning. |

What earns partial credit: Reflections that describe what the Boondoggle Score contains without analyzing what it means. Describing is not analyzing.

What earns full credit: Reflections that would read as useful to an engineer who had not done this assignment — someone who could use your analysis to make better decisions about when to trust Claude output and when to verify it.

### Submission Format

One PDF or markdown document containing:

- Your full SDD output (Gru's output, unedited except for the required personal addition after /v1)
- Your Boondoggle Reflection (four labeled prompts, 600–900 words total)

Label each section clearly. Include the name of your application at the top.

No cover page required. No minimum font size or margin requirements. Clarity of argument, not length, is what is graded.

### A Note on What This Assignment Is Not

This is not a prompt engineering exercise. It is not a test of whether you can produce a good-looking SDD. It is not a test of whether you chose an interesting application.

It is a test of whether you can distinguish the work a capable AI system does from the work that requires a human being standing outside the AI system — and whether you can argue why that distinction matters for the specific technical context you chose.

The Boondoggle Score is the answer to that question made explicit. The reflection is whether you can read the answer and say something true about it.

*Assignment connects to: Chapter 1 (four skeptical moves, five supervisory capacities, fluency trap, solve-verify asymmetry) | Gru system prompt (boondoggling methodology, problem formulation gate, handoff conditions)*
