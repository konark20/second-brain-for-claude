---
name: calibrate
version: 1.0.0
trigger: weekly (if the owner agreed in onboarding question rhythm.calibrate), after the owner corrects how the brain did something, or on /calibrate
inputs: USER_PROFILE.md, 99-Meta/onboarding/portrait.md, the last week of 05-Journal/, PATTERN_LOG.md, questions.yaml (skipped and optional questions)
outputs: two or three answered tuning questions, approved diffs to USER_PROFILE and portrait.md, a calibration line in the journal
depends_on: onboard, brief
---

# Calibrate

## Purpose

Onboarding captures who the owner is on day one. People change, and first answers are often guesses. Calibrate keeps the profile true with a few short questions at a time, drawn from what actually happened that week, so the brain keeps learning the person without ever needing a second long interview.

## When to use

- Weekly, inside or right after `/weekly`, if the owner agreed to tuning questions.
- Right after the owner corrects the brain ("too long", "I'd never say that", "don't ask me that again"): ask one question to turn the correction into a standing preference.
- On `/calibrate`.

## When NOT to use

- When the owner is busy or mid-task. Offer once, later.
- To re-ask a question the owner declined.

## Procedure

1. Pick at most three questions, in this order of value:
   a. A correction from this week that is not yet a standing rule ("You shortened my last three drafts by half. Should short be the default for client emails?").
   b. A contradiction between the profile and behaviour ("Your profile says reasoning first, but you've asked for the answer first four times. Switch?").
   c. A skipped or optional onboarding question from `progress.yaml` (asked gently, once).
   d. A deep-mode module not yet done, one question from it.
2. Ask one at a time, with suggested answers in the same style as onboard.
3. Show the exact diff to USER_PROFILE or portrait.md; write only after yes.
4. Log one journal line: `calibrate: <n> questions, <n> changes`.

## Style rules

- Three questions at most per run. Stop early if answers get short.
- Evidence first: say what you noticed, then ask.
- No em dashes, no emoji.

## Example

```text
Claude: Quick tune-up, two questions.
        1) Three times this week you cut my email drafts to under 80 words.
           Make that the default for emails?
           a. Yes, always  b. Only for clients  c. No, it depends
Owner:  b
Claude: Added to Communication: "Client emails under 80 words by default." 
        2) You skipped "how do you learn best" in onboarding. Want to answer now?
           a. Examples first  b. Explanations first  c. Quiz me  d. Skip for good
```

## Links

- [[onboard]]
- [[weekly-review]]
- [[USER_PROFILE]]
