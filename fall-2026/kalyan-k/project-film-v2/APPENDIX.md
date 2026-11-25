# APPENDIX — PM Sponsor Check (written, not in the film)

The detail behind the four-part film. All paths are relative to my fork of the Reallocation Engine (`the-reallocation-engine/`). Every number here comes from the 2026-10-09 run log, `logs/runs/2026fa-kalyan-karnati-1.md`, and the run outputs next to it.

## A1. Data and paths

| What | Path |
|---|---|
| 80 Days to Stay table (SEC Form D companies mapped to DOL LCA and USCIS H-1B Employer Data Hub records) | `data/80-days-to-stay/80-days-csv/mapped_student_employment_targets_v3.csv` |
| BLS / O*NET compact SOC table (1,016 rows) | `data/bls/compact/soc_occupation_compact.csv` |
| Recipe (v0.1.0, DRAFT) | `recipes/cases/2026fa/kalyan-karnati-healthtech-pm-sponsor-triage.md` |
| Scan script | `scripts/contrib/2026fa/kalyan-karnati-pm-title-sponsor-scan/pm_title_scan.py` |
| Run 1 outputs | `course/2026fa/submissions/kalyan-karnati/run-2026-10-09/` (shortlist CSV, 352 rows; `pm-soc-candidates.csv`, 7 rows; `roles.json`; `role-scores.json` / `.md`; `stderr.txt`) |
| Run 2 outputs (live posting checks) | `course/2026fa/submissions/kalyan-karnati/run-2026-10-09-live/` |
| Run log | `logs/runs/2026fa-kalyan-karnati-1.md` |
| Worked example (long form of the same run) | `course/2026fa/submissions/kalyan-karnati/worked-example.md` |

## A2. Commands (run 1 and run 2, 2026-10-09)

```bash
python3 scripts/contrib/2026fa/kalyan-karnati-pm-title-sponsor-scan/pm_title_scan.py --run-date 2026-10-09 --max-funding-age-days 730 --out-dir course/2026fa/submissions/kalyan-karnati/run-2026-10-09
node scripts/score/role-scorer.mjs <run-dir>/roles.json --out-dir <run-dir> --md <run-dir>/role-scores.md
npm run ats:liveness      # blocked on this run (no Playwright / network)
npm run bls:local-wage    # blocked on this run (data/bls/local-wage absent)
```

Run 2 used the same `role-scorer.mjs` command with run-dir `course/2026fa/submissions/kalyan-karnati/run-2026-10-09-live`, after manual web checks of the postings.

What run 1 printed (`stderr.txt`):

```
companies scanned: 30369
form-d-health: in-lane 4745 | with H-1B record 288 | PM title listed 6
keyword-health: in-lane 1139 | with H-1B record 64 | PM title listed 3
shortlist rows (H-1B record, either lane): 352
rows whose top-titles list has exactly 1 title: 216/352
```

## A3. The 64-row test set (precision, Evaluation E1)

These are the 64 keyword-lane companies with an H-1B record from run 1. Each was hand-checked against the company's own website domain and its sponsored-title list in the 80 Days data (worked example, Step 4).
- **Labels:** 52 health, 12 not health. Today's keyword filter gets **52 of 64 right (81%)**; ten of the twelve errors are "med" matching "media".
- **The test:** the tightened filter must beat 52 on these same 64 rows, measured by one logged command. My target is at least 58 of 64.
- **What to expect:** the worked example's proposed regex, `\bmed(ical)?\b|health|clinic|patient|thera|pharm`, would have removed 11 of the 12 false matches. That would score 63/64 if it keeps every true match, so 58 is a deliberately conservative target.

| # | Company (as in the 80 Days data) | Form D industry | H-1B approvals | Label | Note |
|---|---|---|---|---|---|
| 1 | 1UPHEALTH INC | Other Technology | 12 | health |  |
| 2 | AKOYA BIOSCIENCES INC | Other | 26 | health | PM title listed: Sr. Product Manager, PhenoCycler Instruments |
| 3 | AMBIENCE HEALTHCARE INC | Other Technology | 6 | health |  |
| 4 | AURIS HEALTH INC | Other Technology | 276 | health |  |
| 5 | AVAIL MEDSYSTEMS INC | Other | 8 | health |  |
| 6 | BIOME ANALYTICS INC | Computers | 2 | health |  |
| 7 | BORDERX LAB INC | Other Technology | 2 | not health | "rx"; cross-border e-commerce |
| 8 | CAPITAL RX INC | Other | 6 | health |  |
| 9 | CAPTION HEALTH INC | Other | 10 | health |  |
| 10 | CAREDOX INC | Other Technology | 44 | health |  |
| 11 | CHARMED AI INC | Other Technology | 2 | not health | "med" in "charmed"; AI tools for game development |
| 12 | CIPHERHEALTH INC | Other Technology | 10 | health | PM title listed: Technical Product Manager |
| 13 | COHERE HEALTH INC | Other Technology | 104 | health |  |
| 14 | COMPASS THERAPEUTICS INC | Other | 6 | health |  |
| 15 | ECLINICAL SOLUTIONS LLC | Other Technology | 40 | health |  |
| 16 | EVERYDAY HEALTH INC | Other Technology | 4 | health |  |
| 17 | FLATIRON HEALTH INC | Other Technology | 98 | health |  |
| 18 | GAMECHANGER MEDIA INC | Other Technology | 18 | not health | "med" in "media"; youth-sports app |
| 19 | GINKGO BIOWORKS INC | Other | 122 | health |  |
| 20 | HEALTHEDGE SOFTWARE INC | Other Technology | 156 | health |  |
| 21 | HINGE HEALTH INC | Other Technology | 84 | health |  |
| 22 | IDEAYA BIOSCIENCES INC | Other | 18 | health |  |
| 23 | INCLUDED HEALTH INC | Other Technology | 46 | health |  |
| 24 | INFORMED INC | Other Technology | 28 | not health | "med" in "informed"; automotive |
| 25 | INMARKET MEDIA LLC | Other | 46 | not health | "med" in "media"; ad tech |
| 26 | INTELYCARE INC | Other | 6 | health |  |
| 27 | IOTA BIOSCIENCES INC | Other Technology | 48 | health |  |
| 28 | JAWBONE HEALTH HUB INC | Other | 6 | health |  |
| 29 | K HEALTH INC | Other Technology | 10 | health |  |
| 30 | KONEKSA HEALTH INC | Other Technology | 4 | health |  |
| 31 | LEVELS HEALTH INC | Other Technology | 4 | health |  |
| 32 | LEVITASBIO INC | Other Technology | 8 | health |  |
| 33 | LOOP MEDIA INC | Other | 6 | not health | "med" in "media"; streaming |
| 34 | LYRA HEALTH INC | Other | 24 | health |  |
| 35 | MAVEN CLINIC CO | Other | 32 | health |  |
| 36 | MEDALLIA INC | Other Technology | 116 | not health | "med" in name; customer-experience software |
| 37 | MEDIAMATH INC | Other | 12 | not health | "med" in "media"; ad tech |
| 38 | MEETCAREGIVERS INC | Other | 2 | health |  |
| 39 | MENDEL HEALTH INC | Other Technology | 22 | health |  |
| 40 | MERIDIAN BIOTECH LLC | Other Technology | 2 | health |  |
| 41 | MORE HEALTH INC | Other Technology | 14 | health |  |
| 42 | NANTHEALTH INC | Other Technology | 26 | health |  |
| 43 | NIMBLE RX INC | Other | 14 | health | PM title listed: Product Manager |
| 44 | NURIX THERAPEUTICS INC | Other | 42 | health |  |
| 45 | ODK MEDIA INC | Other Technology | 12 | not health | "med" in "media"; streaming |
| 46 | OPEN ROAD INTEGRATED MEDIA INC | Other | 14 | not health | "med" in "media"; publisher |
| 47 | PACIFIC BIOSCIENCES OF CALIFORNIA INC | Other Technology | 32 | health |  |
| 48 | PARTICLE MEDIA INC | Other Technology | 32 | not health | "med" in "media"; news app |
| 49 | PATIENTFI LLC | Other Technology | 4 | health |  |
| 50 | PIVOT BIO INC | Other Technology | 10 | health |  |
| 51 | PIXELOGIC MEDIA PARTNERS LLC | Other | 4 | not health | "med" in "media"; media localization |
| 52 | PRELLIS BIOLOGICS INC | Other Technology | 2 | health |  |
| 53 | PROBIOTIC LABS INC | Other | 2 | health |  |
| 54 | Q BIO INC | Other Technology | 6 | health |  |
| 55 | QUARTET HEALTH INC | Other Technology | 2 | health |  |
| 56 | RIBBON HEALTH INC | Other Technology | 4 | health |  |
| 57 | SLINGSHOT BIOSCIENCES INC | Other | 8 | health |  |
| 58 | SMITH HEALTH INC | Other | 42 | health |  |
| 59 | TWIN HEALTH INC | Other Technology | 40 | health |  |
| 60 | TWINE HEALTH INC | Other Technology | 40 | health |  |
| 61 | VIDEAHEALTH INC | Other | 14 | health |  |
| 62 | VOR BIOPHARMA INC | Other | 22 | health |  |
| 63 | WALTZ HEALTH INC | Other | 10 | health |  |
| 64 | ZAKIPOINT HEALTH INC | Other Technology | 14 | health |  |

## A4. Run logs, in short

- **Run 1 (2026-10-09):**
  - 30,369 companies scanned, 352 shortlisted (288 from the Form D health category, 64 from the keyword lane).
  - 9 list a PM title among their top sponsored titles (6 + 3), and none of those titles is entry level.
  - Scorer: Apply 2 · Consider 2 · Skip 0, all TENTATIVE.
  - G4 liveness was not run.
- **Run 2 (2026-10-09, live posting checks):**
  - Cohere Health's PM role was live (Greenhouse job 7532618003; 3+ years; posted pay from $101,000) and scored Consider 0.255.
  - Hinge Health's Associate PM role was closed, so it was Skip.
  - Sirona and Nimble Rx had no posting identified and their liveness wasn't checked, yet they scored Apply 0.446.
  - Built In Boston still showed copies of Cohere roles marked "Sorry, this job was removed".
  - G5 and G6 were recommended by Claude, then reviewed and adopted by me.

## A5. The scorer bug (Evaluation E2)

1. **Run 1:** `role-scorer.mjs` defaults a missing liveness value to `1 [record]`, so postings nobody had checked were marked as checked. Sponsorship p was also mislabelled `record` in `roles.json`; it should be `your-input`.
2. **Run 2:** I corrected the labels (sponsorship p = `your-input`, liveness explicit on every role). Even so, the two roles I couldn't check (Sirona, Nimble Rx, Apply 0.446) still ranked above the checked ones (Cohere, Consider 0.255; Hinge, Skip).
3. **Proposed rule:** no Apply without a liveness check.
4. **Pass condition:** no unchecked posting ever ranks above a checked one, and the log shows it.

## A6. Failure conditions (Evaluation E3)

It didn't work, logged rather than hidden, if either of these happens:

1. any Apply goes out without a liveness check;
2. a company is called a PM sponsor without a filing record behind it.

## A7. The LCA plan (Methods M3)

The 80 Days table keeps only a truncated top-titles list per company: 216 of the 352 shortlisted companies have exactly one title, so a missing PM title is not proof of no PM sponsorship. The full DOL LCA disclosure data is the only way to confirm product-manager sponsorship. It is large and its job titles are inconsistent, so step four starts with one fiscal year, the most recent complete one, and the log will say so. (The v1 plan also limited it to Massachusetts employers; v2 drops that.)

## A8. Resource constraints (Methods M4)

- **Have:** the public data above, the scripts, and a free local pipeline (Kokoro, Manim, Remotion, ffmpeg; no paid service).
- **Tight:**
  - an 8 GB laptop: the 4K render ran out of memory on 2026-10-20 (ffmpeg on the first scene), so this film is rendered at 1080p (FRICTIONAL.md);
  - the C: drive also filled during that render;
  - AI usage limits: I hit my Claude Code usage limit once, on 2026-10-08, while setting up the Reallocation Engine (FRICTIONAL.md).

## A9. Prior work (Introduction I1A, I1B)

- **USCIS H-1B Employer Data Hub** (https://www.uscis.gov/tools/reports-and-studies/h-1b-employer-data-hub): queried by fiscal year, employer, city, state, ZIP and NAICS industry code; no job title.
- **MyVisaJobs** (https://www.myvisajobs.com/): search by job title, with wage levels.
- **What neither does:** check whether a posting is still open, or label which answers are records and which are guesses.

Claude did the initial research on both tools; I verified them on the live sites on 2026-11-24.
