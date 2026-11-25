# BEAT-PLAN v2 — PM Sponsor Check, four-part structure

Restructures the existing film into Professor Bear's four parts, in order:
1 Executive summary · 2 Introduction (prior work) · 3 Methods · 4 Evaluation.
Reuses existing scenes wherever possible (marked REUSE) so only a few beats need new drawings and audio (NEW / EDIT).
Narrator: Kalyan Karnati. Numbers come from my run logs (2026-10-09 runs 1 and 2) and match FACTCHECK.md.
Prior-work facts in I1 verified by me against both sites; initial research by Claude.

## Part 1 — Executive summary (what and why; no "how")

| Beat | Status | Picture | Narration |
|---|---|---|---|
| BIDEA | REUSE | Writer corrects "sponsor visas" to "sponsor product managers" | (unchanged greeting and corrected question) |
| BDEFS | REUSE | Terms: H-1B sponsor · SOC code · liveness check | (unchanged) |
| S1 | EDIT of B00 | The box arrives; its parts drop in (constructed) | I'm building PM Sponsor Check: a tool that tells an early-career product manager which health-tech employers have public evidence of sponsoring product managers, not just engineers, and labels every answer as a record or a guess. |
| S2 | REUSE B02 | 9 of 352 | It matters because the usual check misleads. On my first run, only nine of three hundred fifty-two possible health sponsors listed a product manager title among their top sponsored roles, and none of those titles was entry level. |

## Part 2 — Introduction (what others have done)

| Beat | Status | Picture | Narration |
|---|---|---|---|
| I1 | NEW | Two windows side by side, labelled "Data Hub" and "MyVisaJobs"; a third, mine, labelled "constructed" | Two public tools already exist. The government's H-1B Employer Data Hub counts petitions by company, industry and year, but not by job title, so it can't tell me who sponsors product managers. MyVisaJobs goes further: I can search by job title and see wage levels. What neither does is check whether a posting is still open, or label which answers are records and which are guesses. That's what mine adds. |
| I2 | REUSE B04 | Engine scorer vs mine (constructed) | The Reallocation Engine I'm building on rates each company's sponsorship as one tier, like "Likely," for the whole company, not for a role. |
| I3 | REUSE B05 | Built In vs company board | Job boards repeat stale postings: on my second run, aggregator copies were still listed after the company's own board had closed them. |
| I4 | REUSE B03 | Health filter drops 64 | And filtering by health industry would have quietly dropped sixty-four sponsors filed under technology and other categories. That's why mine is worth building: it checks the role, not just the company. |

## Part 3 — Methods (how, step by step)

| Beat | Status | Picture | Narration |
|---|---|---|---|
| M1 | REUSE B01 | 30,369 boxes through a gate, 352 out | The data is public. I start from the repository's 80 Days to Stay table, which joins SEC Form D funding filings with Labor Department H-1B records for about thirty thousand companies. |
| M2 | NEW | Three steps on one conveyor: filter · title scan · liveness check | Step one, a keyword filter finds possible health companies. Step two, a scan reads each one's sponsored job titles for product roles. Step three, a liveness check confirms the posting is still open before anything gets an Apply. |
| M3 | REUSE B09 (was B08) | Big filing stack; a labelled slice cut off (constructed) | Step four will add the full Labor Department filing data, the only way to confirm product-manager sponsorship beyond a top-titles list. It's large and messy, so I'll start with one fiscal year, the most recent complete one, and say so in the log. |
| M4 | NEW | A small desk: laptop, one key, one gauge | What I have: the public data, the scripts, and a free local pipeline. What's tight: an eight-gigabyte laptop, which already forced me to render this film at ten-eighty p, and limited Claude usage, which ran out once mid-build. |
| M5 | REUSE B08 (was B07) | Fence: out items; first box moves forward | It will not say which job code an employer will file, and it will not give immigration advice. |

## Part 4 — Evaluation (how I'll know it worked)

| Beat | Status | Picture | Narration |
|---|---|---|---|
| E1 | EDIT of B08 gauge | Gauge 52 of 64 → target mark (constructed) | First, precision. I hand-checked sixty-four keyword matches; today the filter gets fifty-two right, eighty-one percent. It works if the tightened filter beats that on the same sixty-four, measured by one logged command. My target is at least fifty-eight of sixty-four. |
| E2 | REUSE B07 (was B06) | Unchecked vs checked cards; order flips | Second, honesty of the ranking. On my first run the scorer treated unchecked postings as checked. It works if no unchecked posting ever ranks above a checked one, and the log proves it. |
| E3 | NEW | A run log page with a pass mark and a fail mark | It didn't work if any Apply goes out without a liveness check, or if a company is called a PM sponsor without a filing record behind it. Either one counts as a failure, logged, not hidden. |
| BHTF | REUSE | Your Turn composer (constructed) | (unchanged) |
| BOUT | REUSE | PM Sponsor Check · Kalyan Karnati | (unchanged) |

Dropped from v1: B10 "why this project" (not one of the four parts; move it to the appendix if wanted).

## Appendix (written, not in the film)
APPENDIX.md holds the detail: exact data paths and commands, the 64-row test set, run logs, the scorer bug, the LCA plan, and the resource constraints.
