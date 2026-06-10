#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import re
import sys


REPO_ROOT = Path(__file__).resolve().parent.parent
EVALS_DIR = REPO_ROOT / "evals"
CASES_DIR = EVALS_DIR / "cases"
SCENARIO_MATRIX = EVALS_DIR / "scenario-matrix.md"

DIMENSIONS = [
    "state_continuity",
    "evidence_discipline",
    "freshness_handling",
    "task_orchestration",
    "safety_and_professional_review",
    "learner_clarity_in_russian",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_matrix() -> list[dict[str, str]]:
    text = read_text(SCENARIO_MATRIX)
    rows: list[dict[str, str]] = []
    table_re = re.compile(r"^\| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$")
    for line in text.splitlines():
        match = table_re.match(line.strip())
        if not match:
            continue
        scenario, focus, type_, priority = [item.strip() for item in match.groups()]
        if scenario == "Scenario":
            continue
        rows.append(
            {
                "scenario": scenario,
                "focus": focus,
                "type": type_,
                "priority": priority,
            }
        )
    return rows


def parse_case_file(path: Path) -> dict[str, object]:
    text = read_text(path)
    title = ""
    goal = ""
    expected: list[str] = []
    fail_if: list[str] = []
    current = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if line.startswith("# "):
            title = line[2:].strip()
            continue
        if line == "## Goal":
            current = "goal"
            continue
        if line == "## Expected behavior":
            current = "expected"
            continue
        if line == "## Fail if":
            current = "fail_if"
            continue
        if line.startswith("## "):
            current = None
            continue

        stripped = line.strip()
        if current == "goal" and stripped:
            goal = stripped
        elif current == "expected" and stripped.startswith("- "):
            expected.append(stripped[2:].strip())
        elif current == "fail_if" and stripped.startswith("- "):
            fail_if.append(stripped[2:].strip())

    return {
        "title": title,
        "goal": goal,
        "expected": expected,
        "fail_if": fail_if,
        "path": path,
    }


def load_scenarios(selected: set[str] | None = None) -> list[dict[str, object]]:
    matrix = parse_matrix()
    scenarios: list[dict[str, object]] = []
    for row in matrix:
        scenario_id = row["scenario"]
        if selected and scenario_id not in selected:
            continue
        case_path = CASES_DIR / f"{scenario_id}.md"
        if not case_path.exists():
            raise FileNotFoundError(f"Missing case file for scenario: {scenario_id}")
        case_data = parse_case_file(case_path)
        scenarios.append({**row, **case_data})
    return scenarios


def render_report(scenarios: list[dict[str, object]]) -> str:
    lines = [
        "# Eval Report",
        "",
        "## Summary",
        "",
        f"- Total scenarios: {len(scenarios)}",
        "- Reviewer:",
        "- Date:",
        "- Change under review:",
        "",
        "## Scenario Results",
        "",
    ]

    for scenario in scenarios:
        lines.extend(
            [
                f"### {scenario['scenario']} — {scenario['title']}",
                "",
                f"- Focus: {scenario['focus']}",
                f"- Type: {scenario['type']}",
                f"- Priority: {scenario['priority']}",
                f"- Goal: {scenario['goal']}",
                "",
                "#### Expected Behavior",
                "",
                *[f"- {item}" for item in scenario["expected"]],
                "",
                "#### Fail If",
                "",
                *[f"- {item}" for item in scenario["fail_if"]],
                "",
                "#### Dimension Scores",
                "",
            ]
        )
        for dimension in DIMENSIONS:
            lines.append(f"- {dimension}: pass | borderline | fail")
        lines.extend(
            [
                "",
                "#### Failure Notes",
                "",
                "- First failure symptom:",
                "- Root cause guess:",
                "- Follow-up action:",
                "",
                "#### Overall Scenario Result",
                "",
                "- pass | borderline | fail",
                "",
            ]
        )

    lines.extend(
        [
            "## Release Gate Decision",
            "",
            "- Safety gate satisfied? yes | no",
            "- State continuity gate satisfied? yes | no",
            "- Freshness gate satisfied? yes | no",
            "- High/critical scenarios passing? yes | no",
            "- Final decision: pass | fail",
            "",
        ]
    )
    return "\n".join(lines)


def cmd_list(_: argparse.Namespace) -> int:
    for scenario in load_scenarios():
        print(f"{scenario['scenario']}\t{scenario['priority']}\t{scenario['focus']}")
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    selected = set(args.scenarios) if args.scenarios else None
    scenarios = load_scenarios(selected)
    report = render_report(scenarios)
    if args.output:
        output_path = Path(args.output)
        if not output_path.is_absolute():
            output_path = REPO_ROOT / output_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report + "\n", encoding="utf-8")
        print(f"Wrote report template: {output_path.relative_to(REPO_ROOT)}")
    else:
        print(report)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Cross-platform eval runner for First US Home.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List available eval scenarios")
    list_parser.set_defaults(func=cmd_list)

    report_parser = subparsers.add_parser("report", help="Generate a markdown eval report template")
    report_parser.add_argument("scenarios", nargs="*", help="Optional subset of scenario IDs")
    report_parser.add_argument("-o", "--output", help="Optional output path for the report")
    report_parser.set_defaults(func=cmd_report)

    return parser


def main(argv: list[str]) -> int:
    parser = build_parser()
    args = parser.parse_args(argv[1:])
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
