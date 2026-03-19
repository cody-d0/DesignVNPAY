---
description: "Pipeline end-to-end: Figma → PRD .md (figma-to-prd-md) → UX Review Report (ux-review-pipe). Expect ~20-40 min tuỳ số screens."
---

# Pipeline: Figma tới UX Review (.md pack + UX Report)

Workflow này kết hợp 2 pipe chính để sinh PRD .md từ link Figma, đồng thời tự động đánh giá UI/UX trên ảnh wireframe.

**MỤC TIÊU BẮT BUỘC:** Giữ nguyên toàn bộ các lượt scan, Agent Vision đọc ảnh, và cross-reference DDL của mỗi phase để đảm bảo không thất thoát dữ liệu context hay thay đổi hành vi chuẩn của pipe.

---

## ⚓ Architectural Rule: Biên Màn Hình (Screen Boundary)

> **Định nghĩa:** Biên màn hình = **1 screen + tất cả state/variant** của screen đó.
> Nhiều artboard cùng tên (hoặc cùng `screen_type`) = **gộp vào 1 biên** (variants).
> Artboard khác tên/khác `screen_type` = **biên riêng**.
> Source of truth: `screen_boundaries` — produced at Phase 2a-bis (provisional), **locked at Merged Human Checkpoint** (sau Gate E).

**Rule này là nguyên tắc XÃ XUYÊN SUỐT toàn pipeline. Mọi gen/suy luận/tool PHẢI dựa trên biên màn hình.**

### 3 Sub-rules

| # | Sub-rule | Nghĩa | Ví dụ vi phạm |
|:---|:---|:---|:---|
| **R1** | **Lưu ảnh vào 1 folder `ui/` duy nhất** | Tất cả PNG lưu tại `{output_dir}/ui/`. KHÔNG tạo subfolder per screen. Ảnh thuộc biên nào được xác định bởi `wireframe_images[]` trong `screen_inventory.json`, KHÔNG bởi vị trí folder | ❌ Tạo `dang-nhap/ui/`, `trang-chu/ui/` rồi copy ảnh vào — gây duplicate, tăng complexity |
| **R2** | **Gen/suy luận scoped theo biên** | 1 file .md = 1 biên; UX inference gọi 1 lần per biên; OCR chạy per biên | ❌ Suy luận chung cho cả section |
| **R3** | **Tool input/output theo biên** | OCR đơn vị = 1 biên; Skill A/B/C payload per biên; score per biên | ❌ Tool chạy chung toàn section |

### Flat Output Structure (BẮT BUỘC)

```
{output_dir}/
├── SCR-XX-001-tên-màn-hình.md     ← tất cả .md ở root
├── SCR-XX-002-tên-khác.md
├── ...
├── ui/                            ← 1 folder duy nhất cho tất cả PNG
│   ├── artboard-name-1.png
│   ├── artboard-name-2.png
│   └── ...
├── .handoff/
│   ├── screen_inventory.json
│   ├── flow_graph.json
│   ├── handoff-manifest.json
│   └── ddl-context.json
├── ux-review-report.md
└── pitch-deck.html                ← mandatory (Bước 6)
```

**Anti-patterns (flat structure):**
- ❌ Tạo subfolder per screen (`dang-nhap/`, `trang-chu/`) — gây duplicate PNG + phức tạp hóa path
- ❌ Copy ảnh từ `ui/` vào subfolder `*/ui/` — KHÔNG có subfolder ui/
- ❌ Reference ảnh bằng `*/ui/*.png` glob — luôn dùng `ui/*.png`
- ❌ Tạo folder tên tiếng Việt có dấu (`Chuyển tiền nội bộ/`) — dùng slug ASCII (`chuyen-tien-noi-bo/`)

### Enforcement Map (biên màn hình thể hiện ở đâu)

| Phase/Step | File | Cách enforce |
|:---|:---|:---|
| **⛔ Gate 0** | Workflow § Bước 1 | **Output Folder Guard:** `output_dir` phải rỗng. Nếu có data → hỏi user: [A] Empty / [B] Change folder / [C] Abort |
| **Phase 2a-bis** | `phases/phase-2-inventory.md` § 2a-bis | **Boundary Detection (Round 1 — Provisional):** 6 bước (incl. Bước 2.5 icon fingerprint, **Bước 2.6 `overlay-detect` skill** — 7-signal weighted vision+metadata) + 4 assertions. Heuristic: text + icon + **overlay-detect scoring** → provisional boundaries. **NOT locked here — locked at Merged CP** |
| **Phase 2a-pre** | `phases/phase-2-inventory.md` § 2a-pre | **Single-Pass Extraction:** `text_nodes[]`, `icon_fingerprint[]`, `icon_inventory[]` từ metadata XML. 1 lần grep |
| **Phase 2d** | `phases/phase-2-inventory.md` § 2d | **Flow + Icon Trigger Inference (Round 2 — Enrichment):** 2d.1 text-based + **2d.2 agent reasoning** icon triggers + 2d.3 boundary annotation + 2d.4 flow_graph merge. May flag boundary inconsistencies for Merged CP |
| **🛑 Merged CP** | Workflow § sau Gate E | **Merged Human Checkpoint:** Show 3 tabs (Boundaries + Flow Graph + Icons). User confirms → boundaries LOCKED. If edit → redo 2a-bis..2d |
| **Phase 2f** | `phases/phase-2-inventory.md` § 2f | **Mapping ảnh ↔ biên:** `wireframe_images[k]` chỉ chứa **đúng** filename ảnh thuộc biên k. Tất cả ảnh nằm trong 1 folder `ui/`, không subfolder |
| **Phase 2g** | `phases/phase-2-inventory.md` § 2g | **OCR per biên:** Đơn vị thực thi = 1 biên; Round 1 + Round 2 trên ảnh biên k → `ocr_full_table[k]` |
| **Phase 3** | `phases/phase-3-generate.md` § 3a | **1 biên = 1 file .md ở root:** `len(screen_boundaries) == len(feature_files)`. File đặt tại `{output_dir}/{screen_id}-{slug}.md`, KHÔNG trong subfolder |
| **Phase 4e** | `phases/phase-4-augment.md` § 4e | **UX inference per biên:** `scope=screen`, payload (text_list, context_hint, ocr_icons) chỉ thuộc biên đó |
| **Pipe 2 Skill A** | `ux-review-pipe/SKILL.md` § Skill A | **consumer_payload per biên:** text_list + context_hints thuộc cùng biên |
| **Pipe 2 Skill B** | `ux-review-pipe/SKILL.md` § Skill B | **Parse .md per biên:** 1 feature file = 1 biên → `prd_ddl_report[k]` |
| **Pipe 2 Skill C** | `ux-review-pipe/SKILL.md` § Skill C | **Vision review per biên:** Đọc `wireframe_images[k]` bằng Agent Vision cho biên k |
| **Gate A** | `tools/scripts/gate-screenshot-check.sh` | Verify `{output_dir}/ui/` có ≥1 PNG (1 folder duy nhất) |
| **Boundary Gate** | Agent self-check (Phase 2a-bis) | 4 assertions: boundaries > 0, sum match, unique, triggers. **Automated** — không chờ user (user xem ở Merged CP) |
| **⚠️ Gate D** | Agent self-check (sau 2a-pre) | Icon inventory: schema validate + duplicate check. WARNING only |
| **⛔ Gate E** | Agent self-check (sau 2d.4) | Flow graph: orphan refs = HARD-FAIL; coverage ≥50% = warning |
| **⛔ Gate F** | Agent self-check (sau Phase 5) | Handoff completeness: 3 mandatory files. HARD-FAIL nếu thiếu |
| **Gate B** | `tools/scripts/gate-ocr-check.js` | Verify mỗi screen có `wireframe_images` + `ocr_full_table` |
| **Gate C** | `tools/scripts/gate-vision-files.sh` | Verify mỗi ảnh referenced trong .md tồn tại |
| **⛔ Score Gate** | `tools/ux-score-calculator.js` | Verify UX scores. Auto-fix nếu discrepancy → re-verify = 0 |

### Anti-patterns (vi phạm biên màn hình)

- ❌ Gộp text_list của 2 screens vào 1 lần gọi ux-signal-inference
- ❌ Chạy OCR cho toàn section thay vì per biên
- ❌ File .md chứa nội dung từ nhiều biên khác nhau
- ❌ `wireframe_images[k]` chứa ảnh thuộc biên khác
- ❌ Skill C ghi verdict dựa trên ảnh của biên khác
- ❌ Dùng icon trigger lookup table cứng thay vì agent reasoning (2d.2)
- ❌ Bỏ qua Phase 2a-pre icon extraction → Phase 2d thiếu signal
- ❌ Restructure (merge/split) boundaries ở Phase 2d — Phase 2d chỉ annotate + flag inconsistencies
- ❌ Lock boundaries tại Boundary Gate (2a-bis) mà không chờ Merged CP — boundaries chỉ locked SAU Gate E + user confirm
- ❌ Chạy Phase 2f/2g/3 trên provisional boundaries TRƯỚC Merged CP confirm
- ❌ **OVERLAY-AS-SCREEN:** Dùng text/icon content khác nhau để tách overlay/bottomsheet thành biên riêng khi artboard chứa cả base screen layer. **FIX:** Luôn chạy `overlay-detect` skill (`.agents/skills/overlay-detect/SKILL.md`) — 7-signal weighted detection (vision+metadata): S1 cùng tên, S2 shared header, S3 dimmed background, S4 close affordance, S5 partial coverage, S6 picker pattern, S7 supplementary action. Score ≥5/12 → PHẢI gộp vào biên cha

### Anti-patterns (generate-first — vi phạm thứ tự đọc-rồi-viết)

- ❌ **GENERATE-BEFORE-READ:** Tạo `screen_inventory.json`, `ux-review-report.md`, hoặc bất kỳ output nào mà GATE/TOOL sẽ validate, **TRƯỚC KHI** đọc source code/schema của gate/tool đó. **FIX:** Trước khi generate output file, agent PHẢI đọc validator source (VD: `gate-ocr-check.js` lines kiểm tra schema, `ux-score-calculator.js` regex parsing heading + table format) để biết exact expected format. Cost tiết kiệm: ~30s đọc vs ~5 phút sửa lại khi fail.
- ❌ **WRITE-SUMMARY-BEFORE-TOOL:** Viết overview/summary counts (Pass, Gap, Score) trong chat hoặc report header TRƯỚC KHI chạy `ux-score-calculator.js`. **FIX:** Viết placeholder `0` cho overview → chạy tool → update bằng tool output. KHÔNG bao giờ viết con số từ ước chừng.
- ❌ **SELECTIVE-OCR-TABLE:** Ghi "representative" entries vào `ocr_full_table` thay vì toàn bộ. **FIX:** `ocr_full_table` PHẢI exhaustive — ghi TẤT CẢ text items từ OCR Round 1, không selective. Gate B sẽ kiểm tra coverage (xem bên dưới).

---

## Skill References

| Skill / Pipe | Path | Vai trò |
|:---|:---|:---|
| `figma-to-prd-md` | `.cursor/skills/figma-to-prd-md/SKILL.md` | Pipe 1: Sinh PRD .md pack từ Figma |
| `ux-review-pipe` | `.cursor/skills/ux-review-pipe/SKILL.md` | Pipe 2: Review UX trên ảnh wireframe |
| `ux-signal-inference` | `.cursor/skills/ux-signal-inference/SKILL.md` | Sub-skill: Suy luận UX text signals |
| `ui-ux-pro-max` | `.agents/skills/ui-ux-pro-max/SKILL.md` | DDL data source (ux-guidelines, ux-laws, web-interface) |
| `overlay-detect` | `.agents/skills/overlay-detect/SKILL.md` | Sub-skill: 7-signal weighted overlay/modal detection (vision+metadata) |
| `ux-score-calculator` | `tools/ux-score-calculator.js` | Tool: Verify + fix UX scores (Bước 5.2, MANDATORY) |

## Tool References

| Tool | Path | Mục đích |
|:---|:---|:---|
| `figma-save-to-ui.sh` | `tools/scripts/figma-save-to-ui.sh` | Wrapper: Tải ảnh Figma → move thẳng vào `ui/` |
| `save-figma-section-screenshots.js` | `tools/scripts/save-figma-section-screenshots.js` | Core: Tải từng artboard từ Figma REST API |
| `extract-icon-inventory.js` | `tools/scripts/extract-icon-inventory.js` | Phase 2c-bis: Icon extraction + sim check (3 conventions) |
| `overlay-classify.js` | `.agents/skills/overlay-detect/scripts/overlay-classify.js` | Phase 2a-bis: Metadata pre-classifier for overlay detection |
| `gate-screenshot-check.sh` | `tools/scripts/gate-screenshot-check.sh` | Gate A: Verify `ui/` folders có PNG |
| `gate-ocr-check.js` | `tools/scripts/gate-ocr-check.js` | Gate B: Verify OCR data trong screen_inventory |
| `gate-vision-files.sh` | `tools/scripts/gate-vision-files.sh` | Gate C: Verify ảnh referenced trong .md tồn tại |
| `gate-ddl-sources.sh` | `tools/scripts/gate-ddl-sources.sh` | Gate DDL: Verify DDL data sources (10 files) |
| `ddl-prefetch.js` | `tools/scripts/ddl-prefetch.js` | Gate DDL-PF: Query DDL → output `ddl-context.json` |
| `ddl-api.js` | `DDL/scripts/ddl-api.js` | DDL Query Engine (30+ commands, 6,421 data points) |

---

## Bước 0: Pre-flight Check (BẮT BUỘC trước mọi run)

**PHẢI chạy toàn bộ checks dưới đây BẰNG TOOL trước khi bắt đầu pipeline:**

| # | Check | Cách kiểm tra | Expected |
|:---|:---|:---|:---|
| T-1 | Figma MCP access | Gọi `get_metadata()` hoặc `get_screenshot()` | Trả về data/ảnh |
| T-2 | Figma token env | `echo ${FAT:+SET} ${FIGMA_ACCESS_TOKEN:+SET}` | Ít nhất 1 = SET |
| T-3 | Save screenshot script | `node tools/scripts/save-figma-section-screenshots.js --help` | Exit 0 |
| T-4 | Save wrapper script | `bash tools/scripts/figma-save-to-ui.sh` (no args → usage) | Exit 1 + usage |
| T-5 | Gate scripts exist | `ls tools/scripts/gate-*.sh tools/scripts/gate-*.js` | ≥4 files |
| T-6 | DDL data files | `ls .agents/skills/ui-ux-pro-max/data/ux-guidelines.csv` | File exists |
| T-7 | Signal registry | `ls .cursor/skills/ux-signal-inference/data/text-signals-*.json` | ≥2 files |
| T-8 | ux-score-calculator | `node tools/ux-score-calculator.js --help` | Usage text |
| T-9 | Icon extraction tool | `node tools/scripts/extract-icon-inventory.js --test` | Self-test 14/14, exit 0 |
| T-10 | DDL API | `node DDL/scripts/ddl-api.js --stats 2>&1 \| head -5` | JSON stats output |
| T-11 | DDL Prefetch | `node tools/scripts/ddl-prefetch.js --help 2>&1` | Usage or prefetch start |
| T-12 | DDL Database | `ls DDL/design-data-layer/ddl.db` | File exists (≥2MB) |

**Nếu BẤT KỲ check nào fail → DỪNG, thông báo user cụ thể check nào fail.**

---

## Bước 1: Khởi tạo Input

1. Yêu cầu user cung cấp:
   - `figma_url` (hoặc `file_key` & `node_id`)
   - `product_name`
   - `domain` (mặc định `banking`; dùng chọn `text-signals-{domain}.json` cho Skill A)
   - Thư mục đầu ra `output_dir` (nếu không có, mặc định `{workspace}/{product-slug}/`).
2. Xác nhận thông tin.

### 🛑 HUMAN_CHECKPOINT — Gate 0: Output Folder Guard

**⚠️ AGENT: BẠN PHẢI DỪNG TẠI ĐÂY VÀ HỎI USER TRƯỚC KHI TIẾP TỤC.**
**KHÔNG được chạy bất kỳ phase nào, KHÔNG gọi get_metadata(), KHÔNG chạy pre-flight cho đến khi Gate 0 PASS.**

**Quy trình:**

```
1. HỎI user xác nhận output_dir:
   "Output folder sẽ là: `{output_dir}` — đúng không?"
   
2. Kiểm tra output_dir tồn tại chưa
   - Chưa tồn tại → mkdir -p → ✅ PASS (folder mới, rỗng)
   - Đã tồn tại → bước 3

3. Kiểm tra output_dir có rỗng không (ls -A | wc -l)
   - Rỗng (0 items) → ✅ PASS
   - Có items → bước 4

4. HIỂN THỊ cho user:
   "⚠️ Folder `{output_dir}` đã có {N} files/folders. 
    Pipeline yêu cầu folder rỗng để đảm bảo data integrity."
   
   Hỏi user chọn 1 trong 3 options:
   
   [A] Xóa toàn bộ nội dung folder → empty → tiếp tục pipeline
   [B] Chọn folder khác → quay lại bước 1 (nhập output_dir mới)
   [C] Ngừng pipeline → STOP

5. CHỜ user trả lời. KHÔNG tiến hành bất kỳ bước nào.
```

**Hành vi chi tiết:**

| Option | Hành vi | Sau đó |
|:---:|:---|:---|
| **A** (Empty) | `rm -rf {output_dir}/*` + `rm -rf {output_dir}/.handoff` | Re-verify folder rỗng → ✅ PASS |
| **B** (Change) | Yêu cầu user nhập `output_dir` mới | Quay lại Gate 0 từ đầu |
| **C** (Abort) | STOP pipeline | Thông báo: "Pipeline dừng theo yêu cầu user." |

**Anti-patterns (ĐÃ XẢY RA — KHÔNG ĐƯỢC LẶP LẠI):**
- ❌ Bỏ qua Gate 0 và nhảy thẳng vào Pre-flight / get_metadata()
- ❌ Tự xác định output_dir mà không hỏi user
- ❌ Tự động xóa folder mà không hỏi user
- ❌ Tiếp tục pipeline khi folder có data cũ (gây lẫn boundaries, ảnh, .md giữa 2 runs)

**Lưu ý:**
- Gate 0 kiểm tra cả hidden files (`.handoff/`, `.ocr_done`)
- Lệnh kiểm tra: `ls -A {output_dir} | wc -l` — nếu > 0 → có items
- Khi chọn option A, ghi log: `GATE_0_FOLDER_EMPTIED: {output_dir}, {N} items removed`

---

## Bước 2: Chạy `figma-to-prd-md` (Sinh MD Pack)

Gọi Agent bắt đầu tiến trình sinh PRD .md. **Bắt buộc bật 2 cờ:**

| Cờ | Giá trị | Hành vi |
|:---|:---:|:---|
| `enable_ocr_reconciliation` | `true` | Bắt buộc OCR bằng agent vision (2 rounds per screen) |
| `enable_ux_signal_inference` | `true` | Bắt buộc Phase 4e suy luận UX theo biên màn hình |

**Quy trình chuẩn cần tuân thủ nghiêm ngặt:**

1. **Phase 0 & 1:** Lấy node, export màn hình thành ảnh, parse cấu trúc.

### Phase 1d: Save Screenshots (CRITICAL — root cause of empty ui/)

**Với MỖI section/sub-section, BẮT BUỘC chạy lưu ảnh:**

```bash
# PREFERRED: Wrapper script (tải + move vào ui/ trong 1 bước)
bash tools/scripts/figma-save-to-ui.sh <file_key> <node_id> <output_dir>/<section>/ui

# FALLBACK: Script gốc + manual move
cd <workspace> && set -a && . ./.env && set +a && \
  node tools/scripts/save-figma-section-screenshots.js <file_key> <node_id> <temp_dir>
# Sau đó: find <temp_dir> -name "*.png" -exec mv {} <section>/ui/ \;
```

**Anti-patterns (ĐÃ XẢY RA — KHÔNG ĐƯỢC LẶP LẠI):**
- ❌ Chỉ `mkdir -p ui/` mà KHÔNG chạy script tải ảnh
- ❌ Skip Phase 1d vì "đã có metadata từ MCP" — metadata ≠ ảnh
- ❌ Tiếp tục pipeline khi ui/ rỗng
- ❌ Dùng đường dẫn `scripts/save-figma-...` (SAI) → đúng: `tools/scripts/save-figma-...`

### ⛔ Gate A: Screenshot Existence (BẮT BUỘC sau Phase 1d)

```bash
bash tools/scripts/gate-screenshot-check.sh <prd_folder>
```

- **Exit 0** → Tiếp tục Phase 2
- **Exit 1** → DỪNG pipeline. Chạy lại Phase 1d cho các section thiếu ảnh.
- **KHÔNG ĐƯỢC bypass gate này bằng agent judgment**

> **📌 CHECKPOINT #1:** Sau Gate A, xả `figma_raw` XML body khỏi context. Giữ lại: `screen_boundaries`, `screen_ids`, tên artboards.

---

2. **Phase 2 (Screen Inventory & OCR):**

   **Phase 2 Architecture: 2-Round Boundary Refinement**

   ```
   Round 1 (2a-bis): metadata heuristic → provisional_boundaries
       ▼
   Boundary Gate: 4 assertions (automated, no user wait)
       ▼
   2a-pre: text + icon extraction (based on provisional)
       ▼
   Gate D: icon validation (automated)
       ▼
   Round 2 (2d): flow inference → enriched boundaries + flow_graph
       ▼
   Gate E: flow validation (automated)
       ▼
   🛑 MERGED HUMAN CHECKPOINT: user sees ALL data → LOCK boundaries
   ```

   - **Phase 2a-bis — Boundary Detection Round 1 (Provisional):**
     - Bước 1: Liệt kê artboard (từ metadata XML)
     - Bước 2: Nhóm theo tên Figma
     - **Bước 2.5: Extract icon fingerprint** per artboard từ **cùng metadata XML** — `ic_*`, `back_*`, `drop_*`, `switch` (w≤48, h≤48). Classify flow-stage: `ic_backhome`→Kết quả, stripped icons→Xác nhận, rich icons→Khởi tạo
     - Bước 3: Heuristic **text + icon** → flow-stage grouping trước, rồi mới tách biên
     - Bước 4: Output `provisional_boundaries[]` ← **NOT final**
     - Bước 5: Self-check (4 assertions — Boundary Gate, automated)

   > **⚠️ Agent: KHÔNG DỪNG tại đây.** Boundaries là provisional. Tiếp tục 2a-pre → Gate D → 2d → Gate E → Merged CP.
   > Agent có thể log Boundary Gate results nhưng KHÔNG hỏi user confirm ở bước này.

---

   - **Phase 2a-pre (Single-Pass Extraction):** Extract `text_nodes[]`, `icon_fingerprint[]`, `icon_inventory[]` từ metadata XML trong **1 lần grep**. Replaces old Phase 2c-bis — icon extraction không còn là phase riêng.

### ⚠️ Gate D: Icon Inventory Validation (WARNING — sau Phase 2a-pre, trước 2d)

Agent tự kiểm tra:
- Mỗi icon phải có: `icon_name`, `figma_node_id`, `parent_screen_id`
- Không có duplicate `figma_node_id`
- Nếu tổng icons = 0 across ALL screens → warning `ICON_EMPTY_ALL` (không hard-fail, có screen hợp lệ không có icon)

**MUST SHOW:** Agent PHẢI hiển thị bảng số icons per screen:
```
Gate D Results:
| Screen | Icons | Categories |
|--------|------:|------------|
| SCR-XX | 12    | trigger:5, nav:3, decoration:4 |
...
Total: {N} icons, {M} screens. Gate D: PASS/WARN
```

   - **Phase 2d — Flow + Icon Trigger Inference (Round 2 — Enrichment):**
     Runs on `provisional_boundaries` from 2a-bis. Enriches but does NOT restructure.
     - 2d.1: Text-based flow (scan "Tiếp tục", nav bar)
     - 2d.2: **Agent reasoning** icon triggers — suy luận mỗi icon trigger mở screen nào, ghi confidence + reasoning log
     - 2d.3: Boundary annotation — annotate boundary_type, triggered_by. **Flag inconsistencies** (e.g., flow suggests merge/split) for Merged CP
     - 2d.4: Merge flow edges → `flow_graph.json`
     - 2d.5 **(MỚI)**: **Boundary Consistency Check** — compare flow_graph edges vs provisional boundaries. Nếu phát hiện:
       - 2 biên khác nhau nhưng flow cho thấy chung 1 flow-stage → flag `SUGGEST_MERGE`
       - 1 biên gộp artboards thuộc flow-stages khác nhau → flag `SUGGEST_SPLIT`
       - Output: `boundary_flags[]` (shown at Merged CP)

### ⛔ Gate E: Flow Graph Validation (sau Phase 2d.4)

Agent tự kiểm tra:
1. `flow_graph.edges.length > 0` — phải có ≥1 edge (WARNING nếu 0 — có thể single-screen)
2. Mọi `from_screen` và `to_screen` phải tồn tại trong `provisional_boundaries` — **HARD-FAIL** nếu vi phạm
3. Không có self-loops (`from === to`) — warning. **Ngoại lệ:** Edge với `type: "overlay_trigger"` cho phép self-loop (overlay mở bên trong cùng biên) → ghi `⚠️ OVERLAY_SELF_LOOP` thay vì `✅ No self-loops`. Đây KHÔNG phải pass — phải ghi rõ trong Gate E output.
4. Icon-inferred edges (`evidence=icon_trigger_inference`) PHẢI có `trigger_icon` + `confidence` — **HARD-FAIL** nếu thiếu
5. Coverage: ≥50% screens phải xuất hiện trong ít nhất 1 edge — WARNING nếu không đạt

**MUST SHOW:** Agent PHẢI log kết quả (hiển thị tại Merged CP):
```
Gate E Results:
✅ 1. edges.length = {N} (> 0)
✅ 2. All from/to screens exist in boundaries
⚠️ 3. {M} overlay self-loops (allowed: overlay_trigger type)
✅ 4. Icon edges have trigger_icon + confidence
⚠️ 5. Coverage: {X}% ({Y}/{Z} screens)
Gate E: PASS/FAIL
```

---

### 🛑 MERGED HUMAN CHECKPOINT — Boundary + Flow + Icon Review (SAU Gate E PASS)

**⚠️ AGENT: DỪNG TẠI ĐÂY. Hiển thị toàn bộ kết quả 3 tabs và CHỜ user xác nhận.**

**Rationale:** User thấy đủ 3 layer data (boundaries + flow_graph + icons) TRƯỚC KHI lock boundaries. Chất lượng quyết định cao hơn so với boundary-only checkpoint.

**MUST SHOW — Tab 1: Screen Boundaries (from 2a-bis)**

```
┌──────────────────────────────────────────────────────────────┐
│ SCREEN BOUNDARIES — Provisional (chờ confirm)                │
├────┬──────────────┬──────────────────────┬────────┬──────────┤
│ #  │ screen_id    │ screen_name_vi       │ type   │ artboards│
├────┼──────────────┼──────────────────────┼────────┼──────────┤
│ 1  │ SCR-XXX-001  │ {tên Figma gốc}      │ form   │ 2        │
│ 2  │ SCR-XXX-002  │ {tên Figma gốc}      │ confirm│ 1        │
│ ...│              │                      │        │          │
├────┴──────────────┴──────────────────────┴────────┴──────────┤
│ Tổng: {N} biên, {M} artboards, {V} variants gộp             │
└──────────────────────────────────────────────────────────────┘
```

Kèm chi tiết artboards per biên:
```
Biên 1: {screen_name_vi} ({screen_type})
  → Artboard: "{tên Figma gốc}" (node {id}, {w}×{h})
  → Artboard: "{tên Figma gốc}" (node {id}, {w}×{h}) — variant: {lý do gộp}
...
```

Kèm Boundary Gate assertions:
```
Boundary Gate Results:
✅ Assertion 1: screen_boundaries.length = {N} (> 0)
✅ Assertion 2: sum(artboard_node_ids) = {M} === {M} total frames
✅ Assertion 3: unique(artboard_node_ids) = {M} === {M} (no duplicates)
⚠️ Assertion 4: {status} trigger targets
```

**MUST SHOW — Tab 2: Flow Graph (from 2d)**

```
Flow Edges:
  SCR-XXX-001 ──"Tiếp tục"──→ SCR-XXX-002
  SCR-XXX-001 ──ic_contact──→ SCR-XXX-003 (confidence: 0.85)
  ...

Boundary Flags (from 2d.5):
  ⚠️ SUGGEST_SPLIT: SCR-XXX-001 contains artboards with different flow-stages
  (hoặc: ✅ No inconsistencies detected)
```

Kèm Gate E assertions.

**MUST SHOW — Tab 3: Icon Inventory (from Gate D)**

```
Gate D Results:
| Screen     | Icons | Categories                    |
|------------|------:|-------------------------------|
| SCR-XXX-001|    12 | trigger:5, nav:3, decoration:4|
...
Total: {N} icons, {M} screens. Gate D: PASS/WARN
```

**Hỏi user:**

> "Kết quả suy luận biên + flow + icon ở trên có đúng không?
> - **[Y] Đúng** → lock boundaries, tiếp tục pipeline (Phase 2f → 2g → 3 → ...)
> - **[N] Sai** → agent dừng, user chỉnh sửa
> - **[E] Chỉnh sửa** → user mô tả cần merge/split biên nào, agent sửa rồi **redo 2a-bis → 2d → show lại Merged CP**"

**CHỜ user trả lời. KHÔNG tiếp tục Phase 2f/2g/3 cho đến khi user chọn [Y].**

**Khi user chọn [Y]:**
- `provisional_boundaries` → promoted to `screen_boundaries` (locked)
- `boundaries_status: "locked"`
- Tất cả Gate D/E results vẫn valid (same boundaries)

**Naming Sync (BẮT BUỘC ngay sau lock):**
Với mỗi `screen_boundaries[k]`:
1. `main_screen_name_vi` ← `sub_sections[].name` chứa screen k (tiếng Việt có dấu)
2. `screen_type_label_vi` ← mapping từ `screen_type` (form→"Form nhập thông tin", confirm→"Xác nhận giao dịch", result→"Kết quả giao dịch", list→"Danh sách", detail→"Chi tiết", error→"Lỗi")
3. `display_name_vi` ← `{main_screen_name_vi} › {screen_type_label_vi}`
4. Gán vào `screen_boundaries[k]` và `screen_inventory.screens[k]`

**Từ bước này trở đi:** tất cả downstream (Phase 2f/2g/3/4/5, Pipe 2, report) **PHẢI** dùng `display_name_vi` làm tên hiển thị chính. `screen_id` chỉ dùng cho file paths, JSON keys.

**Khi user chọn [E]:**
- Agent sửa boundaries theo mô tả user
- **Redo:** 2a-bis (re-run) → 2a-pre → Gate D → 2d → Gate E → show Merged CP lại
- Cost: ~1-2 min (chỉ redo metadata phases, không redo screenshots)

**Anti-patterns:**
- ❌ Lock boundaries tại Boundary Gate (2a-bis) mà không chờ Merged CP
- ❌ Chỉ show boundaries mà không show flow_graph + icons
- ❌ Show count tổng ("9 biên") mà không show chi tiết từng biên
- ❌ Bỏ qua boundary_flags từ 2d.5
- ❌ Chạy Phase 2f/2g/3 trên provisional boundaries TRƯỚC user confirm

> **📌 CHECKPOINT #2:** Sau Merged CP confirm, xả `icon_inventory` raw list và reasoning intermediate. Giữ lại: `icon_trigger_edges`, `boundary_annotations`, `flow_graph`, `screen_boundaries` (locked).

   - **LƯU Ý:** Agent Vision BẮT BUỘC phải soi ảnh của mỗi screen làm 2 round:
     - **Round 1:** Extract toàn bộ Text `ocr_round1_text`.
     - **Round 2:** Extract toàn bộ Icons & vị trí `ocr_round2_icons` (bổ sung/verify `icon_inventory` từ 2c-bis).
   - Tổng hợp ra `ocr_full_table` và các `ocr_ux_improvements` theo ngữ cảnh.

> **📌 CHECKPOINT #3:** Sau Phase 2g, xả OCR intermediates (`ocr_round1_text`, `ocr_round2_icons` raw). Giữ lại: `ocr_full_table`, `ocr_gaps`, `ocr_screen_context`.

   - `screen_inventory.json` **PHẢI chứa `wireframe_images`** cho mỗi screen:
     ```json
     { "id": "screen-id", "wireframe_images": [{ "filename": "screen.png" }], "ocr_full_table": [...] }
     ```

3. **Phase 3:** Tạo folder section và nội dung PRD Draft ban đầu 5 sections.
4. **Phase 4:** Tăng cường PRD (`ui-ux-pro-max`).
   - Đặc biệt chạy **Phase 4e**: Lấy raw text/icon ở trên feed thẳng vào `ux-signal-inference` (`.cursor/skills/ux-signal-inference/SKILL.md`) → tạo `prd_extension` có `ddl_ref`. Merged vào `prd_augmented`.
5. **Phase 5:**
   - Dựng cây Output Folders. Xuất toàn bộ `.md` và copy ảnh vào `/ui`.
   - **Tạo Handoff (BẮT BUỘC):** Xuất ra thư mục `.handoff/` với đầy đủ files:

### Handoff Files Contract

| File | Bắt buộc | Nội dung |
|:---|:---:|:---|
| `screen_inventory.json` | **Có** | Danh sách screen + `consumer_payload` + **`wireframe_images`** + `ocr_full_table` + **`icon_inventory`** + **`boundary_annotations`** per screen |
| `handoff-manifest.json` | **Có** | `schema_version`, `generated_at`, `figma_source`, `flags`, `phases_completed` |
| `flow_graph.json` | **Có** | Edges giữa các screen (from, to, trigger, type) — bao gồm **icon_trigger_inference** edges |
| `figma_context_registry.json` | Tuỳ chọn | context_label, context_type, figma_source, screen_id |

**Schema version:** `figma-prd-handoff-v1`.

### ⛔ Gate F: Handoff Completeness (BẮT BUỘC sau Phase 5, trước Gate B)

Agent tự kiểm tra:
1. `.handoff/screen_inventory.json` exists + valid JSON — **HARD-FAIL**
2. `.handoff/handoff-manifest.json` exists + has `schema_version` — **HARD-FAIL**
3. `.handoff/flow_graph.json` exists + has `edges[]` — **HARD-FAIL**
4. `screen_inventory.screens.length === screen_boundaries.length` — WARNING
5. Every screen has `wireframe_images.length ≥ 1` — WARNING
6. `handoff-manifest.phases_completed` includes `"2a-bis"`, `"2a-pre"`, `"2d"` — WARNING. **Lưu ý:** Phase 2c-bis đã merge vào `"2a-pre"` (xem Phase 2a-pre spec). Chỉ check `"2a-pre"`, KHÔNG check `"2c-bis"` riêng.

**MUST SHOW:** Agent PHẢI hiển thị kết quả:
```
Gate F Results:
✅ 1. screen_inventory.json — exists, valid, {N} screens
✅ 2. handoff-manifest.json — exists, schema=figma-prd-handoff-v1
✅ 3. flow_graph.json — exists, {M} edges
⚠️ 4. Screens match: {N} inventory vs {K} boundaries
✅ 5. All screens have wireframe_images
✅ 6. phases_completed: [2a-bis, 2a-pre, 2d, ...]
Gate F: PASS/FAIL
```

> **📌 CHECKPOINT #4:** Sau Gate F, tất cả Phase 2-5 intermediate data ĐÃ GHI VÀO DISK. Xả toàn bộ in-memory Phase 2-5 data. Pipe 2 đọc lại từ `.handoff/` files.

### ⛔ Gate B: OCR Data Validation (BẮT BUỘC trước khi sang Bước 3)

```bash
node tools/scripts/gate-ocr-check.js <prd_folder>
```

- **Exit 0 (PASS)** → Tiếp tục Bước 3
- **Exit 0 (WARN)** → Tiếp tục Bước 3, nhưng có quality warnings:
  - `ocr_full_table` coverage < 50% → Agent nên bổ sung entries cho đầy đủ
  - `ocr_round2_icons` missing → Agent chưa chạy OCR Round 2 (icon vision). Nên chạy trước khi sang Skill C
- **Exit 1 (FAIL)** → DỪNG pipeline. Kiểm tra:
  - Nếu thiếu `wireframe_images` → quay lại Phase 1d
  - Nếu thiếu `ocr_full_table` → chạy lại Phase 2g
  - Nếu thiếu `ocr_round1_text` → chạy lại Phase 2g Round 1
  - **KHÔNG ĐƯỢC** ghi `ocr_done: true` vào manifest nếu Gate B chưa pass

**7 checks trong Gate B:**
1. `wireframe_images` exists + non-empty — **required**
2. `consumer_payload` exists — **required**
3. `ocr_full_table` exists + non-empty — **required** (nếu có wireframes)
4. `ocr_round1_text` is Array + non-empty — **required** (nếu có wireframes)
5. `ocr_screen_context` is String + non-empty — **required** (nếu có wireframes)
6. `ocr_full_table.length >= 50% of ocr_round1_text.length` — **warning** (coverage check)
7. `ocr_round2_icons` is Array + non-empty — **warning** (Round 2 check)

**Anti-patterns (ĐÃ XẢY RA — KHÔNG ĐƯỢC LẶP LẠI):**
- ❌ Ghi `ocr_done: true` mà không verify OCR data tồn tại
- ❌ Agent "tuyên bố" pass gate mà không chạy script verification
- ❌ `screen_inventory.json` thiếu `wireframe_images` hoặc `ocr_full_table`
- ❌ `ocr_round1_text` ghi dạng string thay vì array — Gate B check `Array.isArray()`
- ❌ `ocr_full_table` chỉ ghi "representative" entries — phải exhaustive (Check 6 sẽ warn)

---

## Bước 3: Chuyển giao dữ liệu (Handoff Preparation)

Khai báo nguồn data đầu vào cho UX review:
- `prd_folder`: Thư mục Output `output_dir` vừa được tạo.
- `consumer_payload`: Load object từ `.handoff/screen_inventory.json`.
  - **Fast-path (có `.handoff/`):** Skill A dùng trực tiếp `text_list`, `context_hint`, `ocr_icons`.
  - **Fallback (không có `.handoff/`):** Skill A tự parse .md Section 3 (chậm hơn, thiếu ocr_icons).
- `domain`: Truyền từ Bước 1 (hoặc mặc định từ `handoff-manifest.json`).

> **📌 CHECKPOINT #5:** Sau Handoff Preparation, xả toàn bộ Pipe 1 context. Pipe 2 chỉ đọc từ `.handoff/` files + `*.md` files + `ui/*.png`.

---

## Bước 4: Chạy `ux-review-pipe` (Đánh giá UI/UX)

### ⛔ Gate DDL: Data Source Verification (BẮT BUỘC trước toàn bộ Bước 4)

```bash
bash tools/scripts/gate-ddl-sources.sh
```

- **Exit 0** → Tất cả data sources tồn tại, cho phép tiếp tục
- **Exit 1** → DỪNG PIPELINE. Thiếu critical data sources → KHÔNG ĐƯỢC chạy UX Review
- **KHÔNG ĐƯỢC** chạy Skills A/B/C nếu Gate DDL fail
- **KHÔNG ĐƯỢC** fabricate DDL references

**MUST SHOW:** Agent PHẢI hiển thị kết quả Gate DDL.

### ⛔ DDL Prefetch: Structured Query (BẮT BUỘC sau Gate DDL PASS)

```bash
node tools/scripts/ddl-prefetch.js {prd_folder} --product {product_type}
```

- **Product type** tự detect từ domain: `banking`, `fintech`, `ecommerce`, etc.
- **Output:** `{prd_folder}/.handoff/ddl-context.json`
- **Exit 0** → `ddl-context.json` tạo thành công, tiếp tục Skills
- **Exit 1** → DỪNG PIPELINE. DDL query thất bại

**MUST SHOW:** Agent PHẢI hiển thị summary prefetch (components detected, guidelines loaded, laws triggered).

**DDL Prefetch query toàn bộ capabilities (1 lần, Skills tái sử dụng):**

| DDL Layer | API Command | Output field | Dùng ở |
|:---|:---|:---|:---|
| **Component Schemas** | `--component <id>` per matched component | `component_specs{}` | Skill A (state audit), Skill C (vision diff) |
| **Component Tokens** | `--component-tokens <id> --mode --platform` | `component_tokens{}` | Skill C (pixel-perfect proposals) |
| **UX Guidelines** | `--guidelines --severity High` + `--source web-interface` | `guidelines{}` | Skill B (check generation) |
| **UX Laws** | `--ux-laws` (incl. `trigger_conditions`) | `ux_laws{}` | Skill A (auto-law matching per screen) |
| **WCAG** | `--accessibility` | `wcag{}` | Skill C (contrast audit) |
| **Product Context** | `--product-type <type>` | `product_context{}` | Skill B (industry-specific checks) |
| **Color Palette** | `--color-palette <type>` | `color_palette{}` | Skill C (palette validation) |
| **Token Resolution** | `--resolve <path> --mode <mode>` | `resolved_tokens{}` | Skill C (exact values) |

**Data trong `ddl-context.json` là SOURCE OF TRUTH cho Skills A/B/C:**
- Agent PHẢI đọc file này trước khi chạy mỗi Skill
- Agent KHÔNG ĐƯỢC query DDL riêng lẻ — tất cả đã prefetch
- Agent KHÔNG ĐƯỢC bịa data không có trong `ddl-context.json`

**DDL Ref Format (MANDATORY):**
- **Guideline ref:** `UXG-{id}` (e.g., `UXG-165`, `UXG-243`) — từ `ddl-context.json → guidelines`
- **Component ref:** `COMP:{block_id}` (e.g., `COMP:otp-input-1`) — từ `component_specs`
- **Law ref:** tên law (e.g., `fitts`, `doherty`) — từ `ux_laws.auto_matches_per_screen`
- **Token ref:** `TOKEN:{path}={value}` (e.g., `TOKEN:base.destructive=#dc2626`)
- **KHÔNG ĐƯỢC** bịa refs không có trong `ddl-context.json`

**Anti-patterns (ĐÃ XẢY RA — KHÔNG ĐƯỢC LẶP LẠI):**
- ❌ Bịa DDL references (DDL-NAV-001, DDL-CTA-001...) không nằm trong bất kỳ database nào
- ❌ Nói "DDL guidelines file không tồn tại" mà không kiểm tra
- ❌ Chạy Skills A/B/C mà không chạy `ddl-prefetch.js` trước
- ❌ Dùng "kinh nghiệm chung" thay vì DDL-grounded data
- ❌ Skip `ddl-context.json` và tự suy luận
- ❌ Chỉ dùng CSV (99 rules) mà bỏ qua DDL DB (129 guidelines + 60 laws)
- ❌ Không check component specs khi DDL có component match

### ⛔ Gate C: Vision File Check (BẮT BUỘC trước Skill C)

```bash
bash tools/scripts/gate-vision-files.sh <prd_folder>
```

- **Exit 0** → Cho phép Skill C chạy vision
- **Exit 1** → DỪNG Skill C. Ảnh missing → quay lại Phase 1d
- **KHÔNG ĐƯỢC** chạy Skill C nếu Gate C fail

Thông báo Agent tiến hành Pipeline Review.

1. **Chạy Song Song (Skill A & Skill B):**

   **Skill A: Component-Aware Signal Detection**
   1. Load `ddl-context.json`
   2. For each screen, load `screen_components[screen_id]` → matched DDL components
   3. For each matched component:
      - Load `component_specs[component_id]` → get `schema.state`, `schema.layout.children`, `schema.accessibility`
      - List expected states (e.g., `otp-input-1` has `activeIndex`, `canResend`, `timeLeft`, `digits`)
      - List expected children (e.g., resend button, countdown timer)
      - List keyboard navigation (e.g., `ArrowLeft`, `ArrowRight`, `Backspace`)
      - Compare against screen variants in Figma artboards
      - **GAP = DDL spec state/child NOT found in Figma variants**
   4. Load `ux_laws.auto_matches_per_screen[screen_id]`
      - For each auto-matched law: generate mandatory check based on `trigger_conditions`
   5. Output: `signal_ddl_report` per screen with:
      - `component_gaps[]`: `{component, expected_state, found_in_figma: bool}`
      - `law_checks[]`: `{law_name, trigger, check_description}`

   **Skill B: Guideline + Product Cross-Reference**
   1. Load `ddl-context.json`
   2. Load `guidelines.high_severity` (39 rules) + `guidelines.web_interface` (30 rules, incl. 5 Critical)
   3. For each guideline:
      - Match `category` to screen type (Forms → input screens, Touch → all, Accessibility → all)
      - Generate check item with `UXG-{id}` ref + `ux_law_ref` if present
   4. Load `product_context.key_considerations` (e.g., "Security-first. Trust paramount.")
      - Generate banking-specific mandatory checks:
        - "Security-first" → OTP protection, loading state, session timeout checks
        - "Accessibility critical" → WCAG contrast, touch targets, form labels
        - "Trust paramount" → confirmation completeness, receipt accuracy, error recovery
   5. Cross-ref PRD text (Flow, User Story, NFR) against guidelines
   6. Output: `prd_ddl_report` per screen with:
      - `guideline_checks[]`: `{id, category, issue, severity, ux_law_ref}`
      - `product_checks[]`: banking-specific requirements
   7. **KHÔNG được đọc ảnh ở bước này.**

2. **Degraded Mode (khi Skill A hoặc B fail):**
   - Nếu **Skill A fail** → Skill C vẫn chạy với chỉ `prd_ddl_report` từ B. Log warning: `SKILL_A_DEGRADED`.
   - Nếu **Skill B fail** → Skill C vẫn chạy với chỉ `signal_ddl_report` từ A. Log warning: `SKILL_B_DEGRADED`.
   - Nếu **cả A và B fail** → DỪNG pipeline. Thông báo user.

3. **Skill C: DDL-Grounded Vision Review**
   - **BẮT BUỘC CHẠY SAU KHI A & B HOÀN TẤT (hoặc degraded).**
   - **Dùng Agent Vision:** Đọc trực tiếp các ảnh thư mục `ui/*.png`.

   **3 Layers kiểm tra (tất cả grounded bởi `ddl-context.json`):**

   **Layer C1 — Component Spec Diff (từ Skill A output):**
   - For each `component_gap` from Skill A:
     - Vision check: Figma screenshot có state/child này không?
     - Evidence: "DDL `otp-input-1` spec requires `canResend` state + 'Gửi lại' button. Screenshot: 6 static cells, NO resend UI."
     - Verdict: ✅ Pass nếu có | ❌ Gap nếu thiếu | ⚠️ Unverifiable nếu ảnh missing

   **Layer C2 — Token + WCAG Audit:**
   - Load `component_tokens[matched]` → verify pixel values in screenshot
     - Evidence: "DDL specifies `cellSize=48px`. Vision: cells appear ~28px."
   - Load `resolved_tokens` → check key colors
   - Check contrast: "Banner text ~ `colors.secondary-light` (#1A4B8C) on white, est. contrast 2.43:1 → FAIL WCAG AA (4.5:1)"

   **Layer C3 — Visual Discovery (traditional):**
   - Truncation, overlap, alignment, spacing anomalies
   - Issues NOT covered by DDL specs
   - Cross-reference with Skill B `guideline_checks`

   **Evidence Format:**
   - Component gap: "DDL `{block_id}` spec: `{state_name}`. Screenshot: {observation}."
   - Token gap: "DDL `TOKEN:{path}={value}`. Vision: {measurement}."
   - WCAG: "Color {hex}, est. contrast {ratio}:1 vs {bg}. {PASS|FAIL} WCAG AA."
   - Guideline: "UXG-{id} ({issue}): {observation}."

   **RULES:**
   - Nếu file ảnh KHÔNG TỒN TẠI → verdict PHẢI = "unverifiable"
   - Nếu `component_specs` có component match → **checklist MANDATORY**, không phải optional discovery
   - Nếu `ux_laws.auto_matches_per_screen` có law match → PHẢI có check item cho law đó

   **Anti-patterns cho Skill C (ĐÃ XẢY RA — KHÔNG ĐƯỢC LẶP LẠI):**
   - ❌ Suy luận verdict "pass" từ `consumer_payload` text khi ảnh không tồn tại
   - ❌ Ghi evidence `"CTA height=44px"` mà không thực sự vision-check ảnh
   - ❌ Toàn bộ evidence_note dựa trên text inference thay vì "Từ ảnh: ..."
   - ❌ Bỏ qua DDL component spec khi có match (e.g., có `otp-input-1` match nhưng không check states)
   - ❌ Nhận token values từ DDL nhưng không compare với ảnh

---

## Bước 5: Tổng hợp và Kết thúc

1. Tổng hợp thành `{prd_folder}/ux-review-report.md`.

2. **⛔ Tool-Verified Scoring (MANDATORY — không được bỏ qua):**
   - Chạy: `node tools/ux-score-calculator.js run --json {prd_folder}/ux-review-report.md`
   - **Nếu có discrepancies** (exit code 3):
     - Chạy `node tools/ux-score-calculator.js run --fix {prd_folder}/ux-review-report.md` để sửa tự động.
     - Chạy lại `run` để verify: exit code **PHẢI = 0** (zero discrepancies).
   - **Chỉ report metrics từ output của tool** — KHÔNG count bằng tay, KHÔNG dùng con số tự viết trong overview header.
   - Scoring model: **Simple Score** (pass/total) + **Weighted Score** (severity-based penalty: Critical=3.0, Major=2.0, Minor=1.0).

   **Anti-pattern (lỗi đã xảy ra — KHÔNG ĐƯỢC lặp lại):**
   - ❌ Viết overview header (Tổng check, Pass, Gap, Score) bằng tay trước khi viết per-screen tables
   - ❌ Count pass/gap bằng ước chừng hoặc "hiểu tổng quát"
   - ❌ Report UX Score chưa qua tool verification

3. Thông báo Output Summary (Pass, Gap, Unverifiable) cho user. Mở file Report để user kiểm tra các lỗi Critical/Major.
4. Nếu degraded mode → ghi rõ trong report: "⚠️ Degraded: Skill X không chạy được — report thiếu coverage từ skill đó."

> **📌 CHECKPOINT #6:** Pipeline hoàn tất. Report on disk. Xả toàn bộ context.

## Bước 6: Pitch Deck (BẮT BUỘC)

Sử dụng skill `ux-audit-pitch-deck` để tạo HTML pitch deck chuyên nghiệp.

1. Đọc `ux-review-report.md` + `.handoff/ddl-context.json` + screenshots từ `ui/*.png`
2. Tạo `{prd_folder}/pitch-deck.html` theo cấu trúc NNg: Executive Summary → Methodology → Detailed Findings → Heuristic Scorecard → Action Plan
3. **Finding cards**: Layout 2-column (40:60 ratio) — phone-frame screenshot trái, structured info phải
4. **Bắt buộc**: Sanitize PII, viết đầy đủ không viết tắt, mỗi UXP có ảnh minh hoạ
5. **Loại bỏ**: KHÔNG include quality gates, pipeline timestamps, internal tooling references — đây là internal metadata, không thuộc client-facing deliverable
6. Mở trong browser để xác nhận rendering

**Anti-patterns:**
- ❌ Bỏ qua Bước 6 vì "user không yêu cầu" — pitch-deck là MANDATORY, luôn tạo
- ❌ Dùng `*/ui/*.png` glob — luôn dùng `ui/*.png` (flat structure)

> **📌 CHECKPOINT #7:** Pitch deck on disk. Thông báo user để review.

---

## Context Checkpoint Summary

| CP | Vị trí | Xả | Giữ lại |
|:---:|:---|:---|:---|
| **CP1** | Sau Gate A | `figma_raw` XML body | `provisional_boundaries`, `screen_ids`, artboard names |
| **CP2** | Sau **Merged CP** confirm | `icon_inventory` raw, reasoning intermediate | `icon_trigger_edges`, `boundary_annotations`, `flow_graph`, `screen_boundaries` (locked) |
| **CP3** | Sau Phase 2g | `ocr_round1_text`, `ocr_round2_icons` raw | `ocr_full_table`, `ocr_gaps`, `ocr_screen_context` |
| **CP4** | Sau Gate F | **Tất cả Phase 2-5 in-memory** | Paths to `.handoff/` files |
| **CP5** | Sau Handoff prep | Toàn bộ Pipe 1 context | `consumer_payload` (from file) |
| **CP6** | Sau Score | Toàn bộ | `ux-review-report.md` path |

## Gate Summary

| Gate | Tier | Type | Vị trí | Script/Method | Evidence | Fail behavior |
|:---|:---:|:---:|:---|:---|:---:|:---|
| **0** | 🛑 T3 | Human CP | Sau Bước 1 | `ls -A` + **user prompt** | User confirms | 3 options: Empty / Change / Abort |
| **A** | 🔧 T1 | Script | Sau 1d | `gate-screenshot-check.sh` | Exit code | STOP pipeline |
| **Boundary** | 🤖 T2 | Agent auto | Phase 2a-bis | 4 assertions (automated) | Log | STOP nếu 1-3 FAIL (auto, no user wait) |
| **D** | 🤖 T2 | Agent auto | Sau 2a-pre | Schema + dedup check | Log | Warning only |
| **E** | 🤖 T2 | Agent auto | Sau 2d.4 | 5 assertions | Log | Hard-fail orphan + missing fields |
| **Merged CP** | 🛑 T3 | Human CP + MUST SHOW | **Sau Gate E** | 3 tabs: Boundaries + Flow + Icons | User [Y]/[N]/[E] | Lock boundaries hoặc redo 2a-bis..2d |
| **F** | 🤖 T2 | Agent + MUST SHOW | Sau Phase 5 | File existence + JSON | Table | STOP if missing mandatory |
| **B** | 🔧 T1 | Script | Trước Bước 3 | `gate-ocr-check.js` | Exit code | STOP pipeline |
| **DDL** | 🔧 T1 | Script + MUST SHOW | **Trước Bước 4** | `gate-ddl-sources.sh` | Exit code | STOP pipeline — KHÔNG được bịa refs |
| **DDL-PF** | 🔧 T1 | Script + MUST SHOW | **Sau Gate DDL** | `ddl-prefetch.js` | `ddl-context.json` | STOP — DDL prefetch thất bại |
| **C** | 🔧 T1 | Script | Trước Skill C | `gate-vision-files.sh` | Exit code | STOP Skill C |
| **Score** | 🔧 T1 | Script | Sau report | `ux-score-calculator.js` | Exit code | Auto-fix + re-verify |

**Enforcement Tiers:**
- **🔧 T1** — Script-enforced: exit code blocks pipeline. Cannot bypass.
- **🤖 T2** — Agent self-check + log evidence. Agent cannot just say "PASS". Results displayed at Merged CP.
- **🛑 T3** — Human checkpoint: agent MUST STOP, SHOW full evidence, and WAIT for user response. (Gate 0: output folder, **Merged CP**: boundaries + flow + icons)
