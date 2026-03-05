#!/usr/bin/env python3
"""
File watcher: auto-run generate-manifest.py when .md files change.
No commit needed — add/edit/delete .md → manifest updates → refresh viewer.
Requires: pip install watchdog (or use without: python3 watch-manifest.py --no-watch for one-shot)
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    HAS_WATCHDOG = True
except ImportError:
    HAS_WATCHDOG = False


def run_generate_manifest():
    """Run generate-manifest.py in current dir"""
    script = Path(__file__).parent / 'generate-manifest.py'
    subprocess.run([sys.executable, str(script)], cwd=Path(__file__).parent)


class ManifestHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self._debounce_sec = 0.5
        self._last_run = 0

    def on_any_event(self, event):
        if event.is_directory:
            return
        path = getattr(event, 'dest_path', None) or event.src_path
        if path and path.endswith('.md'):
            import time
            now = time.time()
            if now - self._last_run >= self._debounce_sec:
                self._last_run = now
                print("\n📝 .md change detected → regenerating files.json")
                run_generate_manifest()


def main():
    parser = argparse.ArgumentParser(description='Watch .md files and auto-update files.json')
    parser.add_argument('--no-watch', action='store_true', help='Run manifest once and exit (no watching)')
    args = parser.parse_args()

    root = Path(__file__).parent
    os.chdir(root)

    if args.no_watch or not HAS_WATCHDOG:
        if not HAS_WATCHDOG and not args.no_watch:
            print("⚠️  Install watchdog for live watching: pip install watchdog")
            print("   Running manifest once (use --no-watch to suppress this message)\n")
        run_generate_manifest()
        if args.no_watch or not HAS_WATCHDOG:
            return

    # Watch content/ if exists, else .
    watch_path = root / 'content' if (root / 'content').exists() else root
    event_handler = ManifestHandler()
    observer = Observer()
    observer.schedule(event_handler, str(watch_path), recursive=True)
    observer.start()

    print(f"👀 Watching {watch_path} for .md changes...")
    print("   Add/edit/delete .md → files.json auto-updates → refresh viewer")
    print("   Press Ctrl+C to stop\n")

    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("\n👋 Stopped.")


if __name__ == "__main__":
    main()
