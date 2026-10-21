# BOOKEND-CHECK — pm-sponsor-check-pitch

Gate report for `runtime/scripts/bookend_check.py` (Brutalist toolkit).

- **Run:** 2026-10-20 18:31 -0400
- **Command:** `python3 <Downloads>/brutalist.art-main/brutalist.art-main/runtime/scripts/bookend_check.py <Downloads>/final-project-film`
- **Exit code:** 2 (BLOCKED)

## Output (verbatim)

```
[bookend] BLOCKED — 2 failure(s) in pm-sponsor-check-pitch:
  ✗ OUTRO handle is empty — must be 'Kalyan Karnati'
  ✗ OUTRO title is missing or is the sentinel placeholder — set title='PM Sponsor Check' in the outro beat props
```

## Why it fails, and why it stays that way

Both failures are on BOUT, and both come from one assignment override.

- The checker reads the outro's `handle` and `title` from the props of a Remotion `ClaudeTitleOutro` beat.
- `ClaudeTitleOutro` hard-codes the instructor's handle on screen. It has no prop to change it.
- My assignment forbids that outro. So BOUT is a drawn Manim close (`scenes.py`, `BOUT_Close`): the film's sealed box, then "PM Sponsor Check" and "Kalyan Karnati", spoken as "PM Sponsor Check. By Kalyan Karnati."
- A Manim beat has no Remotion props, so the checker finds an empty handle and title.

The expected handle is already my name, because `metadata.channel_title` = "Kalyan Karnati". The outro's content matches what the checker wants; only its format differs.

The other bookend checks pass:

| Bookend | Beat | Result |
|---|---|---|
| Cold open | BIDEA (`BrutalistHesitantWriter`) | exempt by `metadata.bookend_exempt` (show-tell opens on the hesitant writer) |
| Recap | — | exempt by `metadata.bookend_exempt` (show-tell has no verdict card) |
| Your Turn | BHTF (`ClaudeComposerAsk`, topic contains "YOUR TURN") | pass |
| Order | BHTF before BOUT | pass |
| Outro | BOUT (drawn Manim) | **fail** (as explained above) |

Not done: restoring the house outro, adding fake Remotion props to BOUT to satisfy the checker, or editing the toolkit. `run.sh` does not call this checker, so the failure does not block the render. See FRICTIONAL.md, 2026-10-20.
