---
name: council
version: 1.0.0
trigger: a high-stakes decision with genuine uncertainty, or the owner says "council this" / "pressure-test this" / "war room this"
inputs: the decision or question, relevant context
outputs: five angled takes, cross-review, a chairman's synthesis and recommendation
depends_on: self-correction, evenhandedness (FOUNDATION), BOUNDARIES.md
---

# Council

## Purpose

One model gives one answer, and you cannot tell if it is right because you only saw one angle. This skill runs a hard decision through five independent advisors who each reason from a different frame, review each other, and end in a chairman's synthesis. Adapted from the llm-council methodology (Karpathy, via Ole Lehmann) as a vault-native skill. It exists for judgment calls where a wrong choice is costly: a job offer, which resume angle to lead, a trade thesis, an architecture decision.

## When to use

- Genuine uncertainty and a costly downside: offer vs offer, pivot or not, which of three angles is strongest.
- The owner asks to pressure-test, stress-test, or war-room something.

## When NOT to use

- Questions with one right answer (a fact, a calculation). Just answer.
- Creation tasks (write this) or processing tasks (summarize this). Not decisions.
- When the owner already knows the answer and wants validation. The council will not flatter; say so if that seems to be the ask.

## Procedure

1. State the decision in one line and the real constraints around it.
2. Run five advisors, each from a distinct frame. Default frames, swap per topic:
   - the skeptic (what breaks this, what is the failure mode)
   - the operator (what actually happens week to week if we do it)
   - the long-game (where does this put the owner in a year)
   - the numbers (what do the figures and base rates say)
   - the contrarian (the strongest case for the opposite choice)
3. Each advisor gives a short, concrete take, no hedging.
4. Cross-review: each reads the others and notes where they agree and where they clash.
5. Chairman synthesis: where the advisors converge, where they genuinely disagree, and one clear recommendation with its main risk named. Present opposing views fairly (FOUNDATION evenhandedness); the recommendation is a best-case reading, not the owner's decision made for them.
6. Self-correction pass on the synthesis.

## Style rules

- Advisors are terse and concrete, not personas performing. No role-play theatre.
- The chairman names one recommendation and its single biggest risk. No fence-sitting.
- No em dashes, no AI-sounding language. Financial or legal calls carry the standard "not a financial/legal advisor" caveat and give the facts to decide, not a directive.

## Links

- [[self-correction]]
- [[project-planner]]
- [[trading-finance-tutor]]
- [[BOUNDARIES]]
