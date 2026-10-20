#!/usr/bin/env python3
"""heartbeat.py: did each tool leave its log for today?

An agent that did not run cannot report that it did not run, so the check lives outside the agents. A tool's log is any file
dated today (YYYY-MM-DD in its name) in logs/<tool>/. Prints the tools with no log and exits 1 if there are any. The alert goes
to an ops channel, never to the channel Professor Bear reads for judgment: wire that up where this runs (see
the plan in forms/PLAN.md: a scheduled GitHub Action at the repository root, not yet written).

  python3 compare/heartbeat.py                   # every folder under logs/
  python3 compare/heartbeat.py --date 2026-10-21 --tools muse grok-bot dots
"""
import argparse, datetime as dt, os, sys

LOGS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")


def missing(logs_dir, date, tools=None):
    tools = tools or sorted(d for d in os.listdir(logs_dir) if os.path.isdir(os.path.join(logs_dir, d))) if os.path.isdir(logs_dir) else (tools or [])
    out = []
    for t in tools:
        folder = os.path.join(logs_dir, t)
        have = [f for f in os.listdir(folder) if date in f] if os.path.isdir(folder) else []
        if not have:
            out.append(t)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", default=dt.date.today().isoformat()); ap.add_argument("--tools", nargs="*"); ap.add_argument("--logs", default=LOGS)
    a = ap.parse_args(argv)
    tools = a.tools or (sorted(d for d in os.listdir(a.logs) if os.path.isdir(os.path.join(a.logs, d))) if os.path.isdir(a.logs) else [])
    if not tools:
        print(f"{a.date}: no tool has a logs/ folder yet, so there is nothing to check (this is not a pass)")
        return 0
    m = missing(a.logs, a.date, tools)
    print(f"{a.date}: " + (f"every tool ({', '.join(tools)}) left a log" if not m else "NO LOG from " + ", ".join(m)))
    return 1 if m else 0


if __name__ == "__main__":
    raise SystemExit(main())
