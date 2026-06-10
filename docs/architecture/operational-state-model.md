# Operational State Model

## Purpose

This document upgrades the repository from a curriculum-and-workflow spec into an operational case-management system.

The agent must not treat each message as an isolated answer. It must treat the user as an active case with persistent state, evidence-backed facts, tracked risks, artifacts, and a bounded next-action queue.

## Canonical runtime object

Use `memory/client-case-schema.yaml` as the primary state object.

All other views are derived from it:

- `memory/progress-tracker.md` is a summary view;
- session close summaries are checkpoint views;
- property reports, lender comparisons, DPA tables, and go/no-go memos are artifacts linked back to the case;
- evidence and task records support the case object rather than replace it.

## Core rule

The agent updates one case object, not multiple competing memories.

Every substantial action should resolve into one or more of:

- update `profile`;
- update `learning`;
- update `execution`;
- add or revise `evidence`;
- add or revise `tasks`;
- add or revise `artifacts`;
- add or revise `risks`;
- update `session.next_actions`.

## Required sections

The case must maintain these sections:

1. `profile`
2. `learning`
3. `execution`
4. `properties`
5. `lenders`
6. `assistance_programs`
7. `creative_finance_cases`
8. `artifacts`
9. `risks`
10. `tasks`
11. `session`

## Update discipline

When the user asks a question, the agent must decide whether the answer changes state.

### State-changing examples

- buyer intake updates;
- lesson completion;
- quiz completion;
- new property review;
- lender quote comparison;
- DPA program verification;
- creative finance case analysis;
- draft document creation;
- red flag identification;
- go/no-go decision.

### Non-state-changing examples

- a short definition with no user-specific implication;
- a generic explanation that does not affect the case;
- a temporary brainstorming branch that the user did not adopt.

## Derived views

The agent should derive these views from the case rather than maintain them independently:

- current path;
- active module;
- open questions;
- stale items;
- primary next action;
- active property;
- active lender comparison;
- active creative finance case;
- summary for the session close.

## Conflict handling

When new information conflicts with existing state:

1. Do not silently overwrite.
2. Preserve both the previous and current claim through evidence records.
3. Mark the disputed field as unresolved if needed.
4. Create a task for verification or professional review.

## Long-running case requirements

A case is stable for multi-month use only if:

- the latest checkpoint is recoverable;
- stale items can be identified from timestamps and freshness rules;
- active tasks survive topic changes;
- artifacts are versioned and updated instead of recreated from scratch;
- risks remain visible until resolved or accepted.

## Minimal operating loop

For every substantial interaction:

1. Load the latest case state.
2. Identify the active subject: lesson, property, lender, DPA, or creative finance case.
3. Check stale evidence before relying on older facts.
4. Answer in Russian for the learner.
5. Update state, tasks, risks, and artifacts.
6. Create a checkpoint if a milestone was reached.
7. End with one primary next action.
