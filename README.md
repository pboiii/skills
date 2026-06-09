# Goal Setup Skill

Goal Setup prepares compact, verifiable launch packets for long-running `/goal` coding tasks. It turns messy repo/session context into durable goal files, acceptance criteria, validation checks, progress logs, state capsules, proof-artifact plans, and a short launch command that stays under the current Codex goal-command limit.

Use it when a task is too large for a single turn, has a measurable end state, and can be validated through tests, builds, screenshots, logs, generated artifacts, data assertions, or a completion audit. It is best for migrations, substantial refactors, UI workflows, deployment retry loops, documentation sweeps, and other autonomous multi-turn work where the agent needs a clear scope and stopping condition.

Do not use it for small one-off fixes, vague backlogs, speculative architecture debates, or tasks that require human judgment before acceptance criteria can be defined.

## What changed in V2

This revision focuses on goal performance:

- `STATE.md` resume capsule for context loss and session continuation.
- Runnable validation harness via `goal-check.sh` plus `checks/commands.txt`.
- Baseline capture before implementation and fresh final evidence after implementation.
- Gated milestones with exit criteria and checkpoint behavior.
- Known failure modes, negative checks, diff review, and final self-review.
- Decision budget that tells the runner what it may decide and what must stop for approval.
- Proof packet structure for screenshots, logs, and generated artifacts.
- Helper scripts for validation, proof indexing, and state updates.

## Install

Keep the skill directory named `goal-setup/`. The Agent Skills `name` field must
match the parent directory name, and this bundle uses `name: goal-setup`.

For user-wide Codex skills:

```bash
mkdir -p ~/.codex/skills
cp -R goal-setup ~/.codex/skills/
```

## Bundle layout

```text
goal-setup/
  SKILL.md
  CHANGELOG.md
  LICENSE.txt
  agents/openai.yaml
  references/
    goal-pack-templates.md
    target-tools.md
    performance-patterns.md
    templates/
      GOAL.md
      PLAN.md
      CONSTRAINTS.md
      CHECKS.md
      PROGRESS.md
      STATE.md
      proof/README.md
    scripts/
      goal-check.sh
      commands.example.txt
      validate-goal-pack.py
      update-goal-state.py
      build-proof-index.py
```

## Recommended generated goal folder

```text
docs/goals/plans-to-implement/<YYYY-MM-DD>-<goal-slug>/
  GOAL.md
  PLAN.md
  CONSTRAINTS.md
  CHECKS.md
  PROGRESS.md
  STATE.md
  goal-check.sh
  checks/commands.txt
  proof/
    README.md
    logs/
    images/
```

## Example launch command shape

```text
/goal Complete <approved objective> until <measurable end state> is proven without violating <key constraints>. Follow docs/goals/plans-to-implement/<slug>/GOAL.md and the goal packet. Capture baseline validation first. Work through PLAN.md gated milestones, run CHECKS.md after each milestone, keep STATE.md current, and update PROGRESS.md with fresh evidence and blockers. Stop/report if safety, permission, credential, budget, or repeated-validation stop conditions are hit. Finish only when final validation passes and every acceptance criterion maps to fresh evidence.
```

## License

MIT.
