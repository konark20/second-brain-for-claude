---
name: archive-stale
version: 1.0.0
trigger: weekly sweep, project close, or on request
inputs: 01-Projects/ notes and their modification dates
outputs: archive proposals, applied on approval
depends_on: 99-Meta/BOUNDARIES.md, 99-Meta/VAULT_MAP.md
---

# Archive Stale

## Purpose

Projects end or go dormant; their notes should stop cluttering the active view. This skill surfaces candidates and moves them only on approval.

## Procedure

1. Scan `01-Projects/` for notes untouched for 30+ days (project hubs judge the whole project: hub untouched 30+ days flags the project).
2. For each candidate: `note/project -> last touched -> proposal (archive | keep, reason)`.
3. On approval, move to `04-Archives/`, preserving the project subfolder structure.
4. Update the project hub status to `archived` and log one line in today's journal.

## When NOT to use

- `02-Areas/` and `03-Resources/`: those are permanent by design.
- Anything the owner has marked `status: active` in frontmatter, regardless of age.

## Style rules

- Dormant is not dead. The proposal wording is "archive", never "delete".

## Links

- [[SKILL_MAP]]
- [[BOUNDARIES]]
- [[VAULT_MAP]]
- [[janitor]]
