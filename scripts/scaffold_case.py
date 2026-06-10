#!/usr/bin/env python3
from __future__ import annotations

import sys

from runtime_common import (
    ensure_absent,
    read_text,
    repo_path,
    replace_tokens,
    today_iso,
    write_text,
)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python scripts/scaffold_case.py <case-id> [YYYY-MM-DD]", file=sys.stderr)
        return 1

    case_id = argv[1]
    case_date = argv[2] if len(argv) > 2 else today_iso()

    case_dir = repo_path("cases", case_id)
    artifact_dir = repo_path("artifacts", case_id)
    checkpoint_dir = repo_path("checkpoints", case_id)

    ensure_absent(case_dir / "client-case.yaml", "Case file")

    replacements = {
        "REPLACE_CASE_ID": case_id,
        "REPLACE_DATE": case_date,
    }

    case_template = replace_tokens(read_text(repo_path("cases", "_case-template.yaml")), replacements)
    operator_template = replace_tokens(
        read_text(repo_path("cases", "_operator-view-template.yaml")),
        {"REPLACE_CASE_ID": case_id},
    )
    artifact_template = replace_tokens(
        read_text(repo_path("artifacts", "_artifact-manifest-template.yaml")),
        {"REPLACE_CASE_ID": case_id},
    )

    write_text(case_dir / "client-case.yaml", case_template)
    write_text(case_dir / "operator-view.yaml", operator_template)
    write_text(artifact_dir / "manifest.yaml", artifact_template)
    write_text(
        case_dir / "notes.md",
        "\n".join(
            [
                "# Case Notes",
                "",
                f"Case ID: {case_id}",
                f"Created: {case_date}",
                "",
                "- Use this file for lightweight human notes that do not belong in canonical YAML state.",
                "",
            ]
        ),
    )
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    print("Created:")
    print(f"  {(case_dir / 'client-case.yaml').relative_to(repo_path())}")
    print(f"  {(case_dir / 'operator-view.yaml').relative_to(repo_path())}")
    print(f"  {(case_dir / 'notes.md').relative_to(repo_path())}")
    print(f"  {(artifact_dir / 'manifest.yaml').relative_to(repo_path())}")
    print(f"  {checkpoint_dir.relative_to(repo_path())}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
