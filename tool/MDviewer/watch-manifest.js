#!/usr/bin/env node
/**
 * File watcher: auto-run generate-manifest.py when .md files change.
 * Run: npm run watch  (requires: npm install chokidar)
 */

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

let chokidar;
try {
  chokidar = require('chokidar');
} catch (e) {
  console.error('Install chokidar: npm install chokidar');
  process.exit(1);
}

const root = path.join(__dirname);
const watchPath = path.join(root, '..', 'MarkdownSV');
const manifestScript = path.join(root, 'generate-manifest.py');

function runManifest() {
  const env = { ...process.env, CONTENT_ROOT: path.resolve(root, '..', 'MarkdownSV') };
  const proc = spawn('python3', [manifestScript], { cwd: root, env, stdio: 'inherit' });
  proc.on('error', () => {
    console.error('Could not run generate-manifest.py');
  });
}

let debounce;
const watcher = chokidar.watch(watchPath, {
  ignored: /(^|[\/\\])(\.|node_modules)/,
  persistent: true
});

watcher.on('change', (p) => {
  if (!p.endsWith('.md')) return;
  clearTimeout(debounce);
  debounce = setTimeout(() => {
    console.log('\n📝 .md change detected → regenerating files.json');
    runManifest();
  }, 300);
});

watcher.on('add', (p) => {
  if (!p.endsWith('.md')) return;
  clearTimeout(debounce);
  debounce = setTimeout(() => {
    console.log('\n📝 New .md file → regenerating files.json');
    runManifest();
  }, 300);
});

watcher.on('unlink', (p) => {
  if (!p.endsWith('.md')) return;
  clearTimeout(debounce);
  debounce = setTimeout(() => {
    console.log('\n📝 .md removed → regenerating files.json');
    runManifest();
  }, 300);
});

watcher.on('addDir', () => {
  clearTimeout(debounce);
  debounce = setTimeout(() => {
    console.log('\n📁 New folder → regenerating files.json');
    runManifest();
  }, 300);
});

watcher.on('unlinkDir', () => {
  clearTimeout(debounce);
  debounce = setTimeout(() => {
    console.log('\n📁 Folder removed → regenerating files.json');
    runManifest();
  }, 300);
});

console.log('👀 Watching', watchPath, 'for .md and folder changes...');
console.log('   Add/edit/delete .md or new/removed folders → files.json auto-updates → refresh viewer');
console.log('   Press Ctrl+C to stop\n');
