---
name: scenario-analysis
version: 1.0.0
trigger: "What if X happens", pre-catalyst check ("what does CPI do to us"), "how bad can this get", any request to stress the current book
inputs: Current positions and open orders (broker), upcoming catalyst calendar, plan risk rails (stops, caps, drawdown ladder), price history for vol estimates
outputs: Scenario table with per-position and portfolio P&L impact, ladder-distance summary, recommended pre-positioning actions
depends_on: broker or market-data connector, strategy plan document
---

# Scenario Analysis

## Purpose

Stress the whole book against specific scenarios before a known catalyst or at any time: what each scenario costs in money and percent of capital, and which drawdown rung it would trip.


## When to use

- Before a known catalyst (FOMC, CPI, earnings, data release)
- After deploying new positions ("we just put on $400k, what is our downside")
- "How close are we to the -5% ladder rung"
- Hedge sizing questions


## When NOT to use

- Judging past trades (trade-analysis)
- Building a new strategy from scratch (strategy-builder)


## Procedure

1. Snapshot the book: positions, weights, resting protective orders. Positions WITHOUT stops get worst-case treatment (gap scenarios apply full move, not stop distance)
2. Define 3-5 scenarios, not more: base, event-up, event-down, tail (gap through stops), plus any user-specified. Anchor magnitudes in data: recent realized vol from price history, or the actual move from the last comparable event. State assumptions
3. Per-position impact: weight x assumed move, with beta adjustment for equity vs the shocked factor. Options at max loss for adverse tails (defined-risk means premium is the floor). Prediction contracts binary: cost or payout
4. Portfolio impact per scenario in dollars and % of NAV. Compare against the drawdown ladder: which scenario trips -5%, which trips -10%
5. Correlation honesty: state which positions fall together in each scenario. A hedge that rises when the core falls gets credited; ballast that just falls less does not count as a hedge
6. Stops math: what the book loses if every resting stop fills at its level, vs the unprotected worst case. The gap between those two numbers is the value of attaching stops today
7. Actions ranked: cheapest risk reduction first (attach stops, trim, then hedges that cost premium)


## Style rules

- Scenario table: scenario, assumption, portfolio P&L $, % NAV, ladder rung hit
- State assumptions before results; no false precision (round to $1k, 0.1%)
- Explicitly label unprotected positions
- No em dashes, no emoji

