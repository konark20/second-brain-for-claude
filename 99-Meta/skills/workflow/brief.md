---
name: brief
version: 1.0.0
trigger: reporting back after doing work in a session; default reporting mode for the owner unless they ask for full prose
inputs: what was done this turn, what is blocked, what needs the owner
outputs: a scannable status block, minimal prose
depends_on: compressed-response, USER_PROFILE.md
---

# Brief

## Purpose

The owner reads updates faster than paragraphs allow. This skill is how the brain reports after doing work: a scannable status block first, prose only when something genuinely needs explaining. It is the default reporting format for session work. Different from [[compressed-response]] (which compresses answers to questions); this governs how completed work is reported back.

## The format

Group by TASK, not by status. Each task is one block showing its own done / needs / next. Then the next task. This is how the owner reads fastest: everything about one thing together, then move on.

```
<Task name>
- did: <what got done, terse>
- needs: <what's blocked on the owner, or "nothing">
- next: <what happens next in this task>

<Next task name>
- did: ...
- needs: ...
- next: ...
```

Drop `needs` or `next` when empty. No global status sections, no multi-paragraph recaps, no restating what the owner asked, no narrating each step.

## Rules

- Lead with Done. The owner wants the outcome first.
- One line per item. If a line needs a sentence of context, it is one sentence, not a paragraph.
- "Needs you" is the section the owner scans for; make it impossible to miss. If nothing is blocked, say "Needs you: nothing".
- Numbers and file paths over adjectives. "moved 37 skills into 5 groups, 0 broken links" not "significantly reorganized the skills".
- Full prose is the exception, used only when the owner asks to discuss, or when a decision needs real reasoning laid out. For a decision, give the honest recommendation in 2-3 lines, not an essay.
- Still obeys USER_PROFILE: no em dashes, no emoji, no AI-sounding language.

## When NOT to use

- When the owner asks to "discuss", "walk through", "explain", or "tell me about" something. That is a conversation, use normal prose.
- When laying out a genuine decision with tradeoffs they need to weigh. Brief the options, but give enough to decide.

## Example

Per task, not per status:

```
Inbox cleanup
- did: archived 4 stale link-suggestion files to 04-Archives
- next: reaper auto-cleans these weekly once you ok its schedule

Graph colours
- did: read the graph, sub-brains not colour-separated
- needs: paste 4 colour-group queries in Obsidian graph settings

Brief skill
- did: built it, per-task format, registered in maps
- needs: your ok on the format
```

## Links

- [[compressed-response]]
- [[USER_PROFILE]]
- [[session-memory]]
