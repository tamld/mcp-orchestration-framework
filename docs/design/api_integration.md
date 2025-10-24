# API Integration Strategy

## Mục tiêu
- Cho phép framework PoC kết nối tới nhiều nền tảng AA bên ngoài thông qua API chuẩn hóa.
- Giữ dữ liệu vận hành dưới quyền kiểm soát của SSoT (state store) để đảm bảo traceability.

## Thành phần
| Module | Vai trò | Artefact |
| --- | --- | --- |
| `config.py` | Nạp cấu hình providers/agents/tasks từ YAML | `configs/providers.example.yaml` |
| `integrations/providers.py` | Adapter HTTP (token-based) | Placeholder class `HttpAgentClient` |
| `pipeline/executor.py` | Điều phối workflow đa tác vụ | `TaskOrchestrator` |
| `ssot/state_store.py` | Lưu assignment/result làm SSoT | `SSoTStateStore.serialize()` |

## Luồng tích hợp
1. Tải config → khởi tạo `FrameworkConfig`.
2. Tạo `AgentRegistry` để ánh xạ skill → provider.
3. Khi có tác vụ mới, `TaskOrchestrator` gọi `TaskAssignment.from_task` lấy agent phù hợp.
4. Adapter `build_provider_client` khởi tạo HTTP client sử dụng token từ biến môi trường.
5. Kết quả invoke được lưu lại trong SSoT để audit.

## Edge cases & Hạn chế
- PoC dùng `httpx.AsyncClient`; khi chuyển production cần pool connection và retries.
- SSoT hiện chỉ lưu trong bộ nhớ; nên thay bằng Redis/Postgres khi mở rộng.
- Config YAML không mã hóa credentials; chỉ lưu reference tên biến môi trường.

## Tích hợp đa provider
- Thêm adapter mới (ví dụ WebSocket, gRPC) trong `integrations/providers.py`.
- Mỗi adapter cần tuân thủ giao diện `AgentAPIClient.invoke`.
- Cập nhật `capabilities` trong YAML để gating theo khả năng provider.

## Kiểm soát & Tuân thủ
- SSoT lưu mọi assignment/result với timestamp UTC.
- Logs/artefact phải tham chiếu `serialize()` output; không đẩy dữ liệu raw khách hàng nếu chưa phê duyệt G3.
- Sanitize script vẫn áp dụng trước khi xuất bản config ví dụ công khai.
