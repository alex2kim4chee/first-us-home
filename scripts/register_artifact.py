#!/usr/bin/env python3
from __future__ import annotations

import sys

from runtime_common import fail, read_text, repo_path, today_iso, write_text


def append_artifact_entry(
    manifest: str,
    artifact_id: str,
    artifact_type: str,
    title: str,
    file_path: str,
    artifact_date: str,
) -> str:
    if f"artifact_id: {artifact_id}" in manifest:
        fail(f"Artifact already exists in manifest: {artifact_id}")

    entry = "\n".join(
        [
            "  - artifact_id: " + artifact_id,
            "    type: " + artifact_type,
            "    title: " + title,
            "    status: draft",
            "    related_subjects: []",
            "    source_ids: []",
            "    version: 1",
            "    last_updated: " + artifact_date,
            "    file_path: " + file_path,
            "    summary: null",
            "",
        ]
    )
    if manifest.endswith("\n"):
        return manifest + entry
    return manifest + "\n" + entry


def main(argv: list[str]) -> int:
    if len(argv) < 6:
        print(
            "Usage: python scripts/register_artifact.py <case-id> <artifact-id> <type> <title> <file-path> [YYYY-MM-DD]",
            file=sys.stderr,
        )
        return 1

    case_id = argv[1]
    artifact_id = argv[2]
    artifact_type = argv[3]
    title = argv[4]
    file_path = argv[5]
    artifact_date = argv[6] if len(argv) > 6 else today_iso()

    manifest_path = repo_path("artifacts", case_id, "manifest.yaml")
    if not manifest_path.exists():
        fail(f"Manifest not found: {manifest_path.relative_to(repo_path())}")

    manifest = read_text(manifest_path)
    updated = append_artifact_entry(
        manifest=manifest,
        artifact_id=artifact_id,
        artifact_type=artifact_type,
        title=title,
        file_path=file_path,
        artifact_date=artifact_date,
    )
    write_text(manifest_path, updated)

    print("Updated:")
    print(f"  {manifest_path.relative_to(repo_path())}")
    print(f"Registered artifact: {artifact_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
