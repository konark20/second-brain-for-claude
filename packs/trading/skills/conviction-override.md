---
name: conviction-override
version: 1.0.0
trigger: When the trader wants to hold a position that has breached a written tripwire or falsifier
inputs: The position, the breached rule, the trader's live thesis, remaining time to expiry/deadline
outputs: A structured override - partial reduction, new hard floor, and a scorecard entry tracking both paths
depends_on: payoff-check, the tracker's falsifier log
---

# Conviction Override

## Purpose

The release valve between rules and judgment. When the rules say exit and the trader wants to hold on conviction, this skill turns the disagreement into a structured, logged decision (usually a partial exit with a defined re-check) instead of a silent rule break.


## When to use

- A written falsifier/tripwire fires and the trader says hold
- The advisor recommends exit and the trader's thesis is intact with time remaining


## When NOT to use

- Positions with no written thesis (no thesis on file means no override is available; the exit rule applies)
- Expiry day (time value is gone; override needs runway)


## Procedure

1. Test the override's standing: does a written thesis exist with a specific level and date? Is the falsifier price-based noise or thesis-based failure? (Thesis-based failure - e.g. the catalyst happened and went the wrong way - gets no override)
2. Default resolution: HALVE, don't flatten. Bank half at market, hold half on conviction
3. The kept half gets a NEW hard floor, written immediately, tighter than the original
4. The kept half gets a confirmation trigger: the observable that proves the thesis is working (for example: call volume at 3x average). Confirmation = hold with conviction; no confirmation by the deadline = the floor executes without debate
5. Log BOTH paths in the scorecard: what the full-exit was worth vs what the override produced. Over time this calibrates whose judgment wins in which regime


## Style rules

- Never relitigate an override once granted. State the floor and the trigger once, then only report "hit / not hit"
- The scorecard entry is neutral: no I-told-you-so in either direction

