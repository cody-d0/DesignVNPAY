---
description: "Pipeline end-to-end: Figma → PRD .md (figma-to-prd-md) → UX Review Report (ux-review-pipe). Expect ~20-40 min tuỳ số screens."
---

# Pipeline: Figma tới UX Review (.md pack + UX Report)

Workflow này kết hợp 2 pipe chính để sinh PRD .md từ link Figma, đồng thời tự động đánh giá UI/UX trên ảnh wireframe.

**MỤC TIÊU BẮT BUỘC:** Giữ nguyên toàn bộ các lượt scan, Agent Vision đọc ảnh, và cross-reference DDL của mỗi phase để đảm bảo không thất thoát dữ liệu context hay thay đổi hành vi chuẩn của pipe.

## Skill References

| Skill / Pipe | Path | Vai trò |
|:---|:---|:---|
| `figma-to-prd-md` | `.cursor/skills/figma-to-prd-md/SKILL.md` | Pipe 1: Sinh PRD .md pack từ Figma |
| `ux-review-pipe` | `.cursor/skills/ux-review-pipe/SKILL.md` | Pipe 2: Review UX trên ảnh wireframe |
| `ux-signal-inference` | `.cursor/skills/ux-signal-inference/SKILL.md` | Sub-skill: Suy luận UX text signals |
| `ui-ux-pro-max` | `.agents/skills/ui-ux-pro-max/SKILL.md` | DDL data source (ux-guidelines, ux-laws, web-interface) |

## Bước 1: Khởi tạo Input

1. Yêu cầu user cung cấp:
   - `figma_url` (hoặc `file_key` & `node_id`)
   - `product_name`
   - `domain` (mặc định `banking`; dùng chọn `text-signals-{domain}.json` cho Skill A)
   - Thư mục đầu ra `output_dir` (nếu không có, mặc định `{workspace}/{product-slug}/`).
2. Xác nhận thông tin và bắt đầu thực pipeline.

## Bước 2: Chạy `figma-to-prd-md` (Sinh MD Pack)

Gọi Agent bắt đầu tiến trình sinh PRD .md. **Bắt buộc bật 2 cờ:**

| Cờ | Giá trị | Hành vi |
|:---|:---:|:---|
| `enable_ocr_reconciliation` | `true` | Bắt buộc OCR bằng agent vision (2 rounds per screen) |
| `enable_ux_signal_inference` | `true` | Bắt buộc Phase 4e suy luận UX theo biên màn hình |

**Quy trình chuẩn cần tuân thủ nghiêm ngặt:**
1. **Phase 0 & 1:** Lấy node, export màn hình thành ảnh, parse cấu trúc.
2. **Phase 2 (Screen Inventory & OCR):**
   - Gom nhóm `screen_boundaries`.
   - **LƯU Ý:** Agent Vision BẮT BUỘC phải soi ảnh của mỗi screen làm 2 round:
     - **Round 1:** Extract toàn bộ Text `ocr_round1_text`.
     - **Round 2:** Extract toàn bộ Icons & vị trí `ocr_round2_icons`.
   - Tổng hợp ra `ocr_full_table` và các `ocr_ux_improvements` theo ngữ cảnh.
3. **Phase 3:** Tạo folder section và nội dung PRD Draft ban đầu 5 sections.
4. **Phase 4:** Tăng cường PRD (`ui-ux-pro-max`).
   - Đặc biệt chạy **Phase 4e**: Lấy raw text/icon ở trên feed thẳng vào `ux-signal-inference` (`.cursor/skills/ux-signal-inference/SKILL.md`) → tạo `prd_extension` có `ddl_ref`. Merged vào `prd_augmented`.
5. **Phase 5:**
   - Dựng cây Output Folders. Xuất toàn bộ `.md` và copy ảnh vào `/ui`.
   - **Tạo Handoff (BẮT BUỘC):** Xuất ra thư mục `.handoff/` với đầy đủ files:

### Handoff Files Contract

| File | Bắt buộc | Nội dung |
|:---|:---:|:---|
| `screen_inventory.json` | **Có** | Danh sách screen + `consumer_payload` per screen (text_list, context_hint, ocr_icons, ocr_screen_context) |
| `handoff-manifest.json` | **Có** | `schema_version`, `generated_at`, `figma_source`, `flags`, `phases_completed` |
| `flow_graph.json` | Nên có | Edges giữa các screen (from, to, trigger, type) |
| `figma_context_registry.json` | Tuỳ chọn | context_label, context_type, figma_source, screen_id |

**Schema version:** `figma-prd-handoff-v1`.

## Gate Check: Trước khi sang Bước 3

**BẮT BUỘC verify trước khi chuyển giao:**
1. File `.handoff/.ocr_done` tồn tại (hoặc `handoff-manifest.json` có `"ocr_done": true`).
2. Mọi screen có ảnh phải có `ocr_full_table` trong `screen_inventory.json`.
3. Nếu thiếu → **DỪNG pipeline**, thông báo user: "OCR chưa hoàn tất cho screen X. Chạy lại Phase 2g hoặc 2g-bis."

## Bước 3: Chuyển giao dữ liệu (Handoff Preparation)

Khai báo nguồn data đầu vào cho UX review:
- `prd_folder`: Thư mục Output `output_dir` vừa được tạo.
- `consumer_payload`: Load object từ `.handoff/screen_inventory.json`.
  - **Fast-path (có `.handoff/`):** Skill A dùng trực tiếp `text_list`, `context_hint`, `ocr_icons`.
  - **Fallback (không có `.handoff/`):** Skill A tự parse .md Section 3 (chậm hơn, thiếu ocr_icons).
- `domain`: Truyền từ Bước 1 (hoặc mặc định từ `handoff-manifest.json`).

## Bước 4: Chạy `ux-review-pipe` (Đánh giá UI/UX)

Thông báo Agent tiến hành Pipeline Review.

1. **Chạy Song Song (Skill A & Skill B):**
   - **Skill A:** Inference & DDL Report. Dùng parameters từ `consumer_payload` (hoặc fallback parse Section 3) để detect signal (action, error, state) dựa vào DDL.
   - **Skill B:** PRD Context DDL. Đọc nội dung Flow, User Story, và NFR để cross-ref với rules DDL (Back button logic, States mapping, Touch target, v.v.). **KHÔNG được đọc ảnh ở bước này.**

2. **Degraded Mode (khi Skill A hoặc B fail):**
   - Nếu **Skill A fail** → Skill C vẫn chạy với chỉ `prd_ddl_report` từ B. Log warning: `SKILL_A_DEGRADED`.
   - Nếu **Skill B fail** → Skill C vẫn chạy với chỉ `signal_ddl_report` từ A. Log warning: `SKILL_B_DEGRADED`.
   - Nếu **cả A và B fail** → DỪNG pipeline. Thông báo user.

3. **Skill C (Vision Review + Đề xuất):**
   - **BẮT BUỘC CHẠY SAU KHI A & B HOÀN TẤT (hoặc degraded).**
   - **Dùng Agent Vision:** Đọc trực tiếp các ảnh thư mục `ui/*.png`. (Bắt buộc dùng agent vision ở bước này để kiểm định, bất kể Pipe 1 đã chạy vision hay chưa).
   - Đối chiếu chéo 2 list errors/gaps từ A và B với bức ảnh xem màn hình code/design đã có chưa. (evidence/verdict).
   - Khám phá lỗi trực quan (contrast, truncation, overlap layout).
   - Tự động map vấn đề với `DDL` và trả lại đề xuất **cụ thể** (thay text cục bộ, di chuyển button, bổ sung outline, v.v.).

## Bước 5: Tổng hợp và Kết thúc

1. Tổng hợp thành `{prd_folder}/ux-review-report.md`.
2. Thông báo Output Summary (Pass, Gap, Unverifiable) cho user. Mở file Report để user kiểm tra các lỗi Critical/Major.
3. Nếu degraded mode → ghi rõ trong report: "⚠️ Degraded: Skill X không chạy được — report thiếu coverage từ skill đó."
