# Performance Patterns For Goal Packets

Use these when the objective is large enough that the runner may lose context, chase side paths, or claim completion too early.

## Executable Checks

Turn validation into a command whenever possible. A runner that can execute `goal-check.sh final` is less likely to drift than one that has to interpret a prose checklist.

## Baseline Then Final

Capture validation before implementation and again after implementation. Label baseline evidence separately so pre-existing failures do not become fake final proof.

## Current State Capsule

Keep `STATE.md` short and current. It should answer: where are we, what is next, what is blocked, what changed, and what evidence is freshest.

## Core Path First

Identify the shortest path to the measurable done condition. Complete that path before polish, refactors, or broad cleanup.

## Gated Milestones

Each milestone should have allowed write scope, inputs to inspect, implementation target, exit gate, evidence, and checkpoint behavior.

## Negative Checks

Ask what could still be broken. Try the common edge case. Inspect nearby code. Review the diff. Confirm the screenshot or log proves the actual acceptance criterion.

## Evidence Freshness

Final proof must be produced after the relevant code or artifact changes. Stale setup evidence is useful context, not final proof.

## Partial Completion

Blocked runs should still leave useful state: safe changes preserved, unsafe changes isolated, failures documented, and `STATE.md` updated with the next best action.
