#!/usr/bin/env python3
"""Static validation for a generated goal packet.

This does not prove the goal is complete. It checks whether the packet contains
execution machinery that helps a runner converge.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable

REQUIRED_LEAN = ["GOAL.md", "CHECKS.md", "PROGRESS.md", "STATE.md"]
STANDARD_EXTRA = ["PLAN.md", "CONSTRAINTS.md"]
REQUIRED_SECTIONS = {
    "GOAL.md": ["Objective", "Acceptance Criteria", "Stop / Report Conditions"],
    "CHECKS.md": ["Baseline Capture", "Evidence Freshness Rule", "Completion Audit"],
    "PROGRESS.md": ["Progress Entries", "Context Compression Rules"],
    "STATE.md": ["Current Verdict", "Next Best Action", "Active Blockers", "Latest Evidence"],
}
PLACEHOLDER_RE = re.compile(r"<[^>\n]{2,80}>")
SECRET_RE = re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{12,}")


def has_heading(text: str, heading: str) -> bool:
    return bool(re.search(rf"^##+\s+{re.escape(heading)}\s*$", text, re.MULTILINE))


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(errors="replace")


def add(result: list[tuple[str, str]], level: str, message: str) -> None:
    result.append((level, message))


def check_required_files(goal_dir: Path, files: Iterable[str], result: list[tuple[str, str]]) -> None:
    for name in files:
        if not (goal_dir / name).exists():
            add(result, "FAIL", f"Missing required file: {name}")


def check_sections(goal_dir: Path, result: list[tuple[str, str]]) -> None:
    for name, sections in REQUIRED_SECTIONS.items():
        path = goal_dir / name
        if not path.exists():
            continue
        text = read(path)
        for section in sections:
            if not has_heading(text, section):
                add(result, "WARN", f"{name} missing section heading: {section}")


def check_goal_size(goal_dir: Path, result: list[tuple[str, str]]) -> None:
    path = goal_dir / "GOAL.md"
    if not path.exists():
        return
    n = len(read(path))
    if n > 4000:
        add(result, "WARN", f"GOAL.md is {n} characters. Keep compact and put detail in other files.")
    else:
        add(result, "PASS", f"GOAL.md is compact at {n} characters.")


def check_placeholders(goal_dir: Path, result: list[tuple[str, str]]) -> None:
    for path in goal_dir.glob("*.md"):
        text = read(path)
        placeholders = PLACEHOLDER_RE.findall(text)
        if placeholders:
            sample = ", ".join(sorted(set(placeholders))[:5])
            add(result, "WARN", f"{path.name} still contains placeholders: {sample}")


def check_scripts(goal_dir: Path, result: list[tuple[str, str]]) -> None:
    script = goal_dir / "goal-check.sh"
    commands = goal_dir / "checks" / "commands.txt"
    if script.exists() and commands.exists():
        add(result, "PASS", "Validation harness present: goal-check.sh and checks/commands.txt")
    elif script.exists() or commands.exists():
        add(result, "WARN", "Partial validation harness present. Include both goal-check.sh and checks/commands.txt.")
    else:
        add(result, "INFO", "No validation harness found. Fine for lean packets, but substantive goals should include one.")


def check_proof(goal_dir: Path, result: list[tuple[str, str]]) -> None:
    proof_dir = goal_dir / "proof"
    text = "\n".join(read(p) for p in goal_dir.glob("*.md") if p.exists())
    visual_requested = any(word in text.lower() for word in ["screenshot", "visual proof", "ux review", "browser"])
    if visual_requested and not proof_dir.exists():
        add(result, "FAIL", "Visual proof appears required, but proof/ directory is missing.")
    elif visual_requested and not (proof_dir / "README.md").exists():
        add(result, "WARN", "Visual proof appears required, but proof/README.md is missing.")


def check_secret_patterns(goal_dir: Path, result: list[tuple[str, str]]) -> None:
    for path in list(goal_dir.glob("*.md")) + list((goal_dir / "proof").rglob("*") if (goal_dir / "proof").exists() else []):
        if not path.is_file() or path.stat().st_size > 2_000_000:
            continue
        text = read(path)
        if SECRET_RE.search(text):
            add(result, "FAIL", f"Potential secret-like value found in {path.relative_to(goal_dir)}")


def print_report(result: list[tuple[str, str]]) -> int:
    order = {"FAIL": 0, "WARN": 1, "INFO": 2, "PASS": 3}
    result.sort(key=lambda item: (order.get(item[0], 9), item[1]))
    print("# Goal Pack Validation")
    print()
    for level, message in result:
        print(f"- {level}: {message}")
    print()
    failures = sum(1 for level, _ in result if level == "FAIL")
    warnings = sum(1 for level, _ in result if level == "WARN")
    print(f"Summary: {failures} failure(s), {warnings} warning(s).")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate goal packet structure.")
    parser.add_argument("goal_dir", nargs="?", default=".", help="Goal packet directory")
    parser.add_argument("--standard", action="store_true", help="Require standard packet files")
    args = parser.parse_args()

    goal_dir = Path(args.goal_dir).resolve()
    if not goal_dir.exists():
        print(f"Goal directory does not exist: {goal_dir}", file=sys.stderr)
        return 2

    result: list[tuple[str, str]] = []
    check_required_files(goal_dir, REQUIRED_LEAN, result)
    if args.standard:
        check_required_files(goal_dir, STANDARD_EXTRA, result)
    check_sections(goal_dir, result)
    check_goal_size(goal_dir, result)
    check_placeholders(goal_dir, result)
    check_scripts(goal_dir, result)
    check_proof(goal_dir, result)
    check_secret_patterns(goal_dir, result)
    return print_report(result)


if __name__ == "__main__":
    raise SystemExit(main())
