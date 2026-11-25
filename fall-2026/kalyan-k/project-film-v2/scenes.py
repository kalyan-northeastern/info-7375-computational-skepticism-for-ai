"""scenes.py — pm-sponsor-check-pitch (show-tell). v2 four-part cut: drawn body beats and the drawn outro BOUT (v1-only scenes B00, B06, B10 removed 2026-11-24).
The iso kit below is pasted from brutalist.art skills/make/show-tell/templates/iso_kit.py (not imported: Gate A copies only scenes.py).
"""
from manim import *
import numpy as np
import json as _json, os as _os

# ═════════════════════════════ ISO KIT (show-tell) ═════════════════════════════
STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"; CARD = "#FAF9F5"
BOX_TOP, BOX_L, BOX_R = "#F3E9D8", "#DCC9AA", "#C7AE86"          # kraft cardboard: top, left face, right face (deep enough for Gate V contrast)
BOX_IN1, BOX_IN2, BOX_FLOOR = "#CDB894", "#BFA67E", "#B39A72"     # inside walls + floor
DARK_TOP, DARK_L, DARK_R = "#3A3530", "#26221F", "#1E1B18"        # MCP / server blocks
PAGE_TOP, PAGE_L, PAGE_R = "#FFFFFF", "#ECE7DF", "#E2DCD2"         # skill pages
BAR1, BAR2, BAR3 = "#8B8F96", "#B4AFA6", "#D9D4C7"                # chart segments, dim to ghost
SERIF = "EB Garamond"
C30 = 0.8660254
config.background_color = STAGE


def T(s, size=36, color=INK, bold=False):
    return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")


class Iso:
    """Isometric projection: x runs right-up, y runs left-up, z runs up. (ox, oy) is where (0,0,0) lands."""
    def __init__(self, ox=0.0, oy=0.0, s=1.0):
        self.ox, self.oy, self.s = ox, oy, s

    def p(self, x, y, z=0.0):
        return np.array([self.ox + (x - y) * C30 * self.s, self.oy + (x + y) * 0.5 * self.s + z * self.s, 0.0])

    def v(self, dx, dy, dz=0.0):
        return self.p(dx, dy, dz) - self.p(0, 0, 0)

    def quad(self, pts, fill, stroke=INK, sw=4):
        return Polygon(*[self.p(*q) for q in pts], fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)

    def box(self, x0, y0, z0, w, d, h, top=BOX_TOP, left=BOX_L, right=BOX_R, sw=4):
        """Closed box: the two front faces (x = x0 and y = y0) plus the top."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        return VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], left, sw=sw),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], right, sw=sw),
            self.quad([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], top, sw=sw))

    def open_box(self, x0, y0, z0, w, d, h):
        """(back, front): floor + inner back walls, then the front walls. Put contents between them."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        back = VGroup(
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)], BOX_FLOOR),
            self.quad([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], BOX_IN1),
            self.quad([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], BOX_IN2))
        front = VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], BOX_L),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], BOX_R))
        back.set_z_index(0); front.set_z_index(2)
        return back, front

    def tape(self, x0, y0, z1, w, d, drop=0.35, t=0.22):
        """Terracotta tape across the top (along x) and down the left front face."""
        ym = y0 + d / 2
        return VGroup(
            self.quad([(x0, ym - t, z1), (x0 + w, ym - t, z1), (x0 + w, ym + t, z1), (x0, ym + t, z1)], TERRA, sw=0),
            self.quad([(x0, ym - t, z1), (x0, ym + t, z1), (x0, ym + t, z1 - drop), (x0, ym - t, z1 - drop)], TERRA, sw=0))

    def mcp(self, x0, y0, z0, w=1.3, d=1.3, h=0.7):
        """Dark MCP block with two light ports on its right front face."""
        body = self.box(x0, y0, z0, w, d, h, DARK_TOP, DARK_L, DARK_R)
        ports = VGroup(*[self.box(x0 + w * f, y0 - 0.18, z0 + h * 0.3, w * 0.16, 0.18, h * 0.3, GHOST, BOX_IN1, BOX_IN2, sw=1)
                         for f in (0.22, 0.58)])
        return VGroup(body, ports)

    def page(self, x0, y0, z0, w=1.1, d=1.4):
        """A skill page lying flat: white slab, three ghost text lines, one terracotta dot."""
        slab = self.box(x0, y0, z0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        zt = z0 + 0.06
        lines = VGroup(*[Line(self.p(x0 + 0.2, y0 + d * f, zt), self.p(x0 + w - 0.2, y0 + d * f, zt), color=GHOST, stroke_width=4)
                         for f in (0.3, 0.5, 0.7)])
        dot = Dot(self.p(x0 + 0.2, y0 + d * 0.86, zt), radius=0.06, color=TERRA)
        return VGroup(slab, lines, dot)

    def server(self, x0, y0, z0, w=1.4, d=1.4, slab=0.42, n=3):
        """A stack of dark server slabs; returns (stack, lights) — lights start ghost, turn terracotta."""
        stack = VGroup(*[self.box(x0, y0, z0 + i * (slab + 0.04), w, d, slab, DARK_TOP, DARK_L, DARK_R) for i in range(n)])
        lights = VGroup(*[Dot(self.p(x0 + 0.25, y0, z0 + i * (slab + 0.04) + slab / 2), radius=0.06, color=GHOST) for i in range(n)])
        return stack, lights


def ease_in(t):
    """Quadratic ease-in (things dropping into a box). Local: Gate A's stub has no ease_in_quad."""
    return t * t


def check(x, y, s=0.2, color=INK, w=7):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.75, 0], color=color, stroke_width=w),
                  Line([x - s * 0.3, y - s * 0.75, 0], [x + s * 1.1, y + s * 0.85, 0], color=color, stroke_width=w))


def cursor(x, y, s=0.45):
    return Polygon([x, y, 0], [x, y - s, 0], [x + s * 0.28, y - s * 0.72, 0], [x + s * 0.62, y - s * 0.66, 0],
                   fill_color=INK, fill_opacity=1, stroke_color=CARD, stroke_width=2)


def pill(x, y, w, h=0.62, fill="#FFFFFF"):
    return RoundedRectangle(width=w, height=h, corner_radius=h / 2, fill_color=fill, fill_opacity=1, stroke_width=0).move_to([x, y, 0])


# ═════════════════════════════ pacing (narration is the clock) ═════════════════════════════
try:
    _SHEET = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}


def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0


def until(self, phrase, lead=0.25):
    """Wait until `phrase` is spoken (its character share of the narration × the measured audio)."""
    bid = type(self).__name__.split("_")[0]
    n, target = _NARR.get(bid, ""), _TARGET.get(bid, 0)
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)


# ═════════════════════════════ font (Windows: Pango does not see the system EB Garamond) ═════════════════════════════
try:
    import manimpango as _mp, glob as _glob
    _home = _os.environ.get("ART_HOME") or r"C:/Users/DELL/Downloads/brutalist.art-main/brutalist.art-main"
    for _f in _glob.glob(_os.path.join(_home, "runtime", "fonts", "EB_Garamond", "static", "*.ttf")):
        _mp.register_font(_f)
except Exception:
    pass


# ═════════════════════════════ midpoint guard (GATE T / Gate V sample the clip midpoint) ═════════════════════════════
def _mid(self):
    return _TARGET.get(type(self).__name__.split("_")[0], 0) / 2.0


def P(self, *anims, rt=0.6, m=0.22, **kw):
    """play(), but never across the clip midpoint: if the span would touch mid ± m, wait past it first."""
    mid, t = _mid(self), _elapsed(self)
    if mid and t < mid + m and t + rt > mid - m:
        self.wait(mid + m - t)
    self.play(*anims, run_time=rt, **kw)


def guard(self, rt=0.6, m=0.22):
    """Wait out the midpoint BEFORE placing an object off-stage, so it is never parked at the frame edge
    on the frame GATE T / Gate V sample (Gate V blocked S1 on 2026-11-24 for exactly this)."""
    mid, t = _mid(self), _elapsed(self)
    if mid and t < mid + m and t + rt > mid - m:
        self.wait(mid + m - t)


# ═════════════════════════════ the film: pm-sponsor-check-pitch ═════════════════════════════
# Cast: the kraft box (the tool), small crates (companies), flat pages (recipe, run log, filings),
# ink windows (other tools), the check (a verified fact). "constructed" marks what does not exist yet.
BOXW, BOXD, BOXH, LIDH = 3.0, 3.0, 1.9, 0.22
MAIN = Iso(0.0, -2.0, 0.78)
DEEP = "#9C8462"          # connector / rail edges (not ink: ink edges fuse into text blobs)


def floor_shadow(iso=MAIN, w=BOXW, d=BOXD):
    sh = iso.quad([(0.15, -0.35, 0), (w + 0.35, -0.35, 0), (w + 0.35, d - 0.15, 0), (0.15, d - 0.15, 0)], "#BFB4A0", sw=0)
    sh.set_z_index(-1)
    return sh


def sealed(iso=MAIN, w=BOXW, d=BOXD, h=BOXH):
    return VGroup(iso.box(0, 0, 0, w, d, h), iso.tape(0, 0, h, w, d))


def strap(iso, x0, y0, z1, w, d, drop=0.35, t=0.22):
    """Grey strap with one spark-sized terracotta seal (GATE T reads a terracotta tape band as accent text)."""
    band = iso.tape(x0, y0, z1, w, d, drop=drop, t=t).set_fill(DIM, opacity=1)
    return VGroup(band, Dot(iso.p(x0 + w / 2, y0 + d / 2, z1), radius=0.08, color=TERRA))


def crate(x, y, s=0.35, h=0.8, stroke=INK, sw=3):
    """A small company crate; (x, y) is its front-bottom corner on screen."""
    I = Iso(x, y, s)
    return VGroup(I.quad([(0, 0, 0), (0, 1, 0), (0, 1, h), (0, 0, h)], BOX_L, stroke, sw),
                  I.quad([(0, 0, 0), (1, 0, 0), (1, 0, h), (0, 0, h)], BOX_R, stroke, sw),
                  I.quad([(0, 0, h), (1, 0, h), (1, 1, h), (0, 1, h)], BOX_TOP, stroke, sw))


def crate_top(x, y, s=0.35, h=0.8):
    return Iso(x, y, s).p(0.5, 0.5, h)


def window(x, y=0.2, w=5.0, h=3.4):
    """A pale UI window: card face, ink outline, grey title band (a dark band inside an ink card fails GATE T)."""
    frame = RoundedRectangle(width=w, height=h, corner_radius=0.18, fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    band = RoundedRectangle(width=w - 0.3, height=0.4, corner_radius=0.12, fill_color=BAR1, fill_opacity=1,
                            stroke_width=0).move_to([x, y + h / 2 - 0.4, 0])
    lights = VGroup(*[Dot([x - w / 2 + 0.45 + i * 0.3, y + h / 2 - 0.4, 0], radius=0.07, color=CARD) for i in range(3)])
    return VGroup(frame, band, lights)


def doc(x, y, w=1.4, h=1.8, fill=PAGE_TOP, stroke=INK, sw=3, n=3):
    face = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color=fill, fill_opacity=1,
                            stroke_color=stroke, stroke_width=sw).move_to([x, y, 0])
    lines = VGroup(*[Line([x - w / 2 + 0.22, y + h / 2 - 0.4 - i * 0.32, 0], [x + w / 2 - 0.22, y + h / 2 - 0.4 - i * 0.32, 0],
                          color=GHOST, stroke_width=6) for i in range(n)])
    return VGroup(face, lines)


# ── B01 [M1] — the 80 Days table: about 30,000 companies, two record sources (v2: retimed; the 352 stack is gone) ─
class B01_Gate(Scene):
    def construct(self):
        cells = sorted([(i, j) for i in range(4) for j in range(4)], key=lambda c: -(c[0] + c[1]))
        G = Iso(-3.8, -2.4, 0.42)
        grid = VGroup(*[crate(*G.p(i * 1.25, j * 1.25, 0)[:2], s=0.42) for i, j in cells])
        P(self, LaggedStart(*[FadeIn(c) for c in grid], lag_ratio=0.05), rt=1.0)
        posts = VGroup(*[Rectangle(width=0.4, height=3.2, fill_color=DIM, fill_opacity=1, stroke_color=INK, stroke_width=4)
                         .move_to([x, -0.9, 0]) for x in (-0.7, 1.1)])
        lintel = Rectangle(width=2.4, height=0.4, fill_color=DIM, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([0.2, 0.9, 0])
        P(self, LaggedStart(GrowFromEdge(posts[0], DOWN), GrowFromEdge(posts[1], DOWN), FadeIn(lintel), lag_ratio=0.3), rt=0.7)

        until(self, "80 Days to Stay table")
        P(self, FadeIn(T("30,369", 52).move_to([-3.8, 1.0, 0])), rt=0.5)

        until(self, "joins SEC Form D filings")
        P(self, grid.animate.shift(RIGHT * 0.7), rt=0.9)

        until(self, "with H-1B records")
        P(self, GrowFromCenter(Dot([0.2, 0.9, 0], radius=0.1, color=TERRA)), rt=0.3)
        finish(self)


# ── B02 — 9 of 352 list a PM title ──────────────────────────────────────────────
NINE = [(2, 8), (5, 3), (9, 6), (13, 1), (16, 9), (20, 4), (24, 7), (27, 2), (30, 5)]   # (col, row) of the nine


class B02_Nine(Scene):
    def construct(self):
        x0, y0, pitch, side = -4.65, -2.9, 0.3, 0.24
        rows = VGroup(*[VGroup(*[Square(side, fill_color=BAR1, fill_opacity=1, stroke_width=0)
                                 .move_to([x0 + c * pitch, y0 + r * pitch, 0]) for c in range(32)]) for r in range(11)])
        P(self, LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.08), rt=0.9)
        scan = Line([-4.95, -3.1, 0], [-4.95, 0.3, 0], color=TERRA, stroke_width=6)
        P(self, Create(scan), rt=0.2)
        lit = VGroup(*[rows[r][c] for c, r in NINE])
        dots = VGroup(*[Dot([x0 + c * pitch, y0 + r * pitch, 0], radius=0.09, color=TERRA) for c, r in NINE])
        P(self, scan.animate.shift(RIGHT * 9.9),
          LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.35),
          *[s.animate.set_fill(INK) for s in lit], rt=2.0, rate_func=linear)
        P(self, FadeOut(scan), rt=0.3)
        P(self, FadeIn(T("9 of 352", 96).move_to([0, 1.9, 0])), rt=0.5)
        finish(self)


# ── B03 [I4] — a health-category filter would drop 64 (v2: retimed) ─────────────
class B03_Filter(Scene):
    def construct(self):
        funnel = VGroup(
            Polygon([-3.0, 1.6, 0], [0.4, 1.6, 0], [-0.9, 0.0, 0], [-1.7, 0.0, 0],
                    fill_color=DEEP, fill_opacity=1, stroke_color=INK, stroke_width=4),
            Rectangle(width=0.8, height=0.8, fill_color=DARK_L, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-1.3, -0.4, 0]))
        top = VGroup(*[crate(x, 2.3, s=0.3) for x in (-2.7, -2.1, -1.5, -0.9, -0.3)])
        P(self, FadeIn(funnel), FadeIn(top), rt=0.6)
        P(self, FadeIn(T("health filter", 36).move_to([-4.75, 0.6, 0])), rt=0.4)

        until(self, "would have quietly dropped")
        through = VGroup(*top[:3])
        P(self, LaggedStart(*[c.animate.move_to([-1.3, 0.2, 0]) for c in through], lag_ratio=0.2), rt=0.7, rate_func=ease_in)
        targets = [[-1.9, -2.6, 0], [-1.3, -2.6, 0], [-0.7, -2.6, 0]]
        P(self, *[c.animate.move_to(t) for c, t in zip(through, targets)], rt=0.5)

        until(self, "sixty-four sponsors")
        off = [top[3], top[4]]
        ends = [np.array([2.9, -1.27, 0]), np.array([3.5, -1.27, 0])]   # centres of the top-row slots
        P(self, *[MoveAlongPath(c, ArcBetweenPoints(np.array(c.get_center()), e, angle=-PI / 3)) for c, e in zip(off, ends)], rt=1.0)
        more = VGroup(crate(2.6, -2.2, s=0.3), crate(3.2, -2.2, s=0.3), crate(3.8, -2.2, s=0.3))
        more.set_z_index(-1)
        P(self, LaggedStart(*[FadeIn(c) for c in more], lag_ratio=0.2), rt=0.5)
        P(self, FadeIn(T("64", 56).move_to([3.4, -0.25, 0])), rt=0.4)
        P(self, FadeIn(T("tech · other", 32).move_to([3.4, -2.85, 0])), rt=0.4)

        until(self, "it checks the role")
        spark = Dot(crate_top(2.9, -1.6, s=0.3), radius=0.07, color=TERRA)
        P(self, GrowFromCenter(spark), rt=0.4)
        finish(self)


# ── B04 [I2] — the engine's scorer vs. mine (v2: retimed) ───────────────────────
def score_rows(x, widths=(1.6, 2.0, 1.2)):
    ys = (0.8, 0.0, -0.8)
    icons = VGroup(*[crate(x - 1.95, y - 0.2, s=0.22, stroke=DIM, sw=2) for y in ys])
    bars = VGroup(*[Rectangle(width=w, height=0.26, fill_color=BAR1, fill_opacity=1, stroke_width=0)
                    .move_to([x - 1.4 + w / 2, y, 0]) for w, y in zip(widths, ys)])
    return icons, bars, ys


class B04_Scorer(Scene):
    def construct(self):
        L, R = window(-3.0), window(3.0)
        P(self, FadeIn(L), FadeIn(R), rt=0.6)
        P(self, FadeIn(T("engine scorer", 36).move_to([-3.0, -2.0, 0])), FadeIn(T("mine", 36).move_to([3.0, -2.0, 0])), rt=0.5)
        # my scorer does not exist yet: labelled beside (below) its window, ink, settled long before the midpoint
        P(self, FadeIn(T("constructed", 32).move_to([3.0, -2.6, 0])), rt=0.4)
        li, lb, ys = score_rows(-3.0)
        ri, rb, _ = score_rows(3.0)
        P(self, FadeIn(li), FadeIn(ri), rt=0.4)

        until(self, "each company's sponsorship")
        P(self, *[GrowFromEdge(b, LEFT) for b in lb], rt=0.8)

        until(self, "like")
        P(self, *[GrowFromEdge(b, LEFT) for b in rb], rt=0.8)
        pages = VGroup(*[doc(4.55, y, w=0.5, h=0.55, stroke=DIM, sw=2, n=1) for y in ys])
        P(self, LaggedStart(*[FadeIn(p) for p in pages], lag_ratio=0.2), rt=0.5)

        until(self, "for the whole company")
        slots = VGroup(*[DashedVMobject(Square(0.45, stroke_color=DIM, stroke_width=3), num_dashes=12).move_to([-1.15, y, 0]) for y in ys])
        P(self, FadeIn(slots), rt=0.5)

        until(self, "not for a role")
        P(self, Create(check(5.05, ys[0], s=0.14)), rt=0.4)
        finish(self)


# ── B05 [I3] — Built In's stale copies vs. the company's own board (v2: retimed) ─
def job_card(x, y, w=4.2, h=0.62):
    face = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color=PAGE_L, fill_opacity=1,
                            stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    line = Line([x - w / 2 + 0.6, y, 0], [x + w / 2 - 0.9, y, 0], color=DIM, stroke_width=8)
    return VGroup(face, line)


class B05_Board(Scene):
    def construct(self):
        L, R = window(-3.0), window(3.0)
        P(self, FadeIn(L), FadeIn(R), rt=0.6)
        P(self, FadeIn(T("Built In", 36).move_to([-3.0, -2.0, 0])), FadeIn(T("company board", 36).move_to([3.0, -2.0, 0])), rt=0.5)

        until(self, "still listed copies")
        ys = (0.7, -0.05, -0.8)
        cards = VGroup(*[job_card(-3.0, y) for y in ys])
        P(self, LaggedStart(*[FadeIn(c) for c in cards], lag_ratio=0.2), rt=0.5)

        until(self, "marked removed")
        crosses = VGroup(*[VGroup(Line([-1.55, y - 0.2, 0], [-1.15, y + 0.2, 0], color=INK, stroke_width=6),
                                  Line([-1.55, y + 0.2, 0], [-1.15, y - 0.2, 0], color=INK, stroke_width=6)) for y in ys])
        P(self, *[c[0].animate.set_fill(BAR2) for c in cards], *[Create(x) for x in crosses], rt=0.6)

        until(self, "the live role")
        live = job_card(3.0, 0.7)
        lamp = Dot([1.25, 0.7, 0], radius=0.1, color=TERRA)
        P(self, FadeIn(live), rt=0.4)
        P(self, GrowFromCenter(lamp), rt=0.3)

        until(self, "own board")
        P(self, Create(check(4.65, 0.7, s=0.16)), rt=0.4)
        finish(self)


# ── B07 [E2] — honesty of the ranking (v2: retimed) ─────────────────────────────
def rank_card(y):
    face = RoundedRectangle(width=5.6, height=1.5, corner_radius=0.16, fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([0.4, y, 0])
    icon = crate(-1.85, y - 0.35, s=0.3, stroke=DIM, sw=2)
    lines = VGroup(*[Line([-1.0, y + dy, 0], [1.6, y + dy, 0], color=GHOST, stroke_width=8) for dy in (0.22, -0.22)])
    return VGroup(face, icon, lines)


class B07_Error(Scene):
    def construct(self):
        top, bot = rank_card(1.0), rank_card(-1.2)
        good = check(2.45, -1.2, s=0.22)
        P(self, FadeIn(top), FadeIn(bot), FadeIn(good), rt=0.6)
        P(self, FadeIn(T("1", 56).move_to([-3.2, 1.0, 0])), FadeIn(T("2", 56).move_to([-3.2, -1.2, 0])),
          FadeIn(T("unchecked", 36).move_to([4.65, 1.0, 0])), FadeIn(T("checked", 36).move_to([4.45, -1.2, 0])), rt=0.5)

        until(self, "as checked")
        fake = check(2.45, 1.0, s=0.22, color=DIM)
        P(self, Create(fake), rt=0.4)

        until(self, "It works if")
        P(self, fake.animate.set_color(GHOST), rt=0.5)

        until(self, "ever ranks above")
        scan = Line([-2.5, 0.1, 0], [-2.5, 1.9, 0], color=TERRA, stroke_width=6)
        P(self, Create(scan), rt=0.2)
        P(self, scan.animate.shift(RIGHT * 5.8), rt=1.1, rate_func=linear)
        P(self, FadeOut(scan), rt=0.3)

        until(self, "the log proves it")
        ring = DashedVMobject(RoundedRectangle(width=6.0, height=1.9, corner_radius=0.22, stroke_color=INK, stroke_width=4), num_dashes=40).move_to([0.4, 1.0, 0])
        flag = Dot([-3.75, 1.0, 0], radius=0.11, color=TERRA)
        P(self, Create(ring), rt=0.6)
        P(self, GrowFromCenter(flag), rt=0.3)
        finish(self)


# ── B08 [M5] — out of scope (v2: the 52 / 64 gauge moved to E1_Gauge; retimed to the scope sentence) ─
FENCE = Iso(-2.3, -2.6, 0.55)
SBOX = Iso(0.6, -2.6, 0.5)


class B08_Scope(Scene):
    def construct(self):
        posts = VGroup(*[FENCE.box(0, y, 0, 0.2, 0.2, 1.5, BAR2, BAR1, DIM, sw=2) for y in (5, 4, 3, 2, 1, 0)])
        rails = VGroup(*[Line(FENCE.p(0.1, 0, z), FENCE.p(0.1, 5.2, z), color=DEEP, stroke_width=6) for z in (0.55, 1.15)])
        rails.set_z_index(-1)
        box = sealed(SBOX)
        P(self, LaggedStart(*[GrowFromEdge(p, DOWN) for p in posts], lag_ratio=0.12), Create(rails), FadeIn(box), rt=0.8)

        until(self, "which job code")
        code = FENCE.mcp(-2.0, 0.6, 0, w=1.3, d=1.3, h=0.6)
        P(self, FadeIn(code), rt=0.5)
        P(self, FadeIn(T("out", 40).move_to([-5.6, -1.4, 0])), rt=0.4)

        until(self, "immigration advice")
        advice = FENCE.page(-2.2, 2.9, 0, w=1.4, d=1.6)
        P(self, FadeIn(advice), rt=0.4)
        P(self, box.animate.shift(RIGHT * 0.9), rt=0.5)
        finish(self)


# ── B09 [M3] — step four: the filing data; the one-year slice (v2: "MA" dropped, retimed) ─
STACK = Iso(-1.8, -2.9, 0.7)
JITTER = [(0.0, 0.0), (0.18, -0.1), (-0.15, 0.12), (0.1, 0.2), (-0.2, -0.05), (0.22, 0.08), (-0.05, -0.2), (0.15, 0.15),
          (-0.18, 0.1), (0.05, -0.15), (0.2, 0.0), (-0.12, -0.12), (0.08, 0.2), (-0.2, 0.05), (0.12, -0.08), (0.0, 0.14)]


class B09_Risk(Scene):
    def construct(self):
        plinth = STACK.box(0, 0, 0, 2.6, 2.6, 0.4, DARK_TOP, DARK_L, DARK_R)
        pages = VGroup(*[STACK.box(0.2 + dx, 0.2 + dy, 0.4 + i * 0.2, 2.2, 2.2, 0.12, PAGE_TOP, PAGE_L, PAGE_R, sw=2)
                         for i, (dx, dy) in enumerate(JITTER)])
        P(self, FadeIn(plinth), LaggedStart(*[FadeIn(p, shift=DOWN * 0.3) for p in pages], lag_ratio=0.06), rt=1.2)
        P(self, FadeIn(T("filing data", 36).move_to([-5.0, 1.5, 0])), rt=0.4)

        until(self, "It's large and messy")
        pivot = np.array(STACK.p(1.3, 1.3, 0.4))
        P(self, Rotate(pages, 3 * DEGREES, about_point=pivot), rt=0.3)
        P(self, Rotate(pages, -6 * DEGREES, about_point=pivot), rt=0.4)
        P(self, Rotate(pages, 3 * DEGREES, about_point=pivot), rt=0.3)

        until(self, "start with one fiscal year")
        small = Iso(3.4, -2.6, 0.7)
        base = small.box(0, 0, 0, 2.6, 2.6, 0.4, DARK_TOP, DARK_L, DARK_R)
        P(self, FadeIn(base), rt=0.4)
        slice_ = VGroup(*pages[-2:])
        P(self, slice_.animate.move_to(small.p(1.3, 1.3, 0.62)), rt=1.0)

        until(self, "the most recent complete one")
        P(self, FadeIn(T("1 year", 36).move_to([3.4, 0.35, 0])), rt=0.4)
        until(self, "say so in the log")
        P(self, FadeIn(T("constructed", 32).move_to([3.4, 1.0, 0])), rt=0.4)
        finish(self)


# ═════════════════════════════ v2 (2026-11-24): new and edited beats for the four-part cut ═════════════════════════════
# ── S1 — executive summary: the box and what it does (edit of B00) ─────────────
class S1_Box(Scene):
    def construct(self):
        back, front = MAIN.open_box(0, 0, 0, BOXW, BOXD, BOXH)
        box = VGroup(back, front)
        box.shift(UP * 4.4)
        self.add(box)
        P(self, box.animate.shift(DOWN * 4.4), rt=1.0, rate_func=rate_functions.ease_out_bounce)
        P(self, FadeIn(floor_shadow()), rt=0.3)

        until(self, "a tool that tells")
        script = MAIN.mcp(1.7, 0.35, 1.35, w=1.1, d=1.1, h=0.7); script.set_z_index(1)
        guard(self); script.shift(UP * 3.2); self.add(script)
        P(self, script.animate.shift(DOWN * 3.2), rt=0.6, rate_func=ease_in)
        P(self, FadeIn(T("scan", 40).move_to([3.7, 1.0, 0])), rt=0.4)

        until(self, "public evidence")
        evidence = MAIN.page(0.35, 1.6, 1.92, w=1.1, d=1.25); evidence.set_z_index(1)
        guard(self); evidence.shift(UP * 3.2); self.add(evidence)
        P(self, evidence.animate.shift(DOWN * 3.2), rt=0.6, rate_func=ease_in)
        P(self, FadeIn(T("evidence", 40).move_to([-3.7, 1.3, 0])), rt=0.4)

        until(self, "labels every answer")
        tray = VGroup(MAIN.box(0.3, 0.3, 1.6, 1.15, 1.15, 0.35),
                      MAIN.page(0.42, 0.42, 1.95, w=0.9, d=0.9))
        tray.set_z_index(1)
        guard(self); tray.shift(UP * 3.2); self.add(tray)
        P(self, tray.animate.shift(DOWN * 3.2), rt=0.6, rate_func=ease_in)
        P(self, FadeIn(T("record · guess", 40).move_to([3.6, -1.3, 0])), rt=0.4)

        until(self, "a record or a guess")
        P(self, FadeIn(T("constructed", 32).move_to([0, -2.95, 0])), rt=0.4)
        finish(self)


# ── I1 (split 2026-11-24 into I1A and I1B, each under 15 s) — shared layout ───────
WX = (-4.15, 0.0, 4.15)
WY, WW, WH = 0.55, 3.6, 3.0
LAMP_Y = 1.2            # just under the title band, clear of the columns


def lamp_slot(x, y):
    return DashedVMobject(Circle(radius=0.17, stroke_color=DIM, stroke_width=3), num_dashes=10).move_to([x, y, 0])


def datahub_state():
    """I1A's end frame (I1B starts from it): two windows and labels, Data Hub's columns and its empty title slot."""
    x0, base = WX[0], -0.75
    wins = VGroup(window(WX[0], WY, WW, WH), window(WX[1], WY, WW, WH))
    labels = VGroup(T("Data Hub", 36).move_to([WX[0], -1.45, 0]), T("MyVisaJobs", 36).move_to([WX[1], -1.45, 0]))
    cols = VGroup(*[Rectangle(width=0.42, height=h, fill_color=c, fill_opacity=1, stroke_width=0)
                    .move_to([x0 - 1.15 + i * 0.6, base + h / 2, 0])
                    for i, (h, c) in enumerate(((1.7, BAR1), (1.2, BAR2), (1.45, BAR1)))])
    slot = DashedVMobject(Rectangle(width=0.55, height=1.45, stroke_color=INK, stroke_width=3), num_dashes=20).move_to([x0 + 0.65, base + 0.73, 0])
    return wins, labels, cols, slot


# ── I1A — prior work 1: the Data Hub counts by company, industry, year; no job title ─
class I1A_DataHub(Scene):
    def construct(self):
        wins, labels, cols, slot = datahub_state()
        P(self, LaggedStart(*[FadeIn(w) for w in wins], lag_ratio=0.2), rt=0.6)
        P(self, *[FadeIn(l) for l in labels], rt=0.5)

        until(self, "counts petitions")
        P(self, *[GrowFromEdge(c, DOWN) for c in cols], rt=0.8)

        until(self, "not by job title")
        P(self, Create(slot), rt=0.5)
        finish(self)


# ── I1B — prior work 2: MyVisaJobs has titles and wages; neither checks or labels; mine does ─
class I1B_Missing(Scene):
    def construct(self):
        wins, labels, cols, slot = datahub_state()
        self.add(wins, labels, cols, slot)
        x0, x1, ys = WX[0], WX[1], (0.75, 0.1, -0.55)

        until(self, "MyVisaJobs goes further")
        titles = VGroup(*[Line([x1 - 1.45, y, 0], [x1 - 0.2, y, 0], color=BAR2, stroke_width=10) for y in ys])
        P(self, LaggedStart(*[Create(t) for t in titles], lag_ratio=0.2), rt=0.6)

        until(self, "wage levels")
        wages = VGroup(*[Rectangle(width=w, height=0.26, fill_color=BAR1, fill_opacity=1, stroke_width=0)
                         .move_to([x1 + 0.05 + w / 2, y, 0]) for w, y in zip((1.2, 0.8, 1.0), ys)])
        P(self, *[GrowFromEdge(b, LEFT) for b in wages], rt=0.7)

        until(self, "What neither does")
        slots = VGroup(lamp_slot(x0 + 1.35, LAMP_Y), lamp_slot(x1 + 1.35, LAMP_Y))
        P(self, Create(slots), rt=0.5)

        until(self, "That's what mine adds")
        x2 = WX[2]
        # two plays, not four: the line lands 1.2 s before the audio ends
        P(self, FadeIn(window(x2, WY, WW, WH)), FadeIn(job_card(x2, 0.4, w=2.9, h=0.7)), FadeIn(T("mine", 36).move_to([x2, -1.45, 0])),
          FadeIn(T("constructed", 32).move_to([x2, -2.05, 0])), rt=0.4)
        P(self, GrowFromCenter(Dot([x2 + 1.35, LAMP_Y, 0], radius=0.12, color=TERRA)), Create(check(x2 + 0.6, -0.45, s=0.2)), rt=0.4)
        finish(self)


# ── M2 — methods: three steps on one conveyor ───────────────────────────────────
GATES = (-3.8, -0.7, 2.4)


class M2_Steps(Scene):
    def construct(self):
        belt = Rectangle(width=12.0, height=0.5, fill_color="#E6E1D4", fill_opacity=1, stroke_color=DEEP, stroke_width=4).move_to([0, -1.25, 0])
        dashes = VGroup(*[Line([x, -1.25, 0], [x + 0.35, -1.25, 0], color=GHOST, stroke_width=4) for x in np.arange(-5.7, 5.8, 0.8)])
        gates, lamps = VGroup(), VGroup()
        for gx in GATES:
            posts = VGroup(*[Rectangle(width=0.3, height=2.3, fill_color=DIM, fill_opacity=1, stroke_color=INK, stroke_width=4)
                             .move_to([gx + dx, -0.25, 0]) for dx in (-0.85, 0.85)])
            lintel = Rectangle(width=2.0, height=0.34, fill_color=DIM, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([gx, 1.0, 0])
            gates.add(VGroup(posts, lintel))
            lamps.add(Dot([gx, 1.0, 0], radius=0.1, color=GHOST))
        P(self, FadeIn(belt), FadeIn(dashes), rt=0.5)
        P(self, LaggedStart(*[FadeIn(g) for g in gates], lag_ratio=0.2), FadeIn(lamps), rt=0.7)
        P(self, *[FadeIn(T(s, 36).move_to([gx, -2.05, 0])) for s, gx in zip(("filter", "title scan", "liveness"), GATES)], rt=0.5)
        P(self, FadeIn(T("constructed", 32).move_to([GATES[2], -2.65, 0])), rt=0.4)

        box = crate(-5.6, -1.1, s=0.55)
        P(self, FadeIn(box, shift=RIGHT * 0.4), rt=0.4)
        stops = (-2.1, 1.0, 4.1)          # crate centre after each gate, clear of the posts
        for phrase, i in (("Step one", 0), ("Step two", 1), ("Step three", 2)):
            until(self, phrase)
            P(self, box.animate.shift(RIGHT * (stops[i] - np.array(box.get_center())[0])), rt=1.0)
            P(self, lamps[i].animate.set_color(TERRA), rt=0.3)

        until(self, "gets an Apply")
        P(self, Create(check(4.1, 0.9, s=0.26)), rt=0.4)
        finish(self)


# ── M4 — methods: what I have, what's tight ─────────────────────────────────────
class M4_Desk(Scene):
    def construct(self):
        # desk, legs and laptop base edged in deep kraft, not ink: connected ink edges fused them into one "text" blob
        # around the laptop screen and failed GATE T §8.6b (2026-11-24)
        desk = Rectangle(width=10.4, height=0.3, fill_color=BOX_R, fill_opacity=1, stroke_color=DEEP, stroke_width=4).move_to([-0.6, -1.55, 0])
        legs = VGroup(*[Rectangle(width=0.3, height=1.3, fill_color=BOX_L, fill_opacity=1, stroke_color=DEEP, stroke_width=4)
                        .move_to([x, -2.35, 0]) for x in (-5.4, 4.2)])
        P(self, GrowFromEdge(desk, LEFT), FadeIn(legs), rt=0.6)

        until(self, "the public data")
        data = doc(-4.2, -0.45, w=1.4, h=1.9)
        guard(self); data.shift(UP * 3.0); self.add(data)
        P(self, data.animate.shift(DOWN * 3.0), rt=0.6, rate_func=ease_in)
        P(self, FadeIn(T("public data", 34).move_to([-4.2, 1.0, 0])), rt=0.4)

        until(self, "the scripts")
        script = Iso(-2.25, -1.4, 0.6).mcp(0, 0, 0, w=1.3, d=1.3, h=0.8)
        guard(self); script.shift(UP * 3.0); self.add(script)
        P(self, script.animate.shift(DOWN * 3.0), rt=0.6, rate_func=ease_in)
        P(self, FadeIn(T("scripts", 34).move_to([-1.55, 0.55, 0])), rt=0.4)

        until(self, "eight-gigabyte")
        screen = RoundedRectangle(width=2.9, height=1.9, corner_radius=0.1, fill_color=DIM, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([1.9, -0.2, 0])
        base = Polygon([0.2, -1.4, 0], [3.6, -1.4, 0], [3.3, -1.2, 0], [0.5, -1.2, 0], fill_color=BOX_L, fill_opacity=1, stroke_color=DEEP, stroke_width=4)
        P(self, FadeIn(screen, shift=DOWN * 0.3), FadeIn(base), rt=0.5)
        P(self, FadeIn(T("8 GB", 40).move_to([1.9, 1.25, 0])), rt=0.4)

        until(self, "AI usage limits")
        track = RoundedRectangle(width=3.6, height=0.4, corner_radius=0.12, fill_color=BAR3, fill_opacity=1, stroke_width=0).move_to([3.4, 2.45, 0])
        P(self, FadeIn(track), FadeIn(T("AI usage limits", 34).move_to([-0.8, 2.45, 0])), rt=0.4)
        used = Rectangle(width=3.6, height=0.4, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([3.4, 2.45, 0])
        P(self, GrowFromEdge(used, LEFT), rt=1.0)

        until(self, "hit once")
        P(self, GrowFromCenter(Dot([5.45, 2.45, 0], radius=0.12, color=TERRA)), rt=0.3)
        finish(self)


# ── E1 — evaluation: precision, 52 of 64 now, target 58 (edit of the B08 gauge) ─
class E1_Gauge(Scene):
    def construct(self):
        GL, GW, GY = -4.0, 8.0, 0.0
        tiles = VGroup(*[Square(0.2, fill_color=BAR3, fill_opacity=1, stroke_width=0).move_to([GL + 0.1 + (i % 32) * 0.25, -2.15 + (i // 32) * 0.3, 0])
                         for i in range(64)])
        P(self, LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.01), rt=0.8)
        P(self, FadeIn(T("64 checked by hand", 34).move_to([0, -2.95, 0])), rt=0.4)

        until(self, "today the filter")
        track = RoundedRectangle(width=GW, height=0.5, corner_radius=0.14, fill_color=BAR3, fill_opacity=1, stroke_width=0).move_to([GL + GW / 2, GY, 0])
        P(self, FadeIn(track), rt=0.4)

        until(self, "fifty-two right")
        w = GW * 52 / 64
        fill = Rectangle(width=w, height=0.5, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([GL + w / 2, GY, 0])
        # grey, not ink: 52 packed ink tiles fuse under GATE T
        P(self, GrowFromEdge(fill, LEFT), *[tiles[i].animate.set_fill(BAR1) for i in range(52)], rt=0.9)
        P(self, FadeIn(T("52 of 64", 44).move_to([GL + w - 1.0, -0.75, 0])), rt=0.4)

        until(self, "My target")
        tx = GL + GW * 58 / 64
        mark = DashedLine([tx, -0.45, 0], [tx, 1.0, 0], color=INK, stroke_width=5, dash_length=0.12)
        P(self, Create(mark), rt=0.5)
        P(self, GrowFromCenter(Dot([tx, 1.15, 0], radius=0.1, color=TERRA)), rt=0.3)
        P(self, FadeIn(T("target 58", 40).move_to([tx - 0.6, 1.75, 0])), FadeIn(T("constructed", 32).move_to([tx - 0.6, 2.4, 0])), rt=0.4)
        finish(self)


# ── E3 — evaluation: what counts as not working, logged ─────────────────────────
class E3_Log(Scene):
    def construct(self):
        page = RoundedRectangle(width=4.6, height=4.4, corner_radius=0.14, fill_color=PAGE_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-1.2, 0.0, 0])
        rows = (1.0, -0.6)
        lines = VGroup(*[Line([-3.1, y + dy, 0], [0.2, y + dy, 0], color=GHOST, stroke_width=8) for y in rows for dy in (0.2, -0.2)])
        P(self, FadeIn(page), rt=0.4)
        P(self, LaggedStart(*[Create(l) for l in lines], lag_ratio=0.1), rt=0.6)
        P(self, FadeIn(T("run log", 36).move_to([-1.2, -2.7, 0])), rt=0.4)
        P(self, Create(check(0.55, rows[0], s=0.22)), rt=0.4)
        P(self, FadeIn(T("pass", 40).move_to([2.6, rows[0], 0])), rt=0.4)

        until(self, "or if a company")
        cross = VGroup(Line([0.35, rows[1] - 0.25, 0], [0.85, rows[1] + 0.25, 0], color=INK, stroke_width=7),
                       Line([0.35, rows[1] + 0.25, 0], [0.85, rows[1] - 0.25, 0], color=INK, stroke_width=7))
        P(self, Create(cross), rt=0.5)
        P(self, FadeIn(T("fail", 40).move_to([2.6, rows[1], 0])), rt=0.4)

        until(self, "logged, not hidden")
        P(self, GrowFromCenter(Dot([-3.28, rows[1], 0], radius=0.1, color=TERRA)), rt=0.3)
        finish(self)


# ── BOUT — the box comes back sealed: the title and the author ──────────────────
OBOX = Iso(-3.4, -1.9, 0.62)


class BOUT_Close(Scene):
    def construct(self):
        box = sealed(OBOX)
        box.shift(UP * 4.0); self.add(box)
        P(self, box.animate.shift(DOWN * 4.0), rt=0.8, rate_func=rate_functions.ease_out_bounce, m=0.1)
        P(self, FadeIn(floor_shadow(OBOX)), rt=0.2, m=0.1)
        P(self, FadeIn(T("PM Sponsor Check", 64).move_to([2.3, 0.5, 0])), rt=0.3, m=0.1)
        P(self, FadeIn(T("Kalyan Karnati", 44).move_to([2.3, -0.55, 0])), rt=0.3, m=0.1)
        finish(self)
