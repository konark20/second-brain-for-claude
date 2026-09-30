---
name: context-loader
version: 1.0.0
trigger: start of every session that touches the vault
inputs: none
outputs: loaded context and a one-line ready status
depends_on: 99-Meta/FOUNDATION.md, 99-Meta/USER_PROFILE.md, 99-Meta/BOUNDARIES.md
---

# Context Loader

## Purpose

The session-start ritual. Primes the session so the agent behaves like a colleague who knows the owner, not a stranger being re-briefed. If this fails, nothing else runs.

## Procedure

1. Read `99-Meta/FOUNDATION.md`. If missing or unreadable, stop and tell the owner. Do nothing else.
2. Read `99-Meta/USER_PROFILE.md`. Same failure rule.
3. Read `99-Meta/BOUNDARIES.md`.
4. Check `00-Inbox/` item count and oldest item age.
5. Check `05-Journal/` for today's entry.
6. If the session names a project, read that project's `_hub.md`, including its "Agents and skills assigned" section — those skills are the session's working set, loaded up front, not discovered one at a time mid-task. If the work is multi-phase, run `skill-orchestrator` to confirm the chain before starting.
7. Report one line: `loaded: profile ok, boundaries ok, inbox <n> items (oldest <d>d), journal <exists|missing>, skills <chain or n/a>`.
8. At session end, check: did any work happen that no skill covered, or that bent a skill out of shape? If yes, append a row to `PATTERN_LOG.md`. This is one line of effort and it is what feeds skill-creator.

## When NOT to use

- Never skipped. This is the one mandatory skill.

## Style rules

- The status line is the entire output. No greeting, no summary of what was read.

## Links

- [[START_HERE]]
- [[SKILL_MAP]]
- [[FOUNDATION]]
- [[USER_PROFILE]]
- [[BOUNDARIES]]
