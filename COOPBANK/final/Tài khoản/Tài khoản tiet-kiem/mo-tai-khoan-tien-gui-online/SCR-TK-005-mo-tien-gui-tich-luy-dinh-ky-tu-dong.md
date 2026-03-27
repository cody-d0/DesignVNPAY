# SCR-TK-005 · Mở tiền gửi trực tuyến - Tích luỹ định kỳ tự động › Form nhập thông tin

> `SCR-TK-005` · form · 2 artboards

---

## 1. Mục đích màn hình

Form mở tiền gửi tích luỹ định kỳ tự động. Tương tự form tích luỹ linh động nhưng có thêm:
- Hình thức tích luỹ: Tích luỹ định kỳ tự động
- Chu kỳ tích luỹ (Hàng tháng)
- Số tiền tích luỹ định kỳ (min 1,000,000 VND)
- Tài khoản trích tiền tự động

## 2. Wireframes

![Form empty](ui/SCR-TK-005-form-tltd-empty.png)
![Form filled](ui/SCR-TK-005-form-tltd-filled.png)

## 3. Nội dung OCR

| # | Text | Loại | Vị trí |
|:--|:-----|:-----|:-------|
| 1 | Mở tiền gửi trực tuyến | header | top-center |
| 2 | Tài khoản nguồn | label | card-header |
| 3 | 9099798712313123 | value | card-body |
| 4 | 20,000,000 VND | value | card-body |
| 5 | Loại sản phẩm · Tiền gửi tích luỹ | field | form-field-1 |
| 6 | Kỳ hạn · 1 tháng | field | form-field-2 |
| 7 | Lãi suất · 3,98%/năm | field | form-field-3 |
| 8 | Số tiền · 250,000,000 VND | field | form-field-6 |
| 9 | Số tiền gửi tối thiểu là 1,000,000 VND | helper-text | form-field-6 |
| 10 | Hình thức tích luỹ · Tích luỹ định kỳ tự động | field | form-field-8 |
| 11 | Chu kỳ tích luỹ · Hàng tháng | field | form-field-9 |
| 12 | Số tiền tích luỹ định kỳ · 1,000,000 | field | form-field-10 |
| 13 | Số tiền gửi định kỳ tối thiểu là 1,000,000 VND | helper-text | form-field-10 |
| 14 | Tài khoản trích tiền · 123123123123 | field | form-field-11 |
| 15 | Phương thức đáo hạn · Tự động tất toán, nhận gốc và lãi về TKTT | field | form-field-12 |
| 16 | Tài khoản nhận gốc lãi · 123123123123 | field | form-field-13 |
| 17 | Phương thức tất toán/rút gốc · Tất toán/ rút gốc Online | field | form-field-14 |
| 18 | Mã giới thiệu | field-label | form-field-15 |
| 19 | Tiếp tục | button | bottom-cta |

## 4. User Flow

```
SCR-TK-001 → [SCR-TK-005]
  └── Tap "Tiếp tục" → SCR-TK-006
```

## 5. DDL References

| Ref | Mô tả |
|:----|:------|
| COMP:text-input-1 | Text input — states: error, errorMessage, disabled, focused |
| UXG-243 | Form usability and validation |
| Hick's Law | Form quá dài (~15 fields), cần stepper/wizard |
| Fitts's Law | CTA reachability after long scroll |
