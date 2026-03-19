# Template: CLI Tool

Full-featured CLI tool với subcommands, config file, và interactive prompts.

## Khi nào dùng

- Developer tools phục vụ team
- Internal utilities
- Project scaffolding tools
- Data query/inspection tools

## Node.js Skeleton — Subcommand-Based

```javascript
#!/usr/bin/env node
// @ts-check
'use strict';

/**
 * <name> — <description>
 *
 * Usage: <name> <command> [options]
 *
 * Commands:
 *   init     Initialize project
 *   run      Execute operation
 *   status   Show current state
 *   config   Manage configuration
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const NAME = '<name>';
const VERSION = '1.0.0';
const CONFIG_FILE = `.${NAME}rc.json`;

// ─── Colors ─────────────────────────────────────────────────
const isTTY = process.stderr.isTTY;
const c = {
  b: isTTY ? '\x1b[1m' : '',      // bold
  d: isTTY ? '\x1b[2m' : '',      // dim
  r: isTTY ? '\x1b[31m' : '',     // red
  g: isTTY ? '\x1b[32m' : '',     // green
  y: isTTY ? '\x1b[33m' : '',     // yellow
  c: isTTY ? '\x1b[36m' : '',     // cyan
  _: isTTY ? '\x1b[0m' : '',      // reset
};

// ─── Logging ────────────────────────────────────────────────
const log = (...a) => console.error(`${c.d}${new Date().toISOString().slice(11,19)}${c._}`, ...a);
const info = (...a) => log(`${c.g}ℹ${c._}`, ...a);
const warn = (...a) => log(`${c.y}⚠${c._}`, ...a);
const error = (...a) => log(`${c.r}✖${c._}`, ...a);

// ─── Config ─────────────────────────────────────────────────
function loadConfig() {
  const configPath = findUp(CONFIG_FILE);
  if (!configPath) return {};
  try {
    return JSON.parse(fs.readFileSync(configPath, 'utf-8'));
  } catch (err) {
    warn(`Invalid config: ${configPath}`);
    return {};
  }
}

function saveConfig(config) {
  fs.writeFileSync(CONFIG_FILE, JSON.stringify(config, null, 2) + '\n');
  info(`Config saved: ${CONFIG_FILE}`);
}

function findUp(filename, dir = process.cwd()) {
  const file = path.join(dir, filename);
  if (fs.existsSync(file)) return file;
  const parent = path.dirname(dir);
  if (parent === dir) return null;
  return findUp(filename, parent);
}

// ─── Interactive Prompt ─────────────────────────────────────
async function prompt(question, { defaultValue, validate } = {}) {
  const rl = readline.createInterface({ input: process.stdin, output: process.stderr });
  const suffix = defaultValue ? ` ${c.d}(${defaultValue})${c._}` : '';

  return new Promise((resolve) => {
    rl.question(`${c.c}?${c._} ${question}${suffix}: `, (answer) => {
      rl.close();
      const value = answer.trim() || defaultValue || '';
      if (validate && !validate(value)) {
        error('Invalid input');
        process.exit(2);
      }
      resolve(value);
    });
  });
}

async function confirm(question) {
  const answer = await prompt(`${question} (y/N)`, { defaultValue: 'n' });
  return answer.toLowerCase() === 'y';
}

// ─── Commands ───────────────────────────────────────────────
const commands = {
  async init(args) {
    if (fs.existsSync(CONFIG_FILE)) {
      if (!await confirm('Config already exists. Overwrite?')) {
        info('Aborted');
        return;
      }
    }

    const config = {
      name: await prompt('Project name', { defaultValue: path.basename(process.cwd()) }),
      version: '1.0.0',
      created: new Date().toISOString(),
    };

    saveConfig(config);
    info('✅ Initialized');
  },

  async run(args) {
    const config = loadConfig();
    if (!config.name) {
      error(`Not initialized. Run: ${NAME} init`);
      process.exit(1);
    }

    info(`Running for: ${config.name}`);

    // ... main logic ...

    info('✅ Done');
  },

  async status(args) {
    const config = loadConfig();
    console.log(`${c.b}${NAME}${c._} v${VERSION}`);
    console.log(`${c.d}Config:${c._} ${config.name || '(not initialized)'}`);
    console.log(`${c.d}CWD:${c._}    ${process.cwd()}`);
  },

  async config(args) {
    const subCmd = args[0];
    const config = loadConfig();

    switch (subCmd) {
      case 'get': {
        const key = args[1];
        console.log(key ? config[key] : JSON.stringify(config, null, 2));
        break;
      }
      case 'set': {
        const [key, ...rest] = args.slice(1);
        config[key] = rest.join(' ');
        saveConfig(config);
        break;
      }
      default:
        console.log(JSON.stringify(config, null, 2));
    }
  },
};

// ─── Help ───────────────────────────────────────────────────
function showHelp() {
  console.log(`
${c.b}${NAME}${c._} v${VERSION}

${c.y}USAGE${c._}
  ${NAME} <command> [options]

${c.y}COMMANDS${c._}
  init       Initialize a new project
  run        Execute the main operation
  status     Show current state
  config     Manage configuration
    get [key]     Show config (or specific key)
    set <key> <value>  Set config value

${c.y}OPTIONS${c._}
  -h, --help      Show this help
  -v, --version   Show version
  --verbose        Enable debug output

${c.y}EXAMPLES${c._}
  ${NAME} init
  ${NAME} run --verbose
  ${NAME} config set name "my-project"
`);
}

// ─── Main ───────────────────────────────────────────────────
async function main() {
  const args = process.argv.slice(2);

  if (args.includes('-h') || args.includes('--help') || args.length === 0) {
    showHelp();
    process.exit(0);
  }

  if (args.includes('-v') || args.includes('--version')) {
    console.log(VERSION);
    process.exit(0);
  }

  const [command, ...rest] = args.filter(a => !a.startsWith('-'));
  const flags = new Set(args.filter(a => a.startsWith('-')));

  if (flags.has('--verbose')) {
    process.env.DEBUG = '1';
  }

  if (!commands[command]) {
    error(`Unknown command: ${command}`);
    showHelp();
    process.exit(2);
  }

  await commands[command](rest);
}

main().catch(err => {
  error(err.message);
  process.exit(1);
});
```

## Key Patterns

### 1. Self-Updating Help
```javascript
// Generate help from command functions' JSDoc
function generateHelp() {
  const maxLen = Math.max(...Object.keys(commands).map(k => k.length));
  return Object.entries(commands)
    .map(([name, fn]) => {
      const desc = fn.description || 'No description';
      return `  ${name.padEnd(maxLen + 2)} ${desc}`;
    })
    .join('\n');
}
```

### 2. Shell Completion Script
```bash
# Generate completion for bash/zsh
_complete() {
  local cur="${COMP_WORDS[COMP_CWORD]}"
  COMPREPLY=($(compgen -W "init run status config help" -- "$cur"))
}
complete -F _complete <name>
```

### 3. Plugin Architecture
```javascript
function loadPlugins(pluginDir) {
  if (!fs.existsSync(pluginDir)) return;
  for (const file of fs.readdirSync(pluginDir).filter(f => f.endsWith('.js'))) {
    const plugin = require(path.join(pluginDir, file));
    if (plugin.command && plugin.handler) {
      commands[plugin.command] = plugin.handler;
      info(`Loaded plugin: ${plugin.command}`);
    }
  }
}
```
