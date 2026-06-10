# Artifacts Runtime Directory

This directory stores working documents by case.

Recommended layout:

```text
artifacts/<case-id>/
  manifest.yaml
  buyer-profile.md
  property-...md
  lender-comparison-...md
  dpa-shortlist-...md
```

Use `artifacts/_artifact-manifest-template.yaml` for the case-level artifact registry.

To register a new artifact entry in a case manifest:

- `python scripts/register_artifact.py <case-id> <artifact-id> <type> <title> <file-path> [YYYY-MM-DD]`
- Windows: `py -3 scripts\register_artifact.py <case-id> <artifact-id> <type> <title> <file-path> [YYYY-MM-DD]`
