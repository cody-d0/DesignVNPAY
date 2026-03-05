#!/usr/bin/env bash
# fix-localhost.sh — Fix local Markdown viewer (port 9999). Kills zombie process, starts viewer, verifies.

set -e
PORT=9999
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🔍 Diagnosing localhost:$PORT..."

# Kill any process already on port
if lsof -ti:$PORT >/dev/null 2>&1; then
  echo "⚠️  Port $PORT in use. Stopping existing process..."
  kill -9 $(lsof -ti:$PORT) 2>/dev/null || true
  sleep 1
fi

echo "🚀 Starting Markdown viewer (content: MarkdownSV)..."
cd "$PROJECT_ROOT"
nohup python3 viewer/serve-markdown.py > /dev/null 2>&1 &
sleep 2

# Verify
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 "http://127.0.0.1:$PORT/" 2>/dev/null || echo "000")

if [ "$HTTP_CODE" = "200" ]; then
  echo ""
  echo "✅ Server running"
  echo "📍 Open: http://127.0.0.1:$PORT"
  echo "   (Use 127.0.0.1 if localhost fails in Firefox)"
  echo ""
  echo "🦊 Firefox still “Unable to connect”?"
  echo "   → macOS: System Settings → Privacy & Security → Local Network → allow Firefox"
  echo "   → Or try the same URL in Safari/Chrome"
  echo ""
  echo "⏹  To stop: kill \$(lsof -ti:$PORT)"
else
  echo "❌ Server did not respond (HTTP $HTTP_CODE). Check viewer/serve-markdown.py"
  kill $(lsof -ti:$PORT) 2>/dev/null || true
  exit 1
fi
