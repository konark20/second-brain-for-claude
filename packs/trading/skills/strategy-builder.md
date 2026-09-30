---
name: strategy-builder
version: 1.0.0
trigger: "I want to trade X thesis", "build a strategy for", "turn this idea into a plan", new sleeve or account setup
inputs: The thesis (from user), market data to validate it (broker price history, betas, momentum), capital and constraints, catalyst calendar
outputs: A written plan document: thesis, instruments, entries, sizing, stops, caps, catalysts, contingency ladder, review cadence. Compatible with the tracker format
depends_on: broker or market-data connector for validation data, scenario-analysis for pre-trade stress, trading-finance-tutor for instrument mechanics if needed
---

# Strategy Builder

## Purpose

Turn a directional opinion into a rules-based, self-defending plan before any order exists: a validated thesis, budgets per sleeve, exits written before entries, and a contingency ladder written before the drawdown. Every strategy gets the same skeleton so the review skills can check it mechanically.


## When to use

- New trade idea that needs structure ("I think banks rally into earnings")
- New sleeve, account, or trading challenge
- Re-arguing a thesis after a stop-out (per contingency rules, re-entry requires a written re-argument)


## When NOT to use

- Reviewing existing trades or performance (trade-analysis, performance-analysis)
- Pure concept questions (trading-finance-tutor)


## Procedure

1. State the thesis in one sentence with a falsifier: what observation kills it. No falsifier, no strategy
2. Validate with data before structuring: pull price history, compute the relevant stats (momentum blend, beta vs benchmark, realized vol, correlation to existing book). If the data contradicts the thesis, stop and say so
3. Instrument selection: cheapest expression of the view with defined or stopped risk. Prefer defined-risk options for event bets, stopped equity/ETF for trends, event contracts for binary macro outcomes. Note liquidity
4. Sizing from risk, not conviction: position size = risk budget / stop distance. Risk budget 1-2% of capital per trade unless user overrides in writing
5. Exits before entries: hard stop level, thesis-invalidation trigger (event-based, fires same-week), profit rule (trail, target, or % of max profit for spreads)
6. Catalyst map: what known events hit this position during its life, and what the plan is for each (hold through, trim before, pre-built contingent orders)
7. Rails: single-position cap, sleeve budget, aggregate premium cap, leverage ceiling, drawdown ladder if this is a whole account
8. Run scenario-analysis on the proposed position against the existing book before recommending
9. Write the plan into the project tracker or a new plan doc. The plan is the contract that trade-analysis and the weekly session-cadence review check against later


## Style rules

- Every level is a number, not a vibe ("stop 176.20", not "tight stop")
- State what the market already prices (check option-implied or event-contract odds) so the edge claim is explicit
- Plans are versioned; changes get a dated line, the original stays
- No em dashes, no emoji

