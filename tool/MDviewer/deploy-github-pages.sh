#!/bin/bash
# Deploy MDviewer to GitHub Pages — Manual Script
# Run from repo root: ./tool/MDviewer/deploy-github-pages.sh
# Or use GitHub Actions (recommended): push to MDviewer branch

set -e  # Exit on error

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "🚀 MDviewer → GitHub Pages Deploy"
echo "=================================="
echo ""

# Navigate to repo root (script may be called from anywhere)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VIEWER_DIR="$SCRIPT_DIR"
cd "$REPO_ROOT"

echo -e "${BLUE}📍 Repo root: ${REPO_ROOT}${NC}"
echo -e "${BLUE}📍 Viewer dir: ${VIEWER_DIR}${NC}"
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo -e "${RED}❌ Error: Not a git repository${NC}"
    exit 1
fi

# Get repository info
REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "")

if [ -z "$REMOTE_URL" ]; then
    echo -e "${RED}❌ No remote repository configured${NC}"
    echo "Run: git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
    exit 1
fi

# Extract username and repo name from URL
if [[ $REMOTE_URL =~ github\.com[:/]([^/]+)/([^/.]+) ]]; then
    USERNAME="${BASH_REMATCH[1]}"
    REPO="${BASH_REMATCH[2]}"
    PAGES_URL="https://${USERNAME}.github.io/${REPO}/"
else
    echo -e "${RED}❌ Could not parse GitHub URL${NC}"
    exit 1
fi

echo -e "${BLUE}👤 User: ${USERNAME}${NC}"
echo -e "${BLUE}📦 Repo: ${REPO}${NC}"
echo -e "${BLUE}🌐 URL:  ${PAGES_URL}${NC}"
echo ""

# Step 1: Generate manifest
echo -e "${YELLOW}📝 Generating files.json from MarkdownSV...${NC}"
cd "$VIEWER_DIR"
python3 generate-manifest.py --content MarkdownSV
cd "$REPO_ROOT"

if [ ! -f "$VIEWER_DIR/files.json" ]; then
    echo -e "${RED}❌ Error: files.json not generated${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Manifest generated${NC}"
echo ""

# Step 2: Prepare deploy folder
echo -e "${YELLOW}📦 Preparing deploy folder...${NC}"
TEMP_DIR=$(mktemp -d)
echo "   Temp dir: $TEMP_DIR"

# Copy viewer SPA
cp "$VIEWER_DIR/index.html" "$TEMP_DIR/"
cp "$VIEWER_DIR/files.json" "$TEMP_DIR/"

# Copy markdown content (flat copy so paths match manifest)
if [ -d "$VIEWER_DIR/MarkdownSV" ]; then
    cp -r "$VIEWER_DIR/MarkdownSV/." "$TEMP_DIR/"
    echo -e "${GREEN}   ✅ Copied MarkdownSV content${NC}"
else
    echo -e "${RED}❌ MarkdownSV folder not found${NC}"
    rm -rf "$TEMP_DIR"
    exit 1
fi

# Add .nojekyll to prevent Jekyll processing (important for _ prefixed files)
touch "$TEMP_DIR/.nojekyll"

echo -e "${GREEN}✅ Deploy folder ready${NC}"
echo ""

# Step 3: Push to gh-pages
echo -e "${YELLOW}🚀 Deploying to gh-pages branch...${NC}"
cd "$TEMP_DIR"
git init -b gh-pages
git add -A
git commit -m "Deploy MDviewer to GitHub Pages — $(date '+%Y-%m-%d %H:%M:%S')"
git push -f "$REMOTE_URL" gh-pages

cd "$REPO_ROOT"
rm -rf "$TEMP_DIR"

echo ""
echo -e "${GREEN}✅ Deployed to gh-pages branch${NC}"
echo ""

# Instructions
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}🎉 Deployment Complete!${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 Next Steps (first time only):"
echo ""
echo "1. Go to repo settings:"
echo "   https://github.com/${USERNAME}/${REPO}/settings/pages"
echo ""
echo "2. Under 'Build and deployment':"
echo "   - Source: Deploy from a branch"
echo "   - Branch: gh-pages"
echo "   - Folder: / (root)"
echo ""
echo "3. Click 'Save' → wait 2-3 min"
echo ""
echo "4. Visit your site:"
echo -e "   ${BLUE}${PAGES_URL}${NC}"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
