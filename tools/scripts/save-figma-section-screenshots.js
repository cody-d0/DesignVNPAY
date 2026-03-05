/**
 * Save section screenshots with auto folder structure from Figma metadata.
 * Folder: {file_name}/{page}/{section}/*.png — chỉ từng artboard (frame con), không chụp ảnh toàn section.
 *
 * Usage:
 *   node scripts/save-figma-section-screenshots.js <file_key> <node_id> [output_base_dir]
 *
 * Env: FAT or FIGMA_ACCESS_TOKEN (required)
 */

const https = require('https');
const http = require('http');
const fs = require('fs');
const path = require('path');

const token = process.env.FAT || process.env.FIGMA_ACCESS_TOKEN;
const [,, fileKey, nodeId, outputBaseDir] = process.argv;

const API_TIMEOUT = 30_000;
const DOWNLOAD_TIMEOUT = 60_000;
const CONCURRENCY_LIMIT = 5;

function usage() {
  console.error('Usage: FAT=<token> node scripts/save-figma-section-screenshots.js <file_key> <node_id> [output_base_dir]');
  console.error('Example: FAT=xxx node scripts/save-figma-section-screenshots.js kPft93N2A3gYOC3YwuXpQR 5197:5929');
  console.error('Output: {file_name}/{page}/{section}/*.png (auto from Figma)');
  process.exit(1);
}

if (!fileKey || !nodeId) usage();
if (!token) {
  console.error('Error: FAT or FIGMA_ACCESS_TOKEN is required.');
  usage();
}

const normalizedNodeId = nodeId.replace(/-/g, ':');

function slugify(name) {
  if (!name || typeof name !== 'string') return 'frame';
  const from = 'àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ';
  const to   = 'aaaaaaaaaaaaaaaaaeeeeeeeeeeeiiiiiooooooooooooooooouuuuuuuuuuuyyyyyydAAAAAAAAAAAAAAAAAEEEEEEEEEEEIIIIIOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYYD';
  let s = name.trim();
  for (let i = 0; i < from.length; i++) s = s.replace(new RegExp(from[i], 'g'), to[i]);
  s = s.replace(/[^a-zA-Z0-9\s-]/g, '').replace(/\s+/g, '-').replace(/-+/g, '-').toLowerCase();
  return s || 'frame';
}

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

function figmaGet(url) {
  return new Promise((resolve, reject) => {
    const req = https.request(url, { method: 'GET', headers: { 'X-Figma-Token': token } }, (res) => {
      let body = '';
      res.on('data', (ch) => { body += ch; });
      res.on('end', () => {
        if (res.statusCode !== 200) {
          reject(new Error(`Figma API ${res.statusCode}: ${body.slice(0, 200)}`));
          return;
        }
        try { resolve(JSON.parse(body)); }
        catch (e) { reject(e); }
      });
    });
    req.on('error', reject);
    req.setTimeout(API_TIMEOUT, () => { req.destroy(); reject(new Error('Figma API timeout')); });
    req.end();
  });
}

function getNodePathInFile() {
  return figmaGet(`https://api.figma.com/v1/files/${fileKey}?depth=3`).then((data) => {
    const fileName = data.name || fileKey;
    const doc = data.document;
    if (!doc || !Array.isArray(doc.children)) {
      return { fileName, pageName: 'unknown', sectionName: normalizedNodeId, isPage: false };
    }
    for (const page of doc.children) {
      if (page.id === normalizedNodeId) {
        return { fileName, pageName: page.name || 'unknown', sectionName: page.name || normalizedNodeId, isPage: true };
      }
      if (!Array.isArray(page.children)) continue;
      for (const child of page.children) {
        if (child.id === normalizedNodeId) {
          return { fileName, pageName: page.name || 'unknown', sectionName: child.name || normalizedNodeId, isPage: false };
        }
        if (!Array.isArray(child.children)) continue;
        for (const gc of child.children) {
          if (gc.id === normalizedNodeId) {
            return { fileName, pageName: page.name || 'unknown', sectionName: gc.name || normalizedNodeId, isPage: false };
          }
        }
      }
    }
    return { fileName, pageName: 'unknown', sectionName: normalizedNodeId, isPage: false };
  });
}

function getPageSections() {
  return figmaGet(`https://api.figma.com/v1/files/${fileKey}/nodes?ids=${encodeURIComponent(normalizedNodeId)}&depth=3`)
    .then((data) => {
      const entry = data.nodes && data.nodes[normalizedNodeId];
      const doc = entry && entry.document;
      if (!doc) throw new Error('Node not found');
      return (Array.isArray(doc.children) ? doc.children : []).map((section) => ({
        id: section.id,
        name: section.name != null ? String(section.name) : 'section',
        children: Array.isArray(section.children)
          ? section.children.map((c) => ({ id: c.id, name: c.name != null ? String(c.name) : 'frame' }))
          : [],
      }));
    });
}

function getSectionWithChildren() {
  return figmaGet(`https://api.figma.com/v1/files/${fileKey}/nodes?ids=${encodeURIComponent(normalizedNodeId)}&depth=2`)
    .then((data) => {
      const entry = data.nodes && data.nodes[normalizedNodeId];
      const doc = entry && entry.document;
      if (!doc) throw new Error('Node not found');
      return {
        name: doc.name != null ? String(doc.name) : null,
        children: Array.isArray(doc.children)
          ? doc.children.map((c) => ({ id: c.id, name: c.name != null ? String(c.name) : 'frame' }))
          : [],
      };
    });
}

function getImageUrls(ids) {
  const normalized = ids.map((id) => id.replace(/-/g, ':'));
  return figmaGet(`https://api.figma.com/v1/images/${fileKey}?ids=${encodeURIComponent(normalized.join(','))}&format=png`)
    .then((data) => {
      if (data.err) throw new Error(data.err);
      const map = new Map();
      const images = data.images || {};
      for (const id of normalized) { if (images[id]) map.set(id, images[id]); }
      return map;
    });
}

function downloadToFile(url, filePath) {
  return new Promise((resolve, reject) => {
    const protocol = url.startsWith('https') ? https : http;
    const dir = path.dirname(filePath);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    const file = fs.createWriteStream(filePath);
    let settled = false;
    const finish = (err) => {
      if (settled) return;
      settled = true; clearTimeout(timer); file.close();
      if (err) { fs.unlink(filePath, () => {}); reject(err); }
      else resolve(filePath);
    };
    const timer = setTimeout(() => finish(new Error('Download timeout')), DOWNLOAD_TIMEOUT);
    const req = protocol.get(url, (res) => {
      if (res.statusCode === 301 || res.statusCode === 302) {
        settled = true; clearTimeout(timer); file.close();
        try { fs.unlinkSync(filePath); } catch (_) {}
        res.resume();
        downloadToFile(res.headers.location, filePath).then(resolve).catch(reject);
        return;
      }
      res.pipe(file);
      file.on('finish', () => finish(null));
    });
    req.on('error', (err) => finish(err));
  });
}

async function parallelLimit(tasks, limit) {
  const results = new Array(tasks.length);
  let index = 0;
  async function worker() {
    while (index < tasks.length) { const i = index++; results[i] = await tasks[i](); }
  }
  await Promise.all(Array.from({ length: Math.min(limit, tasks.length) }, () => worker()));
  return results;
}

async function saveSectionFiles(fileNameSlug, pageNameSlug, sectionId, sectionName, artboards, baseDir) {
  const sectionSlug = slugify(sectionName);
  const outDir = path.join(baseDir, fileNameSlug, pageNameSlug, sectionSlug);
  fs.mkdirSync(outDir, { recursive: true });

  // Chỉ export từng artboard (frame con). Không export ảnh toàn section. Nếu section không có con thì export chính node section.
  const idsToExport = artboards.length > 0 ? artboards.map((c) => c.id) : [sectionId];
  const urlMap = await getImageUrls(idsToExport);

  if (artboards.length > 0) {
    const usedSlugs = new Set();
    const tasks = artboards.map((child) => () => {
      const cid = child.id.replace(/-/g, ':');
      const url = urlMap.get(cid);
      if (!url) return Promise.resolve(null);
      const baseSlug = slugify(child.name);
      const slug = uniqueSlug(baseSlug, usedSlugs);
      const filePath = path.join(outDir, `${slug}.png`);
      return downloadToFile(url, filePath).then(() => { console.log(filePath); return filePath; });
    });
    await parallelLimit(tasks, CONCURRENCY_LIMIT);
  } else {
    const sNid = sectionId.replace(/-/g, ':');
    const sectionUrl = urlMap.get(sNid);
    if (sectionUrl) {
      const sectionPath = path.join(outDir, `${sectionSlug}.png`);
      await downloadToFile(sectionUrl, sectionPath);
      console.log(sectionPath);
    }
  }
  return artboards.length;
}

(async () => {
  try {
    const pathInfo = await getNodePathInFile();
    const { fileName, pageName, isPage } = pathInfo;
    const baseDir = outputBaseDir
      ? (path.isAbsolute(outputBaseDir) ? outputBaseDir : path.resolve(process.cwd(), outputBaseDir))
      : process.cwd();
    const fileNameSlug = slugify(fileName);
    const pageNameSlug = slugify(pageName);

    if (isPage) {
      const sections = await getPageSections();
      let totalArtboards = 0;
      for (const section of sections) {
        const count = await saveSectionFiles(fileNameSlug, pageNameSlug, section.id, section.name, section.children, baseDir);
        totalArtboards += count;
        console.error(`  Section: ${section.name} (${count} artboards)`);
      }
      console.error(`Done: ${fileName} > ${pageName} [PAGE] (${sections.length} sections, ${totalArtboards} artboards)`);
    } else {
      const sectionInfo = await getSectionWithChildren();
      const { sectionName } = pathInfo;
      const count = await saveSectionFiles(fileNameSlug, pageNameSlug, normalizedNodeId, sectionName, sectionInfo.children, baseDir);
      console.error(`Done: ${fileName} > ${pageName} > ${sectionName} (${count} artboards)`);
    }
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
})();
