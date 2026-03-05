# Deploy to GitHub Pages Skill

Automates deployment of static sites (markdown viewers, docs, portfolios) to GitHub Pages with step-by-step setup and deployment workflow.

## Trigger Keywords

Use this skill when user mentions:
- `deploy to github pages`
- `publish to github`
- `host on github pages`
- `push markdown viewer to github`
- `create github pages site`
- `setup github pages`

## Prerequisites Check

Before starting, verify:
1. Git is installed: `git --version`
2. GitHub CLI is installed (optional but recommended): `gh --version`
3. User has GitHub account
4. Repository exists or needs to be created

## Workflow Steps

### Step 1: Repository Setup

Check current git status:

```bash
git status
git remote -v
```

**Case A: No remote repository**
- Ask user for GitHub username
- Ask for repository name (suggest: `markdown-viewer`)
- Create repository via GitHub CLI or provide manual instructions

**Case B: Remote exists**
- Verify remote URL
- Check if it's the correct repository

### Step 2: Prepare GitHub Pages Branch

GitHub Pages supports two deployment methods:

**Method 1: `gh-pages` branch (Recommended)**
- Separate branch for deployment
- Keeps source code clean
- Use for projects with build process

**Method 2: `main` branch with `/docs` folder**
- Single branch deployment
- Simpler for static sites
- Use for simple HTML/CSS/JS projects

**For Markdown Viewer, use Method 1 (gh-pages branch)**

### Step 3: Create Deployment Files

Create `deploy-to-pages.sh` script:

```bash
#!/bin/bash
# GitHub Pages Deployment Script

echo "🚀 Starting GitHub Pages deployment..."

# Check if gh-pages branch exists
if git show-ref --verify --quiet refs/heads/gh-pages; then
    echo "✅ gh-pages branch exists"
else
    echo "📝 Creating gh-pages branch..."
    git checkout --orphan gh-pages
    git rm -rf .
    git checkout main -- serve-markdown.py README-MARKDOWN-SERVER.md
    git commit -m "Initial gh-pages commit"
    git push -u origin gh-pages
    git checkout main
fi

# Create deployment directory
rm -rf .deploy
mkdir .deploy

# Copy necessary files
echo "📦 Copying files..."
cp serve-markdown.py .deploy/
cp README-MARKDOWN-SERVER.md .deploy/
cp -r XPOS .deploy/ 2>/dev/null || true
cp -r docs .deploy/ 2>/dev/null || true
find . -maxdepth 3 -name "*.md" -not -path "*/node_modules/*" -not -path "*/.git/*" -exec cp --parents {} .deploy/ \;

# Create index.html for GitHub Pages
cat > .deploy/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Markdown Viewer</title>
  <script>
    // Redirect to Python server instructions or serve static content
    window.location.href = 'static-viewer.html';
  </script>
</head>
<body>
  <h1>Redirecting...</h1>
</body>
</html>
EOF

# Create static viewer (client-side only)
cat > .deploy/static-viewer.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Markdown Viewer</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <!-- Add complete static viewer HTML here -->
</head>
<body>
  <!-- Static viewer implementation -->
</body>
</html>
EOF

# Deploy to gh-pages
echo "🚀 Deploying to gh-pages..."
cd .deploy
git init
git add -A
git commit -m "Deploy to GitHub Pages"
git push -f https://github.com/USERNAME/REPO.git main:gh-pages

cd ..
rm -rf .deploy

echo "✅ Deployment complete!"
echo "📍 Your site will be available at: https://USERNAME.github.io/REPO/"
```

### Step 4: GitHub Pages Configuration

Guide user to:

1. Go to repository Settings
2. Navigate to "Pages" section
3. Configure:
   - **Source**: Deploy from a branch
   - **Branch**: `gh-pages`
   - **Folder**: `/ (root)`
4. Click "Save"

### Step 5: Alternative - Pure Client-Side Viewer

Since Python server won't run on GitHub Pages, create a pure JavaScript solution:

**Create `index.html` for GitHub Pages:**

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Markdown Viewer</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    /* Copy all CSS from serve-markdown.py */
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>📄 Markdown Viewer</h1>
      <div class="breadcrumb">Select a file to view</div>
    </div>
    <div class="content">
      <div id="file-list"></div>
      <div id="markdown-content" class="markdown-body" style="display:none;"></div>
    </div>
  </div>
  
  <script>
    // JavaScript to load file list from files.json
    // JavaScript to load and render markdown files
    // Hash-based routing for navigation
  </script>
</body>
</html>
```

### Step 6: Generate File Manifest

Create a script to generate `files.json`:

```python
#!/usr/bin/env python3
import json
from pathlib import Path

def find_markdown_files():
    files = []
    for md_file in Path('.').rglob('*.md'):
        if any(part.startswith('.') for part in md_file.parts) or 'node_modules' in md_file.parts:
            continue
        files.append(str(md_file))
    return sorted(files)

manifest = {
    'files': find_markdown_files(),
    'generated_at': str(Path.cwd())
}

with open('files.json', 'w') as f:
    json.dump(manifest, f, indent=2)

print(f"Generated manifest with {len(manifest['files'])} files")
```

### Step 7: Deployment Commands

```bash
# 1. Commit current changes
git add .
git commit -m "Add GitHub Pages deployment"

# 2. Push to main
git push origin main

# 3. Run deployment script
chmod +x deploy-to-pages.sh
./deploy-to-pages.sh

# OR use GitHub CLI
gh repo create markdown-viewer --public --push
```

## GitHub CLI Setup (Recommended)

If GitHub CLI not installed:

```bash
# macOS
brew install gh

# Login
gh auth login

# Create repository
gh repo create markdown-viewer --public --description "Beautiful Markdown Viewer"

# Push code
git remote add origin https://github.com/USERNAME/markdown-viewer.git
git branch -M main
git push -u origin main
```

## Manual GitHub Setup (Without CLI)

1. Go to https://github.com/new
2. Create new repository:
   - Name: `markdown-viewer`
   - Description: "Beautiful Markdown Viewer"
   - Public
   - No README/gitignore (already have local)
3. Copy the repository URL
4. Run commands:

```bash
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git push -u origin main
```

## Output Files

The skill should create:

1. `deploy-to-pages.sh` - Deployment script
2. `index.html` - GitHub Pages landing page
3. `files.json` - Markdown files manifest
4. `generate-manifest.py` - Manifest generator
5. `.github/workflows/deploy.yml` - GitHub Actions workflow (optional)

## GitHub Actions Auto-Deploy (Optional)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Generate manifest
        run: python3 generate-manifest.py
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: .
          publish_branch: gh-pages
```

## Success Criteria

- ✅ Repository created and connected
- ✅ Code pushed to GitHub
- ✅ GitHub Pages enabled
- ✅ Site accessible at https://username.github.io/repo-name/
- ✅ Markdown files render correctly
- ✅ Navigation works

## Troubleshooting

**Issue: 404 Page Not Found**
- Check GitHub Pages settings enabled
- Verify branch is `gh-pages` or correct branch
- Wait 2-3 minutes for deployment

**Issue: Files not loading**
- Check `files.json` generated correctly
- Verify CORS not blocking requests
- Check browser console for errors

**Issue: Authentication failed**
- Run `gh auth login` to re-authenticate
- Use Personal Access Token if needed
- Check SSH keys configured

## User Prompts

Ask user:

1. "Do you have a GitHub account?" (username)
2. "What should the repository be named?" (suggest: markdown-viewer)
3. "Public or private repository?" (recommend: public for Pages)
4. "Use GitHub CLI or manual setup?" (recommend: CLI if available)
5. "Enable automatic deployment with GitHub Actions?" (recommend: yes)

## Execution Flow

1. Check prerequisites (git, gh, credentials)
2. Ask user for repository details
3. Create repository (if needed)
4. Generate static viewer files
5. Generate manifest
6. Commit and push
7. Setup GitHub Pages
8. Provide site URL
9. Test deployment

## Example Usage

```
User: "Deploy my markdown viewer to GitHub Pages"