#!/bin/sh
# Cài pre-commit hook: mỗi lần commit sẽ tự chạy generate-manifest.py và add files.json nếu có thay đổi.

set -e
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
HOOK_SRC="${ROOT}/githooks/pre-commit"
HOOK_DST="${ROOT}/.git/hooks/pre-commit"

if [ ! -f "$HOOK_SRC" ]; then
  echo "Không tìm thấy githooks/pre-commit"
  exit 1
fi

cp "$HOOK_SRC" "$HOOK_DST"
chmod +x "$HOOK_DST"
echo "Đã cài pre-commit hook: manifest (files.json) sẽ tự tạo lại trước mỗi commit."
echo "Hook: .git/hooks/pre-commit"
