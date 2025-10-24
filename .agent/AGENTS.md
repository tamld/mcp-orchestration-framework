# Hướng dẫn Agent – MCP PoC Operations

## Nguồn chỉ đạo
- **SSoT Global**: `${MCP_ROOT}` (tham chiếu MCP-Server). Không tự ý chỉnh sửa luật.
- **Repo này**: chỉ bổ sung quy trình PoC, không được nới lỏng guardrail.
- Nếu thấy xung đột → ưu tiên Global, ghi chú vào `.agents/backlog/conflicts.yaml`.

## Bootstrap
1. Chạy `tools/bootstrap_orchestrator.sh --fast`.
2. Đọc `README.md` và `docs/design/overview.md`.
3. Thực hiện LAW-REFLECT-001: reflect → plan ≤5 bước → execute tối thiểu.

## Artefact must-have
- `tech_fit.yaml`
- `tests/PLAN.md`
- `.agents/logs/*.jsonl` (schema lấy từ `${MCP_ROOT}/schemas/aa_log.schema.json`)
- `docs/briefs/*` (Cons/Pros, roadmap) kèm checklist sanitize.

## Chính sách bảo mật
- Thay chi tiết độc quyền bằng `REDACTED`.
- Tất cả PR public phải chạy `python tools/sanitize_manifest.py --dry-run`.
- Anchors, bundle thực tế bị vô hiệu (PoC); nếu cần kích hoạt phải chuyển Gate G3 và dùng repo private.

## Checklist trước commit
- [ ] Contract phạm vi và giả định được cập nhật trong `.agents/logs/`.
- [ ] Chạy sanitize script và ghi lại kết quả.
- [ ] Bổ sung evidence link vào artefact.
- [ ] Ghi lý do nếu bỏ qua artefact “should”.

## Liên hệ
- `owner`: MCP AI Operations Team (placeholder)
- `aa_id`: điền định danh tác nhân khi log hành động.
