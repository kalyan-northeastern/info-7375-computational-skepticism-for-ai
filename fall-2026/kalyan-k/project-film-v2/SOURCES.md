# SOURCES

## What I used
- Brutalist toolkit — https://github.com/nikbearbrown/brutalist.art (free local pipeline), local copy at `C:\Users\DELL\Downloads\brutalist.art-main\brutalist.art-main`; `show-tell` skill (`skills/make/show-tell/SKILL.md`) and its isometric kit (`templates/iso_kit.py`); downloaded as `brutalist.art-main.zip` on 2026-10-01 (no git history in my copy, so no commit hash)
- The Reallocation Engine — https://github.com/nikbearbrown/the-reallocation-engine
- 80 Days to Stay data (SEC Form D + DOL H-1B), BLS/O*NET compact SOC table, as included in the repo
- USCIS, "H-1B Specialty Occupations" — definition of an H-1B sponsor (BDEFS)
- BLS, Standard Occupational Classification, https://www.bls.gov/soc/ — definition of a SOC code (BDEFS)

## Prior work (v2, Part 2 — Introduction, beat I1)
- USCIS, H-1B Employer Data Hub — https://www.uscis.gov/tools/reports-and-studies/h-1b-employer-data-hub. Queried by fiscal year, employer, city, state, ZIP and NAICS (industry) code; no job-title field.
- MyVisaJobs — https://www.myvisajobs.com/. Search by job title, with wage levels.
- Claude did the initial research on these two tools. I verified both claims myself on the live sites on 2026-11-24. Claude Code also read the USCIS page on 2026-11-24, and it matches. Its read of the MyVisaJobs homepage couldn't confirm the job-title and wage details, so those rest on my check (FACTCHECK.md rows 9–12).
- `the-reallocation-engine/data/80-days-to-stay/README.md`, line 13: the 80 Days to Stay table maps SEC Form D companies against the DOL LCA disclosure data and the USCIS H-1B Employer Data Hub (M1; FACTCHECK.md row 19). So the Data Hub is both prior work and one of my inputs.

## Where every number in the film comes from
- `the-reallocation-engine/logs/runs/2026fa-kalyan-karnati-1.md` — run 1 and run 2, 2026-10-09 (30,369 scanned; 352 shortlisted; 9 with a PM title; 64 keyword-lane sponsors; 12/64 rejected → 52/64; scorer liveness bug; unchecked roles outranking checked ones; Built In Boston stale copies)
- `the-reallocation-engine/course/2026fa/submissions/kalyan-karnati/worked-example.md` — the long form of the same run (PM titles table, filed-under categories, live posting checks)
- `…/kalyan-karnati/run-2026-10-09/healthtech-pm-shortlist.csv` and `role-scores.md` — counted again on 2026-10-20 to check B02, B03 and B04
- FRICTIONAL.md (this folder) — the 8 GB laptop forcing a 1080p render (2026-10-20) and the Claude Code usage limit (2026-10-08), spoken in M4
- Every claim is listed with its verdict in FACTCHECK.md

## What I made
- healthtech-pm-sponsor-triage recipe, card, `pm_title_scan.py`, run logs (2026-10-09)
- PROJECT-BRIEF.md, BEAT-PLAN.md, beat sheet, narration script (my words, narrated in first person as me)
- BEAT-PLAN-v2.md (2026-11-24): the four-part restructure (executive summary, introduction, methods, evaluation), its new narration, and which beats reuse v1 scenes
- Voice: Kokoro preset voice `af_heart` (a synthetic voice, not a recording of me), chosen by me on 2026-10-20

## What I changed in the toolkit
- 2026-10-20 — `runtime/scripts/run.sh`, Manim render loop: the resolution now follows `--height` (`RES="$((HEIGHT * 16 / 9)),$HEIGHT"`, swapped for 9:16) instead of a hard-coded 3840×2160, so `--height 1080` renders Manim scenes at 1920×1080. The default `--height 2160` output is unchanged. Patched by Claude Code with my approval after the 4K render ran out of memory on my 8 GB laptop; logged in the toolkit's `PORT-LOG.md` and in FRICTIONAL.md. Apart from the Gate T exemptions below, no other toolkit file was changed for this film.
- 2026-10-21 — `runtime/scripts/type_check.py` (Gate T): added my four scenes `B00_Repo`, `B02_Nine`, `B08_Scope` and `BOUT_Close` to `KERNING_EXEMPT_PATTERNS`, the checker's existing list of documented false positives for the pixel letter-spacing test. At 1080p that test measured my drawings (box edges, tile grid, fence posts, outro box) instead of text; I checked the frames by eye (`_qc/gateT-exempt-*-50pct.png`). No threshold or other check changed. Patched by Claude Code with my approval; logged in the toolkit's `PORT-LOG.md` and in FRICTIONAL.md.
- 2026-11-24 — `runtime/scripts/type_check.py` (Gate T): added `S1_Box` to `KERNING_EXEMPT_PATTERNS`. S1 is B00's open box redrawn for the v2 four-part cut, and the pixel letter-spacing test measured its box edges, as it did B00's on 2026-10-21. I checked the frame by eye (`_qc/gateT-exempt-S1-50pct.png`); the failing report is `TYPECHECK-v2-before-exemption.md`. No threshold or other check changed. Patched by Claude Code with my approval; logged in the toolkit's `PORT-LOG.md` and in FRICTIONAL.md.
- 2026-11-24 — `runtime/scripts/type_check.py` (Gate T): also added `M4_Desk` to `KERNING_EXEMPT_PATTERNS`. After the M4 redraw below, the pixel letter-spacing test measured the laptop screen's edge instead of text. Checked by eye (`_qc/gateT-exempt-M4-50pct.png`); the failing report is `TYPECHECK-v2-before-exemption-M4.md`. Patched by Claude Code with my approval; logged in PORT-LOG.md and FRICTIONAL.md.
- 2026-11-24 — Not a toolkit change: M4 failed Gate T's label-overlap check because its ink-outlined desk, legs and laptop base fused into one blob around the laptop screen. I re-edged those parts in deep kraft in my `scenes.py` rather than exempting the scene.
- 2026-10-21 — Not a toolkit change: B06's terracotta box tape failed Gate T contrast, so I changed the drawing in my `scenes.py` to a grey strap with one small terracotta seal (the show-tell skill's documented fix) rather than exempting it.
- Earlier toolkit Windows fixes (2026-10-01) are listed in FRICTIONAL.md.

## What Claude contributed
- Claude (claude.ai chat, 2026-10-20): drafted PROJECT-BRIEF.md from my assignment 2 files; I edited and filled the TODOs.
- Claude Code (2026-10-20): fact-checked BEAT-PLAN.md against my run log and run outputs and reworded five lines (see FACTCHECK.md rows 8, 10, 11, 14, 19); split BEAT-PLAN B04 into two beats; wrote FACTCHECK.md, SHOTLIST.md, PROMPTS.md, `make_sheet.py`, `beat_sheet.json` and the Manim drawings in `scenes.py`; ran the Kokoro audio and low-res stills. Applied the same corrections to PROJECT-BRIEF.md §2 and §4 at my request.
- Claude Code (2026-10-20 to 2026-10-21): ran the renders (`art run`, `art final` at 1080p); stopped at each failed gate and proposed fixes that I chose (run.sh patch, Gate V colour fixes, Gate T exemptions, B06 strap); made those edits; checked the master; wrote BUILD-PROMPT.md and README.md and assembled the submission folder at my request.
- Claude (2026-11-24 or before): initial research on the two prior-work tools, the USCIS H-1B Employer Data Hub and MyVisaJobs; I verified both on the live sites on 2026-11-24.
- Claude Code (2026-11-24): restructured `make_sheet.py` and `beat_sheet.json` into the four parts of BEAT-PLAN-v2.md. Fact-checked every new line against my run logs, the worked example, the 80 Days README, FRICTIONAL.md and the USCIS page, and reworded five lines (FACTCHECK.md rows 15, 19, 21, 28, 32). Drew the new and edited scenes (`S1_Box`, `I1_Tools`, `M2_Steps`, `M4_Desk`, `E1_Gauge`, `E3_Log` in `scenes.py`). Voiced those six beats with local Kokoro `af_heart` ($0), checked them with a whisper transcript (`_qc/whisper-v2-new-beats.md`), and rendered low-res stills (`_qc/stills-lowres-v2/`). Rewrote FACTCHECK.md and SHOTLIST.md for v2. The v1 files are kept in `_superseded/v1-before-four-part-2026-11-24/`.
- Claude Code (2026-11-24, round 2, on my answers to its review questions):
  - re-voiced the eight reused beats with their v2 narration;
  - split I1 into I1A and I1B (13.0 s and 13.5 s);
  - changed M4 to "AI usage limits" at my request;
  - reworded B01 so Kokoro says "Form D" and "U S C I S" correctly;
  - removed the 52 / 64 gauge from B08 and retimed it;
  - changed B09's label to "1 year" and retimed it;
  - whisper-checked every changed beat (`_qc/whisper-v2-round2.md`) and re-rendered low-res stills.
  The re-voice overwrote the v1 `mp3/beat-B0x.mp3` files; v1 copies remain as `clips/_work/audio-B0x.wav`.
- Claude Code (2026-11-24, round 3, on my instructions):
  - retimed B01, B03, B04 and B05 and B07 to their v2 narration; B01's out-stack and "352" were dropped because M1 no longer says 352;
  - dropped the Your Turn beat (BHTF) at my request;
  - checked every clip against its audio, re-rendered the changed clips at 1080p and ran `art run` and `art final`;
  - stopped at Gate V (S1) and twice at Gate T (S1 and M4), and applied the fixes and exemptions I chose;
  - wrote APPENDIX.md (its 64-row test-set table is generated from my run-1 shortlist CSV);
  - updated README.md, BUILD-PROMPT.md, BOOKEND-CHECK.md and PROMPTS.md, and assembled the submission folder and zip.
- Claude Code (2026-10-01, earlier session): toolkit Windows fixes (see FRICTIONAL.md).
- Assignment 2: G5/G6 recommendations were made by Claude and reviewed and adopted by me on 2026-10-09 (see run log).

## Third-party assets and licences
Nothing third-party is redistributed in this folder except what the film itself shows and plays.

**Voice**
- Kokoro-82M text-to-speech model and voice pack (`kokoro-v1.0.onnx`, `voices-v1.0.bin`, voice `af_heart`): Apache-2.0. Run locally through `kokoro-onnx` (MIT). The toolkit's README notes that the model is not in the toolkit repo (GitHub's 100 MB file limit); `./setup --install` fetches it once from the kokoro-onnx releases (`model-files-v1.0`, github.com/thewh1teagle/kokoro-onnx).

**Fonts**
- EB Garamond (all labels in the Manim drawings, B00–B10 and BOUT): SIL Open Font License 1.1, Copyright 2017 The EB Garamond Project Authors (github.com/octaviopardo/EBGaramond12). Shipped with the toolkit at `runtime/fonts/EB_Garamond/` with its `OFL.txt`, and loaded by `scenes.py` from there.
- Remotion bookends (BIDEA, BDEFS, BHTF): the toolkit's Claude font stacks fall back to fonts installed with Windows, rendered at build time: Georgia (serif), Segoe UI (interface text), Arial (composer labels) and the system monospace. These are Microsoft fonts used under the Windows licence, and no font files are included. The toolkit also bundles Lato and Montserrat (SIL OFL, licences alongside in `runtime/remotion/public/fonts/`), but these bookends don't load them.

**Software**
- Manim Community v0.18.1: MIT.
- Remotion: Remotion License (free for individuals). It renders the three bookend scenes (hesitant writer, terms card, Your Turn composer).
- ffmpeg: LGPL/GPL, used as a local tool. Not redistributed.
- The Brutalist toolkit: my copy has no LICENSE file. It is used as published, with the two changes listed above.

**Images and music**
- No stock images, no generated images, no music. All pictures are drawn in code.
