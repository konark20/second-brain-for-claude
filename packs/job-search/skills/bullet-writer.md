---
name: bullet-writer
version: 1.0.0
trigger: any resume or cover letter bullet being written or rewritten
inputs: raw material (archive entry, PROJECT_BANK box, owner's notes), target JD keywords
outputs: finished bullets that follow RESUME_RULES
depends_on: action-word list, RESUME_RULES, number-miner
---

# Bullet Writer

One job: turn true raw material into strong resume bullets.

## Procedure

1. Identify the claim: what was built, run, sold or measured, how, and what changed because of it.
2. Pick a strong, accurate verb. No repeats within a section.
3. Assemble: verb + artifact + method + quantified outcome. Two numbers when possible (scale and result).
4. Numbers must be real. If missing, ask [[number-miner]] to dig; if still missing, flag it. Never invent.
5. Work JD keywords into the concrete claim, never stuff them.
6. Style: one to two lines compiled, no semicolons, no trailing full stop, no pronouns, no orphan last line. Name the specific method or tool; it is both the keyword and the depth signal.
7. Read it as a sceptical interviewer: every word must survive a follow-up question.
8. Two bullets per project where space allows: first what was built and how, second the result and how it was validated.

## Banned

"Responsible for", "assisted", "helped", "leveraged", "utilized", and any claim the owner could not explain in detail.

## Example

Weak: "Worked on a pricing model."
Strong: "Built a Monte Carlo pricing engine in Python for 40 structured notes, cutting valuation time from 3 hours to 12 minutes" / "Validated prices against dealer quotes within 0.4% on 95% of notes and documented the three outliers."
(Fictional example. Your numbers come from your own artifacts.)
