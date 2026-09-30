---
name: model-handoff
version: 1.0.0
trigger: a coding task would be better done by a different model (e.g. GPT-5.5), or the owner says "hand this off" / "write a prompt for another model"
inputs: the ticket or task, the relevant files, the constraints
outputs: a self-contained prompt for the external model, then a re-entry that reviews what comes back
depends_on: project-handoff, code-review, self-correction, MODEL_SELECTOR.md, BOUNDARIES.md
---

# Model Handoff

## Purpose

The owner sometimes wants a different model to write the code (they find GPT-5.5 stronger on some tasks) while the brain still owns the spec, the standards, and the review. This skill packages a clean, self-contained coding prompt to hand to any external model, then brings the result back through the brain's own quality gate. The brain stays the architect and reviewer; the external model is just the hands. Extends [[project-handoff]] from "another Claude session" to "another vendor's model".

## When to use

- A ticket is specced (architect + builder done) and the owner wants an external model to implement it.
- The owner says to write a prompt for ChatGPT / GPT-5.5 / another model to code something.

## When NOT to use

- The task touches real sensitive or regulated data or credentials. That never leaves to any external model (BOUNDARIES).
- Trivial edits the brain can just make. No handoff ceremony.
- Anything where the external model would need vault content on the BOUNDARIES blocklist. Strip or refuse.

## Procedure

### Outbound (build the prompt)

1. Confirm the ticket is specced. If not, run architect/builder first; do not hand off a vague task.
2. Write a single self-contained prompt block containing: the goal, the exact acceptance criteria, the files it may touch (with current contents or clear excerpts), the constraints (ponytail ladder, validation/error-handling/security never cut, no em dashes in comments, diff-only output), and the expected output format (a diff or full files, its choice stated).
3. Sentinel-check the prompt before it leaves: no identity numbers, no credentials, no real data. Strip anything on the blocklist.
4. Give the owner the prompt to paste into the external model. Nothing is sent automatically.

### Inbound (bring the result back)

5. The owner pastes the external model's output back.
6. Run [[code-review]] on it against the ticket's acceptance criteria: severity-grade, critical blocks. Trace logic, do not run against real data.
7. Run [[self-correction]]. Fix or flag what the external model got wrong.
8. Apply only after review passes. Record in the ticket's coder block which model wrote it and that it was reviewed here.

## Style rules

- The outbound prompt is self-contained: a fresh model with zero context can act on it. That is the test.
- The brain owns acceptance and review. An external model's output is never trusted unread.
- No em dashes, no AI-sounding language.

## Links

- [[project-handoff]]
- [[code-review]]
- [[self-correction]]
- [[MODEL_SELECTOR]]
- [[BOUNDARIES]]
