---
name: trade-analysis
version: 1.0.0
trigger: "Review this trade / these trades", after any closed trade or batch of fills, or when a stop or target hits
inputs: Trade fills (broker trade history or a fills export), the thesis behind the trade (tracker, journal, or user statement), price history around the trade window
outputs: Per-trade scorecard appended to the strategy tracker or journal; verdict on thesis, execution, and rule compliance
depends_on: broker or market-data connector or trade log, performance-analysis (for aggregates), strategy plan document
---

# Trade Analysis

## Purpose

A per-trade post-mortem that separates the three things that decide a result: was the thesis right, was the execution clean, were the rules followed. Luck and skill get scored separately.


## When to use

- A position closed (stop, target, discretionary exit, expiry, settlement)
- A batch review of the week's fills
- "Why did this trade lose/win"


## When NOT to use

- Portfolio-level questions (use performance-analysis)
- Pre-trade sizing or structure decisions (use strategy-builder)
- Open positions with no exit yet (scenario-analysis covers what-if on open risk)


## Procedure

1. Reconstruct the trade: entry fills, exit fills, size, holding period, realized P&L including commissions. For broker exports, aggregate fills with jq by symbol and side
2. Restate the thesis as written at entry (tracker/journal). If no written thesis exists, flag that as finding number one
3. Thesis verdict: did the predicted event/move happen? Right/wrong/never-tested. A stop-out before the catalyst is never-tested, not wrong
4. Execution verdict: entry vs the plan's intended level, slippage, was the stop attached at entry, exit vs the exit rule (e.g. 50-70% max profit rule for spreads, stop honored vs overridden)
5. Rules verdict: size cap, per-trade risk (size x stop distance vs 1-2% budget), instrument scope, premium cap
6. Counterfactuals, max two: what the exit rule would have produced vs actual, and what holding to plan would have produced. No hindsight beyond that
7. One-line lesson only if it generalizes. Append scorecard to the tracker's closed-trades section


## Style rules

- Scorecard format: Thesis R/W/NT, Execution pass/fail per item, Rules pass/fail per item, P&L, lesson
- Losing-but-correct trades get called out as good trades. Winning rule-breaches get called out as breaches
- No em dashes, no emoji, numbers first

