#!/usr/bin/env python3
"""Build or refresh proof/README.md for a goal packet."""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
LOG_EXTS = {".log", ".txt", ".md", ".json", ".xml"}


def rel(path: Path, base: Path) -> str:
    return path.relative_to(base).as_posix()


def main() -> int:
    parser = argparse.ArgumentParser(description="Build proof/README.md for a goal packet.")
    parser.add_argument("goal_dir", nargs="?", default=".", help="Goal packet directory")
    parser.add_argument("--verdict", default="Pending review", help="Final verdict text")
    args = parser.parse_args()

    goal_dir = Path(args.goal_dir).resolve()
    proof_dir = goal_dir / "proof"
    proof_dir.mkdir(parents=True, exist_ok=True)

    images = sorted(p for p in proof_dir.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_EXTS)
    logs = sorted(p for p in proof_dir.rglob("*") if p.is_file() and p.suffix.lower() in LOG_EXTS and p.name != "README.md")
    artifacts = sorted(p for p in proof_dir.rglob("*") if p.is_file() and p not in images and p not in logs and p.name != "README.md")

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = [
        "# Proof Packet",
        "",
        f"Generated: {stamp}",
        "",
        "## Final Verdict",
        "",
        args.verdict,
        "",
        "## Acceptance Criteria Evidence",
        "",
        "| AC | Evidence | Why This Proves It |",
        "| --- | --- | --- |",
        "| `<AC>` | `<path>` | `<explanation>` |",
        "",
        "## Screenshots",
        "",
        "| File | State | What To Inspect | Redaction Reviewed? |",
        "| --- | --- | --- | --- |",
    ]

    if images:
        for image in images:
            lines.append(f"| `{rel(image, goal_dir)}` | `<state>` | `<visual signal>` | NO |")
    else:
        lines.append("| None found | N/A | N/A | N/A |")

    lines.extend(["", "## Logs", "", "| File | Command | Result |", "| --- | --- | --- |"])
    if logs:
        for log in logs:
            lines.append(f"| `{rel(log, goal_dir)}` | `<command>` | `<PASS/FAIL>` |")
    else:
        lines.append("| None found | N/A | N/A |")

    lines.extend(["", "## Artifacts", "", "| File | Contract | Validation |", "| --- | --- | --- |"])
    if artifacts:
        for artifact in artifacts:
            lines.append(f"| `{rel(artifact, goal_dir)}` | `<required properties>` | `<check>` |")
    else:
        lines.append("| None found | N/A | N/A |")

    lines.extend([
        "",
        "## Reviewer Notes",
        "",
        "- Review this index against CHECKS.md before claiming completion.",
        "- Replace placeholder AC rows with the actual acceptance criteria evidence.",
    ])

    out = proof_dir / "README.md"
    out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
