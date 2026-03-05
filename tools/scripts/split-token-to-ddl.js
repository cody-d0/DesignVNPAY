#!/usr/bin/env node

/**
 * Split a Figma-exported token.json (array of 4 collections with nested modes)
 * into flat per-collection-per-mode DDL files under design-data-layer/global/.
 *
 * Usage:
 *   node scripts/split-token-to-ddl.js [path/to/token.json] [--dry-run]
 *
 * Defaults:
 *   input  = first argument or ~/Downloads/token.json
 *   output = <repo>/design-data-layer/global/
 */

const fs = require('fs');
const path = require('path');

const GLOBAL_DIR = path.resolve(__dirname, '..', 'design-data-layer', 'global');

const FILE_MAP = {
  '1. TailwindCSS': {
    Default: { file: 'tailwind.json', collection: 'TailwindCSS' },
  },
  '2. Theme': {
    Default: { file: 'theme-default.json', collection: 'Theme' },
  },
  '3. Mode': {
    Light: { file: 'mode-light.json', collection: 'Mode' },
    Dark: { file: 'mode-dark.json', collection: 'Mode' },
  },
  '4. Custom': {
    Desktop: { file: 'custom-desktop.json', collection: 'Custom' },
    Mobile: { file: 'custom-mobile.json', collection: 'Custom' },
  },
};

function countTokens(obj) {
  let count = 0;
  for (const val of Object.values(obj)) {
    if (val && typeof val === 'object' && '$type' in val) {
      count++;
    } else if (val && typeof val === 'object') {
      count += countTokens(val);
    }
  }
  return count;
}

function main() {
  const args = process.argv.slice(2).filter((a) => !a.startsWith('--'));
  const dryRun = process.argv.includes('--dry-run');

  const inputPath =
    args[0] || path.join(require('os').homedir(), 'Downloads', 'token.json');

  if (!fs.existsSync(inputPath)) {
    console.error(`token.json not found at ${inputPath}`);
    process.exit(1);
  }

  console.log(`Reading ${inputPath}`);
  const raw = JSON.parse(fs.readFileSync(inputPath, 'utf-8'));

  if (!Array.isArray(raw)) {
    console.error('Expected top-level JSON array');
    process.exit(1);
  }

  if (!fs.existsSync(GLOBAL_DIR)) {
    fs.mkdirSync(GLOBAL_DIR, { recursive: true });
  }

  const summary = [];

  for (const entry of raw) {
    const collectionKey = Object.keys(entry)[0];
    const collectionData = entry[collectionKey];
    const modes = collectionData.modes;

    if (!modes) {
      console.warn(`No "modes" key in collection "${collectionKey}", skipping`);
      continue;
    }

    const mapping = FILE_MAP[collectionKey];
    if (!mapping) {
      console.warn(
        `No FILE_MAP entry for "${collectionKey}", skipping all its modes`
      );
      continue;
    }

    for (const [modeName, modeTokens] of Object.entries(modes)) {
      const target = mapping[modeName];
      if (!target) {
        console.warn(
          `Skipping "${collectionKey}" mode "${modeName}" (no mapping — likely PRODUCT override)`
        );
        continue;
      }

      const ddl = {
        meta: {
          collection: target.collection,
          mode: modeName,
          ddl_scope: 'GLOBAL',
          source_file: 'token.json',
        },
        ...modeTokens,
      };

      const outPath = path.join(GLOBAL_DIR, target.file);
      const groups = Object.keys(modeTokens);
      const tokens = countTokens(modeTokens);

      summary.push({
        file: target.file,
        collection: target.collection,
        mode: modeName,
        groups: groups.length,
        tokens,
      });

      if (dryRun) {
        console.log(
          `  [dry-run] ${target.file}  (${groups.length} groups, ${tokens} tokens)`
        );
      } else {
        fs.writeFileSync(outPath, JSON.stringify(ddl, null, 2) + '\n', 'utf-8');
        console.log(
          `  wrote ${target.file}  (${groups.length} groups, ${tokens} tokens)`
        );
      }
    }
  }

  console.log('\n--- Summary ---');
  console.table(summary);
  console.log(
    dryRun ? '\nDry run — no files written.' : '\nDone. Files written to ' + GLOBAL_DIR
  );
}

main();
