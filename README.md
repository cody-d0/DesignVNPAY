# 📄 MDviewer — Markdown Viewer

Standalone Markdown viewer tool. Xem tài liệu `.md` với giao diện đẹp, dark/light theme, search, drag & drop.

## 🚀 Quick Start

```bash
cd tool/MDviewer
python3 serve-markdown.py
# Mở: http://localhost:9999
```

## ✨ Features

- 🎨 **Beautiful UI** — Dark / Light / Mesh themes
- 📱 **Responsive** — Mobile & desktop
- 🔍 **Search** — Tìm file với debounce
- 📂 **Folder tree** — Cây thư mục collapsible
- 📊 **Multi-format** — Markdown, JSON, YAML, CSV, SVG
- 🖱️ **Drag & Drop** — Kéo thả file để xem trước
- 📋 **Paste-and-Go** — Dán path vào search → mở file
- ⏰ **Auto-refresh** — Polling + webhook sync
- 🌐 **GitHub Pages** — Deploy static site
- ⌨️ **Keyboard** — `/` to focus search

## 📂 Cấu trúc

```
tool/MDviewer/
├── index.html              # SPA viewer
├── serve-markdown.py       # Local server + API
├── generate-manifest.py    # Manifest generator
├── MarkdownSV/             # Content folder
├── deploy-github-pages.sh  # GitHub Pages deploy
└── README.md               # Viewer docs
```

## 📖 Chi tiết

Xem [tool/MDviewer/README.md](tool/MDviewer/README.md) để biết chi tiết cấu hình, API, deployment.
