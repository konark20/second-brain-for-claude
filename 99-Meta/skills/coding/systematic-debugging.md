---
name: systematic-debugging
version: 1.0.0
trigger: a bug, failing test, or wrong output needs diagnosing before a fix is written
inputs: the failing behavior, the code, the ticket if any
outputs: a root cause located and named, then a minimal fix or a ticket back to builder
depends_on: 99-Meta/agents/coder.md, tdd, self-correction, BOUNDARIES.md
---

# Systematic Debugging

## Purpose

Stops the guess-and-patch loop. When something breaks, the temptation is to change a line and rerun. This skill forces a four-phase root-cause process so the fix addresses the cause, not a symptom. Idea borrowed from superpowers' systematic-debugging, rebuilt as a vault skill under our trace-not-run rule.

## When to use

- A test fails, output is wrong, or behavior diverges from the ticket's acceptance criteria.
- A bug reappears after a previous fix (sign the previous fix hit a symptom).

## When NOT to use

- A one-line typo with an obvious cause. Fix it.
- Anything requiring code run against real sensitive or regulated data (BOUNDARIES). Trace the logic by reading; never execute against real data to reproduce.

## Procedure (four phases, in order)

1. **Reproduce and isolate.** Pin the exact input and the smallest code path that triggers it. On synthetic data only. State the expected vs actual in one line each.
2. **Trace to root cause.** Read the path backward from the failure to the first point where state goes wrong. Name the cause explicitly: "the comparison uses X where it should use Y", not "something in the parser". Do not propose a fix until the cause is named.
3. **Confirm the cause explains everything.** The named cause must account for the full symptom, including any related failures. If it explains only part, keep tracing; there are two bugs or the wrong root.
4. **Minimal fix at the cause.** Fix at the root location, not at the caller or the symptom site. Add a regression test per [[tdd]] that fails before and passes after. Self-correction pass.

## When the cause is architectural

If the root is a design flaw, not a local bug, stop. Do not patch around it. Flag it back to [[builder]] or [[architect]] with the named cause, per the pipeline's "when the plan is wrong" rule.

## Style rules

- Name the cause before proposing any fix. This is the whole discipline.
- Flat output: `expected / actual / root cause / fix / regression test`.
- No em dashes, no AI-sounding language.

## Links

- [[coder]]
- [[tdd]]
- [[code-review]]
- [[self-correction]]
- [[BOUNDARIES]]
