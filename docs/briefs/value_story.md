# Value Story – MCP PoC Operations

## Persona mục tiêu
- **Khách hàng doanh nghiệp** đang cân nhắc áp dụng AI Agent cho vận hành nội bộ.
- **Đội ngũ kỹ thuật** cần hiểu cách PoC kiểm soát rủi ro nhưng chưa muốn lộ bí quyết.

## Tuyên bố giá trị
> "Quan sát được toàn bộ quy trình điều hành MCP mà không cần truy cập vào kỹ thuật độc quyền."

## Tác động dự kiến
| Thời điểm | Tác động | Chứng minh |
| --- | --- | --- |
| Ngắn hạn | Khách hàng hiểu luồng vận hành và guardrail | README, mermaid workflow |
| Trung hạn | Khách hàng tin tưởng cơ chế kiểm soát rủi ro | Sanitize checklist, log JSONL |
| Dài hạn | Bước đệm để triển khai sản phẩm thật | Gate roadmap, tech_fit.yaml |

## Hạn mức chia sẻ
- Không cung cấp pipeline CI/CD thực tế.
- Không đưa tài sản trí tuệ (model, prompt chuyên biệt).
- Mọi request đào sâu kỹ thuật sẽ chuyển sang giai đoạn thương mại hóa (Gate G3).
