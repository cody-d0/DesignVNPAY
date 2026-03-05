# 📄 Markdown Viewer & GitHub Pages Deployment

Beautiful markdown viewer with GitHub Pages deployment for XPOS documentation.

## 🎯 Quick Start

### Local Development (thư mục riêng viewer/)

```bash
cd viewer
python3 serve-markdown.py
# Open: http://localhost:9999
```

**Tự động danh sách file và folder:** Khi chạy qua `serve-markdown.py`, viewer dùng GET /api/files và quét chỉ từ folder **MarkdownSV**. Thêm folder mới hoặc thêm/sửa/xóa .md trong MarkdownSV → refresh trang là thấy, không cần commit hay manifest.

### Local Development (từ root)

```bash
python3 serve-markdown.py
open http://localhost:9999
```

### Deploy to GitHub Pages

```bash
# Run deployment script
./deploy-github-pages.sh
```

## 📦 What's Included

### Files Created

- ✅ `index.html` - Static viewer for GitHub Pages
- ✅ `serve-markdown.py` - Local Python server
- ✅ `generate-manifest.py` - File discovery script
- ✅ `files.json` - Manifest of all markdown files (18 files)
- ✅ `deploy-github-pages.sh` - Automated deployment script
- ✅ `DEPLOY-INSTRUCTIONS.md` - Detailed deployment guide

### Features

- 🎨 **Beautiful UI** - Purple gradient theme
- 📱 **Responsive** - Works on all devices
- 🔍 **Search** - Find files quickly
- 📊 **Tables** - Beautiful table rendering
- 💻 **Code Blocks** - Syntax highlighting
- ⚡ **Fast** - Client-side rendering
- 🌐 **GitHub Pages Ready** - Deploy in minutes

## 🚀 Deployment Steps

### 1. Create GitHub Repository

Go to https://github.com/new and create:
- Name: `markdown-viewer` (or your choice)
- Visibility: **PUBLIC** (required for free GitHub Pages)
- Don't initialize with anything

### 2. Connect to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit: Markdown viewer with GitHub Pages support"

# Connect to GitHub (replace with your info)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to main
git branch -M main
git push -u origin main
```

### 3. Deploy to GitHub Pages

```bash
# Run the deployment script
./deploy-github-pages.sh
```

The script will:
1. Generate file manifest
2. Commit changes
3. Push to main branch
4. Deploy to gh-pages branch
5. Show you next steps

### 4. Enable GitHub Pages

1. Go to: `https://github.com/YOUR_USERNAME/YOUR_REPO/settings/pages`
2. Set:
   - Source: **Deploy from a branch**
   - Branch: **gh-pages**
   - Folder: **/ (root)**
3. Click **Save**
4. Wait 2-3 minutes

### 5. Visit Your Site! 🎉

```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

## 📂 Project Structure

```
.
├── index.html                  # GitHub Pages viewer
├── serve-markdown.py          # Local server
├── generate-manifest.py       # Manifest generator
├── deploy-github-pages.sh     # Deployment script
├── files.json                 # File manifest (18 files)
├── DEPLOY-INSTRUCTIONS.md     # Detailed guide
├── README.md                  # This file
└── XPOS/                      # Your markdown files
    └── XPOS PRD - updated 2026.02.10/
        ├── xpos-app/
        │   ├── home.md
        │   ├── login.md
        │   ├── register.md
        │   ├── forgot-password.md
        │   ├── inventory-management.md
        │   ├── order-management.md
        │   ├── order-payment.md
        │   ├── settings.md
        │   ├── pipeline-home-output.md
        │   └── xpos-app-overview.md
        └── xpos-bo/
            ├── bo-home.md
            ├── bo-login.md
            ├── bo-order.md
            ├── bo-permission.md
            ├── bo-store.md
            ├── bo-user.md
            └── xpos-bo-overview.md
```

## 🔄 Update Workflow

When you add or modify markdown files:

```bash
# 1. Generate new manifest
python3 generate-manifest.py

# 2. Deploy
./deploy-github-pages.sh
```

## 🎨 Customization

### Change Colors

Edit `index.html` and modify the CSS:

```css
.header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Change Port (Local Server)

Edit `serve-markdown.py`:

```python
PORT = 9999  # Change to your preferred port
```

## 📊 Statistics

- **Total Markdown Files**: 18
- **XPOS App Docs**: 10 files
- **XPOS BO Docs**: 7 files
- **Other Docs**: 1 file

## 🛠️ Troubleshooting

### Local Server Won't Start

```bash
# Try different port
# Edit serve-markdown.py and change PORT = 9999 to PORT = 8888
python3 serve-markdown.py
```

### GitHub Pages Shows 404

1. Check Settings → Pages is enabled
2. Verify branch is `gh-pages`
3. Wait 2-3 minutes
4. Clear browser cache

### Files Not Loading

```bash
# Regenerate manifest
python3 generate-manifest.py

# Redeploy
./deploy-github-pages.sh
```

### Authentication Issues

```bash
# Use Personal Access Token
git remote set-url origin https://YOUR_TOKEN@github.com/USERNAME/REPO.git
```

Get token at: https://github.com/settings/tokens

## 📝 Commands Reference

```bash
# Local development
python3 serve-markdown.py              # Start server
python3 generate-manifest.py           # Generate manifest

# Git operations
git status                             # Check status
git add .                              # Stage changes
git commit -m "message"                # Commit
git push origin main                   # Push to main

# Deployment
./deploy-github-pages.sh               # Deploy to Pages
chmod +x deploy-github-pages.sh        # Make executable

# Troubleshooting
git remote -v                          # Check remotes
git log --oneline                      # View history
```

## 🎯 Next Steps

1. ✅ Files created and ready
2. ⏳ Create GitHub repository
3. ⏳ Connect local repo to GitHub
4. ⏳ Run deployment script
5. ⏳ Enable GitHub Pages
6. ⏳ Visit your site!

## 📖 Documentation

- **Detailed Guide**: See `DEPLOY-INSTRUCTIONS.md`
- **Local Server**: See `README-MARKDOWN-SERVER.md`
- **Deployment Skill**: See `.cursor/skills/deploy-github-pages/SKILL.md`

## 🆘 Need Help?

1. Read `DEPLOY-INSTRUCTIONS.md` for step-by-step guide
2. Check troubleshooting section above
3. Verify GitHub credentials
4. Make sure repository is PUBLIC
5. Wait a few minutes after deployment

---

**Ready to deploy?** Follow the steps above or run `./deploy-github-pages.sh`

Made with ❤️ for XPOS Documentation
