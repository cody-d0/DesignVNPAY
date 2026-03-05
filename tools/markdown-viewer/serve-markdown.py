#!/usr/bin/env python3
"""
Markdown Viewer Server - Serves SPA (index.html) with live file list API.
Uses marked.js CDN for client-side rendering. No external Python dependencies.
"""

import http.server
import socketserver
import os
import json
import re
import urllib.parse
from pathlib import Path

PORT = 9999

# Import get_manifest from generate-manifest.py (module name has hyphen)
import importlib.util
_manifest_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'generate-manifest.py')
_spec = importlib.util.spec_from_file_location('gen_manifest', _manifest_path)
_gen_manifest = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_gen_manifest)
get_manifest = _gen_manifest.get_manifest

# Project root = 2 levels up from viewer/ (tools/markdown-viewer/ → tools/ → UXreview/)
VIEWER_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(VIEWER_DIR, '..', '..'))
# Content: chỉ MarkdownSV cho index (Last update + All). MarkdownSV chứa symlinks tới toàn bộ content.
CONTENT_FOLDERS = ['MarkdownSV']

# Extra roots allowed for Paste and go (absolute paths). Env: MARKDOWN_VIEWER_EXTRA_ROOTS, comma-separated.
# Example: export MARKDOWN_VIEWER_EXTRA_ROOTS="/Users/you/.gemini"
def _extra_allowed_roots():
    raw = os.environ.get('MARKDOWN_VIEWER_EXTRA_ROOTS', '').strip()
    if not raw:
        return []
    roots = []
    for p in raw.split(','):
        p = p.strip()
        if not p:
            continue
        try:
            roots.append(os.path.realpath(os.path.abspath(p)))
        except Exception:
            pass
    return roots

EXTRA_ALLOWED_ROOTS = _extra_allowed_roots()

# Revision tăng khi webhook POST /api/refresh được gọi → client poll /api/revision và sync (loadManifest)
manifest_revision = 0

# Load MSV error code registry (viewer/error-codes.json) for agent-friendly error pages
def _load_error_codes():
    p = os.path.join(VIEWER_DIR, 'error-codes.json')
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('codes', {})
    except Exception:
        return {}

ERROR_CODES = _load_error_codes()

# Error pages: mã HTTP → (tiêu đề ngắn, mô tả thân thiện) — ui-ux-pro-max: rõ ràng, có CTA về trang chủ
ERROR_PAGES = {
    400: ('Bad Request', 'Yêu cầu không hợp lệ. Kiểm tra lại đường dẫn hoặc tham số.'),
    403: ('Forbidden', 'Bạn không có quyền truy cập tài nguyên này.'),
    404: ('Not Found', 'Không tìm thấy trang hoặc tệp. Có thể đường dẫn sai hoặc tài nguyên đã bị xóa.'),
    405: ('Method Not Allowed', 'Phương thức yêu cầu không được phép cho đường dẫn này.'),
    500: ('Server Error', 'Lỗi máy chủ. Vui lòng thử lại sau.'),
    502: ('Bad Gateway', 'Lỗi kết nối upstream. Thử lại sau.'),
    503: ('Service Unavailable', 'Dịch vụ tạm thời không khả dụng. Thử lại sau.'),
}


def html_escape(s):
    if s is None:
        return ''
    return (s
        .replace('&', '&amp;')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
        .replace('"', '&quot;')
        .replace("'", '&#39;'))


def get_error_html(code, message=None, msv_code=None, msv_context=None):
    """Trả về HTML trang lỗi. Luôn có toàn bộ thông tin lỗi (ẩn bớt sau 2 câu), CTA Copy cho agent. Hỗ trợ theme light/dark/mesh giống viewer."""
    title, friendly = ERROR_PAGES.get(code, ('Error', 'Đã xảy ra lỗi. Vui lòng thử lại.'))
    detail = (message or '').strip()
    if detail:
        detail_escaped = html_escape(detail)
        detail_block = ('<p class="error-detail" role="status">Chi tiết: <code>%s</code></p>' % detail_escaped)
    else:
        detail_block = ''

    # Build full payload (toàn bộ thông tin) cho copy — luôn đủ, không cắt
    lines = [
        'HTTP %s %s' % (code, title),
        'Message: %s' % friendly,
    ]
    if detail:
        lines.append('Detail: %s' % detail)

    agent_block = ''
    agent_json = None
    if msv_code and msv_code in ERROR_CODES:
        rec = ERROR_CODES[msv_code]
        ctx = msv_context or {}
        try:
            msg_detail = (rec.get('message_detail') or '').format(**ctx)
        except KeyError:
            msg_detail = (rec.get('message_detail') or '') + ' ' + str(ctx)
        agent_fix = rec.get('agent_fix') or []
        file_ref = rec.get('file_ref') or []
        if isinstance(agent_fix, str):
            agent_fix = [agent_fix]
        agent_json = {
            'msv_code': msv_code,
            'category': rec.get('category'),
            'message_short': rec.get('message_short'),
            'message_detail': msg_detail or detail,
            'agent_fix': agent_fix,
            'file_ref': file_ref,
            'http_status': code,
        }
        lines.append('MSV: %s' % msv_code)
        lines.append('Detail: %s' % (msg_detail or detail))
        lines.append('File ref: %s' % ', '.join(file_ref))
        for i, step in enumerate(agent_fix, 1):
            lines.append('Fix %s: %s' % (i, step))
        fix_lines = ''.join('<li>' + html_escape(step) + '</li>' for step in agent_fix)
        ref_line = ', '.join(html_escape(f) for f in file_ref)
        agent_block = '''
    <section class="error-agent" role="complementary" aria-labelledby="agent-title">
      <h2 id="agent-title" class="error-agent-title">Cho agent: ''' + html_escape(msv_code) + '''</h2>
      <p class="error-agent-detail">''' + html_escape(msg_detail or detail) + '''</p>
      <p class="error-agent-ref"><strong>File tham chiếu:</strong> ''' + ref_line + '''</p>
      <ol class="error-agent-fix">''' + fix_lines + '''</ol>
      <script type="application/json" id="error-meta">''' + html_escape(json.dumps(agent_json, ensure_ascii=False)) + '''</script>
    </section>'''

    full_payload = '\n'.join(lines)
    full_payload_escaped = html_escape(full_payload)

    preview_escaped = html_escape(friendly)

    return '''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>''' + html_escape(str(code)) + ' ' + html_escape(title) + '''</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --color-primary: #475569;
      --color-cta: #2563EB;
      --color-background: #F8FAFC;
      --color-text: #1E293B;
      --color-text-muted: #64748B;
      --color-surface: #FFFFFF;
      --color-border: #E2E8F0;
      --color-hover: #F1F5F9;
      --color-accent: #10B981;
      --font: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --space-sm: 0.5rem;
      --space-md: 1rem;
      --space-lg: 1.5rem;
      --space-xl: 2rem;
      --space-2xl: 3rem;
      --text-sm: 0.875rem;
      --text-base: 1rem;
      --text-lg: 1.125rem;
      --text-2xl: 1.5rem;
      --text-3xl: 1.875rem;
      --radius: 8px;
      --transition: 150ms cubic-bezier(0.4, 0, 0.2, 1);
    }
    [data-theme="dark"] {
      --color-primary: #94A3B8;
      --color-cta: #60A5FA;
      --color-background: #0F172A;
      --color-text: #F1F5F9;
      --color-text-muted: #94A3B8;
      --color-surface: #1E293B;
      --color-border: #334155;
      --color-hover: #334155;
      --color-accent: #34D399;
    }
    [data-theme="light-mesh"] {
      --color-primary: #475569;
      --color-cta: #4F46E5;
      --color-text: #1E293B;
      --color-text-muted: #64748B;
      --color-border: rgba(100, 116, 139, 0.4);
      --color-surface: rgba(255, 255, 255, 0.65);
      --color-hover: rgba(255, 255, 255, 0.5);
      --color-accent: #10B981;
    }
    [data-theme="dark-mesh"] {
      --color-primary: #A5B4FC;
      --color-cta: #818CF8;
      --color-text: #F1F5F9;
      --color-text-muted: #94A3B8;
      --color-border: rgba(148, 163, 184, 0.35);
      --color-surface: rgba(255, 255, 255, 0.08);
      --color-hover: rgba(255, 255, 255, 0.06);
      --color-accent: #34D399;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html { font-family: var(--font); font-size: 16px; line-height: 1.6; -webkit-font-smoothing: antialiased; }
    body {
      min-height: 100vh;
      background: var(--color-background);
      color: var(--color-text);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: var(--space-xl);
    }
    .error-card {
      max-width: 560px;
      width: 100%;
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: 12px;
      padding: var(--space-2xl);
      text-align: center;
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -2px rgba(0,0,0,0.05);
    }
    .error-agent {
      text-align: left;
      margin-top: var(--space-xl);
      padding-top: var(--space-lg);
      border-top: 1px solid var(--color-border);
      font-size: var(--text-sm);
      color: var(--color-text-muted);
    }
    .error-agent-title { font-size: var(--text-base); font-weight: 600; color: var(--color-text); margin-bottom: var(--space-sm); }
    .error-agent-detail { margin-bottom: var(--space-sm); }
    .error-agent-ref { margin-bottom: var(--space-md); }
    .error-agent-fix { margin-left: 1.25rem; padding-left: 0; }
    .error-agent-fix li { margin-bottom: 0.25rem; }
    .error-code {
      font-size: var(--text-3xl);
      font-weight: 700;
      color: var(--color-cta);
      letter-spacing: -0.02em;
      margin-bottom: var(--space-sm);
    }
    .error-title {
      font-size: var(--text-lg);
      font-weight: 600;
      color: var(--color-text);
      margin-bottom: var(--space-md);
    }
    .error-message {
      font-size: var(--text-base);
      color: var(--color-text-muted);
      line-height: 1.6;
      margin-bottom: var(--space-lg);
    }
    .error-detail {
      font-size: var(--text-sm);
      color: var(--color-text-muted);
      text-align: left;
      background: var(--color-hover);
      border-radius: var(--radius);
      padding: var(--space-md);
      margin-bottom: var(--space-lg);
      word-break: break-word;
    }
    .error-detail code { font-family: ui-monospace, monospace; font-size: 0.9em; }
    .error-actions { margin-top: var(--space-xl); display: flex; flex-wrap: wrap; gap: var(--space-md); justify-content: center; align-items: center; }
    .btn-primary, .btn-copy {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: var(--space-sm);
      padding: 0.625rem 1.25rem;
      font-size: var(--text-base);
      font-weight: 500;
      border: none;
      border-radius: var(--radius);
      cursor: pointer;
      text-decoration: none;
      transition: opacity var(--transition), background-color var(--transition), color var(--transition);
    }
    .btn-primary {
      color: #fff;
      background: var(--color-cta);
    }
    .btn-primary:hover { opacity: 0.95; }
    .btn-primary:focus-visible {
      outline: 2px solid var(--color-cta);
      outline-offset: 2px;
    }
    .btn-copy {
      color: var(--color-text);
      background: var(--color-hover);
      border: 1px solid var(--color-border);
    }
    .btn-copy:hover { background: var(--color-border); }
    .btn-copy:focus-visible {
      outline: 2px solid var(--color-cta);
      outline-offset: 2px;
    }
    .btn-copy.copied { background: var(--color-accent); color: #fff; border-color: var(--color-accent); }
    .error-full-wrap { text-align: left; margin-top: var(--space-lg); }
    .error-full-toggle {
      font-size: var(--text-sm);
      color: var(--color-cta);
      background: none;
      border: none;
      cursor: pointer;
      padding: var(--space-sm) 0;
      margin-bottom: var(--space-sm);
      text-decoration: underline;
    }
    .error-full-toggle:hover { opacity: 0.9; }
    .error-full-toggle:focus-visible { outline: 2px solid var(--color-cta); outline-offset: 2px; }
    .error-full-payload {
      display: none;
      font-size: var(--text-sm);
      font-family: ui-monospace, monospace;
      white-space: pre-wrap;
      word-break: break-word;
      background: var(--color-hover);
      border: 1px solid var(--color-border);
      border-radius: var(--radius);
      padding: var(--space-md);
      max-height: 280px;
      overflow: auto;
      color: var(--color-text);
      margin-bottom: var(--space-md);
    }
    .error-full-payload[aria-hidden="false"] { display: block; }
    .error-copy-status { font-size: var(--text-sm); color: var(--color-accent); margin-left: var(--space-sm); }
    @media (prefers-reduced-motion: reduce) { .btn-primary, .btn-copy { transition: none; } }
  </style>
</head>
<body>
  <script>
    (function() {
      var t = localStorage.getItem('xpos-docs-theme');
      var mode = 'light';
      if (t === 'light' || t === 'dark') mode = t;
      else if (t === 'light-mesh') mode = 'light-mesh';
      else if (t === 'dark-mesh') mode = 'dark-mesh';
      else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) mode = 'dark';
      document.documentElement.setAttribute('data-theme', mode);
    })();
  </script>
  <!-- Markdown Viewer custom error page (viewer/serve-markdown.py) -->
  <main class="error-card" role="main" aria-labelledby="error-title">
    <p class="error-code" aria-hidden="true">''' + str(code) + '''</p>
    <h1 id="error-title" class="error-title">''' + html_escape(title) + '''</h1>
    <p class="error-message" role="status">''' + preview_escaped + '''</p>
    <div class="error-full-wrap">
      <button type="button" class="error-full-toggle" aria-expanded="false" aria-controls="error-full-payload" id="error-full-toggle">Xem toàn bộ thông tin lỗi</button>
      <pre id="error-full-payload" class="error-full-payload" aria-hidden="true" role="region" aria-label="Toàn bộ thông tin lỗi">''' + full_payload_escaped + '''</pre>
    </div>
    <div class="error-actions">
      <button type="button" class="btn-copy" id="error-copy-btn" aria-label="Copy thông tin lỗi để dán cho agent">Copy thông tin lỗi</button>
      <a href="/" class="btn-primary">Về trang chủ</a>
      <span class="error-copy-status" id="error-copy-status" aria-live="polite"></span>
    </div>
    <script>
      (function() {
        var btn = document.getElementById('error-copy-btn');
        var pre = document.getElementById('error-full-payload');
        var toggle = document.getElementById('error-full-toggle');
        var status = document.getElementById('error-copy-status');
        var payload = pre && pre.textContent ? pre.textContent : '';
        if (toggle && pre) {
          toggle.addEventListener('click', function() {
            var isHidden = pre.getAttribute('aria-hidden') === 'true';
            pre.setAttribute('aria-hidden', isHidden ? 'false' : 'true');
            toggle.setAttribute('aria-expanded', isHidden ? 'true' : 'false');
            toggle.textContent = isHidden ? 'Ẩn bớt' : 'Xem toàn bộ thông tin lỗi';
          });
        }
        if (btn && payload) {
          btn.addEventListener('click', function() {
            navigator.clipboard.writeText(payload).then(function() {
              btn.classList.add('copied');
              btn.textContent = 'Đã copy!';
              if (status) status.textContent = '';
              setTimeout(function() {
                btn.classList.remove('copied');
                btn.textContent = 'Copy thông tin lỗi';
              }, 2000);
            }).catch(function() {
              if (status) status.textContent = 'Không copy được';
            });
          });
        }
      })();
    </script>
''' + agent_block + '''
  </main>
</body>
</html>'''


class MarkdownHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PROJECT_ROOT, **kwargs)

    def send_error(self, code, message=None, explain=None, msv_code=None, msv_context=None):
        """Gửi trang lỗi HTML tùy chỉnh (404, 500, ...). msv_code + msv_context → block 'Cho agent' để fix nhanh."""
        self.log_error("HTTP %s: %s", code, message or '')
        body = get_error_html(code, message, msv_code=msv_code, msv_context=msv_context).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        if self.command != 'HEAD' and body:
            self.wfile.write(body)

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path.rstrip('/') or '/'

        if path == '/':
            self.serve_index()
        elif path == '/api/files':
            self.serve_api_files()
        elif path == '/api/revision':
            self.serve_api_revision()
        elif path == '/api/file' or path.startswith('/api/file?'):
            self.serve_api_file(urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query))
        elif path.endswith('.md'):
            self.serve_markdown_file(path)
        else:
            super().do_GET()

    def serve_markdown_file(self, path):
        """Serve .md file with Cache-Control: no-cache so homepage always gets fresh content (no stale cache)."""
        path_clean = urllib.parse.unquote(path).lstrip('/')
        if not path_clean:
            self.send_error(404, 'Not found', msv_code='MSV-F001', msv_context={'path': '(empty)'})
            return
        full_path = os.path.normpath(os.path.join(PROJECT_ROOT, path_clean))
        try:
            full_path = os.path.abspath(full_path)
            base_real = os.path.realpath(PROJECT_ROOT)
            if full_path != base_real and not (os.path.realpath(full_path).startswith(base_real + os.sep)):
                self.send_error(404, 'Not found', msv_code='MSV-F002', msv_context={'path': path_clean})
                return
            if not os.path.isfile(full_path):
                self.send_error(404, 'Not found', msv_code='MSV-F001', msv_context={'path': path_clean})
                return
        except Exception:
            self.send_error(404, 'Not found', msv_code='MSV-F001', msv_context={'path': path_clean})
            return
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            body = content.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/markdown; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Content-Length', len(body))
            self.end_headers()
            self.wfile.write(body)
        except FileNotFoundError:
            self.send_error(404, 'Not found', msv_code='MSV-F001', msv_context={'path': path_clean})
        except Exception as e:
            self.send_error(500, str(e), msv_code='MSV-F004', msv_context={'path': path_clean, 'reason': str(e)})

    def do_POST(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path.rstrip('/') or '/'
        if path == '/api/refresh':
            self.serve_api_refresh()
        elif path == '/api/file':
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                if content_length <= 0:
                    self.send_error(400, 'Missing body')
                    return
                body_bytes = self.rfile.read(content_length)
                data = json.loads(body_bytes.decode('utf-8'))
                raw = (data.get('path') or '').strip()
                if not raw:
                    self.send_error(400, 'Missing or empty path', msv_code='MSV-A001', msv_context={'path': raw or '(empty)'})
                    return
                self.serve_api_file_with_path(raw)
            except json.JSONDecodeError as e:
                self.send_error(400, 'Invalid JSON: ' + str(e))
            except Exception as e:
                self.send_error(500, str(e))
        else:
            self.send_error(404, 'Not found', msv_code='MSV-A003', msv_context={'path': path})

    def serve_index(self):
        """Serve viewer/index.html as SPA (from viewer/, not project root)"""
        index_path = os.path.join(VIEWER_DIR, 'index.html')
        try:
            with open(index_path, 'rb') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, 'index.html not found', msv_code='MSV-I001', msv_context={'path': index_path})

    def serve_api_files(self):
        """Serve live manifest. Chỉ quét .md trong CONTENT_FOLDERS (mặc định: MarkdownSV)."""
        try:
            manifest = get_manifest(PROJECT_ROOT, include_folders=CONTENT_FOLDERS)
            manifest['revision'] = manifest_revision
            body = json.dumps(manifest, ensure_ascii=False).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', len(body))
            self.end_headers()
            self.wfile.write(body)
        except Exception as e:
            self.send_error(500, str(e), msv_code='MSV-A002', msv_context={'reason': str(e)})

    def serve_api_revision(self):
        """Lightweight endpoint for client polling: khi revision đổi → client gọi loadManifest (sync)."""
        global manifest_revision
        body = json.dumps({'revision': manifest_revision}, ensure_ascii=False).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)

    def serve_api_file(self, query):
        """GET /api/file?path=... — path có thể là absolute hoặc relative to PROJECT_ROOT."""
        path_list = query.get('path')
        if not path_list or not path_list[0].strip():
            self.send_error(400, 'Missing or empty path', msv_code='MSV-A001', msv_context={'path': (path_list[0] if path_list else '') or '(empty)'})
            return
        raw = path_list[0].strip()
        try:
            raw_decoded = urllib.parse.unquote(raw)
        except Exception:
            raw_decoded = raw
        self.serve_api_file_with_path(raw_decoded)

    def serve_api_file_with_path(self, raw_decoded):
        """Trả về nội dung file. Dùng chung cho GET (query path) và POST (body path)."""
        base_real = os.path.realpath(PROJECT_ROOT)
        allowed_bases = [base_real] + [r for r in EXTRA_ALLOWED_ROOTS if os.path.isdir(r)]
        if os.path.isabs(raw_decoded):
            full_path = os.path.normpath(raw_decoded)
        else:
            full_path = os.path.normpath(os.path.join(PROJECT_ROOT, raw_decoded))
        try:
            full_path = os.path.abspath(full_path)
            real_full = os.path.realpath(full_path)
            allowed = (real_full == base_real or any(real_full.startswith(b + os.sep) for b in allowed_bases))
            if not allowed:
                self.send_error(403, 'Path outside project root', msv_code='MSV-F002', msv_context={'path': raw_decoded})
                return
            if not os.path.isfile(real_full):
                self.send_error(404, 'Not a file or not found', msv_code='MSV-F001', msv_context={'path': raw_decoded})
                return
            ext = os.path.splitext(real_full)[1].lower()
            basename = os.path.basename(real_full).lower()
            allowed_exts = ('.md', '.markdown', '.mdx', '.mkd', '.mdoc', '.rst', '.txt', '.resolved')
            if ext not in allowed_exts and not basename.endswith('.md.resolved'):
                self.send_error(400, 'Only .md / .txt and similar text files are allowed', msv_code='MSV-F003', msv_context={'path': raw_decoded, 'ext': ext or '(none)'})
                return
            with open(real_full, 'r', encoding='utf-8') as f:
                content = f.read()
            try:
                resolved_relative = os.path.relpath(real_full, base_real).replace(os.sep, '/')
            except ValueError:
                resolved_relative = os.path.basename(real_full)
            body = content.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/markdown; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('X-Resolved-Path', resolved_relative)
            self.send_header('Content-Length', len(body))
            self.end_headers()
            self.wfile.write(body)
        except FileNotFoundError:
            self.send_error(404, 'Not found', msv_code='MSV-F001', msv_context={'path': raw_decoded})
        except Exception as e:
            self.send_error(500, str(e), msv_code='MSV-F004', msv_context={'path': raw_decoded, 'reason': str(e)})

    def serve_api_refresh(self):
        """Webhook: tăng revision để client (poll /api/revision) biết cần sync — gọi khi MarkdownSV thay đổi."""
        global manifest_revision
        manifest_revision += 1
        body = json.dumps({'ok': True, 'revision': manifest_revision}, ensure_ascii=False).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)


def main():
    missing = [f for f in CONTENT_FOLDERS if not os.path.isdir(os.path.join(PROJECT_ROOT, f.strip()))]
    if missing:
        print(f"\n⚠️  Some content folders not found: {missing}")
        print("   Server will run with available folders.")
    with socketserver.TCPServer(("", PORT), MarkdownHandler) as httpd:
        print("\n🚀 Markdown Viewer is running!")
        print(f"📍 Open: http://localhost:{PORT}")
        print("   Trang lỗi 404/500: dùng giao diện tùy chỉnh (card, nút \"Về trang chủ\")")
        print("\n✨ Features:")
        print("   - SPA with folder view, search, theme")
        print("   - Live file list (GET /api/files) — no manifest/commit needed")
        print("   - Webhook: POST /api/refresh → clients sync; poll GET /api/revision")
        print(f"   - Content: {', '.join(CONTENT_FOLDERS)}")
        if EXTRA_ALLOWED_ROOTS:
            print("   - Paste and go extra roots: " + ", ".join(EXTRA_ALLOWED_ROOTS))
        print("\n⏹  Press Ctrl+C to stop\n")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped.")


if __name__ == "__main__":
    main()
