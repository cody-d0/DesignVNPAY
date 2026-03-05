# ⚡ Quick Start - Deploy to GitHub Pages

## 🎯 5-Minute Deployment

### Step 1: Create GitHub Repository (2 minutes)

1. Open: https://github.com/new
2. Fill in:
   - Repository name: `markdown-viewer`
   - Visibility: **PUBLIC** ⚠️ Important!
   - Don't check any boxes
3. Click "Create repository"

### Step 2: Copy Your Repository URL

After creating, you'll see commands like:

```bash
git remote add origin https://github.com/YOUR_USERNAME/markdown-viewer.git
```

**Copy your actual URL!** It will look like:
```
https://github.com/dataism/markdown-viewer.git
```

### Step 3: Run These Commands (2 minutes)

Open Terminal in this folder and run:

```bash
# 1. Initialize git
git init

# 2. Add all files
git add .

# 3. First commit
git commit -m "Initial commit"

# 4. Connect to GitHub (REPLACE WITH YOUR URL!)
git remote add origin https://github.com/YOUR_USERNAME/markdown-viewer.git

# 5. Push to GitHub
git branch -M main
git push -u origin main
```

### Step 4: Deploy to GitHub Pages (1 minute)

```bash
./deploy-github-pages.sh
```

If permission denied:
```bash
chmod +x deploy-github-pages.sh
./deploy-github-pages.sh
```

### Step 5: Enable GitHub Pages (1 minute)

1. Go to: `https://github.com/YOUR_USERNAME/markdown-viewer/settings/pages`
2. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **gh-pages**
   - Folder: **/ (root)**
3. Click **Save**

### Step 6: Visit Your Site! 🎉

Wait 2-3 minutes, then visit:
```
https://YOUR_USERNAME.github.io/markdown-viewer/
```

Example:
```
https://dataism.github.io/markdown-viewer/
```

## 🎊 Done!

Your markdown viewer is now live with:
- ✅ 18 markdown files
- ✅ Beautiful UI
- ✅ Search functionality
- ✅ Responsive design

## 🔄 Update Your Site

**Local (serve-markdown.py):** Folder và file mới trong **MarkdownSV** tự hiện khi refresh — API quét chỉ từ MarkdownSV.

**Deploy tĩnh / GitHub Pages:** Khi thêm folder hoặc file .md mới trong MarkdownSV, cần tạo lại manifest rồi deploy:

```bash
cd viewer
CONTENT_ROOT=../MarkdownSV python3 generate-manifest.py
# Hoặc chạy watcher: npm run watch (tự cập nhật files.json khi có .md hoặc folder mới trong MarkdownSV)
./deploy-github-pages.sh
```

## 🆘 Problems?

### "Permission denied" error
```bash
chmod +x deploy-github-pages.sh
```

### "Authentication failed"
Use Personal Access Token:
1. Go to: https://github.com/settings/tokens
2. Generate new token (classic)
3. Select: `repo` scope
4. Copy token
5. Use it:
```bash
git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/markdown-viewer.git
```

### "404 Not Found" on GitHub Pages
- Wait 2-3 minutes
- Check Settings → Pages is enabled
- Verify branch is `gh-pages`
- Clear browser cache

---

**Need detailed instructions?** See `DEPLOY-INSTRUCTIONS.md`
