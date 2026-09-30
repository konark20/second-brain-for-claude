---
name: daily
version: 1.0.0
trigger: first vault touch of the day, or /daily
inputs: templates/daily.md, yesterday's journal entry
outputs: 05-Journal/YYYY-MM-DD.md
depends_on: 99-Meta/templates/daily.md
---

# Daily

## Purpose

Creates today's journal entry with yesterday's loose ends carried forward, so the day starts with context instead of a blank page.

## Procedure

1. If `05-Journal/<today>.md` exists, open it and stop. One entry per day.
2. Instantiate `templates/daily.md` with today's date.
3. Read yesterday's entry. Copy anything under "Tomorrow" and unresolved "Open questions" into today's sections.
4. Write the file. Report: `journal ready: <today>, carried <n> items`.

## When NOT to use

- A second entry the same day. Append to the existing one.
- Weekly reflection. That is `weekly-review`.

## Style rules

- Carried items keep their original wording. No rephrasing.

## Links

- [[SKILL_MAP]]
- [[weekly-review]]
