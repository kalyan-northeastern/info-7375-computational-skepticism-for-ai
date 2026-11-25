# BOOKEND-CHECK — pm-sponsor-check-pitch (v2, four-part cut)

Gate report for `runtime/scripts/bookend_check.py` (Brutalist toolkit). The v1 report (2026-10-20, 2 failures) is in `_superseded/v1-before-four-part-2026-11-24/`.

- **Run:** 2026-11-24
- **Command:** `python3 C:/Users/DELL/Downloads/brutalist.art-main/brutalist.art-main/runtime/scripts/bookend_check.py C:/Users/DELL/Downloads/project-film-v2`
- **Exit code:** 2 (BLOCKED)

## Output (verbatim)

```
[bookend] BLOCKED — 3 failure(s) in pm-sponsor-check-pitch:
  ✗ YOUR TURN (BHTF): no beat with beat_id=BHTF — add the Your Turn beat
  ✗ OUTRO handle is empty — must be 'Kalyan Karnati'
  ✗ OUTRO title is missing or is the sentinel placeholder — set title='PM Sponsor Check' in the outro beat props
```

## Why it fails, and why it stays that way

**Failures 2 and 3 (BOUT)** are unchanged from v1. The checker reads the outro's `handle` and `title` from a Remotion `ClaudeTitleOutro`. That outro hard-codes the instructor's handle on screen, and my assignment forbids it. So BOUT is a drawn Manim close (`BOUT_Close`), showing "PM Sponsor Check" and "Kalyan Karnati" and spoken as "PM Sponsor Check. By Kalyan Karnati." A Manim beat has no Remotion props, so the checker reads both fields as empty.

**Failure 1 (Your Turn)** is new in v2 and deliberate. I dropped the BHTF beat on 2026-11-24 because it isn't one of the four parts (executive summary, introduction, methods, evaluation), and the cut is 3:46 without it.

| Bookend | Beat | Result |
|---|---|---|
| Cold open | BIDEA (`BrutalistHesitantWriter`) | exempt by `metadata.bookend_exempt` |
| Recap | — | exempt by `metadata.bookend_exempt` |
| Your Turn | — (BHTF dropped) | **fail** (my choice, above) |
| Outro | BOUT (drawn Manim) | **fail** (assignment override, above) |

Not done: restoring the house outro or the Your Turn beat, adding fake props, or editing the toolkit. `run.sh` doesn't call this checker, so it doesn't block the render. See FRICTIONAL.md.
