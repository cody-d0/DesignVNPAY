# Cập nhật danh sách file (khi đổi vị trí / tên file)

## Vì sao bị "missing"?

Viewer đọc danh sách file từ **`files.json`**. Khi bạn **đổi vị trí** (move) hoặc **đổi tên** file `.md`, `files.json` vẫn giữ đường dẫn cũ → link mở file bị sai → trông như "missing".

**Không phải do git push.** Git push chỉ đẩy commit lên remote, không tự tạo lại `files.json`.

---

## Thao tác cần làm: tạo lại manifest

Mỗi khi bạn **thêm / xóa / đổi vị trí / đổi tên** file markdown, chạy lệnh sau trong thư mục project:

```bash
python3 generate-manifest.py
```

Script sẽ:

- Quét toàn bộ file `.md` (trừ thư mục ẩn, `node_modules`)
- Ghi lại đường dẫn, thư mục, thời gian sửa
- Ghi đè file **`files.json`**

Sau đó reload trang viewer (hoặc hard refresh) là danh sách và link đúng lại.

---

## Quy trình gợi ý

| Bước | Việc làm |
|------|----------|
| 1 | Sửa / di chuyển / đổi tên file `.md` |
| 2 | Chạy `python3 generate-manifest.py` |
| 3 | (Tùy chọn) Commit + **git push** nếu bạn dùng GitHub Pages và muốn deploy bản mới |

**Tóm lại:** Cập nhật danh sách = chạy `generate-manifest.py`.  
**Git push** = đẩy code đã commit lên GitHub (để deploy hoặc backup), không thay thế bước tạo lại `files.json`.

---

## Manifest tự động (pre-commit hook)

Để **tự tạo lại `files.json` mỗi khi commit** (không cần nhớ chạy tay):

1. Cài hook một lần:

```bash
./install-manifest-hook.sh
```

2. Sau đó mỗi lần `git commit`, script sẽ:
   - Chạy `python3 generate-manifest.py`
   - Nếu `files.json` thay đổi thì tự `git add files.json` vào commit

Như vậy khi bạn thêm/xóa/đổi tên file `.md` rồi commit, manifest luôn được cập nhật theo.

- Hook nằm tại: `githooks/pre-commit` (bản mẫu), `.git/hooks/pre-commit` (sau khi cài).
- Gỡ hook: xóa file `.git/hooks/pre-commit`.
