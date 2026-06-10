# Checkpoints Runtime Directory

This directory stores immutable milestone snapshots by case.

Recommended layout:

```text
checkpoints/<case-id>/
  YYYY-MM-DD-buyer_intake_updated.yaml
  YYYY-MM-DD-property_review_done.yaml
  YYYY-MM-DD-go_no_go_recorded.yaml
```

Use `checkpoints/_checkpoint-template.yaml` as the starting structure.

Prefer:

```text
python scripts/create_checkpoint.py <case-id> <checkpoint-type> [YYYY-MM-DD]
```

Examples:

```text
python scripts/create_checkpoint.py buyer-20260610-atlanta-fha buyer_intake_updated
python scripts/create_checkpoint.py buyer-20260610-atlanta-fha property_review_done 2026-06-10
```

Windows alternative:

```text
py -3 scripts\create_checkpoint.py buyer-20260610-atlanta-fha buyer_intake_updated
```
