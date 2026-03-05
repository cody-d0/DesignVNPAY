# Reuse device frame — gen 1 lần, reuse khung iPhone

**DEPRECATED.** Quy trình này không còn được dùng. Mockup screen (type = "screen") dùng **canvas trắng 600×free, margin 5%**, không vẽ khung thiết bị (device frame). Xem MOCKUP_DESIGN_SYSTEM.md và CANVAS_RULES.md. Tài liệu dưới đây giữ lại chỉ để tham khảo lịch sử.

---

Tài liệu chuẩn cho quy trình **sinh một lần khung iPhone, reuse cho mọi mockup** khi spec type = `"screen"` hoặc nội dung phân loại = **Screen**. Đảm bảo đồng nhất từ lớp thiết bị trở lên.

Tham chiếu: MOCKUP_DESIGN_SYSTEM.md, CANVAS_RULES.md, img-to-mockup SKILL.md, md-to-mockup SKILL.md.

---

## Khi nào dùng

- **img-to-mockup:** Khi có ít nhất một spec với `type === "screen"`.
- **md-to-mockup:** Khi phân loại nội dung .md = **Screen** (có `# Screen:` / Component Stack / Mobile Layout).

Khi không (vd. chỉ state_guide): không vẽ khung máy; không dùng tài liệu này.

---

## Kích thước mockup (canvas) — 1:2 vertical

Mọi mockup (full canvas và device frame) cho frame/screen dùng **tỷ lệ 1:2 vertical** (width : height = 1 : 2, portrait). File ảnh output phải **portrait**, margin **5% mỗi cạnh** (bằng nhau bốn cạnh). Sau khi gen, có thể chuẩn hóa bằng `scripts/normalize-mockup-canvas.py` để đảm bảo đúng tỉ lệ và margin.

| Biến | Giá trị | Mô tả |
|------|---------|--------|
| **Canvas ratio** | **1:2 vertical** (portrait) | width : height = 1 : 2. Chiều cao gấp đôi chiều ngang. |

---

## Spec khung thiết bị (device frame) — gen một lần

- **Output:** Một ảnh .png duy nhất: khung iPhone front-view, Dynamic Island, **bên trong chỉ vùng màn hình trống** (nền #FFFFFF hoặc #FAFAFA), không vẽ UI.
- **Canvas:** Tỷ lệ **1:2 vertical** (portrait).
- **Device:** 90% chiều cao và 90% chiều ngang canvas, căn giữa.
- **Dynamic Island:** Hình pill ở giữa cạnh trên khung máy, ~12% chiều ngang màn hình.
- **Nét vẽ:** Đen #000000, wobbly hand-drawn; không accent trong frame (chỉ viền).

**Prompt mẫu (device frame only):**

```
Hand-drawn low-fi smartphone frame only. No UI content inside. Strict rules: Portrait, front view only (no tilt, no 3D). Canvas ratio 1:2 vertical (portrait). Device frame fills 90% height and 90% width, centered. Dynamic Island: one pill shape at top center of the frame, about 12% of screen width. Inside the frame: empty screen area, solid white or #FAFAFA background only. Lines: black #000000, wobbly hand-drawn style. No buttons, no text, no icons inside the screen. No accent color.
```

Lưu vào `output_dir` với tên cố định, vd. `device-frame.png`. Sau đó chạy `scripts/normalize-mockup-canvas.py` (vd. `--in-place`) để ép đúng 1:2, width đồng nhất (mặc định 400px), margin 5% bốn cạnh.

---

## Spec content-only — gen cho từng spec

- **Output:** Chỉ nội dung wireframe (header, body, nút, FAB, …) trên nền trắng; **không** vẽ viền máy, không Dynamic Island.
- **Canvas:** Tỷ lệ **trùng với vùng màn hình bên trong** device frame để khi composite không méo.

**Tính vùng màn hình trong device frame (theo %):**

- Device = 90% width, 90% height canvas, căn giữa.
- Padding nội dung (trong device): ~6% chiều ngang trái/phải, ~4% chiều cao trên/dưới (theo MOCKUP_DESIGN_SYSTEM).
- Vùng content = 88% width × 92% height của device.

**Tỷ lệ content-only canvas:** Tỷ lệ trùng vùng content trong device (portrait, tương đương 1 : 2.09). **Chỉ dùng khi composite vào device frame.** Khi tạo mockup screen **đứng riêng** (không composite), bắt buộc dùng MOCKUP_DESIGN_SYSTEM Block 1 (screen) với **portrait 1:2**, không dùng prompt 1:2.09 bên dưới.

**Prompt content-only:** Dùng cùng line color, line weight, accent #7DD3FC, typography từ MOCKUP_DESIGN_SYSTEM (Block 1) nhưng **bỏ** mọi mô tả device frame/island. Chỉ mô tả nội dung màn hình (Block 2: screen_title + component_stack_text). Ví dụ:

```
Hand-drawn low-fi wireframe content only. No phone frame, no device border, no Dynamic Island. Canvas ratio same as inner content area of device (portrait, 1:2.09). Background white #FFFFFF or #FAFAFA. Lines: black #000000, wobbly hand-drawn. Only one accent #7DD3FC for primary button or FAB. Typography: hand-lettered/sketch. No overlapping.

Content: Screen title: "Danh bạ thụ hưởng". From top to bottom: [component_stack_text]. Use accent #7DD3FC only for FAB/primary.
```

Lưu tạm vd. `{basename}-content.png` trong `output_dir`.

---

## Composite — đặt content vào device frame

1. **Đọc ảnh:** `device-frame.png` và từng `{basename}-content.png`.
2. **Vùng màn hình trên device-frame.png:** Device = 90% width, 90% height canvas, căn giữa. Inner content rect = padding 6% L+R, 4% T+B trong device (tức 88%×92% vùng device). Tính tọa độ và kích thước từ kích thước ảnh device khi load (xem script composite-mockup.py).
3. **Scale content:** Resize ảnh content-only để fit vùng content, giữ aspect ratio trùng tỷ lệ vùng content (1 : 2.09 portrait).
4. **Paste:** Đặt ảnh content đã resize lên device-frame tại vùng content. Ghi đè pixel (hoặc blend tùy chọn).
5. **Lưu:** Ghi ra `{basename}-mockup.png` (img-to-mockup) hoặc `output_filename` (md-to-mockup).

**Gợi ý công cụ:** Script Python (PIL/Pillow) hoặc ImageMagick — scale và paste content vào vùng content theo tỷ lệ device (90%) và padding (6%, 4%). Tham chiếu `scripts/composite-mockup.py` (tính inner rect tại runtime từ kích thước ảnh).

---

## Tóm tắt số liệu

| Tham số | Giá trị |
|---------|---------|
| Canvas (full / device frame) | Tỷ lệ **1:2 vertical** (portrait) |
| Device trên canvas | 90% × 90%, căn giữa |
| Inner content (trong device) | Padding 6% L+R, 4% T+B → vùng 88% × 92% device |
| Content-only canvas ratio | Tỷ lệ vùng content (portrait, ~1 : 2.09) |
