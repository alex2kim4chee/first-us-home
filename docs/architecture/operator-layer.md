# Operator Layer

## Purpose

The canonical case model is intentionally detailed. The agent still needs a fast operational cockpit so it can steer a case without rereading the full state every turn.

This document defines that thin operator layer.

## Design goal

Do not build a CRM inside the prompt architecture.

Build only the minimum derived view needed to answer:

1. What case is active?
2. What is blocked?
3. What is stale?
4. What is waiting on the user or a professional?
5. What is the one best next action?

## Source of truth

The operator layer is derived from:

- `memory/client-case-schema.yaml`
- `memory/evidence-schema.yaml`
- `memory/task-schema.yaml`

Use `memory/operator-view-schema.yaml` as the format for the derived cockpit.

## What the operator view should show

### Active subjects

- active property
- active lender comparison
- active DPA shortlist
- active creative finance case
- current learning module

### Immediate action panel

- one primary next action
- up to two secondary actions
- highest-severity unresolved risks
- stale facts that can distort decisions
- waiting items
- blocked items

### Progress snapshot

- readiness
- lender comparison
- property search
- offer status
- closing status

## Derivation rule

The operator layer must not introduce new facts.

It should only compress and prioritize what already exists in the case.

## Prioritization order

When selecting what to surface first:

1. critical or high risks
2. blocked items
3. stale items that affect a live decision
4. waiting items that need follow-up
5. the next workflow step

## Topic switch behavior

When the user changes topic:

- preserve the previous branch in the case;
- switch the active subject in the operator view;
- keep unresolved blockers visible if they remain strategically important.

## When to regenerate

Regenerate the operator view after:

- every checkpoint;
- any change to primary next action;
- any new high-severity risk;
- any stale-item detection event;
- any topic switch;
- any go/no-go change.

## User-facing versus operator-facing

The operator view is internal guidance for disciplined case handling.

The user-facing response should still be:

- in Russian unless requested otherwise;
- practical;
- narrow in scope;
- centered on the current next step.
