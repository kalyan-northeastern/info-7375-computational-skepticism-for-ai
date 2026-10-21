#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for pm-sponsor-check-pitch (show-tell).

Final-project pitch film for INFO 7375, Fall 2026, narrated as Kalyan Karnati.
Built from BEAT-PLAN.md and PROJECT-BRIEF.md with the show-tell skill, with these
assignment overrides: the narrator is Kalyan Karnati (the house narrator persona and its sign-off
are dropped), the voice is Kokoro af_heart (not the house default voice), and the house outro is
not used. BOUT is a drawn Manim close because ClaudeTitleOutro hard-codes the house handle on screen.

Every number comes from the 2026-10-09 run log
(the-reallocation-engine/logs/runs/2026fa-kalyan-karnati-1.md); see FACTCHECK.md.
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


B = [
 beat("B00", "What I will build is a repository: a recipe that says what to check, a scan script, a labelled test set, "
             "and an evaluation log, added to the Reallocation Engine.",
      "B00_Repo", "An open kraft box drops onto the floor; a recipe page, a dark script block and a test-set tray drop into it. Labelled 'constructed'.",
      [{"at": 0.1, "event": "box drops"}, {"at": 0.35, "event": "recipe"}, {"at": 0.5, "event": "script"}, {"at": 0.65, "event": "test set"}]),
 beat("B01", "Part of it already exists. On October ninth, I ran a first version on the repository's public data. "
             "Over thirty thousand companies went in. Three hundred fifty-two possible health sponsors came out.",
      "B01_Gate", "A wide grid of crates slides through an ink gate; a small stack lands on the other side.",
      [{"at": 0.2, "event": "crates + gate"}, {"at": 0.55, "event": "30,369"}, {"at": 0.8, "event": "352 stack lands"}]),
 beat("B02", "On that run, only nine of those three hundred fifty-two listed a product manager title among their top "
             "sponsored job titles, and none of those titles was entry level.",
      "B02_Nine", "352 crate tops in rows; a scan line sweeps; nine light up; the hero number '9 of 352' lands.",
      [{"at": 0.1, "event": "352 rows"}, {"at": 0.3, "event": "scan"}, {"at": 0.6, "event": "9 of 352"}]),
 beat("B03", "A filter on health industry categories would have missed the sixty-four sponsors that filed under "
             "technology and other categories instead, including digital-health companies I would actually apply to.",
      "B03_Filter", "A funnel marked 'health filter'; a row of crates slides off its side and lands under a second sign, '64'.",
      [{"at": 0.15, "event": "funnel"}, {"at": 0.45, "event": "crates slide off"}, {"at": 0.75, "event": "64"}]),
 beat("B04", "On October ninth, I compared this with two things. The first was the Reallocation Engine's own sponsorship "
             "scorer. It rated each company's sponsorship as one tier, but never asked whether that company sponsored "
             "product managers. Mine will show product-manager evidence separately.",
      "B04_Scorer", "Two windows: the engine scorer's row grows one tier bar; my row grows the same bar plus a separate PM chip with a check.",
      [{"at": 0.2, "event": "two windows"}, {"at": 0.45, "event": "tier bar"}, {"at": 0.85, "event": "PM chip + check"}]),
 beat("B05", "The second was Built In Boston's job listings. They still showed copies of Cohere Health roles marked removed, "
             "while the live role sat on Cohere's own job board. Mine will check each posting on the company's own board.",
      "B05_Board", "Left window 'Built In': job cards greyed with a cross. Right, the company's own board: one live card; a check lands.",
      [{"at": 0.15, "event": "Built In window"}, {"at": 0.4, "event": "removed copies"}, {"at": 0.6, "event": "live card"}, {"at": 0.85, "event": "check"}]),
 beat("B06", "The reader I'm building for is a hiring manager for a product role. In the first minute, they open one card "
             "listing what the tool can and cannot verify, then one run log showing a check catching a real error.",
      "B06_Reader", "A reader figure beside the box; the lid lifts; a card and a run-log page rise; a check lands on the log.",
      [{"at": 0.15, "event": "reader"}, {"at": 0.4, "event": "card rises"}, {"at": 0.75, "event": "run log + check"}]),
 beat("B07", "Here's that error. On my October ninth run, the scorer marked postings nobody had checked as checked. "
             "Even after I fixed the labels, the two roles I couldn't check still ranked above the ones I had. "
             "Catching that is the skill this project is about: verifying output instead of trusting it.",
      "B07_Error", "A two-row ranking: the unchecked card sits on top with a false grey check; a scan line sweeps it and the false check is struck.",
      [{"at": 0.15, "event": "ranking"}, {"at": 0.3, "event": "false check"}, {"at": 0.75, "event": "scan + strike"}]),
 beat("B08", "It will not tell anyone which job code an employer will file, and it will not give immigration advice. "
             "The first piece will be a tighter health-keyword filter, tested against the sixty-four matches I reviewed "
             "with evidence. Today's filter gets fifty-two right; the evaluation log will show the change.",
      "B08_Scope", "A fence; two items stay outside it; the box moves forward; a gauge fills to 52 / 64 beside an empty after-gauge labelled 'constructed'.",
      [{"at": 0.15, "event": "fence, out"}, {"at": 0.45, "event": "box forward"}, {"at": 0.8, "event": "52 of 64"}]),
 beat("B09", "The risk is the full government filing data, the only way to confirm product-manager sponsorship. It is large, "
             "and job titles are inconsistent. If I can't match it in time, I will limit it to the most recent fiscal year "
             "published, for Massachusetts employers only, and say so in the log.",
      "B09_Risk", "A tall messy stack of filing pages wobbles; a thin slice slides off to the right, labelled '1 year · MA', 'constructed'.",
      [{"at": 0.15, "event": "stack"}, {"at": 0.4, "event": "wobble"}, {"at": 0.7, "event": "slice"}]),
 beat("B10", "Why this project? It's a mix. Product management in health tech is something I've done, in my internship at "
             "Andor Health, and you can see that thinking in the health-tech recipe I submitted on October ninth. "
             "Python data pipelines, test sets, and verification gates are what I'm learning.",
      "B10_Skills", "Two shelves: one box sits on 'have'; three boxes drop onto 'learning' one by one.",
      [{"at": 0.2, "event": "have"}, {"at": 0.75, "event": "learning boxes"}]),
]

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

BEATS = OPEN + B + [YOURTURN, OUTRO]

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
    "source_doc": "final-project-film/BEAT-PLAN.md + PROJECT-BRIEF.md; numbers from the-reallocation-engine/logs/runs/2026fa-kalyan-karnati-1.md (2026-10-09)",
    "playlist": "INFO 7375 Final Project Pitches", "chapter_number": 0,
    "tags": ["H-1B", "product management", "health tech", "Reallocation Engine", "INFO 7375", "Kalyan Karnati"]},
    "beats": BEATS}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(len(BEATS), "beats; est", round(sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in BEATS)), "s")
