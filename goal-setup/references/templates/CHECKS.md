# Checks

## Validation Harness

For substantive goals, create and run:

```bash
bash ./goal-check.sh baseline
bash ./goal-check.sh milestone-M1
bash ./goal-check.sh final
```

The latest harness summary must be linked from `PROGRESS.md` and reflected in `STATE.md`.

## Baseline Capture

Before implementation, run the relevant validation commands and record the current state.

| Check | Command | Baseline Result | Notes |
| --- | --- | --- | --- |
| Lint | `<command>` | PASS / FAIL / NOT RUN | `<known issue or environment blocker>` |
| Tests | `<command>` | PASS / FAIL / NOT RUN | `<known issue or environment blocker>` |
| Build | `<command>` | PASS / FAIL / NOT RUN | `<known issue or environment blocker>` |
| UI smoke | `<command/manual path>` | PASS / FAIL / NOT RUN | `<known issue or environment blocker>` |

Do not treat pre-existing failures as newly introduced regressions, but do not hide them. If a baseline failure blocks proof of the goal, fix it if in scope or stop and report the blocker.

## Milestone Checks

| Milestone | Required Check | Evidence Path | Status |
| --- | --- | --- | --- |
| M1 | `<command or proof>` | `<log/screenshot/artifact>` | NOT RUN |

## Acceptance Criteria Evidence

| AC | Evidence | Fresh? | Status | Notes |
| --- | --- | --- | --- | --- |
| AC-001 | `<post-change command/log/screenshot/artifact>` | YES / NO | PASS / FAIL | `<notes>` |

## Evidence Freshness Rule

Final evidence must be generated after the relevant implementation changes.

Every final evidence item must include:

- command or capture method
- timestamp or log filename
- exit code/result
- relevant changed files already present
- path to artifact when applicable

Do not use setup-time, pre-change, or stale evidence as final completion proof unless explicitly labeled as baseline evidence.

## Artifact Contracts

| Artifact | Required Properties | Validation Method | Status |
| --- | --- | --- | --- |
| `<file/path>` | `<schema, sections, format, content expectations>` | `<command/manual review>` | NOT RUN |

## Negative Checks

Before completion, search for counterexamples and likely regressions.

- Try the primary workflow with the most common edge case.
- Inspect nearby code paths touched by the diff.
- Confirm no unrelated files were changed.
- Confirm proof artifacts actually show each acceptance criterion, not just a nearby success state.
- Confirm no new secrets, local paths, debug logs, or placeholder TODOs were introduced.

## Diff Review

Before final completion, run:

```bash
git status --short
git diff --stat
git diff --check
```

Inspect the diff for unrelated file changes, debug code, temporary logs, TODOs introduced by the run, formatting churn, secrets, local paths, unexplained snapshots, and config/migration changes not mentioned in `PLAN.md`.

## Visual Proof Capture Standard

Required for UI, browser, frontend, visual-regression, before/after, or user-facing workflow goals.

- Save screenshots inside this goal folder, usually under `proof/images/`.
- Prefer browser viewport, component, or page screenshots. Do not use full-desktop screenshots unless the desktop layout itself is the subject.
- Each screenshot must have a caption, capture method, timestamp or filename, and the acceptance criterion it proves.
- Review screenshots before committing or sharing. Redact secrets, customer data, private tabs, notifications, unrelated apps, and personal files.
- Re-capture unreadable, stale, unrelated, or ambiguous screenshots.

## UX Review Standard

| Area | Evidence | Status | Notes |
| --- | --- | --- | --- |
| Primary workflow | `<screenshot/log/path>` | PASS / FAIL | `<notes>` |
| Empty state | `<evidence>` | PASS / FAIL / N/A | `<notes>` |
| Loading state | `<evidence>` | PASS / FAIL / N/A | `<notes>` |
| Error state | `<evidence>` | PASS / FAIL / N/A | `<notes>` |
| Copy and affordances | `<evidence>` | PASS / FAIL | `<notes>` |
| Keyboard/focus basics | `<evidence>` | PASS / FAIL / N/A | `<notes>` |
| Responsive or viewport behavior | `<evidence>` | PASS / FAIL / N/A | `<notes>` |
| Adjacent regression check | `<evidence>` | PASS / FAIL | `<notes>` |

## Final Self-Review

Before claiming completion, answer:

1. What is the strongest reason this might still be incomplete?
2. What evidence rules that out?
3. What changed outside the intended write scope?
4. What validation is missing, and why?
5. What would a reviewer most likely object to?
6. Is there a smaller or safer fix that should have been used instead?

## Completion Audit

| AC | Final Evidence | Status | Reviewer Notes |
| --- | --- | --- | --- |
| AC-001 | `<fresh evidence>` | PASS / FAIL | `<notes>` |

## Bounded Completion Standard

Complete the approved objective thoroughly within the stated scope, safety limits, and budget. Prefer durable fixes over workarounds, but do not expand into unrelated cleanup, speculative improvements, or open-ended polish.

- Search before building when the answer is not already known.
- Verify before claiming done: run the listed checks or record the exact blocker.
- Preserve user work, secrets, external systems, and production data.
- Stop and report when a required decision, permission, credential, budget limit, repeated validation failure, or safety constraint blocks progress.
- Finish with evidence: changed files, commands and results, screenshots or artifacts when relevant, and residual risks.
