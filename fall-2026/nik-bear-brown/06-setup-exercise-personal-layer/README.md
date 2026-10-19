# Setup Exercise: Your Search's Personal Layer (Professor Bear's example)

Brief: [`06-setup-exercise-personal-layer.md`](../../../assignments/fall-2026/06-setup-exercise-personal-layer.md) · Plan: [`PLAN.md`](PLAN.md)

## Executive summary

**What this is.** Professor Bear's worked example of the exercise that builds the personal data layer of a job search: three files in a `search/` folder (`resume.json`, `profile.yml`, `gaps.md`) that make a search's scores specific to one person. The exercise's rule is that the agent drafts and the owner attests.

**Where it stands (2026-10-18).**
- **`search/resume.json`: present, not attested as a résumé.** It is a copy of the résumé derived from his CV record. The record itself, `facts/professor-bear-cv.json`, was read and attested by him on 2026-09-23 ("accurate, no errors"); two sections added on 2026-09-27 are still unread by him. The exercise expects the owner to find at least three import errors; he found none, and this folder does not claim three.
- **`search/profile.yml`: done**, from his own answers, with a dated `revisions` block recording how the targets changed as he looked at the market.
- **`search/gaps.md`: not written, on purpose.** The gap between his record and his target roles has to be measured against real postings (the Google and Microsoft collectors, the business-school listing check, the existing 3,243-posting run). Written now it would be a guess presented as a finding.

**Why the order matters.** The exercise's evidence column demands that every gap cite a posting or a requirement. Collecting the postings comes first.

## The steps, and what exists

| Step | Artifact | Status | Where |
|---|---|---|---|
| 0 | `search/` created; `private-notes.md` gitignored | ✅ | `.gitignore` here |
| 1 | `search/resume.json`, attested, three errors noted | 🟡 present, not attested | [`search/resume.json`](search/resume.json) |
| 2 | `search/profile.yml` | ✅ | [`search/profile.yml`](search/profile.yml) |
| 3 | `search/gaps.md`: evidence column, plan column, one killed row, one row in his own words | ⬜ waits for collected data | none yet |
| 4 | Verification check | 🟡 partly: see [`RUN_LOG.md`](RUN_LOG.md) | `RUN_LOG.md` |
| 5 | RUN_LOG entry | 🟡 partly | [`RUN_LOG.md`](RUN_LOG.md) |

## What the agent got wrong in its first draft of `profile.yml`

These are real and are what the exercise asks the owner to find:
- **It left business schools out** (a footnote under "not about tenure"). He corrected it: they are a main target, to bring real AI expertise in to direct an AI research centre or educational effort.
- **It could not fill visa, sponsorship, location or exclusions**, and left them blank. He supplied them.
- **It recorded the reason for dropping Stripe and Writer wrongly** ("must believe in the product", "a tool he does not think is good"). He corrected it: not a judgment that they are bad or not useful, but that he does not see them as directly applicable to transformative, AI-driven improvement of education.

## Files here
- [`PLAN.md`](PLAN.md): the plan and status for this assignment.
- `search/`: the three artifacts above.
- [`RUN_LOG.md`](RUN_LOG.md): the exercise's log entry, with what is not done marked.

*Nothing in this folder records an approval, attestation or understanding that Professor Bear did not state.*
