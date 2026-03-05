# 📄 Markdown Presentation Server

Beautiful local web server for presenting Markdown files with modern UI.

## 🚀 Quick Start

```bash
python3 serve-markdown.py
```

Then open your browser: **http://localhost:9999**

## ✨ Features

- 🎨 **Beautiful Design** - Modern gradient header with purple/blue theme
- 📁 **Auto-Discovery** - Automatically finds all `.md` files in the project
- 📱 **Responsive** - Works on desktop and mobile
- 🎯 **Easy Navigation** - Click any file to view, back button to return
- 📊 **Table Support** - Beautiful table rendering with hover effects
- 💻 **Code Highlighting** - Syntax-highlighted code blocks
- 🔗 **Smart Links** - Clickable links with hover effects
- 📝 **Full Markdown** - Supports all standard markdown features

## 🎨 UI Highlights

- **Gradient Header**: Purple to blue gradient (#667eea → #764ba2)
- **Hover Effects**: Smooth transitions on file list items
- **Beautiful Tables**: Gradient headers, hover rows
- **Code Blocks**: Dark theme with syntax highlighting
- **Blockquotes**: Left border with light purple background
- **Clean Typography**: System fonts for best readability

## 📂 File Structure

```
serve-markdown.py    # Main server script
README-MARKDOWN-SERVER.md    # This file
```

## 🛠️ How It Works

1. **File Discovery**: Scans all directories for `.md` files (skips hidden folders and node_modules)
2. **Client-Side Rendering**: Uses marked.js CDN for fast markdown parsing
3. **No Dependencies**: Pure Python 3 with built-in libraries only
4. **Zero Config**: Just run and go!

## 🎯 Use Cases

- Present PRD documents to team
- Review markdown documentation
- Share technical specs
- Display project README files
- Present design system docs
- Review meeting notes

## 🔧 Customization

Edit `serve-markdown.py` to customize:

- **PORT**: Change port number (default: 9999)
- **CSS Styles**: Modify the `<style>` blocks
- **Color Scheme**: Update gradient colors in header
- **File Filters**: Adjust file discovery logic

## 🛑 Stop Server

Press `Ctrl+C` in the terminal to stop the server.

## 📝 Notes

- Server runs on localhost only (not accessible from network)
- All markdown files are auto-discovered on each page load
- Images in markdown must use relative paths
- No installation required - uses Python 3 standard library

## 🎉 Enjoy!

Your markdown files are now beautifully presented at:
**http://localhost:9999**
