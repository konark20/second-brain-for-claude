---
name: capture
version: 1.0.0
trigger: any fleeting thought, link, or fragment the owner wants saved without deciding where it goes
inputs: the raw content, optionally a hint about topic
outputs: a note in 00-Inbox/ with minimal frontmatter
depends_on: none
---

# Capture

## Purpose

Capture is cheap and can happen anywhere. This skill makes the dump frictionless: no classification, no perfect title, no thinking. Processing happens later, on desktop, through `process-inbox`.

## Procedure

1. Take the content as-is. Do not rewrite it, summarize it, or improve it.
2. Create `00-Inbox/YYYY-MM-DD <short-slug>.md` where the slug is the first few meaningful words.
3. Add frontmatter: `captured: <ISO datetime>`, `source: <chat|mobile|url|terminal>`, `hint: <topic hint if given>`.
4. Paste the content below the frontmatter.
5. Confirm in one line: `captured: <filename>`.

## When NOT to use

- The content already has an obvious home and the owner said where. File it directly.
- Long-form original writing. That is a working document, not a capture.

## Style rules

- Never editorialize on captured content. It lands verbatim.

## Links

- [[SKILL_MAP]]
- [[process-inbox]]
