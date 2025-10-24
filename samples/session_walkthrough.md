# Walkthrough Demo – MCP PoC Operations

## Bối cảnh
yêu cầu khách hàng: "Cho thấy cách các agent MCP lên kế hoạch và ghi log mà không lộ bí mật."

## Các bước trình diễn
1. **Bootstrap** – chạy `./tools/bootstrap_orchestrator.sh --fast` và trình chiếu log.
2. **Reflection** – mở template `memory/templates/contract_template.md`, điền tóm tắt (ẩn chi tiết).
3. **Thực thi** – cập nhật README (chỉ giới thiệu kiến trúc) và ghi evidence vào `.agents/logs/`.
4. **Review** – duyệt checklist `docs/briefs/sanitize_checklist.md` trước khi push.

## Kết quả kỳ vọng
- Khách hàng thấy toàn bộ quy trình tuân thủ guardrail.
- Không có dữ liệu nhạy cảm hiển thị.
- Log minh chứng khẳng định các bước đã thực hiện.

> Ghi chú: PoC không bật chức năng ghi anchors thật. Mọi yêu cầu nâng cấp phải được thương thảo ở Gate G3.
