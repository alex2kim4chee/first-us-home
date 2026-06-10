# File Runtime

## Purpose

This repository now has the operational rules for long-running buyer support. It also needs a concrete on-disk layout for storing active cases, checkpoints, and artifacts.

This runtime is intentionally lightweight:

- file-based
- human-readable
- git-friendly
- simple enough for manual inspection and agent-driven updates

## Directory layout

```text
cases/
  _case-template.yaml
  _operator-view-template.yaml
  <case-id>/
    client-case.yaml
    operator-view.yaml
    notes.md

artifacts/
  _artifact-manifest-template.yaml
  <case-id>/
    manifest.yaml
    *.md

checkpoints/
  _checkpoint-template.yaml
  <case-id>/
    YYYY-MM-DD-<checkpoint-type>.yaml

scripts/
  scaffold_case.py
  create_checkpoint.py
  register_artifact.py
  update_client_case.py
  update_operator_view.py
  scaffold-case.sh
  create-checkpoint.sh
  register-artifact.sh
  update-client-case.sh
  update-operator-view.sh
```

## Source-of-truth rule

Use these files with strict roles:

- `cases/<case-id>/client-case.yaml`: canonical runtime state
- `cases/<case-id>/operator-view.yaml`: thin derived cockpit
- `artifacts/<case-id>/manifest.yaml`: registry of case artifacts
- `checkpoints/<case-id>/*.yaml`: immutable milestone snapshots

Do not treat checkpoints or artifact manifests as replacements for `client-case.yaml`.

## Update pattern

For substantial work:

1. load `client-case.yaml`
2. update state
3. update `operator-view.yaml`
4. update or add artifact files
5. append a checkpoint file when a milestone is reached

Helper scripts:

Cross-platform entrypoints:

- `python scripts/scaffold_case.py <case-id> [YYYY-MM-DD]`
- `python scripts/create_checkpoint.py <case-id> <checkpoint-type> [YYYY-MM-DD]`
- `python scripts/register_artifact.py <case-id> <artifact-id> <type> <title> <file-path> [YYYY-MM-DD]`
- `python scripts/update_client_case.py <command> ...`
- `python scripts/update_operator_view.py <case-id>`

Windows alternative:

- `py -3 scripts\scaffold_case.py <case-id> [YYYY-MM-DD]`
- `py -3 scripts\create_checkpoint.py <case-id> <checkpoint-type> [YYYY-MM-DD]`
- `py -3 scripts\register_artifact.py <case-id> <artifact-id> <type> <title> <file-path> [YYYY-MM-DD]`
- `py -3 scripts\update_client_case.py <command> ...`
- `py -3 scripts\update_operator_view.py <case-id>`

POSIX helper wrappers:

- `sh scripts/scaffold-case.sh <case-id> [YYYY-MM-DD]`
- `sh scripts/create-checkpoint.sh <case-id> <checkpoint-type> [YYYY-MM-DD]`
- `sh scripts/register-artifact.sh <case-id> <artifact-id> <type> <title> <file-path> [YYYY-MM-DD]`
- `sh scripts/update-client-case.sh <command> ...`
- `sh scripts/update-operator-view.sh <case-id>`

Supported `update_client_case.py` commands:

- `set-scalar`
- `append-list-item`
- `set-primary-next-action`
- `add-task`
- `add-risk`
- `touch-session`

## Naming guidance

Case IDs should be short, stable, and human-readable.

Recommended pattern:

```text
buyer-YYYYMMDD-short-label
```

Examples:

- `buyer-20260610-atlanta-fha`
- `buyer-20260610-househack-nj`

## Artifact naming guidance

Use descriptive names tied to the subject:

- `buyer-profile.md`
- `property-123-main-st-verification.md`
- `lender-comparison-2026-06-10.md`
- `dpa-shortlist-ga-fulton.md`
- `go-no-go-123-main-st.md`

## Checkpoint naming guidance

Checkpoint files should be immutable snapshots:

```text
YYYY-MM-DD-buyer_intake_updated.yaml
YYYY-MM-DD-property_review_done.yaml
YYYY-MM-DD-go_no_go_recorded.yaml
```

## Minimal runtime discipline

This runtime is working correctly when:

- one active case can be resumed from disk;
- stale items are visible in operator view;
- artifacts are easy to locate by case;
- checkpoints show when and why the case changed.

## Minimal checkpoint discipline

Checkpoint files should be:

- immutable after creation when practical;
- named from the actual milestone type;
- created whenever the next action, risk state, or active branch changes materially.
