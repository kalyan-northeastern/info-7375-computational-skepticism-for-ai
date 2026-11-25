# FACTCHECK — pm-sponsor-check-pitch (v2, four-part cut)

Status: v2 checked 2026-11-24 by Claude Code (round 2 the same day: I1 split into I1A and I1B, M4 and B01 reworded for Kokoro; round 3: BHTF dropped, no claim changed) against the files and pages named below; to be signed off by Kalyan Venkata Swamy Karnati before any render. v1 (2026-10-20) is kept at `_superseded/v1-before-four-part-2026-11-24/FACTCHECK.md`; rows marked "v1 #n" carry its verdict forward because the claim is unchanged.

Sources:
- Run log = `the-reallocation-engine/logs/runs/2026fa-kalyan-karnati-1.md` (run 1 and run 2, 2026-10-09).
- Worked example = `the-reallocation-engine/course/2026fa/submissions/kalyan-karnati/worked-example.md`.
- 80 Days README = `the-reallocation-engine/data/80-days-to-stay/README.md` (line 13: what the table is joined from).
- FRICTIONAL.md (this folder): the 8 GB / 1080p render and the Claude usage limit.
- USCIS, H-1B Employer Data Hub, https://www.uscis.gov/tools/reports-and-studies/h-1b-employer-data-hub — verified by Kalyan on 2026-11-24; Claude Code also read the page on 2026-11-24 ("Data can be queried by fiscal year, employer name, city, state, zip code, and NAICS code"; no job title, SOC code or wage field).
- MyVisaJobs, https://www.myvisajobs.com/ — verified by Kalyan on 2026-11-24. Claude Code's read of the homepage on 2026-11-24 could neither confirm nor rule out the job-title search and wage levels, so those two rows rest on Kalyan's check.

Beat ids are the beat-sheet ids. A reused scene keeps its v1 id, and the BEAT-PLAN-v2 label is in brackets.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | Narrator is Kalyan Karnati; this is the final-project pitch | EXEMPT | your-input (assignment); unchanged from v1 #1 | — |
| 2 | BDEFS | An H-1B sponsor is an employer that files work-visa petitions | PASS | v1 #2: USCIS, "H-1B Specialty Occupations" | — |
| 3 | BDEFS | A SOC code is the government's job category for a role | PASS | v1 #3: BLS SOC | — |
| 4 | BDEFS | A liveness check asks whether a job posting is still open | PASS | v1 #4 | — |
| 5 | S1 | PM Sponsor Check will tell an early-career PM which health-tech employers have public evidence of sponsoring PMs, and label every answer as a record or a guess | EXEMPT | plan (PROJECT-BRIEF §1); parts labelled "constructed" on screen | — |
| 6 | B02 [S2] | The usual check misleads | EXEMPT | argument, backed by row 7 | — |
| 7 | B02 [S2] | On my first run, only 9 of 352 possible health sponsors listed a PM title among their top sponsored roles | PASS | run log run 1 Result: 6 (form-d-health) + 3 (keyword-health) = 9; v1 #8 and #9 | — |
| 8 | B02 [S2] | None of those titles was entry level | PASS | worked example line 60; v1 #10 | — |
| 9 | I1A | The government's H-1B Employer Data Hub counts petitions by company, industry and year, but not by job title | PASS | USCIS page (read 2026-11-24): queries by fiscal year, employer, city, state, ZIP, NAICS (industry) code; data on first decisions on petitions; no job-title field. Verified by Kalyan 2026-11-24 | — |
| 10 | I1A | So it can't tell me who sponsors product managers | PASS | follows from row 9 | — |
| 11 | I1B | MyVisaJobs lets me search by job title and see wage levels | PASS | verified by Kalyan on myvisajobs.com, 2026-11-24 (Claude's homepage read inconclusive; see Sources) | — |
| 12 | I1B | Neither tool checks whether a posting is still open, or labels which answers are records and which are guesses | PASS | verified by Kalyan on both sites, 2026-11-24; the USCIS page lists no posting or labelling feature | — |
| 13 | I1B | That's what mine adds | EXEMPT | plan (Brief §2) | — |
| 14 | B04 [I2] | The Reallocation Engine rates each company's sponsorship as one tier, like "Likely," for the whole company, not for a role | PASS | run-2026-10-09/role-scores.md: one sponsorship p and tier per company; v1 #14 | — |
| 15 | B05 [I3] | On my second run, Built In Boston still listed copies of Cohere Health roles marked removed, while the live role sat on Cohere's own board | CORRECTED | run log run 2 Open issues ("Built In Boston copies of Cohere roles stale"); worked example line 108 ("Sorry, this job was removed"); live role Greenhouse job 7532618003 | BEAT-PLAN-v2 said "aggregator copies were still listed after the company's own board had closed them". The log does not say Cohere closed those roles, only that the copies were marked removed while a live role was on Cohere's board, and it is one board, not job boards in general. Named Built In Boston and Cohere, and kept to what was logged |
| 16 | B03 [I4] | Filtering by health industry would have dropped 64 sponsors filed under technology and other categories | PASS | run log run 1 Result: keyword-health 64; worked example: Other Technology 38, Other 25, Computers 1; v1 #11 | — |
| 17 | B03 [I4] | That's why mine is worth building: it checks the role, not just the company | EXEMPT | argument / plan | — |
| 18 | B01 [M1] | The data is public | PASS | 80 Days README line 13 (SEC, DOL and USCIS public datasets) | — |
| 19 | B01 [M1] | The 80 Days to Stay table joins SEC Form D filings, which report funding, with H-1B records from the Labor Department and USCIS ("U S C I S" in the narration) | CORRECTED | 80 Days README line 13: "mapped our SEC startup list against ... the DOL LCA Disclosure Data ... and the USCIS H-1B Employer Data Hub"; CSV header has Total Approvals / Total Denials (USCIS) and top_job_titles_sponsored / median_salary_offered (DOL) | BEAT-PLAN-v2 said "with Labor Department H-1B records" only. The approval counts come from USCIS, so added USCIS. Round 2: Kokoro voiced "Form D funding" as "formed defunding" and USCIS as one word, so reworded to "Form D filings, which report funding" and spelled "U S C I S" (whisper-checked clean) |
| 20 | B01 [M1] | About thirty thousand companies (30,369 on screen) | PASS | run log Inputs: "80 Days CSV (30,369 rows scanned)"; v1 #7 | — |
| 21 | M2 | Step one, the health industry category and a keyword filter find possible health companies | CORRECTED | run log run 1 Result: two lanes, form-d-health (288 of 352) and keyword-health (64 of 352) | BEAT-PLAN-v2 said "a keyword filter finds possible health companies". The keyword lane found only 64 of the 352; the other 288 came from the Form D health industry category. Named both |
| 22 | M2 | Step two, a scan reads each company's sponsored job titles for product roles | PASS | run log Commands: `pm_title_scan.py`; Result: PM titles listed 6 + 3 | — |
| 23 | M2 | Step three, a liveness check confirms the posting is still open before anything gets an Apply | EXEMPT | plan: run log run 1 "G4 liveness NOT run" (`ats:liveness` blocked), run 2 proposed rule "no Apply without liveness". Gate 3 is labelled "constructed" on screen | — |
| 24 | B09 [M3] | The full Labor Department filing data is the only way to confirm PM sponsorship beyond a top-titles list | PASS | Brief §6; worked example line 178; v1 #22 | — |
| 25 | B09 [M3] | It's large and messy; I'll start with one fiscal year, the most recent complete one, and say so in the log | EXEMPT | plan. Changed from v1 #23: Massachusetts-only dropped and "complete" added (Kalyan's v2 plan). The reused scene still shows "1 year · MA" (see SHOTLIST) | — |
| 26 | M4 | What I have: the public data, the scripts, and a free local pipeline | PASS | run log (scripts); this film: Kokoro, Manim, Remotion, $0 (PROMPTS.md) | — |
| 27 | M4 | An 8 GB laptop already forced me to render this film at 1080p | PASS | FRICTIONAL.md 2026-10-20: ffmpeg ran out of memory "on my 8 GB laptop" at 4K; switched to 1080p | — |
| 28 | M4 | AI usage limits, which I hit once while I was setting up the engine | CORRECTED | FRICTIONAL.md 2026-10-08: "Reallocation Engine on Windows ... Hit my Claude Code usage limit mid-task" | BEAT-PLAN-v2 said "ran out once mid-build". The only logged limit was on 2026-10-08, while setting up the Reallocation Engine, not while building this film. Reworded to say where it happened. Round 2, Kalyan's change: "limited Claude usage" became "AI usage limits" (Kokoro voiced "Claude" as "clawed"); the limit was a Claude Code usage limit, which is an AI usage limit |
| 29 | B08 [M5] | It will not say which job code an employer will file, nor give immigration advice | EXEMPT | scope (Brief §5); v1 #20 | — |
| 30 | E1 | I hand-checked 64 keyword matches; today the filter gets 52 right, 81 percent (52 of 64 on screen) | PASS | run log run 1 Result: "Keyword review: 12/64 rejected (not health)" → 52/64 = 81.25%; v1 #21 | — |
| 31 | E1 | It works if the tightened filter beats that on the same 64, measured by one logged command; target at least 58 of 64 | EXEMPT | plan; target mark labelled "constructed". For context: worked example line 188 says the tightened regex would have removed 11 of the 12 false matches (63/64 if it keeps every true match) | — |
| 32 | B07 [E2] | On my first run the scorer marked unchecked postings as checked | CORRECTED | run log run 1 Open issues: "role-scorer defaults missing liveness to `1 [record]`"; v1 #18 | BEAT-PLAN-v2 said "treated unchecked postings as checked"; kept v1's wording ("marked ... as checked"), which is what the log shows |
| 33 | B07 [E2] | It works if no unchecked posting ever ranks above a checked one, and the log proves it | EXEMPT | plan; the failure it targets is run log run 2 ("unchecked roles outrank checked ones") | — |
| 34 | E3 | It didn't work if any Apply goes out without a liveness check, or if a company is called a PM sponsor without a filing record; either counts as a logged failure | EXEMPT | plan (failure criteria) | — |
| 36 | BOUT | PM Sponsor Check, by Kalyan Karnati | EXEMPT | working title; unchanged from v1 #27 | — |

Dropped from the film in v2 (claims no longer spoken): v1 B00 (row 5), B06 (row 17), B10 (rows 24–25), and BHTF, the Your Turn beat (v1 row 26), which Kalyan dropped on 2026-11-24 because it is not one of the four parts.
