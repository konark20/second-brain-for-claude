---
name: performance-analysis
version: 1.0.0
trigger: "How is the portfolio doing", weekly/monthly review, end-of-period report, "compare vs benchmark"
inputs: broker performance series, positions, trades over the period, benchmark price history (an index ETF or user-specified), sleeve definitions from the strategy plan
outputs: Performance report section in the tracker, or a standalone report (research-documentation format if formal)
depends_on: broker or market-data connector, trade-analysis scorecards if available
---

# Performance Analysis

## Purpose

Portfolio-level judgment for a period: return, the risk taken to earn it, where it came from, and whether process or luck produced it.


## When to use

- Weekly or period-end review
- "Are we beating the benchmark", "what drove the P&L"
- Feeding a period retrospective or any formal writeup


## When NOT to use

- Single-trade questions (trade-analysis)
- Forward-looking stress (scenario-analysis)


## Procedure

1. Headline: TWR for the period vs benchmark over identical dates. State NAV, peak, trough, max drawdown, current drawdown from peak
2. Attribution by sleeve (core/momentum/hedge/options/prediction/satellite or whatever the plan defines): realized plus unrealized P&L per sleeve, per period. Flag any sleeve earning outside its budgeted share of risk
3. Concentration: top 5 P&L contributors vs rest, winners and losers separately. If one position or sleeve is most of the return, say so plainly
4. Hit rate and expectancy from closed trades: win%, avg win, avg loss, expectancy per trade. Separate by instrument type (equity, options, prediction contracts)
5. Risk taken: leverage over the period, biggest single-position weight touched, per-trade risk vs the 1-2% budget, drawdown-ladder rungs touched
6. Process vs outcome: count rule breaches from trade-analysis scorecards. High return with high breach count is flagged as fragile, not celebrated
7. Period comparison: this week vs last weeks, same decomposition. Trend in discipline matters more than trend in P&L
8. One inference paragraph per section, then a three-line summary verdict


## Style rules

- Every table gets one short Inference paragraph
- Percentages of NAV alongside dollar figures
- Never annualize a 6-week window; state returns for the window
- No em dashes, no emoji

