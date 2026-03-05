#!/usr/bin/env python3
"""
Simple Markdown Viewer - No external dependencies
Uses marked.js CDN for client-side rendering
"""

import http.server
import socketserver
import os
import json
import urllib.parse
from pathlib import Path

PORT = 9999

# Trang lỗi HTML (đồng bộ với viewer/serve-markdown.py — ui-ux-pro-max)
ERROR_PAGES = {
    400: ('Bad Request', 'Yêu cầu không hợp lệ. Kiểm tra lại đường dẫn hoặc tham số.'),
    403: ('Forbidden', 'Bạn không có quyền truy cập tài nguyên này.'),
    404: ('Not Found', 'Không tìm thấy trang hoặc tệp. Có thể đường dẫn sai hoặc tài nguyên đã bị xóa.'),
    405: ('Method Not Allowed', 'Phương thức yêu cầu không được phép cho đường dẫn này.'),
    500: ('Server Error', 'Lỗi máy chủ. Vui lòng thử lại sau.'),
    502: ('Bad Gateway', 'Lỗi kết nối upstream. Thử lại sau.'),
    503: ('Service Unavailable', 'Dịch vụ tạm thời không khả dụng. Thử lại sau.'),
}

def _html_escape(s):
    if s is None:
        return ''
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('"', '&quot;').replace("'", '&#39;'))

def _get_error_html(code, message=None):
    title, friendly = ERROR_PAGES.get(code, ('Error', 'Đã xảy ra lỗi. Vui lòng thử lại.'))
    detail = (message or '').strip()
    if detail and code >= 500:
        detail_block = '<p class="error-detail" role="status">Chi tiết: <code>' + _html_escape(detail) + '</code></p>'
    else:
        detail_block = ''
    return '''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>''' + _html_escape(str(code)) + ' ' + _html_escape(title) + '''</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root { --color-cta: #2563EB; --color-background: #F8FAFC; --color-text: #1E293B; --color-text-muted: #64748B;
      --color-surface: #FFFFFF; --color-border: #E2E8F0; --color-hover: #F1F5F9; --font: 'Inter', sans-serif;
      --space-md: 1rem; --space-lg: 1.5rem; --space-xl: 2rem; --space-2xl: 3rem; --text-base: 1rem; --text-lg: 1.125rem; --text-3xl: 1.875rem; --radius: 8px; --transition: 150ms ease; }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html { font-family: var(--font); font-size: 16px; line-height: 1.6; }
    body { min-height: 100vh; background: var(--color-background); color: var(--color-text); display: flex; align-items: center; justify-content: center; padding: var(--space-xl); }
    .error-card { max-width: 420px; width: 100%; background: var(--color-surface); border: 1px solid var(--color-border); border-radius: 12px; padding: var(--space-2xl); text-align: center; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
    .error-code { font-size: var(--text-3xl); font-weight: 700; color: var(--color-cta); margin-bottom: 0.25rem; }
    .error-title { font-size: var(--text-lg); font-weight: 600; color: var(--color-text); margin-bottom: var(--space-md); }
    .error-message { font-size: var(--text-base); color: var(--color-text-muted); line-height: 1.6; margin-bottom: var(--space-lg); }
    .error-detail { font-size: 0.875rem; color: var(--color-text-muted); text-align: left; background: var(--color-hover); border-radius: var(--radius); padding: var(--space-md); margin-bottom: var(--space-lg); word-break: break-word; }
    .error-detail code { font-family: ui-monospace, monospace; }
    .btn-primary { display: inline-block; padding: 0.625rem 1.25rem; font-size: var(--text-base); font-weight: 500; color: #fff; background: var(--color-cta); border: none; border-radius: var(--radius); cursor: pointer; text-decoration: none; transition: opacity var(--transition); }
    .btn-primary:hover { opacity: 0.95; }
    .btn-primary:focus { outline: 2px solid var(--color-cta); outline-offset: 2px; }
  </style>
</head>
<body>
  <main class="error-card" role="main" aria-labelledby="error-title">
    <p class="error-code" aria-hidden="true">''' + str(code) + '''</p>
    <h1 id="error-title" class="error-title">''' + _html_escape(title) + '''</h1>
    <p class="error-message">''' + _html_escape(friendly) + '''</p>
    ''' + detail_block + '''
    <div class="error-actions"><a href="/" class="btn-primary">Về trang chủ</a></div>
  </main>
</body>
</html>'''

class MarkdownHandler(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        """Trang lỗi HTML tùy chỉnh thay cho mặc định Python."""
        self.log_error(code, message or '')
        body = _get_error_html(code, message).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        if self.command != 'HEAD' and body:
            self.wfile.write(body)

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        
        if parsed_path.path == '/':
            self.serve_file_list()
        elif parsed_path.path == '/view' and 'file' in query:
            file_path = query['file'][0]
            self.serve_markdown_viewer(file_path)
        elif parsed_path.path == '/api/content' and 'file' in query:
            file_path = query['file'][0]
            self.serve_markdown_content(file_path)
        else:
            super().do_GET()
    
    def serve_file_list(self):
        """List all markdown files"""
        md_files = []
        base_path = Path('.')
        
        for md_file in base_path.rglob('*.md'):
            # Skip hidden directories and node_modules
            if any(part.startswith('.') for part in md_file.parts) or 'node_modules' in md_file.parts:
                continue
            md_files.append(str(md_file))
        
        md_files.sort()
        
        file_list_html = ''
        for file in md_files:
            encoded_file = urllib.parse.quote(file)
            file_list_html += f'<li><a href="/view?file={encoded_file}">📄 {file}</a></li>'
        
        html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Markdown Viewer</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
      background: #f5f5f5;
    }}
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      background: white;
      min-height: 100vh;
      box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }}
    .header {{
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 2rem;
    }}
    .header h1 {{ font-size: 2rem; margin-bottom: 0.5rem; }}
    .breadcrumb {{ font-size: 0.9rem; opacity: 0.9; }}
    .content {{ padding: 3rem; }}
    .file-list {{ list-style: none; padding: 0; }}
    .file-list li {{ margin: 0.5rem 0; }}
    .file-list a {{
      display: block;
      padding: 1rem;
      background: #f8f9ff;
      border-radius: 8px;
      color: #667eea;
      text-decoration: none;
      transition: all 0.3s;
      border-left: 4px solid #667eea;
    }}
    .file-list a:hover {{
      background: #667eea;
      color: white;
      transform: translateX(5px);
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>📄 Markdown Viewer</h1>
      <div class="breadcrumb">Select a file to view • Found {len(md_files)} files</div>
    </div>
    <div class="content">
      <ul class="file-list">
        {file_list_html}
      </ul>
    </div>
  </div>
</body>
</html>"""
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))
    
    def serve_markdown_viewer(self, file_path):
        """Serve HTML viewer that will load markdown via API"""
        filename = os.path.basename(file_path)
        encoded_file = urllib.parse.quote(file_path)
        
        html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{filename}</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
      line-height: 1.6;
      color: #333;
      background: #f5f5f5;
    }}
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      background: white;
      min-height: 100vh;
      box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }}
    .header {{
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 2rem;
      border-bottom: 4px solid #5568d3;
    }}
    .header h1 {{ font-size: 2rem; margin-bottom: 0.5rem; }}
    .breadcrumb {{ font-size: 0.9rem; opacity: 0.9; }}
    .back-button {{
      display: inline-block;
      padding: 0.8rem 1.5rem;
      background: white;
      color: #667eea;
      text-decoration: none;
      border-radius: 6px;
      margin-bottom: 1rem;
      transition: all 0.3s;
      border: 2px solid white;
    }}
    .back-button:hover {{
      background: transparent;
      color: white;
      border-color: white;
    }}
    .content {{ padding: 3rem; }}
    .markdown-body h1 {{
      color: #667eea;
      border-bottom: 3px solid #667eea;
      padding-bottom: 0.5rem;
      margin: 2rem 0 1rem 0;
      font-size: 2rem;
    }}
    .markdown-body h2 {{
      color: #764ba2;
      border-bottom: 2px solid #e0e0e0;
      padding-bottom: 0.4rem;
      margin: 1.5rem 0 1rem 0;
      font-size: 1.6rem;
    }}
    .markdown-body h3 {{
      color: #555;
      margin: 1.2rem 0 0.8rem 0;
      font-size: 1.3rem;
    }}
    .markdown-body h4 {{
      color: #666;
      margin: 1rem 0 0.6rem 0;
      font-size: 1.1rem;
    }}
    .markdown-body p {{ margin: 0.8rem 0; line-height: 1.8; }}
    .markdown-body ul, .markdown-body ol {{ margin: 1rem 0; padding-left: 2rem; }}
    .markdown-body li {{ margin: 0.5rem 0; }}
    .markdown-body table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}
    .markdown-body table thead {{
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
    }}
    .markdown-body table th {{
      padding: 1rem;
      text-align: left;
      font-weight: 600;
    }}
    .markdown-body table td {{
      padding: 0.8rem 1rem;
      border-bottom: 1px solid #e0e0e0;
    }}
    .markdown-body table tbody tr:hover {{ background: #f8f9ff; }}
    .markdown-body code {{
      background: #f4f4f4;
      padding: 0.2rem 0.4rem;
      border-radius: 3px;
      font-family: 'Courier New', monospace;
      font-size: 0.9em;
      color: #e83e8c;
    }}
    .markdown-body pre {{
      background: #2d2d2d;
      color: #f8f8f2;
      padding: 1.5rem;
      border-radius: 8px;
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .markdown-body pre code {{
      background: transparent;
      color: inherit;
      padding: 0;
    }}
    .markdown-body blockquote {{
      border-left: 4px solid #667eea;
      padding-left: 1rem;
      margin: 1rem 0;
      color: #666;
      font-style: italic;
      background: #f8f9ff;
      padding: 1rem 1rem 1rem 1.5rem;
      border-radius: 0 4px 4px 0;
    }}
    .markdown-body a {{
      color: #667eea;
      text-decoration: none;
      border-bottom: 1px solid transparent;
      transition: border-color 0.3s;
    }}
    .markdown-body a:hover {{ border-bottom-color: #667eea; }}
    .markdown-body img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      margin: 1rem 0;
    }}
    .markdown-body hr {{
      border: none;
      border-top: 2px solid #e0e0e0;
      margin: 2rem 0;
    }}
    .loading {{
      text-align: center;
      padding: 3rem;
      color: #667eea;
      font-size: 1.2rem;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <a href="/" class="back-button">← Back to List</a>
      <h1>📄 {filename}</h1>
      <div class="breadcrumb">{file_path}</div>
    </div>
    <div class="content">
      <div id="markdown-content" class="markdown-body">
        <div class="loading">Loading...</div>
      </div>
    </div>
  </div>
  <script>
    fetch('/api/content?file={encoded_file}')
      .then(response => response.text())
      .then(markdown => {{
        marked.setOptions({{
          breaks: true,
          gfm: true
        }});
        document.getElementById('markdown-content').innerHTML = marked.parse(markdown);
      }})
      .catch(error => {{
        document.getElementById('markdown-content').innerHTML = 
          '<p style="color: red;">Error loading markdown: ' + error + '</p>';
      }});
  </script>
</body>
</html>"""
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))
    
    def serve_markdown_content(self, file_path):
        """Serve raw markdown content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
            
        except FileNotFoundError:
            self.send_error(404, 'File not found')
        except Exception as e:
            self.send_error(500, str(e))

def main():
    with socketserver.TCPServer(("", PORT), MarkdownHandler) as httpd:
        print("\\n🚀 Markdown Server is running!")
        print(f"📍 Open: http://localhost:{{PORT}}")
        print("\\n✨ Features:")
        print("   - Beautiful markdown rendering")
        print("   - Auto-discover all .md files")
        print("   - Responsive design")
        print("   - Table support")
        print("   - No external dependencies")
        print("\\n⏹  Press Ctrl+C to stop\\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\\n\\n👋 Server stopped.")

if __name__ == "__main__":
    main()
