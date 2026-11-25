# TYPECHECK.md — GATE T

Reel: `pm-sponsor-check-pitch`  |  Checked: 2026-11-24T19:41  |  Overall: **FAIL**  |  Beats checked: 18  |  FAILs: 1

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BIDEA | bookend | light | min-size §8.1: min text-run height 68px >= floor 41px | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| S1 | manim | light | min-size §8.1: min text-run height 30px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B02 | manim | light | min-size §8.1: min text-run height 31px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| I1A | manim | light | min-size §8.1: min text-run height 28px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| I1B | manim | light | min-size §8.1: min text-run height 28px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B04 | manim | light | min-size §8.1: min text-run height 47px >= floor 20px | PASS | — |
| B05 | manim | light | min-size §8.1: min text-run height 27px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B03 | manim | light | min-size §8.1: min text-run height 23px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B01 | manim | light | min-size §8.1: min text-run height 24px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| M2 | manim | light | min-size §8.1: min text-run height 23px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B09 | manim | light | min-size §8.1: min text-run height 27px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| M4 | manim | light | kerning §8.4: max inter-glyph gap 290px > threshold 67px (15.2× expected 19px) — check ker… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| B08 | manim | light | min-size §8.1: min text-run height 31px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| E1 | manim | light | min-size §8.1: min text-run height 26px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B07 | manim | light | min-size §8.1: min text-run height 207px >= floor 20px | PASS | — |
| E3 | manim | light | min-size §8.1: min text-run height 28px >= floor 20px | PASS | — |
| BOUT | manim | light | min-size §8.1: min text-run height 34px >= floor 20px (individual-char fallback at 1×) | PASS | — |

---

## Failures requiring action before cut

### M4 (manim)
- **kerning §8.4**: max inter-glyph gap 290px > threshold 67px (15.2× expected 19px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 18 | 0 |
| overflow §8.2 | 18 | 0 |
| contrast §8.3 | 18 | 0 |
| contrast-local §8.3b | 18 | 0 |
| bbox-overlap §8.6b | 18 | 0 |
| card-clip §8.13 | 18 | 0 |
| kerning §8.4 | 16 | 1 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
