# Final Project Pitch Film — PM Sponsor Check

- **Name:** Kalyan Venkata Swamy Karnati
- **Target role:** associate / entry-level product manager, health tech
- **Runtime:** 3:32 (212.2 s)
- **Film:** `pm-sponsor-check-pitch.mp4`: 1080p (1920×1080, 24 fps, H.264 video, AAC stereo audio), 8.8 MB (8,760,961 bytes)
- **sha256:** `1973acff1a59d2be3837f73cec7e80a5cb7e50d0622e88fea0812e19599c0f9e`
- **Narration:** my own words in the first person, read by the Kokoro preset voice `af_heart` (a synthetic voice, not a recording of me)

## Contents

| File | What it is |
|---|---|
| `pm-sponsor-check-pitch.mp4` | the film (clean master from `art final`) |
| `PROJECT-BRIEF.md` | the project brief |
| `beat_sheet.json` | the film's single source of truth: narration, timings and scene for every beat, plus build stamps |
| `make_sheet.py` | writes `beat_sheet.json` |
| `scenes.py` | the Manim drawings for the body beats B00–B10 and the outro BOUT |
| `SHOTLIST.md` | what is on screen in every beat |
| `FACTCHECK.md` | every number and claim in the narration, with its source and verdict |
| `SOURCES.md` | sources, what I made, what Claude contributed, toolkit changes, third-party licences |
| `FRICTIONAL.md` | dated log of what broke and what I did about it |
| `BUILD-PROMPT.md` | the prompts I gave Claude Code, and the commands that rebuild the film |
| `BOOKEND-CHECK.md` | bookend check output (fails on BOUT by design; see the file and FRICTIONAL.md) |
| `TYPECHECK.md` | Gate T (type check): PASS |
| `TYPECHECK-before-exemption.md` | the failing Gate T report, kept as a record |
| `_qc/REPORT.md` | Gate V (frame-level visual QC): 30 frames, 0 BLOCKER, 0 MAJOR |
| `_qc/gateT-exempt-{B00,B02,B08,BOUT}-50pct.png` | midpoint frames of the four beats exempted from Gate T's pixel letter-spacing test |

## Gate results (final build, 2026-10-21)

L clean · A clean · W clean · B clean · V 0 BLOCKER / 0 MAJOR · T PASS.

`bookend_check.py` exits 2 on BOUT because my assignment forbids the house outro. BOOKEND-CHECK.md explains this.

## How to rebuild

The film is built locally and free with the Brutalist toolkit's `show-tell` skill: Kokoro, Manim, Remotion and ffmpeg, with no paid service and no API key. It needs:

- **The Brutalist toolkit**, with the two patches listed in SOURCES.md:
  - `run.sh`: the Manim resolution follows `--height`;
  - `type_check.py`: four scene exemptions.

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
