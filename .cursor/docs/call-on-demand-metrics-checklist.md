# Call-on-Demand — Metrics Checklist

> Checklist theo dõi hiệu quả tối ưu: cached_tokens, duplication_rate, latency. Dùng trước/sau khi áp dụng call-on-demand và boundary handoff.

## 1. Token & cache

| Metric | Cách đo | Mục tiêu | Ghi chú |
|--------|---------|----------|---------|
| **Token tiết kiệm** | Tổng input tokens / 1 request pipeline (trước vs sau) | Giảm ít nhất 10–20% khi dùng intent router + progressive loading | Log `usage.prompt_tokens` (và `cached_tokens` nếu API trả về). |
| **Cache hit ratio** | `cached_tokens / prompt_tokens` (khi dùng prefix-stable prompt) | Tăng tỷ lệ cache hit khi prefix giống nhau giữa request | OpenAI/Anthropic usage details. |
| **Duplication rate** | Số lần token mapping hoặc 6 CSV augment chạy trong 1 run | 1 lần cho multi-file pipeline; 1 lần cho single-file (pdr-analyze) | Kiểm tra không gọi cả pdr-analyze Bước 2–3 và comp-extraction Phase 5/7 trên cùng file set. |

## 2. Latency

| Metric | Cách đo | Mục tiêu |
|--------|---------|----------|
| **Single-feature flow** | Thời gian từ lúc bắt đầu đến khi có output (pdr-extract → pdr-analyze) | So sánh trước/sau khi chỉ load section cần thiết. |
| **Full pipeline** | Thời gian từ Resolve Input đến khi có mockup-spec.json + ui-automation/ | Giảm khi dùng .handoff/ thay vì re-parse markdown. |
| **Figma → PRD → pipeline** | Tổng thời gian figma-to-prd-md + prd-full-pipeline | Giảm khi pipeline dùng .handoff/*.json thay vì gọi Figma MCP lại. |

## 3. Boundary handoff (khi có .handoff/)

| Metric | Cách đo | Mục tiêu |
|--------|---------|----------|
| **Handoff hit rate** | Số run pipeline dùng được `.handoff/*.json` / tổng run có prd_folder từ figma-to-prd-md | Tăng khi Phase 5 ghi .handoff/ ổn định. |
| **Handoff fallback rate** | Số run phải fallback parse markdown hoặc Figma MCP / tổng run | Giảm khi handoff đủ và valid. |
| **Context continuity** | Tỷ lệ `figma_context_registry` giữ nguyên context_label/canonical_key từ upstream | 100% khi không có lý do đổi tên (evidence PRD). |

## 4. Step efficiency

| Metric | Cách đo |
|--------|---------|
| **Số skill gọi trung bình / intent** | Đếm skill thực sự được gọi (không tính skip). Ví dụ: single-feature chỉ 2 (pdr-extract, pdr-analyze); full pipeline 4–5 (Skill 0 optional). |
| **Skip rate** | design-system-gen skip khi có figma_source; prd-crossfile skip khi 1 file; visual-spec skip khi không yêu cầu spec. |

## 5. Cách thu thập (gợi ý)

- **Manual:** Chạy 3 luồng (single-feature, full pipeline, figma→prd→pipeline) trước và sau tối ưu; ghi token count và thời gian vào bảng.
- **Pipeline summary:** Bổ sung section tùy chọn trong `generation-manifest.md`: handoff_used (true/false), fallback_reason (nếu có), estimated_token_saving (nếu có).
- **API usage:** Nếu dùng OpenAI/Anthropic, log `usage.prompt_tokens_details.cached_tokens` và `prompt_tokens` mỗi request.

## 6. Tham chiếu

- Intent router & ownership: `.cursor/docs/call-on-demand-intent-router.md`
- Progressive loading: `.cursor/docs/progressive-loading-policy.md`
- Plan: Skill On-Demand Optimization.
- Phương pháp luận (industry): prompt caching (OpenAI/Anthropic), router pattern (LangChain), token architecture (Fowler), Style Dictionary, Handoff, Design System Schema — xem mục "Nguồn phương pháp luận" trong plan.
