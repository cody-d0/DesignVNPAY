#!/bin/bash
# Deploy to GitHub Pages Script

set -e  # Exit on error

echo "🚀 GitHub Pages Deployment Script"
echo "=================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if git is initialized
if [ ! -d .git ]; then
    echo -e "${RED}❌ Error: Not a git repository${NC}"
    echo "Run: git init"
    exit 1
fi

# Get repository info
REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "")

if [ -z "$REMOTE_URL" ]; then
    echo -e "${YELLOW}⚠️  No remote repository configured${NC}"
    echo ""
    echo "Please follow these steps:"
    echo ""
    echo "1. Create a new repository on GitHub:"
    echo "   https://github.com/new"
    echo ""
    echo "2. Name it: markdown-viewer (or your preferred name)"
    echo "3. Make it PUBLIC (required for free GitHub Pages)"
    echo "4. Don't initialize with README"
    echo ""
    echo "5. Then run these commands:"
    echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
    echo "   git branch -M main"
    echo "   git add ."
    echo "   git commit -m \"Initial commit\""
    echo "   git push -u origin main"
    echo ""
    echo "6. Run this script again: ./deploy-github-pages.sh"
    exit 1
fi

echo -e "${BLUE}📍 Repository: ${REMOTE_URL}${NC}"
echo ""

# Extract username and repo name from URL
if [[ $REMOTE_URL =~ github\.com[:/]([^/]+)/([^/.]+) ]]; then
    USERNAME="${BASH_REMATCH[1]}"
    REPO="${BASH_REMATCH[2]}"
    PAGES_URL="https://${USERNAME}.github.io/${REPO}/"
else
    echo -e "${RED}❌ Could not parse GitHub URL${NC}"
    exit 1
fi

echo -e "${BLUE}👤 Username: ${USERNAME}${NC}"
echo -e "${BLUE}📦 Repository: ${REPO}${NC}"
echo -e "${BLUE}🌐 Pages URL: ${PAGES_URL}${NC}"
echo ""

# Generate manifest from MarkdownSV folder
echo -e "${YELLOW}📝 Generating file manifest from MarkdownSV...${NC}"
CONTENT_ROOT="MarkdownSV" python3 generate-manifest.py

if [ ! -f files.json ]; then
    echo -e "${RED}❌ Error: files.json not generated${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Manifest generated${NC}"
echo ""

# Check for uncommitted changes
if [[ -n $(git status -s) ]]; then
    echo -e "${YELLOW}📦 Committing changes...${NC}"
    git add .
    git commit -m "Update for GitHub Pages deployment" || true
    echo -e "${GREEN}✅ Changes committed${NC}"
    echo ""
fi

# Push to main
echo -e "${YELLOW}⬆️  Pushing to main branch...${NC}"
git push origin main

echo -e "${GREEN}✅ Pushed to main${NC}"
echo ""

# Deploy to gh-pages branch
echo -e "${YELLOW}🚀 Deploying to gh-pages branch...${NC}"

# Create temporary directory
TEMP_DIR=$(mktemp -d)
echo "Using temp directory: $TEMP_DIR"

# Copy necessary files
cp index.html "$TEMP_DIR/"
cp files.json "$TEMP_DIR/"

# Copy MarkdownSV content (contents only, so paths match manifest)
if [ -d "MarkdownSV" ]; then
  cp -r MarkdownSV/. "$TEMP_DIR/" 2>/dev/null || cp -r MarkdownSV/* "$TEMP_DIR/" 2>/dev/null || true
else
  echo -e "${RED}❌ Error: MarkdownSV folder not found${NC}"
  exit 1
fi

# Initialize git in temp directory
cd "$TEMP_DIR"
git init
git add -A
git commit -m "Deploy to GitHub Pages"

# Force push to gh-pages
git push -f "$REMOTE_URL" main:gh-pages

cd -
rm -rf "$TEMP_DIR"

echo -e "${GREEN}✅ Deployed to gh-pages branch${NC}"
echo ""

# Instructions
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}🎉 Deployment Complete!${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 Next Steps:"
echo ""
echo "1. Go to your repository settings:"
echo "   https://github.com/${USERNAME}/${REPO}/settings/pages"
echo ""
echo "2. Under 'Build and deployment':"
echo "   - Source: Deploy from a branch"
echo "   - Branch: gh-pages"
echo "   - Folder: / (root)"
echo ""
echo "3. Click 'Save'"
echo ""
echo "4. Wait 2-3 minutes for deployment"
echo ""
echo "5. Visit your site:"
echo -e "   ${BLUE}${PAGES_URL}${NC}"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
