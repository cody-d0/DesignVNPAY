# Phase 0: Scan & Scope

**Chỉ áp dụng khi `node_id` trỏ đến PAGE** (nhiều sections). Khi `node_id` là section/frame cụ thể → bỏ qua Phase 0, vào Phase 1 trực tiếp.

**Mục tiêu**: Tránh gọi `get_design_context` tốn kém cho toàn bộ page khi user chỉ cần một vài sections. `get_metadata` nhẹ hơn `get_design_context` rất nhiều — dùng để scan trước.

## 0a. Metadata scan

Gọi `get_metadata(fileKey, pageNodeId)` — **không** gọi `get_design_context` ở bước này. Thu thập:
- `section_name`, `section_nodeId`, số artboards ước tính, kích thước tổng

## 0b. Hiển thị và chọn scope

| Điều kiện | Hành động |
|-----------|-----------|
| `sections.length <= 3` | Tự động ALL, không hỏi user |
| `sections.length > 3` | Hiển thị danh sách, hỏi user chọn: **ALL** / **SELECTED [ids]** / **BATCH N** |

- **ALL**: xử lý tất cả sections tuần tự
- **SELECTED [ids]**: chỉ xử lý sections được chọn (user liệt kê tên hoặc số thứ tự)
- **BATCH N**: xử lý N sections/lượt theo thứ tự, chờ confirm trước mỗi lượt

## 0c. Batch execution (khi BATCH)

- Lượt 1: Phase 1-5 cho batch đầu → tạo overview file + feature files của batch
- Lượt 2+: Phase 1-5 cho batch tiếp → append feature files vào overview đã có
- `get_variable_defs`: chỉ gọi **1 lần** ở lượt 1, reuse cho các lượt sau
- `flow_graph`: incremental — thêm edges mới ở mỗi lượt, không ghi đè
- US numbering: global counter, **không reset** giữa batches
