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
    if len(argv) < 3:
        print(
            "Usage: python scripts/create_checkpoint.py <case-id> <checkpoint-type> [YYYY-MM-DD]",
            file=sys.stderr,
        )
        return 1

    case_id = argv[1]
    checkpoint_type = argv[2]
    checkpoint_date = argv[3] if len(argv) > 3 else today_iso()

    checkpoint_file = repo_path(
        "checkpoints",
        case_id,
        f"{checkpoint_date}-{checkpoint_type}.yaml",
    )

    ensure_absent(checkpoint_file, "Checkpoint")

    content = replace_tokens(
        read_text(repo_path("checkpoints", "_checkpoint-template.yaml")),
        {
            "REPLACE_CASE_ID": case_id,
            "REPLACE_CHECKPOINT_TYPE": checkpoint_type,
            "REPLACE_DATE": checkpoint_date,
        },
    )

    write_text(checkpoint_file, content)
    print("Created:")
    print(f"  {checkpoint_file.relative_to(repo_path())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
