#!/usr/bin/env python3
"""
Generate manifest of all markdown files for GitHub Pages with folder grouping.
Supports CONTENT_ROOT env (default: '.') for scanning from a different base path.
"""

import json
import os
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

def find_markdown_files(base_path=None, include_folders=None):
    """Find all markdown files in the project. base_path defaults to CONTENT_ROOT env or '.'.
    If include_folders is set (e.g. ['MarkdownSV', 'co-op-bank-khcn']), only scan those subdirs.
    Accepts absolute paths (e.g. project root when called from serve-markdown.py).
    Stores path and folder relative to base_path so manifest is portable.
    Uses os.walk(followlinks=True) to follow symlinks."""
    if base_path is None:
        base_path = os.environ.get('CONTENT_ROOT', '.')
    base_path = Path(base_path).resolve()
    # When in viewer/ with cwd, use content/ symlink if it exists (points to parent project)
    if base_path == Path.cwd() and (Path('.') / 'content').exists():
        base_path = (Path('.') / 'content').resolve()
    files = []

    def _walk_and_collect(scan_root):
        """Walk directory tree following symlinks, collect .md files."""
        for dirpath, dirnames, filenames in os.walk(str(scan_root), followlinks=True):
            # Skip hidden directories and node_modules
            dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != 'node_modules']
            for fname in filenames:
                if fname.lower().endswith('.md'):
                    md_file = Path(os.path.join(dirpath, fname))
                    _add_file(md_file, base_path, files)

    if include_folders:
        # Scan only specified subdirs (paths relative to base_path)
        for folder in include_folders:
            folder_path = base_path / folder
            if not folder_path.is_dir():
                continue
            _walk_and_collect(folder_path)
    else:
        _walk_and_collect(base_path)

    return sorted(files, key=lambda x: x['modified'], reverse=True)


def _add_file(md_file, base_path, files):
    # Skip hidden directories and node_modules
    if any(part.startswith('.') for part in md_file.parts) or 'node_modules' in md_file.parts:
        return
    try:
        rel = md_file.relative_to(base_path)
    except ValueError:
        return
    # Folder and path relative to base_path (portable, not cwd-dependent)
    parent = rel.parent
    folder = str(parent) if str(parent) != '.' else 'Root'
    path_str = str(rel)
    stat = md_file.stat()
    mtime = stat.st_mtime
    ctime = getattr(stat, 'st_birthtime', mtime)  # macOS: creation; else fallback to mtime
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
    return [f for f in files if datetime.fromtimestamp(f['modified']) >= threshold]

def get_manifest(base_path=None, include_folders=None):
    """Return manifest dict (for API or file). base_path defaults to CONTENT_ROOT env or '.'.
    If include_folders is set, only scan those subdirs under base_path."""
    files = find_markdown_files(base_path, include_folders)
    folders = group_by_folder(files)
    days_threshold = 7
    newest = mark_newest(files, days_threshold)
    return {
        'generated_at': datetime.now().isoformat(),
        'total_files': len(files),
        'total_folders': len(folders),
        'newest_count': len(newest),
        'newest_days_threshold': days_threshold,
        'newest': newest,
        'folders': folders,
        'files': files
    }

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Generate files.json manifest from markdown files')
    parser.add_argument('--content', '-c', default=None, help='Content folder (default: CONTENT_ROOT env or MarkdownSV)')
    args = parser.parse_args()
    base_path = args.content or os.environ.get('CONTENT_ROOT', '.')
    print(f"🔍 Scanning for markdown files (base: {base_path})...")
    manifest = get_manifest(base_path)
    
    with open('files.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated manifest with {manifest['total_files']} files")
    print(f"📁 Found {manifest['total_folders']} folders:")
    for folder, folder_files in sorted(manifest['folders'].items(), key=lambda x: len(x[1]), reverse=True):
        print(f"   - {folder}: {len(folder_files)} files")
    print(f"🆕 {manifest['newest_count']} newest files (last {manifest['newest_days_threshold']} days)")
    print(f"📄 Output: files.json")

if __name__ == "__main__":
    main()
