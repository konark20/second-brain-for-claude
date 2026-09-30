---
name: weekly-review
version: 1.0.0
trigger: Sunday evening sweep, or /weekly-review
inputs: the week's journal entries, project hubs, inbox state
outputs: 05-Journal/YYYY-Www-review.md
depends_on: skills/lint-vault.md, skills/dedupe.md, skills/archive-stale.md
---

# Weekly Review

## Purpose

Scans the past week and surfaces what a good manager would notice: accomplishments, blockers, patterns, unfinished items. Also the container for the Janitor's weekly sweep findings.

## Procedure

1. Read the last 7 daily entries in `05-Journal/`.
2. Read the `_hub.md` of every active project; note status changes.
3. Compile:
   - **Done**: concrete accomplishments, one line each.
   - **Blocked**: what stalled and why.
   - **Patterns**: anything appearing 3+ times (feed candidates to `skill-creator`).
   - **Unfinished**: carried items that survived multiple days.
4. Append the Janitor's sweep findings under `## Janitor`.
5. Write `05-Journal/YYYY-Www-review.md`.

## When NOT to use

- Mid-week status checks. Read the journal directly.

## Style rules

- Facts from the journals only. If the week's entries are thin, say the review is thin and why, do not pad.

## Links

- [[SKILL_MAP]]
- [[daily|daily]]
- [[lint-vault]]
- [[dedupe]]
- [[archive-stale]]
- [[skill-creator]]
