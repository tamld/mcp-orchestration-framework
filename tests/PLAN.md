# Test Plan – MCP PoC Operations

## Scope
- Xác minh bootstrap PoC chạy được ở chế độ dry-run.
- Đảm bảo các artefact bắt buộc tồn tại và tuân thủ schema.
- Kiểm tra checklist sanitize không phát hiện rủi ro.

## Test Cases
| ID | Mô tả | Gate | Loại | Artefact |
| --- | --- | --- | --- | --- |
| TC-BOOT-01 | Chạy `tools/bootstrap_orchestrator.sh --fast` | G0 | Manual | console log |
| TC-SAN-02 | Chạy `python tools/sanitize_manifest.py --dry-run` | G1 | Automated | sanitize output |
| TC-DOC-03 | Rà soát `README.md` & `docs/briefs` đảm bảo không có dữ liệu nhạy cảm | G1 | Manual | checklist |
| TC-DEMO-04 | Thực hiện walkthrough khách hàng trong `samples/session_walkthrough.md` | G2 | Manual | feedback form |

## Automation Hooks
- Khi chuyển sang repo private (G3), tích hợp CI với `pre-commit` (ruff, markdownlint).

## Rollback Strategy
- Nếu phát hiện rò rỉ → xóa commit public, cập nhật sanitize checklist, log deviation vào `.agents/logs/`.
