---
name: dedupe
version: 1.0.0
trigger: weekly sweep, or on request
inputs: notes in 02-Areas/ and 03-Resources/
outputs: report of near-duplicate pairs with a merge proposal each
depends_on: 99-Meta/BOUNDARIES.md
---

# Dedupe

## Purpose

Two notes on the same concept means links split between them and neither is complete. This skill flags near-duplicates for merge. It never merges on its own.

## Procedure

1. Compare notes within each area and within Resources: similar titles, overlapping headings, shared distinctive phrases.
2. For each candidate pair, decide: true duplicate, partial overlap, or false positive. Drop false positives silently.
3. For true duplicates: propose which note survives (the better-linked one), what content moves over, and that the loser goes to `04-Archives/` (never deleted).
4. For partial overlaps: propose a cross-link instead of a merge.
5. Present: `note A + note B -> <merge|cross-link> -> rationale`. Wait for approval.

## When NOT to use

- Journal entries. Same-day similarity is normal there.
- Auto-merging anything.

## Style rules

- If unsure whether two notes are duplicates, they are not. Skip.

## Links

- [[SKILL_MAP]]
- [[BOUNDARIES]]
- [[janitor]]
