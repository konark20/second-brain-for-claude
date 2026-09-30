---
type: meta
layer: 2
status: active
owner: system
tags: [pattern-log, skill-creation]
---

# Pattern Log

> The counter behind the self-improving loop. skill-creator fires when the same kind of work repeats three times. This file is where the repeats get recorded. Cheap to append, read by skill-creator and skill-sweep.

## Rules

- Every session appends a line when:
  - work was done manually that no existing skill covered,
  - an existing skill needed significant changes on the fly to fit,
  - the same kind of request was handled for the second time this week,
  - a capability gap was hit (no connector, no skill, missing access).
- One line per event. Append, never rewrite earlier rows.
- When a shape reaches three rows, skill-creator drafts to `proposed/` and marks the rows `-> drafted`.
- Resolved rows stay, with their resolution. This is a history, not a queue.
- `seed` rows come from the onboarding interview (recurring tasks the owner named on day one).

## Log

| Date | Session/context | What happened | Shape | Count so far | Resolution |
|---|---|---|---|---|---|
