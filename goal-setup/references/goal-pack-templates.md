# Goal Pack Templates

This reference is for generating goal packets that improve autonomous execution, not just documentation quality. The packet should make the runner converge, recover, validate, and produce reviewer-trustworthy proof.

## Packet Size

Use the smallest packet that can safely launch the goal.

| Packet | Files | Use when |
| --- | --- | --- |
| Lean | `GOAL.md`, `CHECKS.md`, `PROGRESS.md`, `STATE.md` | The work is multi-turn but low-risk and has straightforward checks. |
| Standard | Lean plus `PLAN.md`, `CONSTRAINTS.md` | Most codebase work, UI work, data work, or anything with meaningful sequencing or risk. |
| Full | Standard plus `goal-check.sh`, `checks/commands.txt`, `proof/README.md`, dashboards, validators, `TASKS.md`, `COORDINATION.md` | Serious migrations, UI proof, deploy loops, cross-cutting refactors, multi-agent work, or anything likely to survive context compaction. |

Delete unused placeholder sections before launch.

## Codex Goal Controls

| Control | Purpose |
| --- | --- |
| `/goal <objective>` | Set the active goal. |
| `/goal` | Inspect current goal status. |
| `/goal pause` | Pause an active goal. |
| `/goal resume` | Resume a paused goal. |
| `/goal clear` | Remove the active goal. |

## Bounded Completion Standard

Use this short form in generated docs.

```markdown
## Bounded Completion Standard

Complete the approved objective thoroughly within the stated scope, safety limits, and budget. Prefer durable fixes over workarounds, but do not expand into unrelated cleanup, speculative improvements, or open-ended polish.

- Search before building when the answer is not already known.
- Verify before claiming done: run the listed checks or record the exact blocker.
- Preserve user work, secrets, external systems, and production data.
- Stop and report when a required decision, permission, credential, budget limit, repeated validation failure, or safety constraint blocks progress.
- Finish with evidence: changed files, commands and results, screenshots or artifacts when relevant, and residual risks.
```

## Core Path First

Add this to `PLAN.md` for anything broad.

```markdown
## Core Path First

Complete the shortest path to the measurable done condition before polish, broad cleanup, refactors, or optional enhancements.

Core path:
1. `<minimum implementation step>`
2. `<minimum validation step>`
3. `<minimum proof step>`

Non-core work is allowed only after the core path passes validation, unless it is required to unblock the core path.
```

## Claim / Evidence Ledger

Use this during setup so guesses do not become implementation facts.

```markdown
## Claim / Evidence Ledger

| Claim | Evidence | Confidence | Used By |
| --- | --- | --- | --- |
| `<fact about bug/code/user need>` | `<file, command, log, screenshot, source>` | High / Medium / Low | `<milestone or AC>` |

Rules:
- High-confidence claims may drive implementation.
- Medium-confidence claims require validation during the relevant milestone.
- Low-confidence claims must not become implementation assumptions unless recorded as a risk or stop condition.
```

## Gated Milestones

Replace loose milestone lists with gates.

```markdown
## Gated Milestones

### M1. `<Milestone name>`

Purpose:
`<why this matters>`

Allowed write scope:
- `<paths>`

Inputs to inspect first:
- `<files/docs/tests>`

Implementation target:
- `<specific change>`

Exit gate:
- `<command, artifact, screenshot, or manual proof required>`

Evidence to record:
- `<log path, screenshot path, diff summary>`

Rollback/checkpoint:
- `<commit, checkpoint, or revert strategy>`

Do not proceed to M2 until:
- `<condition>`
```

## Known Failure Modes

Add this to `PLAN.md` and require the runner to check it before final completion.

```markdown
## Known Failure Modes

| Failure Mode | Why It Might Happen | How To Detect | Required Response |
| --- | --- | --- | --- |
| `<fixes happy path only>` | `<risk>` | `<test/manual check>` | `<add coverage or stop>` |
| `<visual proof shows wrong state>` | `<risk>` | `<screenshot review>` | `<recapture correct state>` |
| `<unrelated files changed>` | `<risk>` | `git diff --stat` | `<revert unrelated edits>` |
```

## Baseline Capture

Add this to `CHECKS.md` and make it the first runner action.

```markdown
## Baseline Capture

Before implementation, run the relevant validation commands and record the current state.

| Check | Command | Baseline Result | Notes |
| --- | --- | --- | --- |
| Lint | `<command>` | PASS / FAIL / NOT RUN | `<known issue or environment blocker>` |
| Tests | `<command>` | PASS / FAIL / NOT RUN | `<known issue or environment blocker>` |
| Build | `<command>` | PASS / FAIL / NOT RUN | `<known issue or environment blocker>` |
| UI smoke | `<command/manual path>` | PASS / FAIL / NOT RUN | `<known issue or environment blocker>` |

Do not treat pre-existing failures as newly introduced regressions, but do not hide them. If a baseline failure blocks proof of the goal, fix it if in scope or stop and report the blocker.
```

## Evidence Freshness Rule

Add this to `CHECKS.md`.

```markdown
## Evidence Freshness Rule

Final evidence must be generated after the relevant implementation changes.

Every final evidence item must include:
- command or capture method
- timestamp or log filename
- exit code/result
- relevant changed files already present
- path to artifact when applicable

Do not use setup-time, pre-change, or stale evidence as final completion proof unless explicitly labeled as baseline evidence.
```

## Negative Checks

Add this before the final audit.

```markdown
## Negative Checks

Before completion, search for counterexamples and likely regressions.

- Try the primary workflow with the most common edge case.
- Inspect nearby code paths touched by the diff.
- Confirm no unrelated files were changed.
- Confirm proof artifacts actually show each acceptance criterion, not just a nearby success state.
- Confirm no new secrets, local paths, debug logs, or placeholder TODOs were introduced.
```

## Diff Review

```markdown
## Diff Review

Before final completion, run:

```bash
git status --short
git diff --stat
git diff --check
```

Inspect the diff for unrelated file changes, debug code, temporary logs, TODOs introduced by the run, formatting churn, secrets, local paths, unexplained snapshots, and config/migration changes not mentioned in `PLAN.md`.
```

## Decision Budget

Add this to `CONSTRAINTS.md`.

```markdown
## Decision Budget

The runner may decide:
- implementation details that preserve documented behavior
- naming consistent with repo conventions
- test placement following existing patterns
- minor copy only when acceptance criteria define intent

The runner must stop/report for:
- product behavior tradeoffs
- data deletion or migration ambiguity
- permission or security model changes
- pricing, billing, email, notification, or external-send behavior
- public API contract changes
- scope expansion beyond the approved objective
```

## Partial Completion Protocol

Add this to `CONSTRAINTS.md` or `PROGRESS.md`.

```markdown
## Partial Completion Protocol

If the full goal cannot be completed, leave the workspace in the most useful safe state.

- Revert or isolate unsafe partial changes.
- Preserve useful completed changes when safe.
- Record exactly what passed and failed.
- Leave reproduction steps for remaining blockers.
- Update `STATE.md` with the next best action.
- Do not claim completion.
```

## Final Self-Review

Add this to `CHECKS.md`.

```markdown
## Final Self-Review

Before claiming completion, answer:

1. What is the strongest reason this might still be incomplete?
2. What evidence rules that out?
3. What changed outside the intended write scope?
4. What validation is missing, and why?
5. What would a reviewer most likely object to?
6. Is there a smaller or safer fix that should have been used instead?
```

## Launch Prompt Shapes

### Codex

```text
/goal Complete <approved objective> until <measurable end state> is proven without violating <key constraints>. Follow <goal-dir>/GOAL.md and the goal packet. Before changing code, read available session context, repo instructions, relevant docs/history, and every goal-packet file. Capture baseline validation first. Work through PLAN.md gated milestones, run CHECKS.md after each milestone, keep STATE.md current, and update PROGRESS.md with fresh evidence and blockers. Stop/report if any safety, permission, credential, budget, or repeated-validation stop condition is hit. Finish only when final validation passes and every acceptance criterion maps to fresh evidence.
```

## Visual Proof Capture Standard

```markdown
## Visual Proof Capture Standard

Required for UI, browser, frontend, visual-regression, before/after, or user-facing workflow goals.

- Save screenshots inside this goal folder, usually under `proof/images/`.
- Prefer browser viewport, component, or page screenshots. Do not use full-desktop screenshots unless the desktop layout itself is the subject.
- Each screenshot must have a caption, capture method, timestamp or filename, and the acceptance criterion it proves.
- Review screenshots before committing or sharing. Redact secrets, customer data, private tabs, notifications, unrelated apps, and personal files.
- Re-capture unreadable, stale, unrelated, or ambiguous screenshots.
```

## UX Review Standard

```markdown
## UX Review Standard

For user-facing work, completion requires review of the actual workflow from the user's point of view.

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
```
