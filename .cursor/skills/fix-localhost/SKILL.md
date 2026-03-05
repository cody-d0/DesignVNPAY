# Fix Localhost Connection Skill

Automatically diagnose and fix localhost connection issues for development servers.

## Trigger Keywords

Use this skill when user mentions:
- `localhost can't connect`
- `localhost not working`
- `connection refused`
- `unable to connect localhost`
- `server not responding`
- `port not accessible`
- `ERR_CONNECTION_REFUSED`

## Problem Types

### 1. Server Not Running
- Process died or was killed
- Server never started
- Crash on startup

### 2. Port Already in Use
- Another process using the port
- Zombie process holding port
- Multiple server instances

### 3. Browser Cache
- Old version cached
- Service worker stale
- DNS cache issue

### 4. Permission Issues
- Port < 1024 requires sudo
- Firewall blocking
- System security settings

## Diagnostic Workflow

### Step 1: Check if Server is Running

```bash
# Check specific port (e.g., 9999)
lsof -ti:9999

# Check process details
ps aux | grep "python.*9999"

# Check all Python servers
ps aux | grep "python.*server"
```

**Interpretation:**
- Output = PID → Server running
- No output → Server not running
- Multiple PIDs → Multiple instances (problem!)

### Step 2: Check Port Availability

```bash
# Check if port is free
nc -zv localhost 9999

# Alternative: Test HTTP connection
curl -I http://localhost:9999
```

**Interpretation:**
- "Connection refused" → Server not running
- "succeeded" → Port accessible
- Timeout → Firewall or routing issue

### Step 3: Check Terminal Logs

```bash
# If using Cursor terminal tracking
cat /path/to/terminals/TERMINAL_ID.txt

# Check for error messages:
# - "Address already in use"
# - "Permission denied"
# - "Port ... is already allocated"
```

## Fix Procedures

### Fix 1: Kill Zombie Processes

```bash
# Kill all processes on port 9999
kill -9 $(lsof -ti:9999)

# Or kill specific PID
kill -9 PID_NUMBER

# Nuclear option: Kill all Python servers
pkill -9 -f "python.*server"
```

### Fix 2: Start Server (Fresh Start)

```bash
# Navigate to project
cd "/path/to/project"

# Option A: Python HTTP Server (Simple)
python3 -m http.server 9999

# Option B: Custom Server Script
python3 serve-markdown.py

# Run in background (if needed)
python3 -m http.server 9999 &

# Check it started
sleep 2 && lsof -ti:9999
```

### Fix 3: Clear Browser Cache

**Automated (macOS):**
```bash
# Safari
rm -rf ~/Library/Caches/com.apple.Safari/

# Chrome
rm -rf ~/Library/Caches/Google/Chrome/Default/Cache/
```

**Manual Instructions:**
```
Chrome/Edge:
  Cmd+Shift+R (Hard refresh)
  Or: DevTools → Right-click reload → "Empty Cache and Hard Reload"

Safari:
  Cmd+Option+R (Hard refresh)
  Or: Develop → Empty Caches

Firefox:
  Cmd+Shift+R (Hard refresh)
```

### Fix 4: Try Different Port

```bash
# Try common alternative ports
python3 -m http.server 8080
python3 -m http.server 8888
python3 -m http.server 3000
```

## Full Recovery Script

Create this as a single command:

```bash
#!/bin/bash
# fix-localhost.sh

PORT=9999
PROJECT_DIR="/Users/dataism/Documents/UXreview"

echo "🔍 Diagnosing localhost:$PORT..."

# Check if port is in use
if lsof -ti:$PORT > /dev/null; then
    echo "⚠️  Port $PORT is in use. Killing processes..."
    kill -9 $(lsof -ti:$PORT)
    sleep 1
else
    echo "✓ Port $PORT is available"
fi

# Start server
echo "🚀 Starting server on port $PORT..."
cd "$PROJECT_DIR"
python3 -m http.server $PORT > /dev/null 2>&1 &

# Wait and verify
sleep 2

if lsof -ti:$PORT > /dev/null; then
    echo "✅ Server running on http://localhost:$PORT"
    echo "📍 Open: http://localhost:$PORT"
    echo ""
    echo "🔄 If browser shows old content:"
    echo "   - Hard refresh: Cmd+Shift+R (macOS) or Ctrl+Shift+R (Windows)"
else
    echo "❌ Failed to start server"
    echo "Try manually: cd '$PROJECT_DIR' && python3 -m http.server $PORT"
fi
```

## Execution Steps

When user reports localhost connection issue:

### 1. Quick Diagnosis
```bash
# Check server status
lsof -ti:9999 || echo "Server not running"

# Check if can connect
curl -I http://localhost:9999 2>&1 | head -1
```

### 2. Apply Fix
```bash
# Kill existing + restart
pkill -9 -f "python.*9999"
cd "/Users/dataism/Documents/UXreview"
python3 -m http.server 9999 &
sleep 2
curl -I http://localhost:9999
```

### 3. Verify
```bash
# Should show:
# - PID from lsof
# - HTTP/1.0 200 OK from curl
```

### 4. Browser Instructions
```
1. Open: http://localhost:9999
2. Hard refresh: Cmd+Shift+R (macOS) or Ctrl+Shift+R (Windows)
3. If still old content: Open Incognito/Private window
```

## Common Error Messages

### "Address already in use"
```bash
# Fix: Kill process on that port
kill -9 $(lsof -ti:9999)
```

### "Permission denied"
```bash
# Fix: Use port > 1024 or run with sudo (not recommended)
python3 -m http.server 8080  # Use higher port
```

### "Connection refused"
```bash
# Fix: Server not running, start it
python3 -m http.server 9999
```

### "ERR_EMPTY_RESPONSE"
```bash
# Fix: Server crashed, check logs and restart
python3 -m http.server 9999
```

## Prevention

### Use Process Manager

**Option 1: Screen (Built-in)**
```bash
# Start in screen session
screen -S webserver
python3 -m http.server 9999
# Detach: Ctrl+A, then D

# Reattach later
screen -r webserver
```

**Option 2: PM2 (If installed)**
```bash
pm2 start "python3 -m http.server 9999" --name markdown-viewer
pm2 save
pm2 startup
```

### Use Different Port Per Project

```bash
# Project 1: Port 8001
# Project 2: Port 8002
# etc.
```

### Create Startup Script

```bash
# start-server.sh
#!/bin/bash
cd "/Users/dataism/Documents/UXreview"
python3 -m http.server 9999
```

## Troubleshooting Matrix

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| "Connection refused" | Server not running | Start server |
| "Address in use" | Port occupied | Kill process + restart |
| Old content shows | Browser cache | Hard refresh |
| Slow/timeout | Server crashed | Check logs + restart |
| 404 on files | Wrong directory | cd to project root |

## Quick Commands Reference

```bash
# Check server
lsof -ti:9999

# Kill server
kill -9 $(lsof -ti:9999)

# Start server (simple)
python3 -m http.server 9999

# Start server (custom)
python3 serve-markdown.py

# Test connection
curl -I http://localhost:9999

# View in browser
open http://localhost:9999  # macOS
start http://localhost:9999  # Windows
```

## Success Criteria

Server is working when:
- ✅ `lsof -ti:9999` shows PID
- ✅ `curl -I http://localhost:9999` shows 200 OK
- ✅ Browser loads page (after hard refresh)
- ✅ No console errors in DevTools

## Output Format

When fixing, provide:
1. Diagnosis (what was wrong)
2. Action taken (what was fixed)
3. Verification (proof it works)
4. Next steps (how to access)

Example:
```
🔍 Diagnosis: Server was not running (no process on port 9999)
🔧 Action: Started Python HTTP server on port 9999
✅ Verification: Server responding with HTTP 200
📍 Access: http://localhost:9999 (Hard refresh: Cmd+Shift+R)
```
