---
name: ingest-url
version: 1.0.0
trigger: The owner shares a URL worth keeping
inputs: the URL, templates/resource.md
outputs: a note in 03-Resources/, cross-linked
depends_on: 99-Meta/templates/resource.md, skills/connect.md, web fetch permission (granted for this skill in BOUNDARIES.md)
---

# Ingest URL

## Purpose

Turns an article into a resource note that sounds like the owner took the notes themselves: what it says, what holds up, what it connects to.

## Procedure

1. Fetch the URL. If paywalled or empty, report and stop; do not summarize from the title.
2. Instantiate `templates/resource.md`: source, author, ingested date.
3. Summary: 3 to 5 sentences on what the piece actually says.
4. Key claims: bullet list, each one falsifiable as stated.
5. My take: leave a stub line for the owner unless they gave a reaction, in which case record their words.
6. Save to `03-Resources/<source-title-slug>.md`.
7. Run `connect` on the new note.

## When NOT to use

- Trivial content (release notes, listicles). Capture the link to Inbox instead if it must be kept.
- Bulk URL lists. One at a time, each gets real treatment.

## Style rules

- No AI-summary voice. Short declarative sentences. The summary should survive being read aloud next to the owner's own notes.

## Links

- [[SKILL_MAP]]
- [[connect]]
- [[BOUNDARIES]]
