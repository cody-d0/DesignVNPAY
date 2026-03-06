# Inference Rules

Cấu trúc rule: **when** (điều kiện match) → **then** (suy ra inferred_ux) + **confidence**.

## Rule mặc định

### bulk_action_mode

- **When:** pattern_group `selection_mode` có đủ instruction + counter + action (vd. text "Chọn danh bạ muốn xóa" + "Xóa (3)" + nút "Xóa").
- **Then:** use_inferred_from `selection_mode` → flow "Xóa nhiều mục (chế độ chọn)", component rows (icon header, bottom bar, checkbox).
- **Confidence:** high.

### confirm_dialog_flow

- **When:** pattern_group `confirm_dialog` có instruction + action + cancel (vd. "Bạn có chắc xóa?", "Xóa", "Hủy").
- **Then:** use_inferred_from `confirm_dialog` → flow "Xác nhận trước khi xóa", component row (Modal/Dialog).
- **Confidence:** high.

### selection_only

- **When:** Chỉ match instruction (chưa có counter/action rõ). Có thể suy luận "màn hình có khả năng chế độ chọn".
- **Then:** inferred_ux với flow_name_vi gợi ý, component_rows rút gọn; state_hint = default.
- **Confidence:** medium.

## Ngành khác (retail, healthcare)

Chỉ cần tạo file `data/text-signals-{domain}.json` theo schema (extends generic, bổ sung instruction/counter/action/tags cho domain). Rule inference dùng chung từ generic; có thể thêm rule riêng trong file domain nếu cần (mở rộng schema cho inference_rules trong file domain).

## Kết hợp với ocr_icons

Khi consumer truyền `ocr_icons` (description_or_label + position_zone): nếu có icon "xóa"/"delete"/"trash" với position_zone = "header" hoặc "right", tăng confidence cho pattern selection_mode (icon header → vào chế độ chọn). Rule không bắt buộc ocr_icons; có thì bổ sung confidence.
