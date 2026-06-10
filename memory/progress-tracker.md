# Progress Tracker

This file is the learner-facing and operator-friendly summary view.

The canonical runtime state lives in `memory/client-case-schema.yaml`.

Tasks live in `memory/task-schema.yaml`.

Material facts and freshness metadata live in `memory/evidence-schema.yaml`.

The thin derived operator cockpit lives in `memory/operator-view-schema.yaml`.

## Status values

- `not_started`
- `in_progress`
- `needs_review`
- `blocked`
- `done`
- `paused`

## Master progress table

| Area | Status | Evidence | Next action |
|---|---|---|---|
| Intake | not_started | | |
| Russian learning foundation | not_started | | |
| Classic path education | not_started | | |
| Creative finance education | not_started | | |
| Financial readiness | not_started | | |
| Lender comparison | not_started | | |
| Professional team | not_started | | |
| Property search | not_started | | |
| Property verification | not_started | | |
| Offer preparation | not_started | | |
| Under contract | not_started | | |
| Closing preparation | not_started | | |
| Post-closing setup | not_started | | |
| Creative finance deal analysis | not_started | | |
| Go/no-go decisions | not_started | | |

## Learning modules

| Module | Path | Status | Quiz score | Assignment | Notes |
|---|---|---|---:|---|---|
| 0. Intake and roadmap | both | not_started | | | |
| 1. U.S. homebuying basics | both | not_started | | | |
| 2. Financial readiness | classic | not_started | | | |
| 3. Loan programs | classic | not_started | | | |
| 4. Property search | both | not_started | | | |
| 5. Offer and negotiation | classic | not_started | | | |
| 6. Inspection, appraisal, title | classic | not_started | | | |
| 7. Closing | classic | not_started | | | |
| 8. Post-closing ownership | classic | not_started | | | |
| 9. Creative finance basics | creative | not_started | | | |
| 10. Seller finance | creative | not_started | | | |
| 11. Lease option / lease purchase | creative | not_started | | | |
| 12. Assumable and advanced structures | creative | not_started | | | |
| 13. Private/hard money and flip analysis | creative | not_started | | | |
| 14. House hacking | both | not_started | | | |
| 15. Final action plan | both | not_started | | | |

## Session update template

```markdown
## Session update

### Completed
- ...

### Verified
- ...

### Still unknown
- ...

### Risks identified
- ...

### Next action
- ...

### Memory updates
- ...
```

## Operational summary rules

- Derive this tracker from the canonical case state instead of treating it as a separate source of truth.
- Reflect blocking stale facts in `Evidence` or `Next action`.
- Keep one primary next action aligned with the active task queue.
- Keep the operator view aligned with the same active subject and blockers.

## Deal status values

- `new_lead`
- `researching`
- `needs_professional_review`
- `ready_for_offer_prep`
- `offer_submitted`
- `under_contract`
- `rejected`
- `paused`
- `closed`
- `no_go`
