#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

from runtime_common import fail, read_text, repo_path, today_iso, write_text


def parse_scalar(value: str) -> str | None:
    cleaned = value.strip()
    if cleaned in {"null", "[]", "{}"}:
        return None
    if len(cleaned) >= 2 and cleaned[0] == cleaned[-1] and cleaned[0] in {'"', "'"}:
        return cleaned[1:-1]
    return cleaned


def parse_client_case(text: str) -> dict[str, object]:
    data: dict[str, object] = {
        "case_status": None,
        "active_path": None,
        "active_property_id": None,
        "active_lender_comparison_id": None,
        "active_dpa_shortlist_id": None,
        "active_creative_finance_case_id": None,
        "current_module": None,
        "readiness_status": None,
        "property_search_status": None,
        "lender_status": None,
        "offer_status": None,
        "closing_status": None,
        "primary_next_action": None,
        "secondary_actions": [],
        "stale_items": [],
        "tasks": [],
        "risks": [],
        "memory_update_summary": None,
    }

    top = None
    sub = None
    current_task: dict[str, str | None] | None = None
    current_risk: dict[str, str | None] | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip("\n")
        if not line.strip():
            continue

        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()

        if indent == 0 and stripped.endswith(":"):
            top = stripped[:-1]
            sub = None
            current_task = None
            current_risk = None
            continue

        if top == "case_identity" and indent == 2 and ":" in stripped:
            key, value = stripped.split(":", 1)
            if key == "case_status":
                data["case_status"] = parse_scalar(value)
            elif key == "active_path":
                data["active_path"] = parse_scalar(value)
            continue

        if top == "learning" and indent == 2 and ":" in stripped:
            key, value = stripped.split(":", 1)
            if key == "current_module":
                data["current_module"] = parse_scalar(value)
            continue

        if top == "execution" and indent == 2 and ":" in stripped:
            key, value = stripped.split(":", 1)
            parsed = parse_scalar(value)
            if key == "readiness_status":
                data["readiness_status"] = parsed
            elif key == "property_search_status":
                data["property_search_status"] = parsed
            elif key == "lender_status":
                data["lender_status"] = parsed
            elif key == "offer_status":
                data["offer_status"] = parsed
            elif key == "closing_status":
                data["closing_status"] = parsed
            continue

        if top == "properties" and indent == 2 and ":" in stripped:
            key, value = stripped.split(":", 1)
            if key == "active_property_id":
                data["active_property_id"] = parse_scalar(value)
            continue

        if top == "lenders" and indent == 2 and ":" in stripped:
            key, value = stripped.split(":", 1)
            if key == "active_lender_comparison_id":
                data["active_lender_comparison_id"] = parse_scalar(value)
            continue

        if top == "assistance_programs" and indent == 2 and ":" in stripped:
            key, value = stripped.split(":", 1)
            if key == "shortlist_id":
                data["active_dpa_shortlist_id"] = parse_scalar(value)
            continue

        if top == "creative_finance_cases" and indent == 2 and ":" in stripped:
            key, value = stripped.split(":", 1)
            if key == "active_case_id":
                data["active_creative_finance_case_id"] = parse_scalar(value)
            continue

        if top == "tasks":
            if indent == 2 and stripped.endswith(":"):
                sub = stripped[:-1]
                current_task = None
                continue
            if indent == 2 and ":" in stripped:
                key, value = stripped.split(":", 1)
                if key == "primary_next_action":
                    data["primary_next_action"] = parse_scalar(value)
                continue
            if indent == 4 and stripped.startswith("- ") and sub == "secondary_actions":
                item = parse_scalar(stripped[2:])
                if item:
                    data["secondary_actions"].append(item)
                continue
            if indent == 4 and stripped.startswith("- ") and sub == "backlog":
                current_task = {}
                payload = stripped[2:]
                if ":" in payload:
                    key, value = payload.split(":", 1)
                    current_task[key.strip()] = parse_scalar(value)
                data["tasks"].append(current_task)
                continue
            if indent == 6 and ":" in stripped and sub == "backlog" and current_task is not None:
                key, value = stripped.split(":", 1)
                current_task[key.strip()] = parse_scalar(value)
                continue

        if top == "risks":
            if indent == 2 and stripped.endswith(":"):
                sub = stripped[:-1]
                current_risk = None
                continue
            if indent == 4 and stripped.startswith("- ") and sub == "active":
                current_risk = {}
                payload = stripped[2:]
                if ":" in payload:
                    key, value = payload.split(":", 1)
                    current_risk[key.strip()] = parse_scalar(value)
                data["risks"].append(current_risk)
                continue
            if indent == 6 and ":" in stripped and sub == "active" and current_risk is not None:
                key, value = stripped.split(":", 1)
                current_risk[key.strip()] = parse_scalar(value)
                continue

        if top == "session":
            if indent == 2 and stripped.endswith(":"):
                sub = stripped[:-1]
                continue
            if indent == 2 and ":" in stripped:
                key, value = stripped.split(":", 1)
                if key == "memory_update_summary":
                    data["memory_update_summary"] = parse_scalar(value)
                continue
            if indent == 4 and stripped.startswith("- ") and sub == "stale_items":
                item = parse_scalar(stripped[2:])
                if item:
                    data["stale_items"].append(item)
                continue

    return data


def build_operator_view(case_id: str, parsed: dict[str, object]) -> str:
    tasks = parsed["tasks"]
    assert isinstance(tasks, list)
    risks = parsed["risks"]
    assert isinstance(risks, list)
    stale_items = parsed["stale_items"]
    assert isinstance(stale_items, list)
    secondary_actions = parsed["secondary_actions"]
    assert isinstance(secondary_actions, list)

    waiting_items = []
    blocked_items = []
    open_tasks = 0
    waiting_user_tasks = 0
    waiting_external_tasks = 0
    blocked_tasks = 0

    for task in tasks:
        if not isinstance(task, dict):
            continue
        title = task.get("title") or task.get("task_id") or "unnamed-task"
        status = task.get("status") or "open"
        owner = task.get("owner") or "agent"
        if status == "open":
            open_tasks += 1
        elif status == "waiting_user":
            waiting_user_tasks += 1
            waiting_items.append(f"{title} | waiting_user | {owner}")
        elif status == "waiting_external":
            waiting_external_tasks += 1
            waiting_items.append(f"{title} | waiting_external | {owner}")
        elif status == "blocked":
            blocked_tasks += 1
            blocked_items.append(f"{title} | blocked | {owner}")

    urgent_risks = []
    active_risks = 0
    for risk in risks:
        if not isinstance(risk, dict):
            continue
        active_risks += 1
        severity = risk.get("severity")
        summary = risk.get("summary") or risk.get("risk_id") or "unnamed-risk"
        if severity in {"high", "critical"}:
            urgent_risks.append(f"{summary} | {severity}")

    what_changed_last = parsed["memory_update_summary"] or f"operator view refreshed {today_iso()}"
    primary_next_action = parsed["primary_next_action"]
    what_blocks_progress = blocked_items[0] if blocked_items else (waiting_items[0] if waiting_items else None)
    if not what_blocks_progress and stale_items:
        what_blocks_progress = f"stale item requires recheck: {stale_items[0]}"
    what_to_do_now = primary_next_action or (secondary_actions[0] if secondary_actions else None)

    def emit_list(lines: list[str], key: str, items: list[str], indent: str = "  ") -> None:
        if items:
            lines.append(f"{indent}{key}:")
            for item in items:
                lines.append(f"{indent}  - {item}")
        else:
            lines.append(f"{indent}{key}: []")

    lines = [
        f"case_id: {case_id}",
        f"case_status: {parsed['case_status'] or 'in_progress'}",
        f"active_path: {parsed['active_path'] or 'compare_both'}",
        "active_subjects:",
        f"  active_property_id: {parsed['active_property_id'] or 'null'}",
        f"  active_lender_comparison_id: {parsed['active_lender_comparison_id'] or 'null'}",
        f"  active_dpa_shortlist_id: {parsed['active_dpa_shortlist_id'] or 'null'}",
        f"  active_creative_finance_case_id: {parsed['active_creative_finance_case_id'] or 'null'}",
        f"  current_module: {parsed['current_module'] or 'null'}",
        "dashboard:",
        f"  primary_next_action: {primary_next_action or 'null'}",
    ]

    emit_list(lines, "secondary_actions", secondary_actions)

    emit_list(lines, "urgent_risks", urgent_risks)
    emit_list(lines, "stale_items", stale_items)
    emit_list(lines, "waiting_items", waiting_items)
    emit_list(lines, "blocked_items", blocked_items)

    lines.extend(
        [
            "progress_snapshot:",
            f"  readiness_status: {parsed['readiness_status'] or 'not_started'}",
            f"  property_search_status: {parsed['property_search_status'] or 'not_started'}",
            f"  lender_status: {parsed['lender_status'] or 'not_started'}",
            f"  offer_status: {parsed['offer_status'] or 'not_started'}",
            f"  closing_status: {parsed['closing_status'] or 'not_started'}",
            "queue_counts:",
            f"  open_tasks: {open_tasks}",
            f"  waiting_user_tasks: {waiting_user_tasks}",
            f"  waiting_external_tasks: {waiting_external_tasks}",
            f"  blocked_tasks: {blocked_tasks}",
            f"  stale_evidence_items: {len(stale_items)}",
            f"  active_risks: {active_risks}",
            "summary:",
            f"  what_changed_last: {what_changed_last or 'null'}",
            f"  what_blocks_progress: {what_blocks_progress or 'null'}",
            f"  what_to_do_now: {what_to_do_now or 'null'}",
            "",
        ]
    )
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python scripts/update_operator_view.py <case-id>", file=sys.stderr)
        return 1

    case_id = argv[1]
    client_case_path = repo_path("cases", case_id, "client-case.yaml")
    operator_view_path = repo_path("cases", case_id, "operator-view.yaml")

    if not client_case_path.exists():
        fail(f"Case file not found: {client_case_path.relative_to(repo_path())}")

    parsed = parse_client_case(read_text(client_case_path))
    content = build_operator_view(case_id, parsed)
    write_text(operator_view_path, content)

    print("Updated:")
    print(f"  {operator_view_path.relative_to(repo_path())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
