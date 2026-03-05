# 🚀 Deploy to GitHub Pages - Step by Step Guide

## 📋 Prerequisites

- ✅ Git installed
- ✅ GitHub account
- ✅ Files ready: `index.html`, `files.json`, `deploy-github-pages.sh`

## 🎯 Deployment Steps

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `markdown-viewer` (or your preferred name)
   - **Description**: "Beautiful Markdown Viewer for XPOS Documentation"
   - **Visibility**: ⚠️ **PUBLIC** (required for free GitHub Pages)
   - **Initialize**: ❌ Don't check any boxes (no README, no .gitignore, no license)
3. Click "Create repository"

### Step 2: Connect Local Repository to GitHub

Copy the commands from GitHub (they look like this):

```bash
# If this is your first commit
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

**OR** if you already have commits:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

### Step 3: Run Deployment Script

```bash
./deploy-github-pages.sh
```

This script will:
- ✅ Generate file manifest (`files.json`)
- ✅ Commit all changes
- ✅ Push to `main` branch
- ✅ Deploy to `gh-pages` branch
- ✅ Show you the next steps

### Step 4: Enable GitHub Pages

1. Go to your repository settings:
   ```
   https://github.com/YOUR_USERNAME/YOUR_REPO/settings/pages
   ```

2. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: `gh-pages`
   - **Folder**: `/ (root)`

3. Click **Save**

4. Wait 2-3 minutes for GitHub to build and deploy

### Step 5: Visit Your Site! 🎉

Your site will be available at:
```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

Example:
- Username: `dataism`
- Repo: `markdown-viewer`
- URL: https://dataism.github.io/markdown-viewer/

## 🔄 Update Your Site

When you add or modify markdown files:

```bash
# 1. Generate new manifest
python3 generate-manifest.py

# 2. Run deployment script
./deploy-github-pages.sh
```

The script will automatically:
- Update files.json
- Commit changes
- Push to main
- Deploy to gh-pages

## 🛠️ Manual Deployment (Alternative)

If the script doesn't work, you can deploy manually:

```bash
# 1. Generate manifest
python3 generate-manifest.py

# 2. Commit changes
git add .
git commit -m "Update documentation"
git push origin main

# 3. Deploy to gh-pages
git checkout --orphan gh-pages
git rm -rf .
git checkout main -- index.html files.json
cp -r XPOS .
find . -name "*.md" -not -path "*/node_modules/*" -not -path "*/.git/*" | cpio -pdm .
git add -A
git commit -m "Deploy to GitHub Pages"
git push -f origin gh-pages
git checkout main
```

## 🎨 Features of Your Site

- 📄 **18 Markdown Files** automatically discovered
- 🔍 **Search** - Find files quickly
- 📱 **Responsive** - Works on all devices
- 🎨 **Beautiful UI** - Purple gradient theme
- 📊 **Tables** - Beautifully rendered
- 💻 **Code Blocks** - Syntax highlighted
- ⚡ **Fast** - Client-side rendering with marked.js

## 📂 What Gets Deployed

```
gh-pages branch:
├── index.html          # Main viewer
├── files.json          # File manifest
└── XPOS/              # All your markdown files
    └── XPOS PRD - updated 2026.02.10/
        ├── xpos-app/
        │   ├── home.md
        │   ├── login.md
        │   ├── register.md
        │   └── ... (all .md files)
        └── xpos-bo/
            └── ... (all .md files)
```

## 🐛 Troubleshooting

### Problem: 404 Page Not Found

**Solution:**
1. Check GitHub Pages is enabled in Settings
2. Verify branch is set to `gh-pages`
3. Wait 2-3 minutes after deployment
4. Clear browser cache

### Problem: Files not loading

**Solution:**
1. Check `files.json` exists and is valid
2. Open browser console (F12) for errors
3. Verify file paths in `files.json` match actual files
4. Re-run `python3 generate-manifest.py`

### Problem: Authentication failed

**Solution:**
```bash
# Use GitHub Personal Access Token
git remote set-url origin https://YOUR_TOKEN@github.com/USERNAME/REPO.git

# Or use SSH
git remote set-url origin git@github.com:USERNAME/REPO.git
```

### Problem: Permission denied

**Solution:**
```bash
# Make script executable
chmod +x deploy-github-pages.sh

# Or run with bash
bash deploy-github-pages.sh
```

## 🔐 Using Personal Access Token

If you need a token:

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes:
   - ✅ `repo` (full control)
   - ✅ `workflow`
4. Copy the token
5. Use it:
   ```bash
   git remote set-url origin https://YOUR_TOKEN@github.com/USERNAME/REPO.git
   ```

## 📝 Quick Reference

```bash
# Generate manifest
python3 generate-manifest.py

# Deploy everything
./deploy-github-pages.sh

# Check status
git status
git remote -v

# View logs
git log --oneline

# Force redeploy
git push -f origin gh-pages
```

## 🎉 Success Checklist

- ✅ Repository created on GitHub
- ✅ Local repo connected to GitHub
- ✅ Code pushed to `main` branch
- ✅ Deployed to `gh-pages` branch
- ✅ GitHub Pages enabled in settings
- ✅ Site accessible at https://username.github.io/repo/
- ✅ All markdown files visible
- ✅ Search works
- ✅ Navigation works

## 🆘 Need Help?

If you encounter issues:

1. Check the script output for error messages
2. Verify your GitHub credentials
3. Make sure repository is PUBLIC
4. Check GitHub Pages settings
5. Wait a few minutes after deployment

---

**Ready to deploy?** Run: `./deploy-github-pages.sh`
