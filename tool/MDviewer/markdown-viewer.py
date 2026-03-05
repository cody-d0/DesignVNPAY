#!/usr/bin/env python3
"""
Beautiful Markdown Viewer Server
Serves markdown files with beautiful styling
"""

import http.server
import socketserver
import os
import markdown
import urllib.parse
from pathlib import Path

PORT = 8080

CUSTOM_CSS = """
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
    line-height: 1.6;
    color: #333;
    background: #f5f5f5;
    padding: 0;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    background: white;
    min-height: 100vh;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
  }
  
  .header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-bottom: 4px solid #5568d3;
  }
  
  .header h1 {
    font-size: 2rem;
    margin-bottom: 0.5rem;
  }
  
  .header .breadcrumb {
    font-size: 0.9rem;
    opacity: 0.9;
  }
  
  .content {
    padding: 3rem;
  }
  
  .markdown-body h1 {
    color: #667eea;
    border-bottom: 3px solid #667eea;
    padding-bottom: 0.5rem;
    margin: 2rem 0 1rem 0;
    font-size: 2rem;
  }
  
  .markdown-body h2 {
    color: #764ba2;
    border-bottom: 2px solid #e0e0e0;
    padding-bottom: 0.4rem;
    margin: 1.5rem 0 1rem 0;
    font-size: 1.6rem;
  }
  
  .markdown-body h3 {
    color: #555;
    margin: 1.2rem 0 0.8rem 0;
    font-size: 1.3rem;
  }
  
  .markdown-body h4 {
    color: #666;
    margin: 1rem 0 0.6rem 0;
    font-size: 1.1rem;
  }
  
  .markdown-body p {
    margin: 0.8rem 0;
    line-height: 1.8;
  }
  
  .markdown-body ul, .markdown-body ol {
    margin: 1rem 0;
    padding-left: 2rem;
  }
  
  .markdown-body li {
    margin: 0.5rem 0;
  }
  
  .markdown-body table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  
  .markdown-body table thead {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
  }
  
  .markdown-body table th {
    padding: 1rem;
    text-align: left;
    font-weight: 600;
  }
  
  .markdown-body table td {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid #e0e0e0;
  }
  
  .markdown-body table tbody tr:hover {
    background: #f8f9ff;
  }
  
  .markdown-body code {
    background: #f4f4f4;
    padding: 0.2rem 0.4rem;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
    font-size: 0.9em;
    color: #e83e8c;
  }
  
  .markdown-body pre {
    background: #2d2d2d;
    color: #f8f8f2;
    padding: 1.5rem;
    border-radius: 8px;
    overflow-x: auto;
    margin: 1.5rem 0;
  }
  
  .markdown-body pre code {
    background: transparent;
    color: inherit;
    padding: 0;
  }
  
  .markdown-body blockquote {
    border-left: 4px solid #667eea;
    padding-left: 1rem;
    margin: 1rem 0;
    color: #666;
    font-style: italic;
    background: #f8f9ff;
    padding: 1rem 1rem 1rem 1.5rem;
    border-radius: 0 4px 4px 0;
  }
  
  .markdown-body a {
    color: #667eea;
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: border-color 0.3s;
  }
  
  .markdown-body a:hover {
    border-bottom-color: #667eea;
  }
  
  .markdown-body img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin: 1rem 0;
  }
  
  .markdown-body hr {
    border: none;
    border-top: 2px solid #e0e0e0;
    margin: 2rem 0;
  }
  
  .file-list {
    list-style: none;
    padding: 0;
  }
  
  .file-list li {
    margin: 0.5rem 0;
  }
  
  .file-list a {
    display: block;
    padding: 1rem;
    background: #f8f9ff;
    border-radius: 8px;
    color: #667eea;
    text-decoration: none;
    transition: all 0.3s;
    border-left: 4px solid #667eea;
  }
  
  .file-list a:hover {
    background: #667eea;
    color: white;
    transform: translateX(5px);
  }
  
  .back-button {
    display: inline-block;
    padding: 0.8rem 1.5rem;
    background: white;
    color: #667eea;
    text-decoration: none;
    border-radius: 6px;
    margin-bottom: 1rem;
    transition: all 0.3s;
    border: 2px solid white;
  }
  
  .back-button:hover {
    background: transparent;
    color: white;
    border-color: white;
  }
  
  .folder {
    color: #f39c12;
    font-weight: 600;
  }
  
  .file {
    color: #667eea;
  }
</style>
"""

class MarkdownHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        
        if parsed_path.path == '/':
            self.serve_file_list()
        elif parsed_path.path == '/view' and 'file' in query:
            file_path = query['file'][0]
            self.serve_markdown(file_path)
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
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Markdown Viewer</title>
          {CUSTOM_CSS}
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
        </html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))
    
    def serve_markdown(self, file_path):
        """Render markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Convert markdown to HTML with extensions
            html_content = markdown.markdown(
                content,
                extensions=['tables', 'fenced_code', 'codehilite', 'nl2br', 'toc']
            )
            
            filename = os.path.basename(file_path)
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <title>{filename}</title>
              {CUSTOM_CSS}
            </head>
            <body>
              <div class="container">
                <div class="header">
                  <a href="/" class="back-button">← Back to List</a>
                  <h1>📄 {filename}</h1>
                  <div class="breadcrumb">{file_path}</div>
                </div>
                <div class="content markdown-body">
                  {html_content}
                </div>
              </div>
            </body>
            </html>
            """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
            
        except FileNotFoundError:
            self.send_error(404, 'File not found')
        except Exception as e:
            self.send_error(500, f'Error: {str(e)}')

def main():
    with socketserver.TCPServer(("", PORT), MarkdownHandler) as httpd:
        print("\n🚀 Markdown Server is running!")
        print(f"📍 Open: http://localhost:{PORT}")
        print("\n✨ Features:")
        print("   - Beautiful markdown rendering")
        print("   - Auto-discover all .md files")
        print("   - Responsive design")
        print("   - Table support")
        print("   - Code highlighting")
        print("\n⏹  Press Ctrl+C to stop\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped.")

if __name__ == "__main__":
    main()
