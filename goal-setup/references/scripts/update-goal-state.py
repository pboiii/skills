#!/usr/bin/env python3
"""Update STATE.md for a goal packet.

This helper keeps the resume capsule current without forcing the runner to edit
large progress logs by hand.

Examples:
  python update-goal-state.py . --verdict "M1 complete; final tests pending" --next "Run goal-check.sh final"
  python update-goal-state.py . --blocker "Missing STAGING_API_KEY" --evidence "proof/logs/latest-summary.md"
"""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
from typing import Iterable

SECTIONS = [
    "Current Verdict",
    "Next Best Action",
    "Validated So Far",
    "Not Yet Validated",
    "Active Blockers",
    "Files Touched",
    "Latest Evidence",
    "Resume Instructions",
]

PLACEHOLDER_MARKERS = ("<", "`<")

TEMPLATE = """# Goal State

Last updated: {timestamp}

## Current Verdict

Not started.

## Next Best Action

Read GOAL.md and CHECKS.md, then capture baseline validation.

## Validated So Far

- None yet.

## Not Yet Validated

- Baseline validation.
- Final acceptance criteria evidence.

## Active Blockers

- None recorded.

## Files Touched

| File | Reason | Status |
| --- | --- | --- |

## Latest Evidence

- None yet.

## Resume Instructions

Start by reading this file, then CHECKS.md, then continue from the next best action.
"""


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def split_sections(text: str) -> dict[str, str]:
    parts: dict[str, str] = {"_preamble": ""}
    current = "_preamble"
    buf: list[str] = []

    for line in text.splitlines():
        if line.startswith("## "):
            parts[current] = "\n".join(buf).strip()
            current = line[3:].strip()
            buf = []
        else:
            buf.append(line)
    parts[current] = "\n".join(buf).strip()
    return parts


def bullet_items(values: Iterable[str]) -> str:
    return "\n".join(f"- {v}" for v in values if v)


def is_placeholder_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith("- "):
        body = stripped[2:].strip()
        return body.startswith(PLACEHOLDER_MARKERS)
    if stripped.startswith("|"):
        cells = [cell.strip().strip("`") for cell in stripped.strip("|").split("|")]
        return any(cell.startswith("<") and cell.endswith(">") for cell in cells)
    return False


def drop_placeholder_lines(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not is_placeholder_line(line)).strip()


def append_bullets(existing: str, values: list[str]) -> str:
    cleaned = drop_placeholder_lines(existing)
    filtered = [v for v in values if v]
    if not filtered:
        return cleaned
    if not cleaned or cleaned == "- None yet.":
        return bullet_items(filtered)
    return cleaned + "\n" + bullet_items(filtered)


def append_files(existing: str, rows: list[str]) -> str:
    if not rows:
        return drop_placeholder_lines(existing)
    lines = [line.rstrip() for line in existing.splitlines() if line.strip() and not is_placeholder_line(line)]
    if not lines:
        lines = ["| File | Reason | Status |", "| --- | --- | --- |"]
    for row in rows:
        parts = row.split(":", 2)
        while len(parts) < 3:
            parts.append("")
        file_path, reason, status = [p.strip() for p in parts]
        lines.append(f"| `{file_path}` | {reason or 'updated'} | {status or 'changed'} |")
    return "\n".join(lines)


def render(parts: dict[str, str]) -> str:
    lines = ["# Goal State", "", f"Last updated: {now()}", ""]
    for section in SECTIONS:
        lines.extend([f"## {section}", "", parts.get(section, "").strip() or "- None recorded.", ""])
    return "\n".join(lines).rstrip() + "\n"


def default_resume(next_action: str) -> str:
    return f"Start by reading this file, then CHECKS.md, then continue from: {next_action}."


def main() -> int:
    parser = argparse.ArgumentParser(description="Update STATE.md for a goal packet.")
    parser.add_argument("goal_dir", nargs="?", default=".", help="Goal packet directory")
    parser.add_argument("--verdict", help="Replace Current Verdict")
    parser.add_argument("--next", dest="next_action", help="Replace Next Best Action")
    parser.add_argument("--validated", action="append", default=[], help="Append a Validated So Far bullet")
    parser.add_argument("--not-validated", action="append", default=[], help="Append a Not Yet Validated bullet")
    parser.add_argument("--blocker", action="append", default=[], help="Append an Active Blocker bullet")
    parser.add_argument("--evidence", action="append", default=[], help="Append a Latest Evidence bullet")
    parser.add_argument("--file", action="append", default=[], help="Append file row as path:reason:status")
    parser.add_argument("--resume", help="Replace Resume Instructions")
    args = parser.parse_args()

    goal_dir = Path(args.goal_dir).resolve()
    state_path = goal_dir / "STATE.md"
    if state_path.exists():
        text = state_path.read_text(encoding="utf-8")
    else:
        text = TEMPLATE.format(timestamp=now())

    parts = split_sections(text)
    if args.verdict:
        parts["Current Verdict"] = args.verdict
    if args.next_action:
        parts["Next Best Action"] = args.next_action
    if args.resume:
        parts["Resume Instructions"] = args.resume
    elif args.next_action and "<next action>" in parts.get("Resume Instructions", ""):
        parts["Resume Instructions"] = default_resume(args.next_action)

    parts["Validated So Far"] = append_bullets(parts.get("Validated So Far", ""), args.validated)
    parts["Not Yet Validated"] = append_bullets(parts.get("Not Yet Validated", ""), args.not_validated)
    parts["Active Blockers"] = append_bullets(parts.get("Active Blockers", ""), args.blocker)
    parts["Latest Evidence"] = append_bullets(parts.get("Latest Evidence", ""), args.evidence)
    parts["Files Touched"] = append_files(parts.get("Files Touched", ""), args.file)

    state_path.write_text(render(parts), encoding="utf-8")
    print(f"Updated {state_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
