---
name: session-cadence
version: 1.0.0
trigger: Every live trading day - scheduled morning run (9:35 ET), on-demand "pull the book", and a weekly deep reconciliation
inputs: broker or market-data connector (positions, orders, summary, flows, trades), tracker, watchlist, the active strategy plan document
outputs: One-table morning brief; tracker positions, orders and tripwires updated; tripwire status line; weekly mode adds a full plan-compliance verdict
depends_on: tilt-guard (runs alongside), live-quote protocol below
---

# Session Cadence

## Purpose

The daily pre-market routine and the weekly deep reconciliation, so the book, the orders and the tracker always agree and nothing enters or leaves the account unannounced.


## Procedure (morning run)

1. Pull: account summary, positions, open orders. Diff against tracker's last state - flag anything that appeared or vanished
2. Tripwire status line: each written floor/falsifier - HIT / NOT HIT / distance. No commentary
3. Flow check on any story-trade positions: today's option volume vs average, stated as a ratio
4. Regime gauges: VIX level and band, CL front month if energy exposure exists
5. Calendar: today's scheduled events touching the book (your broker's event calendar)
6. Expiring today/this week: salvage table - residual value of every long option under 10 DTE (residual premium goes to zero silently; collecting it is un-taking a loss, not booking one)
7. One table out, verdict lines only. Update the tracker's positions, orders and tripwire sections


## Procedure (weekly deep mode)

Run weekly during any live strategy window, or after any deployment of new positions:
1. Everything in the morning run, but trades pulled over DAYS_7 (DAYS_30 if the gap since last update is longer). Large trade pulls: aggregate with jq by symbol+side, do not read raw
2. Rule-compliance sweep against the active plan: every position checked for a resting stop, size vs sleeve caps, scope (is this instrument in the plan at all), aggregate options premium vs ceiling, gross leverage vs cap
3. Verdict message: breaches listed plainly with the pending fix for each; no breach buried in prose
4. Tracker fully reconciled, so the period retrospective writes itself


## When NOT to use

- Personal (non-strategy) account questions
- Concept/teaching questions (trading-finance-tutor)
- Post-trade judgment (trade-analysis) or portfolio attribution (performance-analysis)


## Live-quote protocol (applies to every intraday exchange)

- Every quoted price carries its timestamp; if older than 5 minutes, say so
- Never dispute the trader's live tape with delayed data - re-pull and reconcile
- Order specs must be delay-robust: limits anchored to levels that are good trades regardless of a 15-minute drift, laddered exits instead of single prints
- Delayed data blocks nothing: limit orders route to the real market; the block is market orders, always


## Style rules

- Tables first, one line per position, breach stated once
- The brief is the same shape every day; deviations from the shape ARE the signal
