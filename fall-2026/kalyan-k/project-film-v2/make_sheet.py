#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for pm-sponsor-check-pitch (show-tell).

Final-project pitch film for INFO 7375, Fall 2026, narrated as Kalyan Karnati.
Built from BEAT-PLAN.md and PROJECT-BRIEF.md with the show-tell skill, with these
assignment overrides: the narrator is Kalyan Karnati (the house narrator persona and its sign-off
are dropped), the voice is Kokoro af_heart (not the house default voice), and the house outro is
not used. BOUT is a drawn Manim close because ClaudeTitleOutro hard-codes the house handle on screen.

Every number comes from the 2026-10-09 run log
(the-reallocation-engine/logs/runs/2026fa-kalyan-karnati-1.md); see FACTCHECK.md.
v2 (2026-11-24): restructured into the four parts of BEAT-PLAN-v2.md.
Re-run after any edit:  python3 make_sheet.py   (keeps measured audio durations).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "pm-sponsor-check-pitch"
TITLE = "PM Sponsor Check"
AUTHOR = "Kalyan Karnati"
VOICE = "af_heart"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": VOICE, "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": VOICE, "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


# v2 (2026-11-24): four parts from BEAT-PLAN-v2.md, in order: executive summary, introduction (prior work),
# methods, evaluation. A reused scene keeps its v1 beat id (its class name, clip and pacing are keyed to it);
# "v2_id" is the BEAT-PLAN-v2 label. New / edited scenes take their v2 id as the beat id.
def tag(b, part, v2_id, status):
    b.update({"part": part, "v2_id": v2_id, "v2_status": status})
    return b


SUMMARY = [
 tag(beat("S1", "I'm building PM Sponsor Check: a tool that tells an early-career product manager which health-tech "
               "employers have public evidence of sponsoring product managers, not just engineers, and labels every "
               "answer as a record or a guess.",
      "S1_Box", "The open kraft box drops onto the floor; a scan block, an evidence page and a record-or-guess tray drop into it. Labelled 'constructed'.",
      [{"at": 0.1, "event": "box drops"}, {"at": 0.3, "event": "scan block"}, {"at": 0.55, "event": "evidence page"}, {"at": 0.8, "event": "record · guess tray"}]),
     "1 executive summary", "S1", "EDIT of B00"),
 tag(beat("B02", "It matters because the usual check misleads. On my first run, only nine of three hundred fifty-two "
                "possible health sponsors listed a product manager title among their top sponsored roles, and none of "
                "those titles was entry level.",
      "B02_Nine", "352 crate tops in rows; a scan line sweeps; nine light up; the hero number '9 of 352' lands.",
      [{"at": 0.1, "event": "352 rows"}, {"at": 0.3, "event": "scan"}, {"at": 0.6, "event": "9 of 352"}]),
     "1 executive summary", "S2", "REUSE B02"),
]

INTRO = [
 tag(beat("I1A", "Two public tools already exist. The government's H-1B Employer Data Hub counts petitions by company, "
                "industry and year, but not by job title, so it can't tell me who sponsors product managers.",
      "I1A_DataHub", "Two ink windows, 'Data Hub' and 'MyVisaJobs'. Data Hub grows company, industry and year columns; "
                     "an empty dashed slot appears where a job-title column would be.",
      [{"at": 0.1, "event": "two windows"}, {"at": 0.45, "event": "Data Hub columns"}, {"at": 0.75, "event": "empty title slot"}]),
     "2 introduction", "I1A", "NEW (split of I1)"),
 tag(beat("I1B", "MyVisaJobs goes further: I can search by job title and see wage levels. What neither does is check "
                "whether a posting is still open, or label which answers are records and which are guesses. That's what mine adds.",
      "I1B_Missing", "Continues from I1A: MyVisaJobs grows title rows and wage bars; both windows get an empty dashed lamp; "
                     "a third window, 'mine', arrives with a live card, a terracotta lamp and a check, labelled 'constructed'.",
      [{"at": 0.1, "event": "title rows"}, {"at": 0.3, "event": "wage bars"}, {"at": 0.55, "event": "empty lamps"},
       {"at": 0.85, "event": "mine: lamp + check"}]),
     "2 introduction", "I1B", "NEW (split of I1)"),
 tag(beat("B04", "The Reallocation Engine I'm building on rates each company's sponsorship as one tier, like \"Likely,\" "
                "for the whole company, not for a role.",
      "B04_Scorer", "Two windows: the engine scorer's row grows one tier bar; my row grows the same bar plus a separate PM chip with a check.",
      [{"at": 0.2, "event": "two windows"}, {"at": 0.45, "event": "tier bar"}, {"at": 0.85, "event": "PM chip + check"}]),
     "2 introduction", "I2", "REUSE B04"),
 tag(beat("B05", "Job boards keep stale copies: on my second run, Built In Boston still listed copies of Cohere Health "
                "roles marked removed, while the live role sat on Cohere's own board.",
      "B05_Board", "Left window 'Built In': job cards greyed with a cross. Right, the company's own board: one live card; a check lands.",
      [{"at": 0.15, "event": "Built In window"}, {"at": 0.4, "event": "removed copies"}, {"at": 0.6, "event": "live card"}, {"at": 0.85, "event": "check"}]),
     "2 introduction", "I3", "REUSE B05"),
 tag(beat("B03", "And filtering by health industry would have quietly dropped sixty-four sponsors filed under technology "
                "and other categories. That's why mine is worth building: it checks the role, not just the company.",
      "B03_Filter", "A funnel marked 'health filter'; a row of crates slides off its side and lands under a second sign, '64'.",
      [{"at": 0.15, "event": "funnel"}, {"at": 0.45, "event": "crates slide off"}, {"at": 0.75, "event": "64"}]),
     "2 introduction", "I4", "REUSE B03"),
]

METHODS = [
 tag(beat("B01", "The data is public. I start from the repository's 80 Days to Stay table, which joins SEC Form D filings, "
                "which report funding, with H-1B records from the Labor Department and U S C I S, for about thirty "
                "thousand companies.",
      "B01_Gate", "A wide grid of crates slides through an ink gate; a small stack lands on the other side.",
      [{"at": 0.2, "event": "crates + gate"}, {"at": 0.55, "event": "30,369"}, {"at": 0.8, "event": "352 stack lands"}]),
     "3 methods", "M1", "REUSE B01"),
 tag(beat("M2", "Step one, the health industry category and a keyword filter find possible health companies. Step two, "
               "a scan reads each one's sponsored job titles for product roles. Step three, a liveness check confirms "
               "the posting is still open before anything gets an Apply.",
      "M2_Steps", "One conveyor with three gates, numbered 1 to 3 in ink: filter, title scan, liveness. A crate rides through each "
                  "gate in turn; after gate 3 an 'Apply' pill and a check land. Gate 3 is labelled 'constructed'.",
      [{"at": 0.1, "event": "conveyor + gates"}, {"at": 0.25, "event": "gate 1 filter"}, {"at": 0.5, "event": "gate 2 title scan"},
       {"at": 0.75, "event": "gate 3 liveness"}, {"at": 0.9, "event": "Apply + check"}]),
     "3 methods", "M2", "NEW"),
 tag(beat("B09", "Step four will add the full Labor Department filing data, the only way to confirm product-manager "
                "sponsorship beyond a top-titles list. It's large and messy, so I'll start with one fiscal year, the most "
                "recent complete one, and say so in the log.",
      "B09_Risk", "A tall messy stack of filing pages wobbles; a thin slice slides off to the right, labelled '1 year', 'constructed'.",
      [{"at": 0.15, "event": "stack"}, {"at": 0.4, "event": "wobble"}, {"at": 0.7, "event": "slice"}]),
     "3 methods", "M3", "REUSE B09"),
 tag(beat("M4", "What I have: the public data, the scripts, and a free local pipeline. What's tight: an eight-gigabyte "
               "laptop, which already forced me to render this film at ten-eighty p, and AI usage limits, which I "
               "hit once while I was setting up the engine.",
      "M4_Desk", "A small desk: a data page, a key and a laptop land on it; then the laptop's memory bar fills and a usage gauge fills to its end.",
      [{"at": 0.1, "event": "desk"}, {"at": 0.2, "event": "data page, key, laptop"}, {"at": 0.6, "event": "8 GB bar full"},
       {"at": 0.85, "event": "usage gauge full"}]),
     "3 methods", "M4", "NEW"),
 tag(beat("B08", "It will not say which job code an employer will file, and it will not give immigration advice.",
      "B08_Scope", "A fence with the sealed box inside; a dark job-code block and an advice page land outside it, labelled 'out'; the box moves forward.",
      [{"at": 0.1, "event": "fence + box"}, {"at": 0.3, "event": "job-code block, out"}, {"at": 0.7, "event": "advice page"}, {"at": 0.9, "event": "box forward"}]),
     "3 methods", "M5", "REUSE B08"),
]

EVAL = [
 tag(beat("E1", "First, precision. I hand-checked sixty-four keyword matches; today the filter gets fifty-two right, "
               "eighty-one percent. It works if the tightened filter beats that on the same sixty-four, measured by one "
               "logged command. My target is at least fifty-eight of sixty-four.",
      "E1_Gauge", "The gauge from B08: it fills to 52 / 64; a dashed target mark drops in at 58 / 64, labelled 'constructed'.",
      [{"at": 0.1, "event": "gauge track"}, {"at": 0.3, "event": "fills to 52 of 64"}, {"at": 0.85, "event": "target mark 58"}]),
     "4 evaluation", "E1", "EDIT of B08 gauge"),
 tag(beat("B07", "Second, honesty of the ranking. On my first run the scorer marked unchecked postings as checked. It "
                "works if no unchecked posting ever ranks above a checked one, and the log proves it.",
      "B07_Error", "A two-row ranking: the unchecked card sits on top with a false grey check; a scan line sweeps it and the false check is struck.",
      [{"at": 0.15, "event": "ranking"}, {"at": 0.3, "event": "false check"}, {"at": 0.75, "event": "scan + strike"}]),
     "4 evaluation", "E2", "REUSE B07"),
 tag(beat("E3", "It didn't work if any Apply goes out without a liveness check, or if a company is called a PM sponsor "
               "without a filing record behind it. Either one counts as a failure, logged, not hidden.",
      "E3_Log", "A run-log page: a pass row with a check, then a fail row with a cross; a terracotta dot marks the logged failure.",
      [{"at": 0.1, "event": "run log page"}, {"at": 0.3, "event": "pass row"}, {"at": 0.6, "event": "fail row + cross"}, {"at": 0.9, "event": "logged"}]),
     "4 evaluation", "E3", "NEW"),
]

B = SUMMARY + INTRO + METHODS + EVAL
# Dropped from v1: B00 (replaced by S1), B06 (reader), B10 (why this project). Their v1 audio and clips stay on disk.

OPEN = [
 remotion("BIDEA", "the question",
    "Hello. I'm Kalyan Karnati, and this is the pitch for my final project. The usual question is which health-tech "
    "companies sponsor visas. For an early-career product manager, the real question is which ones sponsor product managers.",
    "BrutalistHesitantWriter",
    {"text": "Which health-tech companies\nsponsor visas", "triggerWords": "sponsor visas",
     "replacementWords": "sponsor product managers",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Which health-tech companies sponsor visas'"},
     {"at": 0.6, "event": "backspaces 'sponsor visas' → 'sponsor product managers' on the spoken correction"}],
    lead_silence_s=0.8,
    motion_claim="The writer types the usual visa question and corrects it to the real one: sponsoring product managers.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "An H-1B sponsor is an employer that files work-visa petitions. A SOC code is the government's job category for a "
    "role. A liveness check asks whether a job posting is still open.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "H-1B sponsor", "meaning": "an employer that files work-visa petitions"},
               {"term": "SOC code", "meaning": "the government's job category for a role"},
               {"term": "liveness check", "meaning": "asks whether a job posting is still open"}],
     "folderLabel": AUTHOR},
    [{"at": 0.1, "event": "'H-1B sponsor' lands"}, {"at": 0.4, "event": "'SOC code' lands"}, {"at": 0.7, "event": "'liveness check' lands"}],
    gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here is a company's list of sponsored job titles: [paste the list]. Does it show evidence of sponsoring "
             "my target role? Label each answer as either taken from the list or a guess.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: \"" + YT_PROMPT + "\" Then check two things: did it say \"not listed\" rather "
    "than \"never sponsored\", and did it label its guesses?",
    "ClaudeComposerAsk",
    # the composer is a mock-up: "CONSTRUCTED" rides in topic, the component's only small-label slot
    {"greeting": "Your turn.", "topic": "PM SPONSOR CHECK · YOUR TURN · CONSTRUCTED", "segment": "Check One Company's Titles",
     "command": YT_PROMPT, "runningText": "paste this into Claude…",
     "output": ["Check: it says “not listed”, not “never sponsored”.", "Check: every guess is labelled as a guess."],
     "folderLabel": AUTHOR, "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

OUTRO = {"beat_id": "BOUT", "act": "outro", "lane": "manim", "proof_gate": "SHOW",
         "narration_text": f"{TITLE}. By {AUTHOR}.", "estimated_duration_s": 4.0, "voice": VOICE, "engine": "kokoro",
         "shot": {"type": "GRAPHIC", "source": "own", "manim": {"class": "BOUT_Close"},
                  "visual_intent": "The film's box, sealed with tape, drops in; the title and the author's name land beside it.",
                  "show": [{"at": 0.0, "event": "box drops"}, {"at": 0.3, "event": "title"}, {"at": 0.6, "event": "name"}],
                  "motion_claim": "The box from B00 comes back sealed: the project, signed by its author."},
         "kind": "outro_voice", "tail_silence_s": 1.0,
         "outro_override": "Assignment requires the author's own close: ClaudeTitleOutro hard-codes the house handle, so BOUT is drawn in Manim."}

SPARSE_REASON = ("show-tell style: one drawn object or scene on a cream stage per beat, minimal labels, with the voice "
                 "carrying the explanation. The negative space is the style, so only underfill and clustered are waived; "
                 "edge-bleed, empty-frame and contrast still apply.")
FILLS = {"B02"}   # the 352-crate grid fills the frame on its own
for b in B + [OUTRO]:
    if b["beat_id"] not in FILLS:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

for b in OPEN:
    tag(b, "1 executive summary", b["beat_id"], "REUSE")
tag(YOURTURN, "4 evaluation", "BHTF", "REUSE")
tag(OUTRO, "4 evaluation", "BOUT", "REUSE")
# v2 (2026-11-24): BHTF (Your Turn) dropped at Kalyan's request: it is not one of the four parts, and the cut
# comes in under 4 minutes without it. YOURTURN stays defined above so the v1 film can be rebuilt.
BEATS = OPEN + B + [OUTRO]

# Carry measured audio forward (show-tell trap: make_sheet must keep audio_file + actual_duration_s).
old_path = HERE / "beat_sheet.json"
if old_path.exists():
    old = {b["beat_id"]: b for b in json.loads(old_path.read_text(encoding="utf-8")).get("beats", [])}
    for b in BEATS:
        o = old.get(b["beat_id"], {})
        if o.get("narration_text") == b["narration_text"]:
            for k in ("audio_file", "actual_duration_s"):
                if k in o:
                    b[k] = o[k]
# Sized-from-audio props.
for b in BEATS:
    rem = (b.get("shot") or {}).get("remotion")
    if rem and b["beat_id"] in ("BIDEA", "BDEFS", "BHTF") and b.get("actual_duration_s"):   # compile centre-cuts a clip longer than its audio
        rem["props"]["durationSeconds"] = b["actual_duration_s"]

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "PM SPONSOR CHECK", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "kalyan-karnati", "channel_title": AUTHOR, "persona": f"{AUTHOR} (narrating as self)",
    "author": "Kalyan Venkata Swamy Karnati",
    "voice": VOICE, "voice_kokoro": VOICE, "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9",
    "width": 3840, "height": 2160, "caption_policy": "none", "greeting_language": "English (Hello)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style: opens on the hesitant writer + terms card, no verdict card; Your Turn is the Claude.ai composer.",
    "assignment_overrides": [
        "narrator is Kalyan Karnati: house narrator persona and its sign-off dropped",
        "Kokoro voice af_heart instead of the house default voice",
        "house outro not used: BOUT is a drawn Manim close signed by the author"],
    "audience": "INFO 7375 reviewers and hiring managers for early-career product roles in health tech",
    "source_doc": "BEAT-PLAN-v2.md (four parts; v1 was BEAT-PLAN.md) + PROJECT-BRIEF.md; numbers from the-reallocation-engine/logs/runs/2026fa-kalyan-karnati-1.md (2026-10-09)",
    "playlist": "INFO 7375 Final Project Pitches", "chapter_number": 0,
    "tags": ["H-1B", "product management", "health tech", "Reallocation Engine", "INFO 7375", "Kalyan Karnati"]},
    "beats": BEATS}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(len(BEATS), "beats; est", round(sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in BEATS)), "s")
