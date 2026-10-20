"""lectern_paths.py: where things are, in one place.

Every script asks this module for its rule files, its run folder and its sibling scripts, instead of guessing from
its own location. That is why the code can live in folders (config/, collect/, publish/, audit/) in the master and
still run unchanged in the other two classes' copies, which keep everything in one flat folder: config() looks in
config/ first and then beside this file, and the sibling folders are added to the import path only if they exist.

Put a copy of this file next to the scripts, import it first, and ask it:  lectern_paths.config("keywords.json").
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))          # lectern/ (structured) or the flat class folder
RUNS = os.path.join(ROOT, "runs")
MONITOR_DB = os.path.join(ROOT, "monitor.db")               # the big-four collectors' local database (never tracked)
CACHE = os.path.join(ROOT, "cache")
FACULTY_RUNS = os.path.normpath(os.path.join(ROOT, "..", "faculty-runs"))   # belongs to the class that runs it; never synced


def config(name):
    """The path of a rule or watch-list file: config/<name> if that folder exists, else beside this file."""
    for folder in (os.path.join(ROOT, "config"), ROOT):
        p = os.path.join(folder, name)
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f"{name} not found in {os.path.join(ROOT, 'config')} or {ROOT}")


for _sub in ("collect", "publish", "audit"):                # so `import notify` works from any script, in either layout
    _p = os.path.join(ROOT, _sub)
    if os.path.isdir(_p) and _p not in sys.path:
        sys.path.insert(0, _p)
