# Final Project Pitch Film — PM Sponsor Check (v2, four-part cut)

- **Name:** Kalyan Venkata Swamy Karnati
- **Target role:** associate / entry-level product manager, health tech
- **Runtime:** 3:47 (226.75 s)
- **Film:** `pm-sponsor-check-pitch.mp4`
  - 1080p: 1920×1080, 24 fps, H.264 video, AAC stereo audio
  - 8.8 MB (8,797,580 bytes)
- **sha256:** `2e351fdb20580aece94a5a5e625f886565d4b3d1a73475f3fd9305ab0180d367`
- **Narration:** my own words in the first person, read by the Kokoro preset voice `af_heart` (a synthetic voice, not a recording of me)
- **Structure:** the four parts in BEAT-PLAN-v2.md:
  1. **Executive summary** — what and why: BIDEA, BDEFS, S1, S2.
  2. **Introduction** — prior work: I1A, I1B, I2, I3, I4.
  3. **Methods** — M1–M5.
  4. **Evaluation** — E1–E3; then the outro, BOUT.

  18 beats. The v1 film (3:32, 15 beats) was restructured on 2026-11-24.

## Contents

| File | What it is |
|---|---|
| `pm-sponsor-check-pitch.mp4` | the film (clean master from `art final`) |
| `PROJECT-BRIEF.md` | the project brief |
| `BEAT-PLAN-v2.md` | the four-part plan this cut is built from |
| `APPENDIX.md` | the detail behind the film: data paths and commands, the 64-row test set, run logs, the scorer bug, the LCA plan, resource constraints |
| `beat_sheet.json` | the film's single source of truth: narration, timings and scene for every beat, plus build stamps |
| `make_sheet.py` | writes `beat_sheet.json` |
| `scenes.py` | the Manim drawings for every body beat and the outro BOUT |
| `SHOTLIST.md` | what is on screen in every beat, by part |
| `FACTCHECK.md` | every number and claim in the narration, with its source and verdict |
| `SOURCES.md` | sources, prior work, what I made, what Claude contributed, toolkit changes, third-party licences |
| `FRICTIONAL.md` | dated log of what broke and what I did about it |
| `BUILD-PROMPT.md` | the prompts I gave Claude Code, and the commands that rebuild the film |
| `BOOKEND-CHECK.md` | bookend check output: fails by design on BOUT (assignment outro) and on the dropped Your Turn beat; see the file |
| `TYPECHECK.md` | Gate T (type check): PASS |
| `TYPECHECK-v2-before-exemption.md`, `TYPECHECK-v2-before-exemption-M4.md` | the two failing v2 Gate T reports, kept as a record |
| `TYPECHECK-before-exemption.md` | the failing v1 Gate T report: the origin of the B02, B08 and BOUT exemptions, which still apply |
| `REPORT.md` | Gate V (frame-level visual QC): 36 frames, 0 BLOCKER, 0 MAJOR |
| `gateT-exempt-{S1,B02,M4,B08,BOUT}-50pct.png` | midpoint frames of the five beats exempted from Gate T's pixel letter-spacing test |

## Gate results (final build, 2026-11-24)

L clean · SHAPE clean · A clean · W clean · B clean (all 16 Manim scenes) · V 36 frames, 0 BLOCKER / 0 MAJOR · T PASS.

Two gates stopped the build first, and both are fixed and logged in FRICTIONAL.md:
- **Gate V** blocked S1, where a page was parked at the top edge at the midpoint frame. I fixed the scene.
- **Gate T** flagged S1 and M4.
  - Letter spacing on S1 and M4: the pixel test measured drawings, not text. Both scenes were added to the toolkit's exemption list.
  - Label overlap on M4: I fixed the drawing.

`bookend_check.py` exits 2. That's expected: my assignment forbids the house outro, and the Your Turn beat isn't one of the four parts. BOOKEND-CHECK.md explains both.

## How to rebuild

The film is built locally and free with the Brutalist toolkit's `show-tell` skill: Kokoro, Manim, Remotion and ffmpeg, with no paid service and no API key. It needs:

- **The Brutalist toolkit**, with the patches listed in SOURCES.md:
  - `run.sh`: the Manim resolution follows `--height`;
  - `type_check.py`: six scene exemptions (`B00_Repo`, `B02_Nine`, `B08_Scope`, `BOUT_Close`, `S1_Box`, `M4_Desk`).

  Without them, a 1080p build renders Manim at 4K or is blocked at Gate T. `./setup --install` fetches the toolkit's dependencies and the Kokoro model.
- Python 3.12 with Manim Community 0.18.1, Node 20 and ffmpeg.
- Git Bash on Windows.

In short:

1. `python make_sheet.py`
2. Kokoro audio.
3. Pad BOUT by 1.0 s.
4. `python make_sheet.py` again.
5. `./art run <reel> --height 1080`
6. `./art final <reel> --height 1080 --out <reel>/exports/landscape`

BUILD-PROMPT.md has the full commands and the prompts. The rendered clips, audio and logs are not included in this folder; the commands regenerate them.
