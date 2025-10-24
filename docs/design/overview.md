# MCP PoC Operations – Kiến trúc & Value Stream

## 1. Mục tiêu
- Chứng minh quy trình vận hành MCP-Server ở quy mô nhỏ cho khách hàng quan sát.
- Giữ bí mật kỹ thuật bằng cách chỉ công khai thành phần chiến lược.
- Chuẩn bị nền tảng để nâng cấp nhanh thành sản phẩm đầy đủ sau khi PoC được duyệt.

## 2. Kiến trúc framework (rút gọn)
```
+------------------+      +------------------+      +---------------------+
| Global MCP SSoT  | ---> | PoC Bootstrapper | ---> | Framework Core      |
+------------------+      +------------------+      +---------------------+
         |                          |                         |
         v                          v                         v
 +----------------------+   +------------------+   +-----------------------+
 | Policies & Templates |   | Task Contracts   |   | API Integrations (AA) |
 +----------------------+   +------------------+   +-----------------------+
                                                          |
                                                          v
                                               +--------------------------+
                                               | SSoT State Store (PoC)   |
                                               +--------------------------+
```

- **Framework Core** (`src/mcp_poc_framework/`):
  - `config.py`: nạp providers/agents/tasks từ YAML.
  - `agents/registry.py`: ánh xạ skill → agent → provider.
  - `pipeline/executor.py`: điều phối tác vụ, ghi nhận kết quả.
  - `tasks/scheduler.py`: chọn agent phù hợp theo skill matrix.
  - `integrations/providers.py`: adapter HTTP (đa nền tảng AA) → mở rộng sang gRPC/WebSocket khi cần.
  - `ssot/state_store.py`: SSoT in-memory, dễ nâng cấp thành dịch vụ riêng.
- **Policies & Templates**: kế thừa guardrail MCP-Server, đảm bảo artefact có bằng chứng.
- **Task Contracts**: `memory/templates/contract_template.md` + `configs/providers.example.yaml`.
- **Secure Channel**: placeholder Gate G3 (repo private, lưu trữ bí mật thực sự).

## 3. Value Stream
1. Nhận yêu cầu khách hàng → ghi contract vào `.agents/logs/`.
2. Chạy bootstrap (LAW-REFLECT-001) → sinh kế hoạch ≤5 bước.
3. Thực thi tác vụ tối thiểu, lưu evidence (`docs/`, `samples/`).
4. Gate Review (G0 → G2) xác nhận PoC đáp ứng tiêu chí.
5. Nếu khách hàng ký kết → chuyển sang repo private, bật Secure Channel.

## 4. Bảo mật & Sanitize
- Script `tools/sanitize_manifest.py` quét email, token, đường dẫn nội bộ.
- Checklist tại `docs/briefs/sanitize_checklist.md` giúp kiểm tra thủ công trước khi công bố.
- Artefact chứa `REDACTED` thay vì thông số nhạy cảm.

## 5. Lộ trình nâng cấp
| Gate | Tiêu chí | Bằng chứng |
| --- | --- | --- |
| G0 | Repo skeleton, luật liên kết MCP | README.md, .agent/AGENTS.md |
| G1 | Artefact must-have + sanitize pass | tech_fit.yaml, tests/PLAN.md |
| G2 | Demo end-to-end + log khách hàng | samples/session_walkthrough.md |
| G3 | Chuyển sang triển khai riêng | Tài liệu thương mại (không public) |

## 6. Rủi ro & Biện pháp
- **Rò rỉ NDA**: bắt buộc chạy sanitize script và đánh giá thủ công → log kết quả.
- **Nhầm lẫn phạm vi**: README chỉ mô tả strategic module, chi tiết kỹ thuật để trống.
- **Thiếu minh chứng**: cung cấp artefact mẫu nhưng không chứa thông tin bí mật.
