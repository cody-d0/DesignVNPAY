/**
 * MCP server: figma-save — save Figma section artboards as PNG (chỉ từng artboard, không ảnh toàn section).
 * Tool: figma_save_section_screenshots.
 * Token: FAT or FIGMA_ACCESS_TOKEN in environment.
 */
import https from 'node:https';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const API_TIMEOUT = 30_000;
const DOWNLOAD_TIMEOUT = 60_000;
const RETRY_DELAY = 2_000;
const CONCURRENCY_LIMIT = 5;

function getToken() {
  return process.env.FAT || process.env.FIGMA_ACCESS_TOKEN || null;
}

function slugify(name) {
  if (!name || typeof name !== 'string') return 'frame';
  const from = 'àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ';
  const to   = 'aaaaaaaaaaaaaaaaaeeeeeeeeeeeiiiiiooooooooooooooooouuuuuuuuuuuyyyyyydAAAAAAAAAAAAAAAAAEEEEEEEEEEEIIIIIOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYYD';
  let s = name.trim();
  for (let i = 0; i < from.length; i++) s = s.replace(new RegExp(from[i], 'g'), to[i]);
  s = s.replace(/[^a-zA-Z0-9\s-]/g, '').replace(/\s+/g, '-').replace(/-+/g, '-').toLowerCase();
  return s || 'frame';
}

/**
 * Return a unique slug so the same base name does not overwrite (e.g. artboards with identical layer names).
 */
function uniqueSlug(baseSlug, used) {
  let s = baseSlug;
  let n = 1;
  while (used.has(s)) {
    n += 1;
    s = `${baseSlug}-${n}`;
  }
  used.add(s);
  return s;
}

// ---------------------------------------------------------------------------
// Figma error parsing
// ---------------------------------------------------------------------------

function parseFigmaError(statusCode, body) {
  if (statusCode === 403) return 'Invalid or expired Figma token (403 Forbidden)';
  if (statusCode === 404) return 'File or node not found (404)';
  if (statusCode === 429) return 'Figma rate limited — retry later (429)';
  if (statusCode >= 500) return `Figma server error (${statusCode})`;
  try {
    const data = JSON.parse(body);
    if (data.err) return `Figma API error: ${data.err}`;
    if (data.message) return `Figma API: ${data.message}`;
  } catch (_) {}
  return `Figma API ${statusCode}: ${body.slice(0, 200)}`;
}

// ---------------------------------------------------------------------------
// HTTP helper with timeout + retry
// ---------------------------------------------------------------------------

function figmaApiGet(url, token, { timeout = API_TIMEOUT, retries = 1 } = {}) {
  const doRequest = () =>
    new Promise((resolve, reject) => {
      const req = https.request(
        url,
        { method: 'GET', headers: { 'X-Figma-Token': token } },
        (res) => {
          let body = '';
          res.on('data', (ch) => { body += ch; });
          res.on('end', () => {
            if (res.statusCode === 200) {
              try { resolve(JSON.parse(body)); }
              catch (e) { reject(new Error(`Failed to parse Figma response: ${e.message}`)); }
              return;
            }
            const err = new Error(parseFigmaError(res.statusCode, body));
            err.statusCode = res.statusCode;
            reject(err);
          });
        },
      );
      req.on('error', reject);
      req.setTimeout(timeout, () => {
        req.destroy();
        reject(new Error(`Figma API request timed out after ${timeout}ms`));
      });
      req.end();
    });

  return (async () => {
    let lastError;
    for (let attempt = 0; attempt <= retries; attempt++) {
      try {
        return await doRequest();
      } catch (err) {
        lastError = err;
        const isRetryable =
          (err.statusCode && (err.statusCode >= 500 || err.statusCode === 429)) ||
          ['ECONNRESET', 'ETIMEDOUT', 'ENOTFOUND'].includes(err.code) ||
          err.message.includes('timed out');
        if (!isRetryable || attempt === retries) throw err;
        await new Promise((r) => setTimeout(r, RETRY_DELAY));
      }
    }
    throw lastError;
  })();
}

// ---------------------------------------------------------------------------
// Core Figma functions (all use figmaApiGet)
// ---------------------------------------------------------------------------

async function getSectionWithChildren(fileKey, nodeId, token) {
  const nid = nodeId.replace(/-/g, ':');
  const data = await figmaApiGet(
    `https://api.figma.com/v1/files/${fileKey}/nodes?ids=${encodeURIComponent(nid)}&depth=2`,
    token,
  );
  const entry = data.nodes && data.nodes[nid];
  const doc = entry && entry.document;
  if (!doc) throw new Error('Node not found or no document');
  return {
    name: doc.name != null ? String(doc.name) : null,
    children: Array.isArray(doc.children)
      ? doc.children.map((c) => ({ id: c.id, name: c.name != null ? String(c.name) : 'frame' }))
      : [],
  };
}

async function getImageUrls(fileKey, nodeIds, token) {
  const normalized = nodeIds.map((id) => id.replace(/-/g, ':'));
  const data = await figmaApiGet(
    `https://api.figma.com/v1/images/${fileKey}?ids=${encodeURIComponent(normalized.join(','))}&format=png`,
    token,
  );
  if (data.err) throw new Error(`Figma images error: ${data.err}`);
  const map = new Map();
  const images = data.images || {};
  for (const id of normalized) {
    if (images[id]) map.set(id, images[id]);
  }
  return map;
}

/**
 * Walk the Figma file tree to resolve { fileName, pageName, sectionName, isPage } for a given node.
 * isPage=true when node_id points to a Figma page (direct child of document).
 * Uses GET /v1/files/:key?depth=3 to cover pages → sections → artboards.
 */
async function getNodePathInFile(fileKey, nodeId, token) {
  const nid = nodeId.replace(/-/g, ':');
  const data = await figmaApiGet(
    `https://api.figma.com/v1/files/${fileKey}?depth=3`,
    token,
  );
  const fileName = data.name || fileKey;
  const doc = data.document;
  if (!doc || !Array.isArray(doc.children)) {
    return { fileName, pageName: 'unknown', sectionName: nid, isPage: false };
  }

  for (const page of doc.children) {
    if (page.id === nid) {
      return { fileName, pageName: page.name || 'unknown', sectionName: page.name || nid, isPage: true };
    }
    if (!Array.isArray(page.children)) continue;
    for (const child of page.children) {
      if (child.id === nid) {
        return { fileName, pageName: page.name || 'unknown', sectionName: child.name || nid, isPage: false };
      }
      if (!Array.isArray(child.children)) continue;
      for (const grandchild of child.children) {
        if (grandchild.id === nid) {
          return { fileName, pageName: page.name || 'unknown', sectionName: grandchild.name || nid, isPage: false };
        }
      }
    }
  }

  return { fileName, pageName: 'unknown', sectionName: nid, isPage: false };
}

/**
 * Fetch sections (direct children) of a page with their artboards (depth=3).
 * Used when isPage=true to iterate over each section independently.
 */
async function getPageSections(fileKey, nodeId, token) {
  const nid = nodeId.replace(/-/g, ':');
  const data = await figmaApiGet(
    `https://api.figma.com/v1/files/${fileKey}/nodes?ids=${encodeURIComponent(nid)}&depth=3`,
    token,
  );
  const entry = data.nodes && data.nodes[nid];
  const doc = entry && entry.document;
  if (!doc) throw new Error('Node not found or no document');
  return (Array.isArray(doc.children) ? doc.children : []).map((section) => ({
    id: section.id,
    name: section.name != null ? String(section.name) : 'section',
    children: Array.isArray(section.children)
      ? section.children.map((c) => ({ id: c.id, name: c.name != null ? String(c.name) : 'frame' }))
      : [],
  }));
}

// ---------------------------------------------------------------------------
// Download with timeout
// ---------------------------------------------------------------------------

function downloadToFile(url, filePath, { timeout = DOWNLOAD_TIMEOUT } = {}) {
  return new Promise((resolve, reject) => {
    const protocol = url.startsWith('https') ? https : http;
    const dir = path.dirname(filePath);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

    const file = fs.createWriteStream(filePath);
    let settled = false;

    const finish = (err) => {
      if (settled) return;
      settled = true;
      clearTimeout(timer);
      file.close();
      if (err) {
        fs.unlink(filePath, () => {});
        reject(err);
      } else {
        resolve(filePath);
      }
    };

    const timer = setTimeout(() => {
      finish(new Error(`Download timed out after ${timeout}ms`));
    }, timeout);

    const req = protocol.get(url, (res) => {
      if (res.statusCode === 301 || res.statusCode === 302) {
        settled = true;
        clearTimeout(timer);
        file.close();
        try { fs.unlinkSync(filePath); } catch (_) {}
        res.resume();
        downloadToFile(res.headers.location, filePath, { timeout }).then(resolve).catch(reject);
        return;
      }
      res.pipe(file);
      file.on('finish', () => finish(null));
    });

    req.on('error', (err) => finish(err));
  });
}

// ---------------------------------------------------------------------------
// Concurrency-limited parallel execution
// ---------------------------------------------------------------------------

async function parallelLimit(tasks, limit) {
  const results = new Array(tasks.length);
  let index = 0;
  async function worker() {
    while (index < tasks.length) {
      const i = index++;
      results[i] = await tasks[i]();
    }
  }
  await Promise.all(
    Array.from({ length: Math.min(limit, tasks.length) }, () => worker()),
  );
  return results;
}

// ---------------------------------------------------------------------------
// Shared section save helper
// ---------------------------------------------------------------------------

async function saveSectionFiles(file_key, fileNameSlug, pageNameSlug, sectionId, sectionName, artboards, baseDir, token) {
  const sectionSlug = slugify(sectionName);
  const outDir = path.join(baseDir, fileNameSlug, pageNameSlug, sectionSlug);
  fs.mkdirSync(outDir, { recursive: true });

  // Chỉ export từng artboard (frame con). Không export ảnh toàn section. Nếu section không có con thì export chính node section.
  const idsToExport = artboards.length > 0 ? artboards.map((c) => c.id) : [sectionId];
  const urlMap = await getImageUrls(file_key, idsToExport, token);

  const saved = [];

  if (artboards.length > 0) {
    const usedSlugs = new Set();
    const tasks = artboards.map((child) => () => {
      const cid = child.id.replace(/-/g, ':');
      const url = urlMap.get(cid);
      if (!url) return Promise.resolve(null);
      const baseSlug = slugify(child.name);
      const childSlug = uniqueSlug(baseSlug, usedSlugs);
      const filePath = path.join(outDir, `${childSlug}.png`);
      return downloadToFile(url, filePath).then(() => ({ name: child.name, path: filePath }));
    });
    const results = await parallelLimit(tasks, CONCURRENCY_LIMIT);
    for (const r of results) { if (r) saved.push(r); }
  } else {
    const sNid = sectionId.replace(/-/g, ':');
    const sectionUrl = urlMap.get(sNid);
    if (sectionUrl) {
      const sectionPath = path.join(outDir, `${sectionSlug}.png`);
      await downloadToFile(sectionUrl, sectionPath);
      saved.push({ name: sectionName || sectionId, path: sectionPath });
    }
  }
  return { outDir, saved, sectionName };
}

// ---------------------------------------------------------------------------
// MCP Server + Tools
// ---------------------------------------------------------------------------

const mcpServer = new McpServer({
  name: 'figma-save',
  version: '2.2.0',
});

mcpServer.registerTool('figma_save_section_screenshots', {
  description:
    'Save section artboards as PNG with auto folder structure: {file_name}/{page}/{section}/*.png. Chỉ lưu từng artboard (frame con), không chụp ảnh toàn section. Accepts section node ID OR page node ID (saves all sections in the page).',
  inputSchema: {
    file_key: z.string().describe('Figma file key from URL'),
    node_id: z
      .string()
      .describe('Section/frame node ID (e.g. 5197:5929) or page node ID. When a page is given, all sections in the page are saved.'),
    output_base_dir: z
      .string()
      .optional()
      .describe('Base directory for output (default: current working directory)'),
  },
}, async ({ file_key, node_id, output_base_dir }) => {
  const token = getToken();
  if (!token) {
    return {
      content: [{ type: 'text', text: 'Error: FAT or FIGMA_ACCESS_TOKEN is required.' }],
      isError: true,
    };
  }
  try {
    const pathInfo = await getNodePathInFile(file_key, node_id, token);
    const { fileName, pageName, sectionName, isPage } = pathInfo;
    const baseDir = output_base_dir
      ? path.isAbsolute(output_base_dir)
        ? output_base_dir
        : path.resolve(process.cwd(), output_base_dir)
      : process.cwd();
    const fileNameSlug = slugify(fileName);
    const pageNameSlug = slugify(pageName);

    if (isPage) {
      const sections = await getPageSections(file_key, node_id, token);
      const allSaved = [];
      for (const section of sections) {
        const { outDir, saved } = await saveSectionFiles(
          file_key, fileNameSlug, pageNameSlug,
          section.id, section.name, section.children,
          baseDir, token,
        );
        for (const s of saved) allSaved.push(s);
      }
      const lines = allSaved.map((s) => `- ${s.name} → ${s.path}`);
      return {
        content: [{
          type: 'text',
          text: `[PAGE MODE] File: ${fileName} | Page: ${pageName} | ${sections.length} section(s)\n${allSaved.length} file(s) saved:\n${lines.join('\n')}`,
        }],
      };
    }

    const sectionInfo = await getSectionWithChildren(file_key, node_id, token);
    const { outDir, saved } = await saveSectionFiles(
      file_key, fileNameSlug, pageNameSlug,
      node_id, sectionName, sectionInfo.children,
      baseDir, token,
    );
    const lines = saved.map((s) => `- ${s.name} → ${s.path}`);
    return {
      content: [{
        type: 'text',
        text: `Folder: ${outDir}\nFile: ${fileName} | Page: ${pageName} | Section: ${sectionName}\n${saved.length} file(s) saved:\n${lines.join('\n')}`,
      }],
    };
  } catch (err) {
    return {
      content: [{ type: 'text', text: err instanceof Error ? err.message : String(err) }],
      isError: true,
    };
  }
});

// ---------------------------------------------------------------------------
// Start
// ---------------------------------------------------------------------------

async function main() {
  const transport = new StdioServerTransport();
  await mcpServer.connect(transport);
}

main().catch((error) => {
  console.error('Server error:', error);
  process.exit(1);
});
