---
name: tilt-guard
version: 1.0.0
trigger: Live trading sessions - fires on specific phrases and behaviors, not on schedule
inputs: The conversation itself; the tracker's loss log
outputs: One line naming the pattern, once, plus the protocol response. Never a lecture
depends_on: conviction-override (the release valve)
---

# Tilt Guard

## Purpose

A behavioural guard for live trading, drawing on Morgan Housel's The Psychology of Money. Most large losses trace to a handful of named patterns, and each pattern has a tell in the trader's own words. The guard names the pattern once, in one line, and routes to a protocol instead of an argument, because repeated risk lectures get ignored while a one-line call gets heard.


## The patterns and their tells

| Pattern | Tell | Protocol response |
|---|---|---|
| Recovery framing | "get the money back", "offset the losses" | "No trade called get-it-back. Cut list + winners list, that's the route" |
| Sunk cost | "it would be booking losses" | Decide-as-if-flat test: would you BUY this today at this price? Route to conviction-override |
| House money / goalpost moving | "we're up, we can risk it", "nothing for 2nd or 3rd" | Housel's "enough": restate the realistic target and what full-cap convexity already buys |
| Round-trip blindness | Winners unbanked at highs | Ladders at entry: bank half at target one, trail the rest |
| Structure-shopping | 3 contradictory structures on one name in an hour | "Pick one thesis or none." Same-name idea limit: 1/day |
| Story-trade sizing | Flow/insider/narrative claims on illiquid names | Point to the scorecard: story trades versus liquid directional calls. Size story trades at a quarter |


## Housel principles wired in

- Tails drive everything: one position can drive a whole period in both directions. Size so you survive to hold the tails, which is why halving often beats both flattening and holding everything
- Room for error: defined-risk structures survive mistakes; naked premium needs rescuing
- Getting wealthy versus staying wealthy: banking into strength usually beats holding for the maximum
- Reasonable beats rational: a protocol that accommodates conviction survives stress; a rule the trader abandons protects nothing


## When NOT to use

- After the pattern is named once, stop. Repetition converts signal to noise
- Not during calm, planned execution - only on the tells


## Style rules

- One line, pattern name, protocol, done. The trader knows their psychology; the job is a mirror, not a sermon
