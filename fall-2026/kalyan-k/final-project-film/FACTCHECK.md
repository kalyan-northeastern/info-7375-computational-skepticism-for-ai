# FACTCHECK — pm-sponsor-check-pitch

Status: checked 2026-10-20 by Claude Code against the files named below; to be signed off by Kalyan Venkata Swamy Karnati before the 4K render.

Run log = `the-reallocation-engine/logs/runs/2026fa-kalyan-karnati-1.md`.
Worked example = `the-reallocation-engine/course/2026fa/submissions/kalyan-karnati/worked-example.md` (the long form of the same run).
Shortlist = `…/kalyan-karnati/run-2026-10-09/healthtech-pm-shortlist.csv` (352 rows; counted 2026-10-20).
Brief = `final-project-film/PROJECT-BRIEF.md`.

Beat ids follow the beat sheet. BEAT-PLAN's B04 was split into B04 (engine scorer) and B05 (Built In Boston) because it held two comparisons, so BEAT-PLAN B05–B09 are B06–B10 here.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | Narrator is Kalyan Karnati; this is the final-project pitch | EXEMPT | your-input (assignment) | — |
| 2 | BDEFS | An H-1B sponsor is an employer that files work-visa petitions | PASS | USCIS, "H-1B Specialty Occupations" (employer files Form I-129 for the worker) | — |
| 3 | BDEFS | A SOC code is the government's job category for a role | PASS | BLS, Standard Occupational Classification (bls.gov/soc); run log uses SOC 13-1111 | — |
| 4 | BDEFS | A liveness check asks whether a job posting is still open | PASS | engine `npm run ats:liveness`; worked example Step 6 | — |
| 5 | B00 | What I will build: recipe, scan script, labelled test set, evaluation log, added to the Reallocation Engine | EXEMPT | plan, not a fact (Brief §1); parts labelled "constructed" on screen | — |
| 6 | B01 | On October ninth, I ran a first version on the repository's data | PASS | run log, run 1, dated 2026-10-09; `pm_title_scan.py` prototype | — |
| 7 | B01 | Over thirty thousand companies went in (30,369 on screen) | PASS | run log Inputs: "80 Days CSV (30,369 rows scanned)"; stderr "companies scanned: 30369" | — |
| 8 | B01 | 352 came out | CORRECTED | run log Outputs: shortlist 352 rows | "352 health-related sponsors" → "352 possible health sponsors": 12 of the 64 keyword-lane rows were later rejected as not health (run log), so not all 352 are health companies |
| 9 | B02 | Only 9 of 352 listed a product-manager title among their top sponsored job titles | PASS | run log Result: PM title listed 6 (form-d-health) + 3 (keyword-health) = 9; shortlist `pm_evidence = pm-title-listed` count = 9 | "among the jobs they sponsored" → "among their top sponsored job titles": the data stores a truncated top-titles list (216/352 have one title), so absence is not proof |
| 10 | B02 | None of those titles was entry level | CORRECTED | worked example Step 2 table (titles: Director, Senior, Specialist III, Technical PM, Product Owner, plain "Product Manager") | BEAT-PLAN said "all nine were senior roles"; Nimble Rx "Product Manager", CipherHealth "Technical Product Manager" and Castle Biosciences "IT, Product Owner" are not senior-titled. Reworded to "none of those titles was entry level" |
| 11 | B03 | A health-category filter would have missed 64 sponsors filed under technology or other categories | CORRECTED | run log Result: keyword-health with H-1B record 64; shortlist keyword-lane `industry_form_d`: Other Technology 38, Other 25, Computers 1 | BEAT-PLAN said "filed under technology"; 25 of 64 filed under "Other". Reworded to "technology and other categories" |
| 12 | B03 | including digital-health companies I would actually apply to | PASS | worked example Step 3: Cohere Health, Hinge Health, Flatiron, Included, Maven, Lyra, K Health, Ambience, all "Other Technology" or "Other" | — |
| 13 | B04 | On October ninth I compared it with the engine's own sponsorship scorer | PASS | run log commands: `node scripts/score/role-scorer.mjs …`, 2026-10-09 | — |
| 14 | B04 | The scorer rated each company's sponsorship as one tier, and never asked whether it sponsored product managers | CORRECTED | run-2026-10-09/role-scores.md: sponsorship is one p-value per company with a tier ("Likely"); no PM term in the audit trace; Brief §2 | BEAT-PLAN said it "showed each company's sponsorship total"; the scorer prints a tier/probability, not a total. Reworded |
| 15 | B05 | Built In Boston still showed copies of Cohere Health roles marked removed, while the live role was on Cohere's own board | PASS | run log run 2 Open issues: "Built In Boston copies of Cohere roles stale"; worked example Step 6: copies "marked 'Sorry, this job was removed'"; live role on Greenhouse job 7532618003, checked 2026-10-09 | wording tightened from "listed roles that had already been removed" |
| 16 | B04, B05 | Mine will show PM evidence separately and check each posting on the company's own board | EXEMPT | plan (Brief §2, "What mine does") | — |
| 17 | B06 | Reader: a hiring manager for a product role; first minute: the card, then one run log | EXEMPT | plan (Brief §3) | — |
| 18 | B07 | The scorer marked postings nobody had checked as checked | PASS | run log run 1 Open issues: "role-scorer defaults missing liveness to `1 [record]`"; role-scores.md rows print `liveness 1[record]` with "posting not verified" | "treated as checked" → "marked as checked" |
| 19 | B07 | Even after the labels were fixed, the two roles I couldn't check ranked above the ones I had | CORRECTED | run log run 2: Sirona, Nimble Rx not checked → Apply 0.446; Cohere checked → Consider 0.255; Hinge checked → Skip; Open issues: "unchecked roles outrank checked ones" | BEAT-PLAN folded run 1 (mislabel) and run 2 (ranking) into one sentence; split into the two facts in order |
| 20 | B08 | It will not say which job code an employer will file, nor give immigration advice | EXEMPT | scope statement (Brief §5) | — |
| 21 | B08 | Tested against the 64 matches reviewed with evidence; today's filter gets 52 right (52 / 64 on screen) | PASS | run log Result: "Keyword review: 12/64 rejected (not health)" → 52/64 = 81%; worked example Step 4 lists all 12 | after-state gauge is empty and labelled "constructed" |
| 22 | B09 | The full government filing data (DOL LCA) is the only way to confirm PM sponsorship; it is large and its job titles are inconsistent | PASS | Brief §6; worked example "What the mode missed": "only the raw DOL LCA file can say" | — |
| 23 | B09 | Fallback: most recent fiscal year published, Massachusetts employers only, noted in the log | EXEMPT | plan (Brief §6); slice labelled "constructed" | — |
| 24 | B10 | PM internship at Andor Health | EXEMPT | your-input (Brief §7: January–August 2026); no internal Andor Health work is shown | — |
| 25 | B10 | The health-tech recipe I submitted on October ninth | PASS | run log: recipe `kalyan-karnati-healthtech-pm-sponsor-triage.md` v0.1.0, run 2026-10-09 | — |
| 26 | BHTF | The Your Turn prompt and its two checks | EXEMPT | instruction to the viewer, not a claim | — |
| 27 | BOUT | PM Sponsor Check, by Kalyan Karnati | EXEMPT | working title (Brief) | — |
