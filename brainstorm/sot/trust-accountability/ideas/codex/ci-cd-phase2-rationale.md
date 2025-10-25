---
author: codex
timestamp: 2025-10-25T17:10:12Z
question: "Tại sao CI/CD nên chuyển sang Phase 2 và roadmap triển khai cụ thể sẽ thế nào?"
session: trust-accountability-brainstorm
related_artifacts:
  - brainstorm/sot/trust-accountability/DECISION_POC_SCOPE.md
  - brainstorm/sot/trust-accountability/FEEDBACK_GAP_ANALYSIS.md
  - brainstorm/sot/project-product-ready-improvements/ideas/gemini/robust-ci-cd-pipeline.md
confidentiality: public-poc
---

## Reflection (LAW-REFLECT-001)
- Rà lại quyết định D-POC-SCOPE-001 và feedback gap analysis để chắc chắn Phase 1 đang khóa gói Hybrid (queue + evidence + safeguards).
- Kiểm tra đề xuất CI/CD của Gemini trong session product-ready để kế thừa thay vì tái brainstorm.
- Đánh giá rủi ro “analysis paralysis” khi kéo CI/CD vào Phase 1 lúc helper script, GPG, evidence vẫn đang hoàn thiện.

## Lý do giữ CI/CD ở Phase 2
1. **Ưu tiên hiện tại**: Phase 1A/1B tập trung chứng minh trust framework hoạt động (queue + evidence + checklist). CI/CD không phải điều kiện chặn việc học (learning) ở giai đoạn này.
2. **Chi phí triển khai**: Thiết lập pipeline (GitHub Actions/Runners, test matrix) tốn thời gian và công sức đáng kể, dễ kéo dài project khi chưa xong nền tảng Hybrid.
3. **Rủi ro loãng nguồn lực**: Nếu chia nguồn lực để vừa xây helper script vừa dựng CI/CD, khả năng cao cả hai đều dang dở → vi phạm khẩu hiệu “Reflect → Plan ≤5 bước → Execute tối giản”.
4. **Blueprint sẵn có**: Đề xuất `robust-ci-cd-pipeline.md` của Gemini đã phác roadmap chi tiết cho sản phẩm; ta có thể nhấc roadmap đó vào Phase 2 thay vì khởi động ngay.
5. **Kiểm soát kỳ vọng**: Việc ghi rõ CI/CD deferred trong `DECISION_POC_SCOPE.md` và `FEEDBACK_GAP_ANALYSIS.md` giúp giữ minh bạch với moderator/user, tránh hiểu nhầm PoC đã có pipeline hoàn chỉnh.

## Roadmap Phase 2 cho CI/CD
**Giai đoạn chuẩn bị (ngay sau khi Phase 1B hoàn tất):**
1. Tạo issue/plan item “Phase 2 – CI/CD enablement” liên kết session product-ready (assignee: Gemini + Codex).
2. Thu thập test hiện có (`tests/`) và bổ sung smoke/regression tối thiểu để pipeline có ý nghĩa.
3. Đánh giá lựa chọn runner (GitHub Actions cloud vs self-host) + bảo mật secrets.

**Milestone Phase 2A – Foundation (1-2 tuần):**
- Dựng workflow cơ bản:
  - `lint` + `pytest` (hoặc script kiểm tra tương ứng)
  - artifact trace (logs/reports) lưu vào `evidence/ci/`
  - badge/trạng thái CI cập nhật trong README hoặc session log.
- Thiết lập chính sách bắt buộc: CI phải pass trước khi merge brainstorm → main.

**Milestone Phase 2B – Guardrails mở rộng (tiếp theo):**
- Thêm static analysis, secret scan, sanitize tự động.
- Trigger pipeline cho cả nhánh brainstorm/sot để phát hiện sớm xung đột.
- Kết nối pipeline vào storyteller (showcase) nếu cần demo.

**Điểm vào Phase 3 (sản phẩm):**
- Khi CI/CD ổn định → cân nhắc container build, deploy rehearsal, policy-as-code.

## Cam kết hành động
- Sau khi checklist Phase 1A hoàn tất, mình sẽ mở issue “Phase 2 – CI/CD enablement” trích dẫn roadmap trên.
- Trong brainstorm-playbook-refresh, ghi chú rõ: CI/CD thuộc Phase 2, hãy tham chiếu file `ideas/codex/ci-cd-phase2-rationale.md` để đảm bảo mọi session sau hiểu bối cảnh.
- Khi mở Phase 2, phối hợp với Gemini (owner đề xuất pipeline) để đồng bộ test + workflow.

> Feedback (codex @2025-10-25T17:10:12Z) [INFO]: Đây là định hướng đề xuất; nếu moderator muốn kéo sớm hơn, mình sẵn sàng điều chỉnh, nhưng ưu tiên vẫn là hoàn thiện Hybrid trước khi mở mặt trận mới.
