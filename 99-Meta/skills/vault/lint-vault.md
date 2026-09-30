---
name: lint-vault
version: 1.0.0
trigger: weekly sweep, /janitor, or on request
inputs: all notes outside hidden folders and 04-Archives
outputs: issue report (no fixes without approval)
depends_on: 99-Meta/BOUNDARIES.md
---

# Lint Vault

## Purpose

Finds structural rot: broken wikilinks, orphan notes, missing frontmatter, malformed dates, stray files at vault root (absorbed vault-root-hygiene, 2026-09-20). Report-only; fixing is a separate approved step.

## Checks

1. **Broken links**: every `[[wikilink]]` resolves to a note.
2. **Orphans**: notes in Areas/Resources with zero inbound links (candidates for `connect`).
3. **Frontmatter**: every note outside Inbox has `type:` and a valid date field.
4. **Dates**: ISO format everywhere. `05-Journal/` filenames match `YYYY-MM-DD` or `YYYY-Www-review`.
5. **Inbox age**: items older than 7 days.
6. **Map drift**: folders or skills that exist on disk but not in VAULT_MAP/SKILL_MAP, and vice versa.
7. **Root hygiene**: files at vault root that do not belong. Root holds `README.md`, `CLAUDE.md`, the numbered folders, `99-Meta/`, `code/`, `skills/`, `_local-only/` and dotfiles. Classify anything else: 0-byte or template-only daily stubs (propose a move to `05-Journal/`, or `04-Archives/` when a real entry exists for that date); scratch files such as `*.tmp`, `testfile`, `Untitled*.base`, `Untitled*.canvas`, `.~lock.*` (propose a `.gitignore` line, deletion only through the owner or [[reaper]]); scratch scripts left by earlier runs; unlisted top-level folders and project files sitting at root (report only, agents do not create or delete top-level folders). If daily stubs keep reappearing after cleanup, the cause is the Obsidian daily-notes folder setting, which is the owner's to change: say so once and point at [[punch-list]] instead of relisting the files.

## Procedure

1. Run all checks. Collect issues as `file -> issue -> proposed fix`.
2. More than 20 issues: report and stop (BOUNDARIES.md). Otherwise present the list for approval.
3. Apply only approved fixes. Never touch Archives or hidden folders.

## When NOT to use

- As an excuse to mass-edit or reformat notes.

## Style rules

- Flat list output. Counts at the top: `<n> issues: <b> broken links, <o> orphans, ...`.

## Links

- [[SKILL_MAP]]
- [[BOUNDARIES]]
- [[VAULT_MAP]]
- [[janitor]]
- [[punch-list]]
- [[reaper]]
