# Public Sanitize Checklist

- [ ] Ran `python tools/sanitize_manifest.py --dry-run` with no warnings.
- [ ] README and docs stay at architecture level; proprietary details replaced with `REDACTED`.
- [ ] Repository contains no personal names, email addresses, or local home paths.
- [ ] Evidence artefacts include `author`, `aa_id`, and `purpose` fields.
- [ ] Images/diagrams originating from internal sources are redrawn or simplified SVGs.
- [ ] `.agents/backlog/conflicts.yaml` updated whenever an exception occurs.
- [ ] Gate state (G0, G1, G2…) recorded inside `.agents/logs/`.
