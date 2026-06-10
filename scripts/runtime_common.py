#!/usr/bin/env python3
from __future__ import annotations

from datetime import date
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parent.parent


def today_iso() -> str:
    return date.today().isoformat()


def repo_path(*parts: str) -> Path:
    return REPO_ROOT.joinpath(*parts)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def replace_tokens(template: str, replacements: dict[str, str]) -> str:
    content = template
    for key, value in replacements.items():
        content = content.replace(key, value)
    return content


def fail(message: str) -> "NoReturn":
    print(message, file=sys.stderr)
    raise SystemExit(1)


def ensure_absent(path: Path, kind: str) -> None:
    if path.exists():
        fail(f"{kind} already exists: {path.relative_to(REPO_ROOT)}")
