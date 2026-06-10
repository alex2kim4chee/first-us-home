# Context Loading Policy

## Purpose

This repository now includes architecture, workflows, templates, runtime files, research playbooks, and evaluation materials.

The agent must not load all of it for every turn.

This policy defines how to keep the agent operationally strong without making it context-heavy.

## Core rule

Load the minimum context needed to complete the current step safely and correctly.

The repository is modular on purpose. Treat it that way.

## Loading tiers

## Tier 1: Hot path

These are the files the agent may need most often.

Load only what is actually needed from this tier, but this is the default working set:

- `AGENTS.md`
- active case file: `cases/<case-id>/client-case.yaml`
- active operator view: `cases/<case-id>/operator-view.yaml`
- `memory/session-close-protocol.md`
- one relevant workflow for the current task

Typical use cases:

- continuing an active case;
- answering a current buyer question;
- updating a property, lender, DPA, or creative-finance case;
- creating a checkpoint.

## Tier 2: Warm path

Load only when the current task explicitly requires it:

- one relevant template
- one relevant research playbook
- `docs/architecture/freshness-policy.md`
- `docs/architecture/operator-layer.md`
- `docs/runtime/file-runtime.md`

Typical triggers:

- preparing or updating a specific artifact;
- verifying live facts;
- resolving stale data;
- creating or updating runtime files.

## Tier 3: Cold path

Do not load these unless there is a clear reason:

- `docs/quality/*`
- `evals/*`
- workflows unrelated to the active path
- templates unrelated to the active artifact
- creative finance materials during standard classic-path work
- DPA materials during a pure property-inspection step

Typical triggers:

- quality review of the agent itself;
- regression work;
- prompt/system redesign;
- diagnosing repeated failure patterns.

## Hard limits

For an ordinary working turn, aim to load:

- `1` main instruction file
- `1` active case file
- `1` operator view
- `1` workflow
- `0-2` supporting files

If the working set grows beyond roughly `5-7` files, stop and justify why.

## Workflow selection rule

Use one primary workflow at a time.

Only load a second workflow if:

- the user's request genuinely spans both; and
- the second workflow changes the immediate next action.

Otherwise, keep the second workflow out of active context.

## Template selection rule

Load a template only when the agent is creating, updating, or validating that artifact.

Do not preload all templates “just in case”.

## Research playbook rule

Load the matching playbook only when the task involves live verification:

- property verification -> `property-verification-playbook.md`
- lender comparison -> `lender-comparison-playbook.md`
- DPA research -> `dpa-verification-playbook.md`

Do not load all research docs together unless the user is explicitly asking for repository-level design work.

## Evaluation rule

`docs/quality/*` and `evals/*` are not part of normal buyer-case execution.

Load them only when:

- testing the agent;
- reviewing architecture quality;
- diagnosing a failure mode;
- designing new regressions.

## Resume rule

When resuming a case after a pause:

1. load `client-case.yaml`
2. load `operator-view.yaml`
3. inspect stale items and primary next action
4. load the one workflow required by that next action
5. load a template or playbook only if needed

## Topic-switch rule

When the user changes topic:

1. checkpoint current work
2. keep prior branch in stored state
3. switch active subject in operator view
4. load only the workflow for the new topic

Do not drag the old workflow into the new turn unless it remains actively blocking.

## Anti-bloat rule

Do not add new “always load” files unless failing to load them would routinely create safety or state-loss errors.

If a document is useful only:

- for architecture work,
- for regression work,
- or for rare edge cases,

then it belongs in warm or cold path, not hot path.
