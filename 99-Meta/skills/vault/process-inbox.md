---
name: process-inbox
version: 1.0.0
trigger: inbox has items; nightly pass; or /process-inbox
inputs: everything in 00-Inbox/, VAULT_MAP.md routing rules
outputs: each item classified with a proposed destination, moved on approval
depends_on: 99-Meta/VAULT_MAP.md, skills/connect.md
---

# Process Inbox

## Purpose

Nothing lives in the inbox longer than 7 days. This skill is how the rule holds: classify each item, propose where it goes, move it when the owner approves.

## Procedure

1. List `00-Inbox/` items oldest first.
2. For each item, classify per the routing rules in `VAULT_MAP.md`: project, area, resource, journal, or trash-candidate (propose archive, never delete).
3. Where the destination note format differs (e.g. a raw link becoming a resource), propose the transformation but show it before applying.
4. Present the full batch as a table: `item -> proposed destination -> transformation if any`.
5. On approval, move items, add proper frontmatter, and run `connect` on anything that landed in Areas or Resources.
6. Report: `processed <n>, remaining <m>`.

## When NOT to use

- One-off filing of a single named item. Just move it.
- Auto-filing without showing the batch first. Approval is the point.

## Style rules

- Items older than 7 days get flagged at the top of the batch.
- Uncertain classification: say so and ask, do not force a guess.

## Links

- [[SKILL_MAP]]
- [[VAULT_MAP]]
- [[capture]]
- [[connect]]
