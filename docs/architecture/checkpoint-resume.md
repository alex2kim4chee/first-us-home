# Checkpoint and Resume Lifecycle

## Purpose

The agent must be able to continue a real buyer case after days or months without asking the user to reconstruct the full history.

This document defines when to checkpoint, what to save, and how to resume.

## Required checkpoint events

Create a checkpoint after any meaningful milestone:

- `lesson_done`
- `quiz_done`
- `buyer_intake_updated`
- `property_review_done`
- `lender_compare_updated`
- `dpa_shortlist_updated`
- `artifact_created`
- `artifact_updated`
- `go_no_go_recorded`
- `red_flag_added`
- `topic_changed`
- `waiting_on_user`
- `waiting_on_professional`

## What a checkpoint must contain

Each checkpoint must preserve:

- updated `client_case` state;
- state delta summary;
- evidence added or revised;
- tasks opened, blocked, or completed;
- stale items identified at checkpoint time;
- active risks;
- one primary next action;
- up to two secondary actions if needed.

## Resume algorithm

When a new session begins:

1. Load the most recent `client_case`.
2. Identify the last active path and active subject.
3. Recompute stale items using freshness rules.
4. Surface open high-priority risks first.
5. Surface blocked or waiting tasks second.
6. Surface the stored primary next action third.
7. If the stored next action is no longer valid, replace it and record why.

## Topic switching rule

If the user changes topic while active work is unfinished:

1. checkpoint the current branch;
2. mark unresolved tasks as open, waiting, or blocked;
3. update the new active branch;
4. do not discard the previous branch.

## Waiting state rule

When progress depends on the user or an external professional:

- convert the relevant task to `waiting_user` or `waiting_external`;
- preserve the exact dependency in the task notes;
- create a short resumption prompt for the next session.

## Portable fallback

If true persistence is unavailable, the agent must still emit a compact portable checkpoint block based on the same case model:

```yaml
PORTABLE_CASE_CHECKPOINT:
  case_id: ...
  active_path: ...
  active_subjects: []
  open_tasks: []
  stale_items: []
  active_risks: []
  primary_next_action: ...
```

## Quality rule

A checkpoint is good only if another agent can resume the case without guessing:

- what is already done;
- what facts are reliable;
- what is still unknown;
- what is blocking progress;
- what should happen next.
