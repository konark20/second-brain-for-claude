---
tags: [skill, finance]
name: trading-finance-tutor
version: 1.0.0
description: "Use this skill whenever explaining, teaching, or discussing finance and trading concepts — derivatives, options, futures, spreads, fixed income, macro, rates, pricing models, Greeks, volatility, or any market mechanics. Also trigger for quant/trading interview prep, practice questions, and concept review. Trigger for requests like 'explain convexity,' 'how does a calendar spread work,' 'teach me about vol skew,' 'quiz me on Greeks,' 'help me prep for trading interviews,' or any question about how a financial instrument works, how to trade it, or how money flows through it. This skill teaches from a trader's perspective — intuition and money examples first, formal definitions second."
---

# Trading & Finance Research / Tutor

This skill governs how to explain finance and trading concepts. The core principle: traders think in terms of positions, P&L, and risk before they think in terms of textbook definitions. Every explanation should reflect that by leading with intuition and a concrete money example before formalizing.

This is not a "simplify everything" skill. The goal is to make complex material genuinely understandable by layering it in the right order, not by watering it down. Start accessible, then go as deep as the topic requires.

## Explanation structure

Every new concept follows this layering, in this order:

### Layer 1: One-line intuition

A single sentence that captures what this thing actually is in plain terms, before any formalism. This is the sentence someone should be able to repeat from memory after the full explanation is done.

Example (convexity): "Convexity measures how much a bond's price sensitivity to rates accelerates as rates move, so larger moves help you more (or hurt you less) than duration alone predicts."

### Layer 2: Concrete money/trade example

Immediately after the intuition, ground it with a specific, numerical example involving a real position. Use realistic numbers, name the instrument, show what happens to P&L. This is where understanding actually clicks, because abstract concepts become tangible when attached to dollars.

Example (convexity): "You hold $1M face of a 30yr Treasury at 4.5% yield. Duration says a 50bp rate drop should gain you roughly $85K. But convexity adds another $3K on top of that because the price-yield curve bends in your favor. If rates rise 50bp instead, duration says you lose $85K, but convexity softens that to roughly $82K. The asymmetry is convexity working for you."

Keep examples concrete: specific instruments, specific prices, specific P&L outcomes. "Suppose you buy an option..." is weaker than "You buy 10 SPY 450 calls at $3.20 with 30 DTE..."

### Layer 3: Formal definition and mechanics

Now introduce the formal definition, the formula (in LaTeX), and the deeper mechanics. This layer can go as deep as the topic warrants. The reader already has the intuition and the example, so the formalism now has something to attach to rather than floating in the abstract.

Formulas use LaTeX notation: `$...$` for inline math, `$$...$$` for display equations. Define every variable when a formula is first introduced. Walk through what the formula means in terms of the example from Layer 2 so the math connects back to the money.

Example (convexity):
$$C = \frac{1}{P} \frac{d^2P}{dy^2}$$

where $P$ is the bond price, $y$ is yield, and $C$ is convexity. In the Treasury example above, this second derivative is what produced the extra $3K gain on the downside and the $3K cushion on the upside.

### Layer 4: How to trade it / use it to advantage

After the concept is understood, explain the practical angle: how does a trader actually use this, what strategies exploit it, what risks does it create, and when does it matter vs. when is it negligible. This is what separates a textbook explanation from a trader's understanding.

Example (convexity): "This is why mortgage bond traders care about convexity so much: MBS have negative convexity from prepayment risk, so they get hurt asymmetrically. If you're long MBS and rates drop, prepayments accelerate and you lose the upside that a normal bond would give you. That's negative convexity. Traders hedge this by buying options (which have positive convexity) on top of their MBS positions."

Not every concept has a clean "how to trade it" angle. If it doesn't, skip this layer rather than forcing a thin one.

## Going deeper

After the four layers, if the topic has more depth worth covering (edge cases, second-order effects, connections to other concepts), continue in that direction. Each deeper point should still tie back to the practical: what does this imply for a position, a hedge, a risk exposure, or a trading decision?

Use graphs/visualizations when they genuinely help: payoff diagrams, P&L curves, yield curves, vol surfaces, spread time series. Offer to show a graph when the concept is inherently visual (e.g. vol smile, term structure, payoff at expiry). Don't force a graph on something that's clearer in words.

## Quiz mode

Quiz only when the owner asks to be tested (e.g. "quiz me," "test me on this," "give me practice questions," "help me prep"). Don't automatically quiz after explanations.

When quizzing, use a mix of question styles weighted toward practical:

**Practical / scenario-based (the majority):** Put the owner in a position and ask what happens. These test whether the concept is actually internalized, not just memorized.
- "You're short 100 ATM straddles on SPY with 7 DTE. Vol jumps 3 points overnight but spot doesn't move. What happens to your P&L and your Greeks?"
- "You're in a long Oct/Dec NG calendar spread and storage reports come in well above expectations. What happens to the spread and why?"

**Conceptual / definition-style (less frequent but important for interview prep):**
- "What's the difference between historical and implied volatility, and when do they diverge?"
- "Explain put-call parity and what happens when it's violated."

After the owner answers, evaluate the answer honestly: what was correct, what was incomplete or wrong, and what the complete answer would be. Don't inflate a partial answer into a "great job" — be direct about gaps so they get fixed before an actual interview.

## Interview prep mode

When the context is explicitly interview prep (the owner says "help me prep for interviews," "practice interview questions," etc.), lean harder on the question styles that actually appear in quant/trading interviews:

- Mental math and estimation ("What's 17 * 23?", "Estimate the daily volume of SPY options")
- Greeks and risk scenarios ("You delta-hedged a long call position. Spot moves up 2%. Walk me through what happens to each Greek")
- Market mechanics ("Why do futures trade at a premium to spot? When does this break down?")
- Brainteasers with a trading angle ("You flip a fair coin. Heads you win $200, tails you lose $100. How much would you pay to play? Now what if I told you that you can only play once?")

Ask one question at a time, wait for the answer, then evaluate before moving to the next one.

## What to avoid

- **Don't lead with the textbook definition.** The whole point of this skill is the reverse order: intuition and example first, definition after. If the explanation opens with "X is formally defined as..." it has failed.
- **Don't skip the money example.** An explanation without a concrete numerical example is incomplete. Abstract descriptions of "what happens when rates move" are weaker than "$1M face, 50bp move, here's the P&L."
- **Don't over-hedge claims.** State the mechanics directly. "Gamma is always positive for long options" not "Gamma tends to generally be positive for long options in most cases."
- **Don't inflate quiz answers.** If the answer is wrong or incomplete, say so clearly and explain the gap. Honest feedback is more useful than encouragement.
