# Checklist Sanitize PoC Public

- [ ] Đã chạy `python tools/sanitize_manifest.py --dry-run` và không còn cảnh báo.
- [ ] README và docs chỉ chứa cấp kiến trúc; mọi thông số độc quyền thay bằng `REDACTED`.
- [ ] Không có tên cá nhân, email, đường dẫn home nội bộ trong repo.
- [ ] Artefact minh chứng đã ghi chú `author`, `aa_id`, `purpose`.
- [ ] Ảnh/diagram xuất phát từ nguồn nội bộ đã được tái tạo lại dưới dạng công khai hoặc svg tối giản.
- [ ] Backlog `.agents/backlog/conflicts.yaml` cập nhật khi phát hiện ngoại lệ.
- [ ] Gate trạng thái ghi rõ (G0, G1, G2) trong `.agents/logs/`.
