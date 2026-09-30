---
name: payoff-check
version: 1.0.0
trigger: Before ANY option order is placed or specced, no exceptions
inputs: The proposed legs, the trader's own stated forecast (price and date)
outputs: One-line verdict - payoff at the trader's forecast, flagged if negative
depends_on: nothing (pure arithmetic)
---

# Payoff Check

## Purpose

The cheapest safeguard in trading: before any option order, compute the position's P&L at the trader's own forecast. Structures wired to lose at the trader's own target are common and expensive, and one question catches them.


## When to use

- Every option ticket, before transmission. Single leg or multi-leg.


## When NOT to use

- Never skip it. Thirty seconds. It has paid five figures per week.


## Procedure

1. Write down the trader's forecast as a number and a date ("XYZ at 93 by Friday", "ABC pulls back to 380 this week")
2. Compute the position P&L at exactly that price on that date (intrinsic values, premium in/out, multiplier x100)
3. If P&L at the forecast is negative or near-zero: STOP. The legs are inverted or the structure fights the thesis. Say: "at your own target this loses $X"
4. Also compute P&L at: current price unchanged (theta cost of being wrong about timing) and the falsifier level (defined worst case)
5. Only then discuss sizing


## Style rules

- The check is one table row: forecast price | P&L there | flat P&L | worst case
- Multiplier stated explicitly: contracts x 100 shares. A "$3,400 max loss" that is actually $34,000 has happened

