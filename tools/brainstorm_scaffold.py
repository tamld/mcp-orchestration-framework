#!/usr/bin/env python3
"""Scaffold a brainstorm session under the shared SoT branch."""

from __future__ import annotations

import argparse
import datetime as dt
import subprocess
from pathlib import Path

TEMPLATE = Path("brainstorm/templates/session_readme_template.md")
BASE_DIR = Path("brainstorm/sot")


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def ensure_branch(branch: str, remote: str = "origin") -> None:
    res = subprocess.run(["git", "rev-parse", "--verify", branch], capture_output=True)
    if res.returncode != 0:
        run(["git", "checkout", "-b", branch, f"{remote}/{branch}"])
    else:
        run(["git", "checkout", branch])
    run(["git", "pull", "--ff-only", remote, branch])


def scaffold(topic: str, moderator: str) -> Path:
    session_id = f"{topic}-{dt.datetime.utcnow():%Y%m%d}".replace(" ", "-")
    session_dir = BASE_DIR / session_id
    session_dir.mkdir(parents=True, exist_ok=True)
    readme = session_dir / "README.md"
    if TEMPLATE.exists():
        content = TEMPLATE.read_text().replace("<Topic>", session_id).replace("<owner>", moderator)
    else:
        content = f"# Brainstorm Session: {session_id}\n\nModerator: {moderator}\n\n"
    checklist = """\n## Quick Checklist\n- [ ] sanitize run\n- [ ] pytest (if applicable)\n- [ ] idea added with front matter\n- [ ] contribution table updated\n- [ ] decision table refreshed\n\n"""
    retro_notes = """\n## Moderator Notes\n-\n\n## What / So What / Now What\n| Stage | Notes |\n| --- | --- |\n| What |  |\n| So What |  |\n| Now What |  |\n\n"""
    readme.write_text(content + checklist + retro_notes)
    return session_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold brainstorm session")
    parser.add_argument("topic", help="Topic slug, e.g., gemini-collab")
    parser.add_argument("--moderator", default="tamld", help="Moderator name")
    args = parser.parse_args()

    ensure_branch("brainstorm/sot")
    session_dir = scaffold(args.topic, args.moderator)
    run(["git", "add", str(session_dir / "README.md")])
    run(["git", "commit", "-m", f"chore(brainstorm): scaffold {args.topic}"])
    print(f"Scaffold created at {session_dir}")


if __name__ == "__main__":
    main()
