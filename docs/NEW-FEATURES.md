# 🎉 New Features - Folder Grouping & Newest Highlight

## 📌 Viewer Updates (2026-02-12)

### Header
- **Minimal flat header** — fixed height 72px, không nhảy khi chuyển view
- **Back above title** — CTA "Quay lại" trên page title, title canh trái
- **Title** — trang chủ: "Markdown"; xem file: tên file + breadcrumb

### Theme
- **Toggle Sáng | Tối** — 2 segment chọn light/dark
- **Mesh toggle** — nút riêng bật/tắt glass mesh gradient
- Kết hợp: Sáng + Mesh = light-mesh; Tối + Mesh = dark-mesh
- Lưu: `xpos-docs-theme` (light/dark) + `xpos-docs-mesh` (true/false)

### Glass Mesh Gradient
- **Light mesh** — nền #EFF6FF + gradient pastel tím/xanh/hồng/cyan
- **Dark mesh** — nền #1E293B + gradient sáng hơn
- Header: backdrop-filter blur 12px

### Images
- **1 view scroll** — tất cả ảnh trong file nằm chung 1 thanh cuộn ngang
- **Alt caption** — chú thích rõ dưới mỗi ảnh

### Manifest
- **Pre-commit hook** — chạy `generate-manifest.py` và add files.json trước mỗi commit
- Cài: `./install-manifest-hook.sh`

---

## ✨ What's New

### 1. **Folder Organization**
Files are now grouped by their parent folders for better navigation:
- **Root** - Documentation files in the project root
- **XPOS App** - XPOS application documentation
- **XPOS BO** - XPOS Back Office documentation

### 2. **Newest Files Highlight**
Files modified within the last 7 days are highlighted with:
- ✅ Green left border
- ✅ "NEW" badge
- ✅ Light green background gradient

### 3. **Filter Tabs**
Quick filter between views:
- **All Files** - Browse by folder
- **🆕 Newest** - Show only recently updated files

### 4. **Enhanced Search**
Search now supports:
- File names
- File paths
- Folder names
- Results grouped by folder

## 🎨 UI Enhancements

### Folder Headers
Each folder section has:
- Folder icon (SVG)
- Folder name
- File count badge

### Newest Indicators
Files are marked as "NEW" when:
- Modified within last 7 days
- Automatic detection via file timestamps
- Visual: Green accent color (#10B981)

### Filter Badges
Each tab shows:
- Total count
- Updates dynamically
- Active state styling

## 📊 Data Structure

### Updated files.json
```json
{
  "generated_at": "2026-02-11T...",
  "total_files": 26,
  "total_folders": 3,
  "newest_count": 26,
  "newest_days_threshold": 7,
  "newest": [...],
  "folders": {
    "Root": [...],
    "XPOS/XPOS PRD - updated 2026.02.10/xpos-app": [...],
    "XPOS/XPOS PRD - updated 2026.02.10/xpos-bo": [...]
  },
  "files": [...]
}
```

## 🎯 UX Improvements

### Navigation
- **Active State** - Current folder/filter visually indicated
- **Breadcrumbs** - Shows folder structure
- **Back Button** - Returns to previous view
- **Smooth Scroll** - Anchor links scroll smoothly

### Accessibility
- **Keyboard Navigation** - All filters keyboard accessible
- **ARIA Labels** - Proper screen reader support
- **Focus States** - Visible focus indicators
- **Tab Order** - Logical tab order

### Performance
- **Debounced Search** - 200ms delay for smooth typing
- **Grouped Rendering** - Efficient DOM updates
- **Lazy Updates** - Only re-render when needed

## 🚀 How to Use

### View All Files by Folder
1. Click "All Files" tab (default view)
2. Browse files organized by folder
3. Each folder shows file count

### View Newest Files
1. Click "🆕 Newest" tab
2. See all files updated in last 7 days
3. Green "NEW" badges indicate recent updates

### Search Within Folders
1. Type in search box
2. Results filtered within current view
3. Folder grouping maintained

### Customize Newest Threshold
Edit `generate-manifest.py`:
```python
days_threshold = 7  # Change to your preference
newest = mark_newest(files, days_threshold)
```

Then regenerate:
```bash
python3 generate-manifest.py
```

## 📐 Design System Updates

### New Colors
```css
--color-accent: #10B981;        /* Green for newest */
--color-accent-light: #D1FAE5;  /* Light green background */
```

### New Components
- **Filter Tabs** - Tab navigation pattern
- **Folder Sections** - Collapsible folder groups
- **Newest Badge** - "NEW" indicator
- **Filter Badges** - Count indicators

## 🎨 UI/UX Pro Max Guidelines Applied

### Category & Navigation (UX Domain)
✅ **Active State** - Current tab highlighted with color + border  
✅ **Heading Hierarchy** - h2 for folder names (semantic)  
✅ **Smooth Scroll** - `scroll-behavior: smooth` on html  
✅ **Breadcrumbs** - Shows location in folder structure

### Interaction
✅ **Tab Order** - Matches visual order  
✅ **Focus States** - Visible on all interactive elements  
✅ **Hover Feedback** - Visual changes on hover  
✅ **Cursor Pointer** - On all clickable elements

### Accessibility
✅ **ARIA Labels** - role="tab", aria-selected  
✅ **Skip Links** - Skip to main content  
✅ **Keyboard Nav** - All features keyboard accessible  
✅ **Semantic HTML** - Proper heading hierarchy

## 🔄 Workflow

### Adding New Files
1. Add `.md` files to project
2. Run: `python3 generate-manifest.py`
3. Files automatically categorized by folder
4. Newest files (last 7 days) highlighted

### Updating Existing Files
1. Edit `.md` file
2. Save (updates timestamp)
3. Run: `python3 generate-manifest.py`
4. File moves to "Newest" if within threshold

## 📊 Statistics

Current project structure:
```
Total Files:    26
Total Folders:  3
Newest Files:   26 (last 7 days)

Breakdown:
- Root:         10 files
- XPOS App:     9 files
- XPOS BO:      7 files
```

## 🎯 Benefits

### For Users
- ✅ **Better Organization** - Logical folder grouping
- ✅ **Quick Discovery** - Find newest content fast
- ✅ **Visual Hierarchy** - Clear folder structure
- ✅ **Efficient Search** - Search within categories

### For Developers
- ✅ **Auto-Detection** - Automatic folder grouping
- ✅ **Timestamp Tracking** - File modification dates
- ✅ **Flexible Threshold** - Configurable "newest" period
- ✅ **Maintainable** - Single script regeneration

## 🛠️ Configuration

### Adjust Newest Threshold
```python
# In generate-manifest.py
days_threshold = 7  # Default: 7 days
```

### Folder Display Names
Folders use directory structure:
- `.` → "Root"
- `XPOS/folder/` → Full path shown

To customize, edit `generate-manifest.py`:
```python
folder = str(md_file.parent) if str(md_file.parent) != '.' else 'Root'
```

## 📱 Responsive Behavior

### Mobile (< 768px)
- Single column layout
- Tabs wrap to multiple rows
- Touch-friendly targets (44px+)

### Tablet (768px+)
- 2-column file grid
- Tabs in single row
- Hover states

### Desktop (1024px+)
- 3-column file grid
- Full folder headers
- Smooth animations

## ✅ Testing Done

- [x] Folder grouping works
- [x] Newest detection accurate
- [x] Filter tabs functional
- [x] Search within folders
- [x] Badge counts correct
- [x] Responsive on all sizes
- [x] Keyboard navigation
- [x] Screen reader compatible
- [x] Newest badge visible
- [x] Hover states smooth

## 🎊 Summary

New features provide:
1. **Better Organization** via folder grouping
2. **Content Discovery** via newest highlighting
3. **Quick Navigation** via filter tabs
4. **Enhanced Search** with folder context

All implemented following UI/UX Pro Max guidelines for professional documentation interfaces.

---

## PRD Cross-File Mapping Skill (2026-02-12)

New Cursor skill for analyzing cross-file dependencies, shared fields, and inconsistencies across PRD markdown files.

- **Skill path:** `.cursor/skills/prd-crossfile-mapping/SKILL.md`
- **Use when:** you need to map links between PRD files, find shared displayed fields, detect enum/scope/requiredness mismatches, or generate a canonical field contract for FE/BE alignment.
- **Outputs:** Priority Findings, mermaid dependency diagram, 10 structured tables, canonical field contract with alias normalization.
- **Includes seed data** from xpos-app analysis (4 known conflicts, 18 shared fields, 10 cross-links).

---

**Version:** 2.0  
**Release Date:** 2026-02-11  
**Design System:** Minimalism & Swiss Style  
**UX Pattern:** Category Navigation + Time-based Filtering
