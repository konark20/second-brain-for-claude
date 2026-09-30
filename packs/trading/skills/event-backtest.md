---
name: event-backtest
version: 1.0.0
trigger: Any trade idea anchored to a scheduled event (earnings, CPI, FOMC, product launch) - run BEFORE the ticket is specced
inputs: Ticker, event date; broker price history (1yr daily), option chain for expected move, option volume vs average
outputs: One-page brief: reaction stats, trend/momentum state, level map, gap behavior, structure recommendation
depends_on: broker or market-data connector; payoff-check for the resulting ticket
---

# Event Backtest

## Purpose

Before trading into a known event (earnings, a data release), look at how this name actually reacted to the same event in the past and what the options market already prices, so the position is sized and placed against evidence rather than a story.


## When to use

- Earnings within the trade's holding period (check your broker's event calendar)
- Macro prints (CPI/FOMC) when sizing event-day exposure


## When NOT to use

- Undated theses (no event = nothing to backtest; that is a different, weaker trade class)


## Procedure

1. Reaction history: last 4+ same-events from daily closes. Table: day 0, day +1, day +2 returns. Classify the name: fader (pops retrace within a couple of days) or drifter (reactions tend to continue)
2. Floors and zones: the level the stock never breached post-event. Short strikes go BELOW the historical fade zone, not at the best-credit strike
3. Current state overlay: MA stack (7/15/30/100/200 order), RSI + StochRSI (a pinned oscillator into the print = reaction pre-bought, MS pattern), level-testing map (touch counts of open/close per 0.5 zone; thin-air zones move fast), gap-fill stats (does this name fill gaps or hold them)
4. Priced-in check: pre-event run-up over 5 days vs the average day-0 move. Run-up >= average reaction = halve size or trade the post-print reaction instead
5. Expected move: event-week straddle vs backtest average absolute move
6. Structure: fader + up-reaction expected = sell puts below the fade zone; drifter = debit spread held past day 0; pre-bought = wait for the day-0 dip at the first tested shelf
7. Feed the ticket through payoff-check


## Style rules

- One page, tables first, every level a number
- Per-name conclusions only - two names can react in opposite ways to similar news in the same week; never apply one name's pattern to another

