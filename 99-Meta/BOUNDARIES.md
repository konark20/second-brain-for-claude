---
type: meta
status: active
owner: "{{OWNER_NAME}}"
---

# Boundaries

> Hard rules. Every agent reads this file. If a request would cross a boundary, refuse and cite this file. Owner-edited only: no agent modifies this file on its own. The universal rules ship with every copy and should not be removed. The owner-specific section is filled during onboarding.

## Universal rules

### The vault

- Never delete a note from an active folder. Move it to `04-Archives/`. The one exception: [[reaper]] may hard-delete a note that has sat in `04-Archives/` for 30+ days, and only from a manifest the owner had a chance to veto.
- Never mass-rewrite existing notes without a diff review.
- Never modify files in `04-Archives/` unless the owner reopens them.
- Never touch hidden app folders (`.obsidian/`, `.smart-env/`, and similar). Exception: `.claude/` (commands, settings) and `.mcp.json` may be edited to wire the vault to Claude Code, with the change logged in the day's journal.
- Never modify `FOUNDATION.md` or `BOUNDARIES.md` on your own.

### Data and secrets

- Never write credentials, API keys, tokens or passwords to any note.
- Never store government ID numbers (passport, national ID, Aadhaar, PAN, SSN, driver's licence, visa or immigration documents) or bank, card or account numbers. Referring to a document's existence and location is fine ("passport scan is in the physical folder"). Recording its number is not. Sentinel quarantines violations.
- If a note contains a secret by mistake, flag it and stop. Do not commit, do not sync.
- Never run code against real credentials or data the owner has marked sensitive. Trace the logic by reading instead.
- Diff-only for code changes. No full-file rewrites unless asked.

### Things only the owner does

- Send, submit, apply, sign, post, or click any final action. The brain drafts; the owner sends.
- Spend money, enable a paid tier, or call a billed API. Confirm that specific action every time.
- Delete a repository or rewrite git history.

### Leaving the machine

- Sentinel runs before every commit, push, upload or share. Silent when clean, blocks on a hit.
- Never send vault content to any external service the owner has not approved.
- Web search is allowed for research skills. Elsewhere, ask first.

### Tone

- No fabrication. If uncertain, say so.
- No unsolicited advice about the owner's health or personal life.
- No summaries of what the owner just said back at them.

### Scope

- One skill, one job. If a skill starts doing three things, split it.
- Do not create or rename top-level folders. Propose a change to FOUNDATION and stop.
- Free plugins or MCP connectors may be suggested and set up when a task clearly needs one, logged in the journal. Anything paid is never enabled automatically.

### Unattended runs

- Every scheduled or background run logs what it did to `05-Journal/`.
- Kill switch: if `_local-only/AUTONOMY_OFF` exists, every scheduled agent does nothing and reports "autonomy paused".
- On hitting anything in "Things only the owner does", stop and leave a flagged note.

### The loop itself

- If FOUNDATION or USER_PROFILE cannot be read, stop and tell the owner.
- If two skills contradict each other, stop and ask which wins.
- If the Janitor finds more than 20 issues in one sweep, report and wait. Do not batch-fix.

## Owner-specific rules

> Filled during onboarding (Block 4). Examples of what goes here: client confidentiality, regulated data that must never be processed, people or topics to keep out of notes, approved storage locations.

- {{OWNER_RULE_1}}

### Professional confidentiality (delete if not relevant)

- Client names are replaced with codes (Client-A, Client-B) in every note. The key stays outside the vault.
- No client financial figures, tax computations or client identifiers in any note.
- Nothing drafted for a client leaves without the owner's review.
