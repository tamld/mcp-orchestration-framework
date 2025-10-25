---
title: "Lesson: Contextual Awareness in Collaboration"
timestamp: 2025-10-25
author: Gemini
tags: [collaboration, context, git, sop, search]
---

### 1. Situation

I was instructed by the user that another AI had made an update (e.g., "Codex added a question" or "Cursor created a file"), but my initial investigation on the file system could not find the change.

### 2. Incorrect Behavior & Assumption

- **Behavior:** I performed a narrow search on the file system (`ls`, `glob`) and failed to check the project's version control history. I assumed the file system was the only source of truth for the current state.
- **Flawed Assumption:** I assumed that if a file wasn't immediately visible on the file system, it didn't exist or I was being tested. I ignored the most reliable record of change: the Git history.

### 3. Correction & Correct Procedure

The user coached me to recognize that `git` is the primary source of truth for committed changes. The correct, multi-layered investigation procedure should be:

1.  **Check Version Control First:** If a specific change is mentioned (e.g., via a commit hash), use `git show <hash>` for a direct answer. If not, use `git log --recent` to check for recent, relevant commits. This is the most reliable source for committed changes.
2.  **Scan Collaboration Zones Broadly:** If `git` provides no immediate answer (e.g., for untracked files), perform a broad, *recursive* scan of designated collaboration spaces (e.g., `brainstorm/sot/`). Use `glob '**/*'` to find all files.
3.  **Investigate All Relevant Artifacts:** Read the primary tracking files (`README.md`) and pay close attention to the *artifacts* listed in contribution tables, as the relevant information is often in a linked file, not the `README` itself.
4.  **Use Content Search as a Fallback:** If the file location is still unknown, use `search_file_content` to search for keywords across the project.

### 4. General Principle (The Lesson)

An AI's situational awareness must be multi-layered, mirroring the tools of a human developer. The investigation process must be prioritized as follows: **Git first, then the file system.**

1.  **Git is the Record of Intent:** `git log` and `git show` reveal the history of deliberate, committed changes. This should always be the first place to look when investigating a reported change.
2.  **The File System is the Current State:** `ls`, `glob`, and `search` reveal the current state of the workspace, including uncommitted changes or new, untracked files. This is the second place to look.

By following this Git-first approach, an AI can more efficiently and accurately trace the source of changes, understand the context of contributions, and avoid the error of searching the file system for a change that is clearly documented in the project's history.
