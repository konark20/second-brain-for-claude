---
name: code-review
version: 1.0.0
trigger: a coder ticket reaches status review, or the owner asks to review a diff before merge
inputs: the ticket (architect + builder + coder blocks), the diff, the acceptance criteria
outputs: a severity-graded review; critical issues block the ticket from done
depends_on: 99-Meta/agents/coder.md, ponytail-review, self-correction, BOUNDARIES.md
---

# Code Review

## Purpose

Fills the gap between coder finishing and a ticket reaching done. Today a coder sets status to `review` and nothing defines how the review happens. This skill defines it: check the diff against the ticket's acceptance criteria, grade findings by severity, and let critical issues block progress. Idea borrowed from superpowers' requesting/receiving-code-review, rebuilt to fit our pipeline and BOUNDARIES rather than installed as a plugin.

## When to use

- A ticket is at status `review` with a filled coder block.
- The owner asks for a review of a diff before merge or push.

## When NOT to use

- Reviewing for over-engineering only. That is [[ponytail-review]], run it first or alongside.
- Reviewing prose or documents. This is code only.
- Mid-code. Coder finishes and self-corrects before review starts.

## Procedure

1. Read the ticket's `architect.acceptance_criteria` and the coder's `diff_summary`.
2. Walk the actual diff. For each file, check: does it meet every acceptance criterion, does it follow the ponytail ladder, are validation, error handling, security, and accessibility intact (never on the chopping block per BOUNDARIES).
3. Trace logic by reading, never by running code against real data (BOUNDARIES). For anything touching sensitive or regulated data, trace only.
4. Grade each finding:
   - **critical**: wrong behavior, security hole, missing validation, breaks an acceptance criterion. Blocks done.
   - **major**: correct but fragile, untested path, silent failure mode. Fix before done unless the owner waives.
   - **minor**: style, naming, a cleaner approach. Note it, do not block.
5. Report as a flat list: `severity | file:line | issue | suggested fix`. Counts at top.
6. Any critical: ticket status goes back to `coding` with a `history` line. Zero critical and no un-waived major: status `done`.

## Style rules

- Severity-first, terse. No praise padding, no restating the diff back.
- A suggested fix per finding, one line each. No paragraphs.
- No em dashes, no AI-sounding language.

## Links

- [[coder]]
- [[ponytail-review]]
- [[self-correction]]
- [[PIPELINE]]
- [[BOUNDARIES]]
