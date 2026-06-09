---
name: goal-setup
description: Prepare compact, verifiable /goal launch packs for long-running Codex work. Use when the user asks to scaffold, write, revise, or harden a /goal objective, GOAL.md, PLAN.md, CONSTRAINTS.md, CHECKS.md, PROGRESS.md, STATE.md, proof packet, validation harness, ExecPlan-style handoff, or autonomous coding runbook. Do not use for small one-turn fixes, vague backlogs, or tasks that lack measurable acceptance criteria.
license: MIT
compatibility: Codex. Git is recommended for repo goals. Browser or Playwright access is optional for UI proof.
metadata:
  version: "2.0.0"
  author: "pboiii"
---

# Goal Setup

Prepare a `/goal` run by converting messy repo, session, and task context into a durable execution packet. Create the packet first, then return the exact launch command. Do not start the goal unless the user explicitly asks you to.

Core rule: the slash command must be compact. For Codex, keep the final `/goal ...` command under 4,000 characters. Prefer 2,000 to 3,000 characters and move detail into files.

Fit rule: use goal mode only for long-running, self-verifiable work. For small, obvious, one-turn work, do the task normally. For broad strategy or stakeholder-judgment work, first narrow it into measurable outcomes.

Goal-control rule: use `/goal <objective>` to set the goal, `/goal` to inspect it, and `/goal pause`, `/goal resume`, or `/goal clear` when the user needs lifecycle control.

Performance rule: the packet should act like a resumable execution protocol, not just a pile of instructions. Prefer runnable checks, baseline capture, a current-state capsule, gated milestones, evidence freshness, failure-mode checks, and a final self-review.

Scope rule: finish the approved objective thoroughly inside the stated scope, budget, and safety boundaries. Do not expand into unrelated cleanup, speculative refactors, or open-ended polish.

Branch/PR rule: for repo goals, inspect git status and branch before editing. Goal agents may create clean branches/worktrees and milestone commits when recorded in PLAN.md. Pushing, opening PRs, deploying, publishing packages, changing production data, or performing destructive operations requires explicit user authorization or a documented repo policy.

Lifecycle rule: goal packets start under `docs/goals/plans-to-implement/<YYYY-MM-DD>-<goal-slug>/` and move to `docs/goals/implemented-plans/<YYYY-MM-DD>-<goal-slug>/` only after the user has confirmed completion.

Evidence rule: a goal is not complete because a narrow happy-path test passed. Completion requires fresh post-change evidence mapped to every acceptance criterion.

Privacy rule: logs, screenshots, traces, and proof artifacts must not expose secrets, tokens, customer data, private tabs, unrelated personal files, notifications, or internal-only content. Redact or keep sensitive proof local.

## Workflow

1. Confirm fit and target.
   - Identify target workspace, git root if present, current branch, dirty state, and write scope.
   - Classify the task: code, UI/UX, deployment/infra, docs/research, local-file workflow, or mixed.
   - Decide packet size: lean, standard, or full. Use the smallest packet that can safely run.
   - Check active goal status where possible or tell the user how to check it.

2. Resolve safe unknowns before drafting.
   - Read available session context, attachments, repo instructions, docs, related code, tests, and recent history.
   - Use read-only commands and searches to resolve factual questions that do not require mutation or approval.
   - Reproduce or trace reported bugs as far as safely possible.
   - Record a Claim/Evidence Ledger, Decision Log, and Remaining Unknowns. Do not turn resolvable setup questions into runner work.
   - Ask at most one concise blocking question only if the packet cannot be made verifiable.

3. Shape the objective.
   - Express the goal as: do `<work>` until `<measurable end state>` is proven without `<constraints>` being violated.
   - Define acceptance criteria, out-of-scope work, allowed write scope, required validation, proof artifacts, and stop/report conditions.
   - Identify the core path, known failure modes, negative checks, and milestone gates.
   - Add turn/time/budget limits for non-trivial goals.

4. Create the packet.
   - Default path: `docs/goals/plans-to-implement/<YYYY-MM-DD>-<goal-slug>/`.
   - Lean packet: `GOAL.md`, `CHECKS.md`, `PROGRESS.md`, and `STATE.md`.
   - Standard packet: lean packet plus `PLAN.md` and `CONSTRAINTS.md`.
   - Full packet: standard packet plus `proof/README.md`, `goal-check.sh`, `checks/commands.txt`, dashboards, `TASKS.md`, `COORDINATION.md`, or generated validators only when they add execution value.
   - Delete unused placeholder sections before launch.
   - Prefer copying and adapting templates from `references/templates/`.

5. Add execution machinery when useful.
   - Create `goal-check.sh` and `checks/commands.txt` for substantive code, UI, deploy, data, or docs validation.
   - Require baseline capture before implementation and final evidence after implementation.
   - Keep `STATE.md` short and current so the runner can resume after context loss.
   - Create `proof/README.md` for proof-heavy or UI goals.
   - Add failure modes, negative checks, artifact contracts, and final self-review when tests alone are insufficient.

6. Draft the launch command.
   - Mandatory output.
   - Keep Codex command under 4,000 characters. Count it when shell access is available.
   - Do not paste the whole task brief into `/goal`. Point to the packet.
   - Include the objective, evidence requirement, goal directory, validation cadence, progress logging, stop/report conditions, and final completion rule.

## Goal Quality Bar

A goal packet is ready only when the runner can check progress against evidence. Good evidence includes tests, builds, typechecks, lint, evals, screenshots, browser checks, deployment health checks, generated artifacts, data assertions, or a completion audit.

For user-facing work, tests are not enough. Add a UX review gate covering the real workflow, expected/empty/loading/error states, copy, affordances, focus/keyboard basics where relevant, responsive behavior, and visual regressions.

For non-code or mixed work, use artifact contracts and reviewer-readable proof. The output should be checkable without relying on the runner's confidence.

## Output

Finish with:

- Created or updated file paths.
- Packet size selected and why.
- Active lifecycle location.
- One short intent summary.
- The exact launch command in a fenced code block with character count when possible.
- Branch/worktree/commit/PR strategy for repo goals.
- Core path, milestone gates, known failure modes, and validation harness path when created.
- Visual proof plan when relevant.
- Setup validation already performed and setup checks still unrun.
- Clear stop/report conditions, including budget, permission, credentials, repeated validation failure, or unresolved product decisions.
