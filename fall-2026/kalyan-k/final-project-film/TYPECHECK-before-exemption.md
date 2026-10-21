# TYPECHECK.md — GATE T

Reel: `pm-sponsor-check-pitch`  |  Checked: 2026-10-21T14:41  |  Overall: **FAIL**  |  Beats checked: 15  |  FAILs: 5

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BIDEA | bookend | light | min-size §8.1: min text-run height 68px >= floor 41px | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B00 | manim | light | kerning §8.4: max inter-glyph gap 125px > threshold 40px (10.8× expected 12px) — check ker… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| B01 | manim | light | min-size §8.1: min text-run height 24px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B02 | manim | light | kerning §8.4: max inter-glyph gap 93px > threshold 37px (8.8× expected 11px) — check kern … | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| B03 | manim | light | min-size §8.1: min text-run height 23px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B04 | manim | light | min-size §8.1: min text-run height 47px >= floor 20px | PASS | — |
| B05 | manim | light | min-size §8.1: min text-run height 27px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B06 | manim | light | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| B07 | manim | light | min-size §8.1: min text-run height 207px >= floor 20px | PASS | — |
| B08 | manim | light | kerning §8.4: max inter-glyph gap 415px > threshold 24px (61.4× expected 7px) — check kern… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |
| B09 | manim | light | min-size §8.1: min text-run height 27px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B10 | manim | light | min-size §8.1: min text-run height 154px >= floor 20px | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | manim | light | kerning §8.4: max inter-glyph gap 355px > threshold 22px (57.0× expected 6px) — check kern… | **FAIL** | Add font='EB Garamond' to all Text() in scenes.py |

---

## Failures requiring action before cut

### B00 (manim)
- **kerning §8.4**: max inter-glyph gap 125px > threshold 40px (10.8× expected 12px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### B02 (manim)
- **kerning §8.4**: max inter-glyph gap 93px > threshold 37px (8.8× expected 11px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### B06 (manim)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

### B08 (manim)
- **kerning §8.4**: max inter-glyph gap 415px > threshold 24px (61.4× expected 7px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

### BOUT (manim)
- **kerning §8.4**: max inter-glyph gap 355px > threshold 22px (57.0× expected 6px) — check kern tables or Pango shaping for this font at this size
- **Fix:** Add font='EB Garamond' to all Text() in scenes.py

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 15 | 0 |
| overflow §8.2 | 15 | 0 |
| contrast §8.3 | 15 | 1 |
| contrast-local §8.3b | 15 | 0 |
| bbox-overlap §8.6b | 15 | 0 |
| card-clip §8.13 | 15 | 0 |
| kerning §8.4 | 12 | 4 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
