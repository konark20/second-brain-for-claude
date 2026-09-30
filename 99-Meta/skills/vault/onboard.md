---
name: onboard
version: 1.0.0
trigger: a new owner sets up their copy of the vault, USER_PROFILE still has {{placeholders}}, or the owner says "run the onboarding interview" / /onboard
inputs: 99-Meta/USER_PROFILE.md, 99-Meta/BOUNDARIES.md, docs/onboarding-interview.md, templates/project-hub.md, templates/daily.md
outputs: filled USER_PROFILE.md, owner-specific section of BOUNDARIES.md, up to five project hubs, today's journal entry, a one-screen setup summary
depends_on: daily, librarian, brief
---

# Onboard

## Purpose

Turns a blank copy of the brain into this owner's brain. Runs a short interview, writes Layer 1 from the answers, and sets up the first projects, so every later session starts from who the owner actually is instead of the original author's habits. The question bank lives in `docs/onboarding-interview.md`; this file is the procedure.

## When to use

- First session in a new copy of the vault.
- `USER_PROFILE.md` still contains `{{placeholders}}`.
- The owner's role or rules changed a lot and they want to redo a block ("redo block 4").

## When NOT to use

- Small edits to the profile. Edit the line directly and show the diff.
- To fill in answers the owner has not given. Blank stays blank.

## Procedure

1. Say what the interview is for, that it takes 30 to 45 minutes, and offer three short sittings instead of one (blocks 1 to 3, 4 to 6, 7 to 9).
2. Ask one block at a time from `docs/onboarding-interview.md`, in plain language. Accept short answers, pasted text, transcribed voice notes, or "skip".
3. After each block, show the exact lines that will be written and to which file. Write only after the owner says yes.
4. Never ask for, and never write, ID numbers, passwords, bank details or client financials. If the owner volunteers one, do not write it and say so in one line.
5. Block 4 answers go into the "Owner-specific rules" section of `BOUNDARIES.md`. Show the diff; the owner must approve it explicitly, since BOUNDARIES is owner-edited only.
6. Block 5: create one `01-Projects/<slug>/_hub.md` per project from `templates/project-hub.md`, five at most.
7. Block 6 and 9: write the recurring tasks and the "first win" into today's journal entry (create it with `daily` if missing). Add one `PATTERN_LOG.md` row per recurring task, shape `seed`, so skill-creator has something to count from day one.
8. Replace `{{OWNER_NAME}}` in FOUNDATION, BOUNDARIES and USER_PROFILE frontmatter once the name is known.
9. Hand off to [[librarian]] to index the new hubs.
10. Report in [[brief]] format: what was written where, which questions were skipped, and the first-win task to do next.

## Style rules

- One question at a time when the owner seems unsure; the whole block at once when they are answering quickly.
- Use their words in the profile, not a polished paraphrase.
- No em dashes, no emoji.

## Example

```
Onboarding
- did: profile blocks 1-3 written to USER_PROFILE, 2 questions skipped (reference material, time zone)
- did: 3 project hubs created: board-report-q4, ai-pilot-review, tax-notes
- needs: approve the 4 owner rules shown above before I write them to BOUNDARIES
- next: first win, draft this week's board update from last month's notes
```

## Links

- [[USER_PROFILE]]
- [[BOUNDARIES]]
- [[daily]]
- [[librarian]]
- [[skill-creator]]
