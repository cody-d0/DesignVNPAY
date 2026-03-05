#!/usr/bin/env python3
"""
Generate manifest of all markdown files for GitHub Pages with folder grouping
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

def find_markdown_files(base_path=None):
    """Find all markdown files. base_path defaults to CONTENT_ROOT env or '.'."""
    import os
    if base_path is None:
        base_path = os.environ.get('CONTENT_ROOT', '.')
    base_path = Path(base_path).resolve()
    files = []
    
    for md_file in base_path.rglob('*.md'):
        # Skip hidden directories, node_modules, and git
        if any(part.startswith('.') for part in md_file.parts) or 'node_modules' in md_file.parts:
            continue
        
        try:
            rel = md_file.relative_to(base_path)
        except ValueError:
            continue
        parent = rel.parent
        folder = str(parent) if str(parent) != '.' else 'Root'
        path_str = str(rel)
        stat = md_file.stat()
        mtime = stat.st_mtime
        ctime = getattr(stat, 'st_birthtime', mtime)
        file_info = {
            'path': path_str,
            'name': md_file.name,
            'folder': folder,
            'size': stat.st_size,
            'modified': mtime,
            'modified_iso': datetime.fromtimestamp(mtime).isoformat(),
            'created': ctime,
            'created_iso': datetime.fromtimestamp(ctime).isoformat()
        }
        files.append(file_info)
    
    return sorted(files, key=lambda x: x['modified'], reverse=True)

def group_by_folder(files):
    """Group files by folder"""
    folders = defaultdict(list)
    for file in files:
        folders[file['folder']].append(file)
    return dict(folders)

def mark_newest(files, days_threshold=7):
    """Mark files as newest if modified within threshold days"""
    now = datetime.now()
    threshold = now - timedelta(days=days_threshold)
    
    newest = []
    for file in files:
        file_time = datetime.fromtimestamp(file['modified'])
        if file_time >= threshold:
            newest.append(file)
    
    return newest

def main():
    import os
    base_path = os.environ.get('CONTENT_ROOT', '.')
    print(f"🔍 Scanning for markdown files (base: {base_path})...")
    files = find_markdown_files(base_path)
    
    # Group by folder
    folders = group_by_folder(files)
    
    # Mark newest files
    days_threshold = 7
    newest = mark_newest(files, days_threshold)
    
    manifest = {
        'generated_at': datetime.now().isoformat(),
        'total_files': len(files),
        'total_folders': len(folders),
        'newest_count': len(newest),
        'newest_days_threshold': days_threshold,
        'newest': newest,
        'folders': folders,
        'files': files
    }
    
    with open('files.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated manifest with {len(files)} files")
    print(f"📁 Found {len(folders)} folders:")
    for folder, folder_files in sorted(folders.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"   - {folder}: {len(folder_files)} files")
    print(f"🆕 {len(newest)} newest files (last {days_threshold} days)")
    print(f"📄 Output: files.json")

if __name__ == "__main__":
    main()
