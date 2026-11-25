# BUILD-PROMPT — how to rebuild the film

The film was built with Claude Code (Opus 5.5) using the Brutalist toolkit's `show-tell` skill: v1 in one session, 2026-10-20 to 2026-10-21, and the v2 four-part cut in a second session on 2026-11-24. Everything runs locally and free: Kokoro TTS, Manim, Remotion and ffmpeg. No paid service or API key was used.

## Commands that rebuild the film

Run them in Git Bash. Set the two paths first:

```bash
export TOOLKIT="/c/Users/DELL/Downloads/brutalist.art-main/brutalist.art-main"   # the Brutalist toolkit
export REEL="/c/Users/DELL/Downloads/project-film-v2"                             # this folder (v2)
export PYTHONUTF8=1
export PATH="$APPDATA/Python/Python312/Scripts:$PATH"   # Manim's launcher, if pip put it in the per-user Scripts folder
```

**0. One-time setup.** Install the toolkit's dependencies and the Kokoro model (kokoro-v1.0.onnx and voices-v1.0.bin, about 340 MB):

```bash
cd "$TOOLKIT" && ./setup --install
```

Then apply the two toolkit patches described in SOURCES.md under "What I changed in the toolkit":

- **`runtime/scripts/run.sh`**: the Manim resolution follows `--height`. In the Manim render loop:

  ```bash
  RES="$((HEIGHT * 16 / 9)),$HEIGHT"
  if grep -q '"aspect_ratio": *"9:16"' "$REEL_DIR/beat_sheet.json" 2>/dev/null; then RES="$HEIGHT,$((HEIGHT * 16 / 9))"; fi
  ```

  This replaces the hard-coded `-r 3840,2160`.
- **`runtime/scripts/type_check.py`**: add these six scenes to `KERNING_EXEMPT_PATTERNS` (the first four from v1, the last two from v2):

  ```python
  "B00_Repo", "B02_Nine", "B08_Scope", "BOUT_Close",
  "S1_Box", "M4_Desk",
  ```

**1. Write the beat sheet.**

```bash
cd "$REEL" && python3 make_sheet.py
```

**2. Generate and measure the narration (Kokoro `af_heart`).**

```bash
cd "$REEL" && python3 "$TOOLKIT/runtime/scripts/generate_audio_kokoro.py" .
```

**3. Pad the outro (BOUT) with 1.0 s of silence, then re-measure it.**

```bash
cd "$REEL" && ffmpeg -y -v error -i mp3/beat-BOUT.mp3 -af "apad=pad_dur=1.0" -c:a libmp3lame -q:a 2 mp3/beat-BOUT.pad.mp3 && mv mp3/beat-BOUT.pad.mp3 mp3/beat-BOUT.mp3
cd "$REEL" && python3 - <<'EOF'
import json, subprocess
s = json.load(open("beat_sheet.json", encoding="utf-8"))
d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", "mp3/beat-BOUT.mp3"]))
for b in s["beats"]:
    if b["beat_id"] == "BOUT":
        b["actual_duration_s"] = round(d, 2)
open("beat_sheet.json", "w", encoding="utf-8").write(json.dumps(s, indent=2, ensure_ascii=False) + "\n")
EOF
```

**4. Re-run the sheet builder.** It keeps the measured audio and sets the bookend durations from it.

```bash
cd "$REEL" && python3 make_sheet.py
```

**5. Optional pre-checks.**

```bash
cd "$REEL" && python3 "$TOOLKIT/runtime/qc/factcheck_check.py" .
cd "$REEL" && python3 "$TOOLKIT/runtime/scripts/bookend_check.py" .
```

The fact check has no blockers (one advisory false alarm on I1A/E1 beat coverage). The bookend check exits 2 by design, on BOUT and on the dropped Your Turn beat; see BOOKEND-CHECK.md.

**6. Review build.** This renders the Manim scenes at 1920×1080 and the Remotion bookends, compiles the review cut, and runs Gates L, SHAPE, A, W, B and V. On a C: drive short of space, set the temp folders to D: first (see the end of this section).

```bash
cd "$TOOLKIT" && bash ./art run "$REEL" --height 1080
```

**7. Clean master.** This runs Gate T (type check), then writes the master and its `.verified.json`.

```bash
cd "$TOOLKIT" && bash ./art final "$REEL" --height 1080 --out "$REEL/exports/landscape"
```

**8. Check the master** for sha256, resolution, runtime and the silent tail.

```bash
cd "$REEL/exports/landscape" && sha256sum pm-sponsor-check-pitch.mp4
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate:format=duration -of compact pm-sponsor-check-pitch.mp4
ffmpeg -sseof -1.0 -i pm-sponsor-check-pitch.mp4 -vn -af volumedetect -f null - 2>&1 | grep max_volume
```

Expected results:

- 1920×1080, 24 fps;
- about 226.75 s long (v2; v1 was 212.2 s);
- the last 1.0 s is silent (`max_volume` about −84 dB).

Kokoro and the encoders can differ by a few bytes between machines, so a rebuilt master may not reproduce the sha256 exactly.

If the C: drive is short of space, point the temp folders at another drive for steps 6 and 7. Remotion writes its frames to the system temp folder:

```bash
export TEMP='D:\tmp' TMP='D:\tmp' TMPDIR='D:/tmp'
```

## Prompts I gave Claude Code (exact, in order)

These are copied from the session history. Where Claude Code asked me a multiple-choice question, my answer is shown as **Answer:**.

**2026-10-20**

1. Build a show-tell film from C:\Users\DELL\Downloads\final-project-film\BEAT-PLAN.md and PROJECT-BRIEF.md, following the show-tell skill's workflow. Important overrides required by my assignment: narrate as me, Kalyan Karnati. No Liam persona, no "in for Bear", no @NikBearBrown outro, and use a Kokoro voice other than am_onyx. If bookend_check.py fails because of these overrides, tell me rather than restoring them. Write SOURCES.md, FACTCHECK.md (numbers sourced from my run log, logs/runs/2026fa-kalyan-karnati-1.md, in my Reallocation Engine files at C:\Users\DELL\Downloads\the-reallocation-engine), SHOTLIST.md and PROMPTS.md first. Stop after audio and low-res stills so I can review before the 4K render.
2. **Answer** to "Which Kokoro voice should narrate as you?": af_heart
3. Apply the same five corrections to PROJECT-BRIEF.md.
4. Two fixes before the 4K render: (1) In B04, add a "constructed" label beside the "mine" window, since that version of the scorer doesn't exist yet. (2) In BHTF, add a small "constructed" label, since the Claude.ai composer is a mock-up. Keep the gate rules in mind for label placement and midpoint timing. Re-render just those two low-res stills so I can check them. Then confirm no Liam, Bear, or @NikBearBrown appears anywhere in the narration, bookends, or metadata, and tell me what bookend_check.py says.
5. Also save the bookend_check.py output as a gate report in final-project-film, and add a dated FRICTIONAL.md entry explaining that it fails on BOUT because the house outro hard-codes the instructor's handle, which my assignment forbids, so I used a Manim outro with my own name instead.
6. Run the 4K render now: art run at --height 2160, then art final into exports/landscape. Show me every gate result (A, B, V, T). If a gate fails, stop and tell me why before fixing anything. When it passes, check the master (sha, 3840×2160, runtime, silent tail) and copy the .mp4 and all gate reports into C:\Users\DELL\Downloads\final-project-film.
7. Render at --height 1080 instead of 2160 for both art run and art final, since 4K ran out of memory on my 8 GB laptop. Move the stale B00 cache to _superseded first. Show me every gate result (A, W, B, V, T). If a gate fails, stop and tell me why. When it passes, check the master (sha, resolution, runtime, silent tail) and copy the .mp4 and all gate reports into C:\Users\DELL\Downloads\final-project-film. Then add a dated FRICTIONAL.md entry in my first person: the 4K render crashed twice (Manim not on PATH, then ffmpeg ran out of memory on my 8 GB laptop), and I switched to 1080p because the assignment requires an mp4, not 4K.
8. **Answer** to "`art run --height 1080` still renders every Manim scene at 4K (run.sh hard-codes 3840×2160), so it would crash again. How should I get 1080p Manim clips?": Patch run.sh (Recommended)
9. Also note this run.sh patch in my FRICTIONAL.md entry and in SOURCES.md under what I changed in the toolkit, with today's date.
10. If Remotion runs out of memory, render bookends at 1080 too
11. Is the render finished? Give me the current stage and gate status.
12. Tell me when Gate V finishes
13. yes i cannot delete anything as of now do accordingly adjustments
14. tell me when Gate V finishes
15. is the render finished? give me gate status
16. If V passes: Go ahead with art final --height 1080 and report Gate T and the master detailsIf V passes, tell it: Go ahead with art final --height 1080 and report Gate T and the master details.

**2026-10-21**

17. Also add a dated FRICTIONAL.md entry: Gate V failed on low contrast in B02, B03 and B05 (0.25–0.28 against a 0.30 floor); I darkened the tiles, the funnel and the removed cards and re-ran, rather than turning the gate off. If Gate V passes, go straight on to art final --height 1080 and report Gate T and the master details.
18. Go with option 1 for the four letter-spacing beats (B00, B02, B08, BOUT) only. For B06, don't add an exemption: apply the show-tell fix for this exact case, a grey strap with one small terracotta seal instead of the terracotta tape, and re-render B06. Save the midpoint frames of the four exempted beats into _qc as evidence, and keep the failing TYPECHECK.md as TYPECHECK-before-exemption.md next to the new one. Log the exemption and the B06 fix in PORT-LOG.md, FRICTIONAL.md and SOURCES.md. Then re-run art final --height 1080 and report Gate T and the master details.

Housekeeping after the master was finished (freeing disk space and tidying files; not part of the build):

19. you give me files or folders which are useless i will delete them on c drive and free up space
20. find these files and delete them i will provide you authorisation to do that
21. **Answer** to "Deleting is permanent. Which groups should I delete?": Windows leftovers
22. delete all the big files as well
23. yes please
24. delete the D: working copy now that everything's back on C: do safely
25. update the build-state paths to C: too
26. update the verified.json too
27. play the master so I can watch it
28. Fill in README.md (runtime 3:32, film file pm-sponsor-check-pitch.mp4, 1080p, how to rebuild) and BUILD-PROMPT.md with the exact prompts I gave you in this session and the commands that rebuild the film. Add third-party assets and licences (fonts, Kokoro voice model) to SOURCES.md from the toolkit's README, plus the two toolkit changes (run.sh resolution patch, type_check.py exemptions). Then build a clean submission folder at C:\Users\DELL\Downloads\submission\final-project-film containing only: README.md, pm-sponsor-check-pitch.mp4, PROJECT-BRIEF.md, beat_sheet.json, BUILD-PROMPT.md, SOURCES.md, FRICTIONAL.md, FACTCHECK.md, SHOTLIST.md, make_sheet.py, scenes.py, and the gate reports (REPORT.md, TYPECHECK.md, TYPECHECK-before-exemption.md, BOOKEND-CHECK.md) plus the four Gate T evidence frames. No clips, no mp3 or media folders, no _qc stills, no _superseded, no logs with private paths, no credentials. List everything you copied and the total size and the .mp4 size.

**2026-11-24 (v2: four-part restructure, in `C:\Users\DELL\Downloads\project-film-v2`)**

29. Get-ChildItem C:\Users\DELL\Downloads\project-film-v2\BEAT-PLAN-v2.md / Select-String -Path C:\Users\DELL\Downloads\project-film-v2\BEAT-PLAN-v2.md -Pattern "TODO" (run twice)
30. Search project-film-v2\BEAT-PLAN-v2.md for "MyVisaJobs" and "fifty-eight" and show me the matching lines.
31. Restructure the film in C:\Users\DELL\Downloads\project-film-v2 into the four parts in its BEAT-PLAN-v2.md (executive summary, introduction, methods, evaluation). Reuse existing scenes and audio wherever it says REUSE; only draw and voice the NEW and EDIT beats. Keep all my overrides (my name, af_heart voice, my outro). Fact-check every new line against my run logs and these sources: USCIS H-1B Employer Data Hub and MyVisaJobs, which I verified myself today. Update FACTCHECK.md, SHOTLIST.md and SOURCES.md (note Claude did the initial research on the two tools). Stop after low-res stills and audio of the new beats so I can review.
32. 1. Yes, re-voice the eight reused beats with the new narration. 2. Fix B08 so it no longer draws the 52/64 gauge (that belongs to E1 now), and change B09's "MA" label to "1 year", since the plan no longer says Massachusetts. Retime both to the new narration. 3. Split I1 into two beats: I1a "Data Hub" and I1b "MyVisaJobs and what's missing", each under about 15 seconds. 4. Yes, dropping B06 and B10 is intended; the four-part structure doesn't need them. 5. The scripts block in M4 is fine. Also, in M4, change "Claude usage" to "AI usage limits" so Kokoro doesn't say "clawed". Then whisper-check all changed beats, re-render low-res stills for every changed scene, and stop again for my review.
33. Yes, retime B01, B03, B04, B05 and B07 the same way as B08 and B09. Drop the BHTF Your Turn beat, since it isn't one of the four parts, to bring the runtime under 4 minutes. Then re-render every changed clip and go straight on to art run and art final at --height 1080 without stopping for another review, unless a gate fails; if one fails, stop and tell me why. When the master is done, report the runtime, resolution and sha, then do the appendix, paperwork, clean submission folder and zip from my earlier instructions.
34. Yes, fix S1 and continue to art final. Add a dated FRICTIONAL.md entry: Gate V blocked on S1 (a page parked at the top edge at the midpoint frame); fixed by moving the page placement after the midpoint guard, then re-rendered S1 only. After the master, carry on with the clean submission folder and zip.
35. If Gate T flags S1 only for letter spacing, it's the same false alarm as B00 in v1. Add S1 to the type_check.py exemption list, save its midpoint frame to _qc as evidence, keep the failing TYPECHECK report as TYPECHECK-v2-before-exemption.md, and log it in PORT-LOG.md, FRICTIONAL.md and SOURCES.md. If it flags anything else, stop and tell me. Then continue to the master, clean folder and zip.
36. **Answer** to "How should I clear Gate T's M4 overlap finding (the laptop screen and desk read as overlapping labels)?": Fix the drawing (Recommended)
37. **Answer** to "M4 now fails only Gate T's letter-spacing test, measured on the laptop screen's bottom edge, not on text. How should I clear it?": Exempt M4 (Recommended)
