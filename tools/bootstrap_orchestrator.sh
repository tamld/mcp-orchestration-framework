#!/usr/bin/env bash
set -euo pipefail

# PoC Bootstrap script — không ghi anchors thật.

usage() {
  cat <<'EOF'
PoC Bootstrap
Usage: tools/bootstrap_orchestrator.sh [--fast|--detail]
EOF
}

mode="fast"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --fast) mode="fast" ;;
    --detail) mode="detail" ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 1 ;;
  esac
  shift
done

echo "--- PoC Bootstrap ---"
echo "Repo       : mcp-poc-operations"
echo "Mode       : ${mode}"
echo "Timestamp  : $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo "Anchors    : DISABLED (PoC dry-run)"
echo "LAW CHECK  : LAW-REFLECT-001 enforced"

if [[ "${mode}" == "detail" ]]; then
  cat <<'EOF'
Tài liệu nên đọc:
- README.md
- docs/design/overview.md
- docs/briefs/sanitize_checklist.md
- MCP-Server/memory/templates/file_specifications.md (tham chiếu)
EOF
fi
