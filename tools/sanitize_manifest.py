#!/usr/bin/env python3
"""
Sanitize scanner for the PoC repository.
Checks for emails, tokens, or local paths before publishing.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PATTERNS: dict[str, re.Pattern[str]] = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}", re.IGNORECASE),
    "ip_address": re.compile(r"\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b"),
    "ssh_private_key": re.compile(r"-----BEGIN (?:RSA|DSA|EC|OPENSSH) PRIVATE KEY-----"),
    "api_token": re.compile(r"(?i)(?:api|secret|token)[=:][A-Za-z0-9\\-_]{16,}"),
    "absolute_home_path": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
}

EXCLUDE = {".git", ".venv", "__pycache__", "docs/assets"}


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(str(rel).startswith(skip) for skip in EXCLUDE):
            continue
        files.append(path)
    return files


def scan(path: Path) -> list[tuple[str, str]]:
    content = path.read_text("utf-8", errors="ignore")
    findings: list[tuple[str, str]] = []
    for name, pattern in PATTERNS.items():
        if match := pattern.search(content):
            findings.append((name, match.group(0)))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Sanitize checker for MCP PoC repo.")
    parser.add_argument("--root", default=".", help="Root directory to scan.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"[sanitize] Directory not found: {root}", file=sys.stderr)
        return 1

    findings: list[tuple[Path, str, str]] = []
    for file_path in iter_files(root):
        for rule, snippet in scan(file_path):
            findings.append((file_path.relative_to(root), rule, snippet))

    if not findings:
        print("✅ No sensitive strings detected.")
        return 0

    print("⚠️ Potential sensitive strings detected:")
    for rel_path, rule, snippet in findings:
        preview = (snippet[:40] + "...") if len(snippet) > 40 else snippet
        print(f" - {rel_path}: {rule} -> \"{preview}\"")
    print("Replace with a placeholder or remove before publishing the PoC.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
