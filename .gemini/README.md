# .gemini — Project brain

Folder **`.gemini`** is the project’s **brain**: persistent context and knowledge for AI (e.g. Gemini CLI, Cursor).

## Role

- **GEMINI.md** — Main context file. Loaded by [Gemini CLI](https://github.com/google-gemini/gemini-cli) from this folder (or project root). Contains project identity, DDL summary, UI/UX rules, and pointers to full docs.
- Any AI that reads this folder gets the same context without re-explaining the stack or UI/UX rules.

## Relation to other “brain” sources

| Source | Role |
|--------|------|
| **.gemini/** | AI-facing context (this folder). |
| **.cursor/docs/ddl/** | Design Data Layer spec (views, hierarchy, contract). |
| **.agents/skills/ui-ux-pro-max/data/** | Raw UX/UI data (CSV: guidelines, laws, colors, styles, icons). |
| **UI-UX-BRAIN-EXTRACT.md** | Human-readable extract of DDL + ui-ux-pro-max; referenced from GEMINI.md. |

## Usage (Gemini CLI)

- Context is loaded from `GEMINI.md` in this directory (and parent directories up to repo root).
- `/memory show` — see loaded context.
- `/memory refresh` — reload GEMINI.md files.
- You can split context with `@file.md` imports inside GEMINI.md if needed.

## Cursor

Cursor does not automatically load `.gemini`; you can @-mention `UI-UX-BRAIN-EXTRACT.md` or `.cursor/docs/ddl/` when you need DDL/UI context. This folder still gives a single place to maintain “brain” content and keep GEMINI.md in sync for Gemini CLI users.
