# Jira Designer Portfolios

Static site bundling portfolio cho 38 designers từ Jira project DES.

## Architecture: 2 templates + JSON per user

Mỗi style là **1 template HTML** fetch JSON từ `data/{user}.json` qua URL param `?u=username`.
Add user mới = chỉ cần thêm JSON file, không phải re-render HTML.

## Cấu trúc

```
dist/
├── index.html                    ← landing page list designers
├── templates/
│   ├── editorial.html            ← monochrome editorial style (template)
│   └── glass.html                ← iOS glass style (template)
├── data/
│   ├── {username}.json           ← bucket data + portrait + logos inline
│   └── buckets.json              ← classification rules
├── logos/                        ← brand SVG logos (optional, embedded in JSON)
├── portraits/                    ← user portraits (optional, embedded in JSON)
├── vercel.json
├── netlify.toml
└── .nojekyll                     ← GitHub Pages
```

## Usage

```
templates/editorial.html?u=phongpd     → editorial style cho phongpd
templates/glass.html?u=longnq          → glass style cho longnq
templates/editorial.html?data=custom.json  → custom data path
```

## Designers

- **Quân, Vũ Văn (TK, TTQLSP)** (`@quanvv`) — 31 brands · 575 tickets
- **Hiếu, Nguyễn Hoàng (Ph. TK, TTQLSP)** (`@hieunh`) — 19 brands · 420 tickets
- **Hùng Vũ** (`@hungv`) — 22 brands · 397 tickets
- **Mai, Phùng Thị Nguyệt (TK, TTQLSP)** (`@maiptn`) — 13 brands · 392 tickets
- **Ly, Nguyễn Khánh (KCN, TK)** (`@lynk2`) — 17 brands · 356 tickets
- **Tung Nguyen Thanh** (`@tungnt2`) — 20 brands · 336 tickets
- **Duy Nguyễn Lê** (`@duynl`) — 16 brands · 335 tickets
- **Ngọc Lê Nguyên** (`@ngocln`) — 20 brands · 331 tickets
- **Uyên Nguyễn Thị Tố** (`@uyenntt1`) — 23 brands · 298 tickets
- **Phong Dinh - TK, TTQLSP** (`@phongpd`) — 47 brands · 293 tickets
- **Giáp, Nguyễn Hoàng (TK, TTQLSP)** (`@giapnh`) — 23 brands · 291 tickets
- **Hao Nguyen** (`@haonv`) — 26 brands · 287 tickets
- **Long, Nguyễn Quốc (TK, TTQLSP)** (`@longnq`) — 36 brands · 284 tickets
- **Hương, Tống Lan (TK, TTQLSP)** (`@huongtl1`) — 5 brands · 275 tickets
- **Nhung, Nguyễn Thị Hồng (TK, TTQLSP)** (`@nhungnth3`) — 16 brands · 266 tickets
- **Nết, Nguyễn Thị (TK, TTQLSP)** (`@netnt`) — 17 brands · 232 tickets
- **Tung Nguyen** (`@tungn`) — 26 brands · 224 tickets
- **Thảo, Trần Lê Phương - TK, TTQLSP** (`@thaotlp`) — 7 brands · 219 tickets
- **Hoa, Đào Thanh (TK, TTQLSP)** (`@hoadt`) — 11 brands · 217 tickets
- **Đạt, Trần Tiến (TK, TTQLSP)** (`@dattt2`) — 11 brands · 213 tickets
- **Anh, Dương Thị Minh (TK, TTQLSP)** (`@anhdtm`) — 19 brands · 204 tickets
- **Quỳnh Thái Ngọc** (`@quynhtn`) — 12 brands · 199 tickets
- **Dũng, Lê Tiến (TK, TTQLSP)** (`@dunglt1`) — 14 brands · 167 tickets
- **Thương, Nguyễn Thị (TK, TTQLSP)** (`@thuongnt3`) — 12 brands · 155 tickets
- **Ngọc, Nguyễn Thị Kim (TK, TTQLSP)** (`@ngocntk`) — 10 brands · 146 tickets
- **MinhHN (TK, TTQLSP)** (`@minhhn`) — 18 brands · 128 tickets
- **Trang Ngo Quynh** (`@trangntq1`) — 18 brands · 119 tickets
- **Anh, Nguyễn Quỳnh (TK, TTQLSP)** (`@anhnq5`) — 8 brands · 100 tickets
- **Linh, Luyện Nhật (TK, TTQLSP)** (`@linhln3`) — 15 brands · 95 tickets
- **Anh, Nguyễn Đức (TK, TTQLSP)** (`@anhnd13`) — 6 brands · 80 tickets
- **Tuyền, Huỳnh Ngọc Lam (TK, TTQLSP)** (`@tuyenhnl`) — 5 brands · 42 tickets
- **Dũng, Nguyễn Tiến  (KCN, TK)** (`@dungnt12`) — 10 brands · 36 tickets
- **Định, Đồng Công (TK, TTQLSP)** (`@dinhdc`) — 3 brands · 32 tickets
- **Trang, Nguyễn Thị Kim (TK, TTQLSP)** (`@trangntk`) — 5 brands · 32 tickets
- **Phương, Nguyễn Ánh (TK, TTQLSP)** (`@phuongna`) — 7 brands · 23 tickets
- **Linh, Vũ Lê Khánh (TK, TTQLSP)** (`@linhvlk`) — 8 brands · 17 tickets
- **Ngân, Vũ Thái (TK, TTQLSP)** (`@nganvt1`) — 7 brands · 16 tickets
- **Thien Hoang Anh** (`@thienha`) — 8 brands · 11 tickets

## Deploy

### Vercel
```bash
cd dist && vercel --prod
```

### Netlify
```bash
cd dist && netlify deploy --prod --dir=.
```

### GitHub Pages
Push `dist/` content to `gh-pages` branch:
```bash
git subtree push --prefix ux-output/_jira-audit/dist origin gh-pages
```

## Refresh data

Re-generate from Jira:
```bash
node scripts/jira-portfolio-by-client.mjs <username>
node scripts/jira-portfolio-by-client.mjs <username> --style=glass
node scripts/jira-portfolio-package.mjs
```
