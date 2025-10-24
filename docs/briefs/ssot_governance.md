# SSoT Governance Snapshot

## Nguyên tắc chính
- **One true state**: mọi assignment/task result đều lưu qua `SSoTStateStore`.
- **Bằng chứng bắt buộc**: artefact công khai phải chỉ rõ nguồn dữ liệu (ví dụ `serialize()` dump).
- **Không tự động sync** ra môi trường production khi chưa qua Gate G3.

## Kiểm soát trong PoC
- Store ở bộ nhớ (RAM) nhưng cung cấp API xuất JSON để nhúng vào báo cáo.
- Kết hợp log `.agents/logs/` cho phép backtrace hành động → task → agent.
- Checklist sanitize kiểm tra không rò rỉ token/base_url riêng.

## Lộ trình nâng cấp
| Giai đoạn | Hành động | Bằng chứng |
| --- | --- | --- |
| G1 | Thêm export JSON ra `memory/anchors/staged/` | Bản dump audit |
| G2 | Gắn CI upload artefact lên kho bảo mật | Log CI |
| G3 | Triển khai SSoT thật (Postgres/Redis) + encryption at rest | Tài liệu kiến trúc riêng |

## Deviation Policy
- Mọi sai lệch khỏi quy trình SSoT phải log vào `.agents/backlog/conflicts.yaml` với `deviation.reason`.
