# SOURCES

## What I used
- Brutalist toolkit — https://github.com/nikbearbrown/brutalist.art (free local pipeline), local copy at `<Downloads>\brutalist.art-main\brutalist.art-main`; `show-tell` skill (`skills/make/show-tell/SKILL.md`) and its isometric kit (`templates/iso_kit.py`); downloaded as `brutalist.art-main.zip` on 2026-10-01 (no git history in my copy, so no commit hash)
- The Reallocation Engine — https://github.com/nikbearbrown/the-reallocation-engine
- 80 Days to Stay data (SEC Form D + DOL H-1B), BLS/O*NET compact SOC table, as included in the repo
- USCIS, "H-1B Specialty Occupations" — definition of an H-1B sponsor (BDEFS)
- BLS, Standard Occupational Classification, https://www.bls.gov/soc/ — definition of a SOC code (BDEFS)

## Where every number in the film comes from
- `the-reallocation-engine/logs/runs/2026fa-kalyan-karnati-1.md` — run 1 and run 2, 2026-10-09 (30,369 scanned; 352 shortlisted; 9 with a PM title; 64 keyword-lane sponsors; 12/64 rejected → 52/64; scorer liveness bug; unchecked roles outranking checked ones; Built In Boston stale copies)
- `the-reallocation-engine/course/2026fa/submissions/kalyan-karnati/worked-example.md` — the long form of the same run (PM titles table, filed-under categories, live posting checks)
- `…/kalyan-karnati/run-2026-10-09/healthtech-pm-shortlist.csv` and `role-scores.md` — counted again on 2026-10-20 to check B02, B03 and B04
- Every claim is listed with its verdict in FACTCHECK.md

## What I made
- healthtech-pm-sponsor-triage recipe, card, `pm_title_scan.py`, run logs (2026-10-09)
- PROJECT-BRIEF.md, BEAT-PLAN.md, beat sheet, narration script (my words, narrated in first person as me)
- Voice: Kokoro preset voice `af_heart` (a synthetic voice, not a recording of me), chosen by me on 2026-10-20

## What I changed in the toolkit
- 2026-10-20 — `runtime/scripts/run.sh`, Manim render loop: the resolution now follows `--height` (`RES="$((HEIGHT * 16 / 9)),$HEIGHT"`, swapped for 9:16) instead of a hard-coded 3840×2160, so `--height 1080` renders Manim scenes at 1920×1080. The default `--height 2160` output is unchanged. Patched by Claude Code with my approval after the 4K render ran out of memory on my 8 GB laptop; logged in the toolkit's `PORT-LOG.md` and in FRICTIONAL.md. Apart from the Gate T exemption below, no other toolkit file was changed for this film.
- 2026-10-21 — `runtime/scripts/type_check.py` (Gate T): added my four scenes `B00_Repo`, `B02_Nine`, `B08_Scope` and `BOUT_Close` to `KERNING_EXEMPT_PATTERNS`, the checker's existing list of documented false positives for the pixel letter-spacing test. At 1080p that test measured my drawings (box edges, tile grid, fence posts, outro box) instead of text; I checked the frames by eye (`_qc/gateT-exempt-*-50pct.png`). No threshold or other check changed. Patched by Claude Code with my approval; logged in the toolkit's `PORT-LOG.md` and in FRICTIONAL.md.
- 2026-10-21 — Not a toolkit change: B06's terracotta box tape failed Gate T contrast, so I changed the drawing in my `scenes.py` to a grey strap with one small terracotta seal (the show-tell skill's documented fix) rather than exempting it.
- Earlier toolkit Windows fixes (2026-10-01) are listed in FRICTIONAL.md.

## What Claude contributed
- Claude (claude.ai chat, 2026-10-20): drafted PROJECT-BRIEF.md from my assignment 2 files; I edited and filled the TODOs.
- Claude Code (2026-10-20): fact-checked BEAT-PLAN.md against my run log and run outputs and reworded five lines (see FACTCHECK.md rows 8, 10, 11, 14, 19); split BEAT-PLAN B04 into two beats; wrote FACTCHECK.md, SHOTLIST.md, PROMPTS.md, `make_sheet.py`, `beat_sheet.json` and the Manim drawings in `scenes.py`; ran the Kokoro audio and low-res stills. Applied the same corrections to PROJECT-BRIEF.md §2 and §4 at my request.
- Claude Code (2026-10-20 to 2026-10-21): ran the renders (`art run`, `art final` at 1080p); stopped at each failed gate and proposed fixes that I chose (run.sh patch, Gate V colour fixes, Gate T exemptions, B06 strap); made those edits; checked the master; wrote BUILD-PROMPT.md and README.md and assembled the submission folder at my request.
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
