# Artifact Lifecycle

## Purpose

Artifacts are the working documents the agent produces while guiding a real buyer case.

They must behave like durable case records, not disposable answer text.

## What counts as an artifact

Typical artifacts include:

- buyer profile
- property intake or property verification report
- lender comparison
- assistance program comparison
- offer preparation memo
- inspection questions
- creative finance due diligence worksheet
- go/no-go memo

## Minimum artifact metadata

Every artifact should expose:

- `artifact_id`
- `artifact_status`
- `case_id`
- related subject IDs
- `date_updated`
- `primary_next_action`

## Artifact rules

1. Reuse and update an artifact when the subject is the same.
2. Create a new artifact only when the subject or document type changes materially.
3. Link material facts back to evidence records when possible.
4. Mark drafts clearly when professional review is required.
5. Preserve unknowns, stale facts, and open review items instead of omitting them.

## Artifact status guidance

- `draft`: first workable version
- `updated`: revised with new facts or decisions
- `needs_review`: blocked on lender, attorney, title, inspector, or another professional
- `final_for_user`: usable learner-facing package for the current step

## Workflow connection

Whenever a workflow creates or changes an artifact, the agent should also:

- update the canonical case object;
- update or create tasks;
- update risks if blockers were found;
- create a checkpoint if the next action changed.
