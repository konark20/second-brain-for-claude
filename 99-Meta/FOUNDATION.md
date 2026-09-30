---
type: meta
layer: 1
status: active
owner: "{{OWNER_NAME}}"
version: 1.0-template
tags: [constitution]
---

# Foundation

> The operating charter for this vault. Every Claude session that touches this folder reads this file before doing anything else. Owner-edited only: no agent changes this file on its own. If a session is ever confused about what to do, the answer is in one of the files this document points to. If it is not there, the correct move is to stop and ask, not to guess.

## 0. What this is

A second brain for one person, run by Claude. The vault is plain Markdown in folders. Claude reads a small set of operating files at the start of every session, which tells it who the owner is, what it must never do, where things live, and which agent or skill file to follow for each kind of request. Nothing here is a plugin or a server. It works on any Claude surface that can read a folder.

## 1. Architecture: four layers plus an always-on loop

**Layer 1, Inner Self.** Who the owner is, how they think, their standing preferences and the tone they want. This layer never executes anything. It primes every session so the agent behaves like a colleague who knows them rather than a stranger who needs re-briefing. File: `USER_PROFILE.md`.

**Layer 2, Mapping.** The vault map and the skill map. Where things live, which skills exist, when to reach for which one. Hosts the Navigator agent, the router. Files: `VAULT_MAP.md`, `SKILL_MAP.md`, `SKILL_INDEX.md`, `MODEL_SELECTOR.md`, `agents/navigator.md`.

**Layer 3, Tools.** The agents and skills that do the work: capture, ingest, synthesize, research, plan, build, review. Folders: `99-Meta/agents/`, `99-Meta/skills/`, `skills/`, `code/`.

**Layer 4, Interface.** How the owner talks to the system: slash commands in Claude Code, chat in the Claude desktop app or claude.ai, capture from a phone, Obsidian's own UI. Different mouths, same brain.

**Always-on loop, Janitor and Guardrails.** Maintenance that runs at the end of every session and on a weekly sweep: broken links, orphans, stale inbox items, contradictions between maps and reality, and the boundary rules. It is what stops a second brain from collapsing under its own weight in three weeks. Files: `agents/janitor.md`, `agents/sentinel.md`, `BOUNDARIES.md`.

```
LAYER 4  Interface (chat, terminal, Obsidian, phone)
   |
LAYER 3  Tools: agents + skills  <----+
   |                                  |   Always-on loop:
LAYER 2  Mapping: Navigator           |   Janitor + Sentinel
   |                                  |   (session end, weekly,
LAYER 1  Inner Self: USER_PROFILE ----+    before anything leaves)
```

A request comes in through Layer 4. The Navigator (Layer 2) reads Layer 1 to know who is asking, checks the skill map, and dispatches to Layer 3. The Janitor cleans up on the way out. Sentinel checks anything leaving the machine.

## 2. Folders

```
00-Inbox/      Capture zone. Nothing lives here longer than 7 days.
01-Projects/   Active work with a defined outcome. One subfolder + _hub.md each.
02-Areas/      Ongoing responsibilities with no end date.
03-Resources/  Reference material: articles, papers, cheat sheets, citations.
04-Archives/   Done or dormant. Read-only unless reopened.
05-Journal/    Daily notes, weekly reviews, session logs.
99-Meta/       The operating layer: this file, maps, agents, skills, templates.
skills/        Portable Claude skills that travel with the vault.
code/          Scripts that serve the vault. Not notes.
_local-only/   Sentinel's quarantine. Never synced.
```

`VAULT_MAP.md` is authoritative for anything more specific. Do not create new top-level folders without the owner's approval and an update to this document.

## 3. The skill and agent formats

A **skill** is a stateless procedure invoked on demand. An **agent** is a persistent role that owns a job across sessions and has a model tier bound to it. Both are Markdown files with frontmatter:

```markdown
---
name: skill-name
trigger: when to invoke, one line
inputs: what it needs
outputs: what it produces
depends_on: other skills or files
---

# Skill Name

## Purpose
## When to use
## When NOT to use
## Procedure
## Style rules
## Example
```

Agents add a `model:` line. One skill, one job. If a skill starts doing two things, split it.

## 4. How the brain learns its owner

1. `onboard` interviews the owner on day one and writes Layer 1.
2. Every session that handles something manually because no skill fits appends one line to `PATTERN_LOG.md`.
3. When the same shape appears three times, `skill-creator` drafts a skill or agent into a `proposed/` folder.
4. The owner approves, edits or rejects. Approved drafts move into the live folders and get a row in `SKILL_MAP.md`.
5. Monthly, `capability-auditor` checks the whole toolkit for overlap, dead capabilities and contradictions.

The output is the owner's own patterns written down, not someone else's workflow.

## 5. Bootstrap sequence for a new copy

1. Run the onboarding interview (`/onboard`, or ask "run the onboarding interview").
2. Create at most five project hubs for real ongoing work.
3. Use only the default agents for two weeks. Capture freely, process the inbox daily, weekly review on Sundays.
4. Let skill-creator propose from the journal. Approve what is genuinely yours.
5. Promote a project to a sub-brain only when it passes the test in `SUB_BRAIN_PATTERN.md`.

## 6. What this document is not

Not a plugin, not code, not something that runs by itself. It is a shared understanding between the owner and every Claude session, written down. If the vault drifts, reread this file, update it, then fix whatever downstream is broken.

## 7. Revisions

Every material change gets a version bump and one line here.

- 1.0-template: public template release.
