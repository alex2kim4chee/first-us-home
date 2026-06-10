# Cases Runtime Directory

This directory stores active buyer cases.

Use one subdirectory per case:

```text
cases/<case-id>/
  client-case.yaml
  operator-view.yaml
  notes.md
```

Use `cases/_case-template.yaml` and `cases/_operator-view-template.yaml` when creating a new case manually.

Prefer the cross-platform scaffolding script:

- `python scripts/scaffold_case.py <case-id> [YYYY-MM-DD]`
- Windows: `py -3 scripts\scaffold_case.py <case-id> [YYYY-MM-DD]`

`scripts/scaffold-case.sh` is an optional POSIX wrapper.

After the canonical case state changes, refresh the derived cockpit:

- `python scripts/update_operator_view.py <case-id>`
- Windows: `py -3 scripts\update_operator_view.py <case-id>`

For common case mutations, prefer the narrow updater instead of manual YAML edits:

- `python scripts/update_client_case.py set-primary-next-action <case-id> "Call lender A for updated APR"`
- `python scripts/update_client_case.py add-task <case-id> task-001 "Collect county target"`
- `python scripts/update_client_case.py add-risk <case-id> risk-001 high "Listing claims duplex but assessor shows single-family"`
