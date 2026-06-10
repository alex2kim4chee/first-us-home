#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from runtime_common import fail, read_text, repo_path, today_iso, write_text
from update_operator_view import build_operator_view, parse_client_case


def yaml_string(value: str | None) -> str:
    if value is None:
        return "null"
    return json.dumps(value, ensure_ascii=False)


def load_case_lines(case_id: str) -> tuple[Path, list[str]]:
    path = repo_path("cases", case_id, "client-case.yaml")
    if not path.exists():
        fail(f"Case file not found: {path.relative_to(repo_path())}")
    return path, path.read_text(encoding="utf-8").splitlines()


def find_section(lines: list[str], section: str) -> int:
    target = f"{section}:"
    for idx, line in enumerate(lines):
        if line == target:
            return idx
    fail(f"Section not found: {section}")


def section_end(lines: list[str], section_idx: int) -> int:
    for idx in range(section_idx + 1, len(lines)):
        line = lines[idx]
        if line and not line.startswith(" "):
            return idx
    return len(lines)


def find_field(lines: list[str], section: str, field: str) -> tuple[int, int]:
    section_idx = find_section(lines, section)
    end_idx = section_end(lines, section_idx)
    prefix = f"  {field}:"
    for idx in range(section_idx + 1, end_idx):
        if lines[idx].startswith(prefix):
            return idx, end_idx
    fail(f"Field not found: {section}.{field}")


def field_indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def field_block_end(lines: list[str], field_idx: int, section_end_idx: int, base_indent: int) -> int:
    for idx in range(field_idx + 1, section_end_idx):
        line = lines[idx]
        if not line.strip():
            continue
        if field_indent(line) <= base_indent:
            return idx
    return section_end_idx


def set_scalar(case_id: str, path: str, value: str | None) -> None:
    section, field = path.split(".", 1)
    case_path, lines = load_case_lines(case_id)
    field_idx, _ = find_field(lines, section, field)
    indent = " " * field_indent(lines[field_idx])
    lines[field_idx] = f"{indent}{field}: {yaml_string(value)}"
    write_text(case_path, "\n".join(lines) + "\n")


def append_list_item(case_id: str, path: str, value: str) -> None:
    section, field = path.split(".", 1)
    case_path, lines = load_case_lines(case_id)
    field_idx, section_end_idx = find_field(lines, section, field)
    line = lines[field_idx]
    indent = " " * field_indent(line)
    item_indent = indent + "  "
    if line.strip().endswith("[]"):
        lines[field_idx] = f"{indent}{field}:"
        lines.insert(field_idx + 1, f"{item_indent}- {yaml_string(value)}")
    else:
        block_end = field_block_end(lines, field_idx, section_end_idx, field_indent(line))
        lines.insert(block_end, f"{item_indent}- {yaml_string(value)}")
    write_text(case_path, "\n".join(lines) + "\n")


def append_block(case_id: str, path: str, block_lines: list[str]) -> None:
    section, field = path.split(".", 1)
    case_path, lines = load_case_lines(case_id)
    field_idx, section_end_idx = find_field(lines, section, field)
    line = lines[field_idx]
    indent = " " * field_indent(line)
    if line.strip().endswith("[]"):
        lines[field_idx] = f"{indent}{field}:"
        insert_at = field_idx + 1
    else:
        insert_at = field_block_end(lines, field_idx, section_end_idx, field_indent(line))
    for offset, block_line in enumerate(block_lines):
        lines.insert(insert_at + offset, block_line)
    write_text(case_path, "\n".join(lines) + "\n")


def touch_case(case_id: str, case_date: str, checkpoint_type: str | None = None) -> None:
    set_scalar(case_id, "case_identity.updated_at", case_date)
    set_scalar(case_id, "session.last_session_date", case_date)
    if checkpoint_type is not None:
        set_scalar(case_id, "session.last_checkpoint_type", checkpoint_type)


def refresh_operator_view(case_id: str) -> None:
    client_case_path = repo_path("cases", case_id, "client-case.yaml")
    operator_view_path = repo_path("cases", case_id, "operator-view.yaml")
    parsed = parse_client_case(read_text(client_case_path))
    content = build_operator_view(case_id, parsed)
    write_text(operator_view_path, content)


def cmd_set_scalar(argv: list[str]) -> int:
    if len(argv) < 4:
        print("Usage: python scripts/update_client_case.py set-scalar <case-id> <section.field> <value>", file=sys.stderr)
        return 1
    case_id, path, value = argv[1], argv[2], argv[3]
    set_scalar(case_id, path, value)
    touch_case(case_id, today_iso())
    refresh_operator_view(case_id)
    return 0


def cmd_append_list_item(argv: list[str]) -> int:
    if len(argv) < 4:
        print(
            "Usage: python scripts/update_client_case.py append-list-item <case-id> <section.field> <value>",
            file=sys.stderr,
        )
        return 1
    case_id, path, value = argv[1], argv[2], argv[3]
    append_list_item(case_id, path, value)
    touch_case(case_id, today_iso())
    refresh_operator_view(case_id)
    return 0


def cmd_set_primary_next_action(argv: list[str]) -> int:
    if len(argv) < 3:
        print(
            "Usage: python scripts/update_client_case.py set-primary-next-action <case-id> <value>",
            file=sys.stderr,
        )
        return 1
    case_id, value = argv[1], argv[2]
    set_scalar(case_id, "tasks.primary_next_action", value)
    touch_case(case_id, today_iso())
    refresh_operator_view(case_id)
    return 0


def cmd_add_task(argv: list[str]) -> int:
    if len(argv) < 4:
        print(
            "Usage: python scripts/update_client_case.py add-task <case-id> <task-id> <title> [status] [priority] [owner]",
            file=sys.stderr,
        )
        return 1
    case_id = argv[1]
    task_id = argv[2]
    title = argv[3]
    status = argv[4] if len(argv) > 4 else "open"
    priority = argv[5] if len(argv) > 5 else "medium"
    owner = argv[6] if len(argv) > 6 else "agent"
    block = [
        f"    - task_id: {yaml_string(task_id)}",
        f"      title: {yaml_string(title)}",
        '      type: "follow_up"',
        f"      status: {yaml_string(status)}",
        f"      priority: {yaml_string(priority)}",
        f"      owner: {yaml_string(owner)}",
        "      related_subjects: []",
        "      depends_on: []",
        "      due_date: null",
        "      created_at: null",
        "      updated_at: null",
        "      done_definition: null",
        "      blocker_reason: null",
        "      notes: null",
    ]
    append_block(case_id, "tasks.backlog", block)
    touch_case(case_id, today_iso())
    refresh_operator_view(case_id)
    return 0


def cmd_add_risk(argv: list[str]) -> int:
    if len(argv) < 5:
        print(
            "Usage: python scripts/update_client_case.py add-risk <case-id> <risk-id> <severity> <summary>",
            file=sys.stderr,
        )
        return 1
    case_id = argv[1]
    risk_id = argv[2]
    severity = argv[3]
    summary = argv[4]
    block = [
        f"    - risk_id: {yaml_string(risk_id)}",
        '      category: "manual"',
        f"      severity: {yaml_string(severity)}",
        "      related_subjects: []",
        f"      summary: {yaml_string(summary)}",
        "      mitigation: null",
        '      status: "open"',
    ]
    append_block(case_id, "risks.active", block)
    touch_case(case_id, today_iso())
    refresh_operator_view(case_id)
    return 0


def cmd_touch_session(argv: list[str]) -> int:
    if len(argv) < 2:
        print(
            "Usage: python scripts/update_client_case.py touch-session <case-id> [YYYY-MM-DD] [checkpoint-type]",
            file=sys.stderr,
        )
        return 1
    case_id = argv[1]
    case_date = argv[2] if len(argv) > 2 else today_iso()
    checkpoint_type = argv[3] if len(argv) > 3 else None
    touch_case(case_id, case_date, checkpoint_type)
    refresh_operator_view(case_id)
    return 0


COMMANDS = {
    "set-scalar": cmd_set_scalar,
    "append-list-item": cmd_append_list_item,
    "set-primary-next-action": cmd_set_primary_next_action,
    "add-task": cmd_add_task,
    "add-risk": cmd_add_risk,
    "touch-session": cmd_touch_session,
}


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] not in COMMANDS:
        print(
            "Usage: python scripts/update_client_case.py "
            "<set-scalar|append-list-item|set-primary-next-action|add-task|add-risk|touch-session> ...",
            file=sys.stderr,
        )
        return 1
    return COMMANDS[argv[1]](argv[1:])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
