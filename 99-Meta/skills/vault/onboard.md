---
name: onboard
version: 2.1.0
trigger: first session in a new copy (99-Meta/onboarding/progress.yaml says not_started), an interrupted interview (in_progress), USER_PROFILE still has {{placeholders}}, or the owner says /onboard, "run the onboarding interview", "redo <module>", or `/onboard migrate` in a vault that already has a profile
inputs: 99-Meta/onboarding/questions.yaml, progress.yaml, welcome.md, portrait-template.md, USER_PROFILE.md, BOUNDARIES.md, templates/project-hub.md, templates/daily.md
outputs: filled USER_PROFILE.md, owner section of BOUNDARIES.md (approved), up to five project hubs, 02-Areas/writing/voice.md (deep mode), 99-Meta/onboarding/portrait.md, PATTERN_LOG seed rows, today's journal entry, progress.yaml kept current
depends_on: daily, librarian, brief, calibrate
---

# Onboard

## Purpose

Turns a blank copy of the brain into this person's brain. It runs a conversational interview, at whatever depth and pace the owner wants, and writes what it learns into the files every later session reads first. The questions live in `99-Meta/onboarding/questions.yaml`, so adding a module or a role pack scales to every future owner without touching this procedure.

## When to use

- The first time a session opens the vault and `progress.yaml` says `not_started`. This runs before any other work unless the owner says skip.
- `progress.yaml` says `in_progress`: offer to resume at the saved question.
- The owner says /onboard, `/onboard deep`, `/onboard resume`, or "redo <module id>".

## When NOT to use

- Small profile edits. Edit the line, show the diff.
- Weekly fine-tuning after onboarding. That is [[calibrate]].
- Filling anything the owner did not say. Blank stays blank.

## How to ask (the interview style)

1. One question at a time. Never a wall of questions.
2. Offer suggestions as answer options when the question has `suggestions`:
   - If an ask-question tool with clickable options is available, use it: up to four options, `multi` when the question allows several, and the free-text "Other" is always there.
   - Otherwise list them numbered, and end with "or tell me in your own words".
   - If the owner chose "let me type freely" in welcome, skip the options unless they ask.
3. Acknowledge briefly, then move on. One short line, never flattery, never a summary of what they just said.
4. Ask the `follow_up` only when an answer is short or vague, and only once.
5. Every 4 or 5 answers, or at the end of a module, reflect back in two or three lines ("So far: you want short answers, decisions with the strongest case against, and nothing sent without you.") and ask "Anything off?"
6. Explain why only when asked, using the question's `why`.
7. Match their language and register from welcome. Questions can be rephrased; the meaning stays.
8. Read the energy. If answers get shorter, offer to stop: "Good place to pause. We've covered N of M. Say /onboard to continue."

## Calibration exercises

Some questions are exercises (`exercise:`). They teach the brain faster than descriptions.

- `tone_ab`: write the same three-line status update twice, A terse and B fuller and warmer. Ask which is closer and what to change. Record the choice and the edit.
- `voice_ab`: from the samples the owner pasted, write one paragraph in two plausible versions of their voice. Ask which is closer and why. Record the specific differences that mattered (sentence length, openers, formality, words they use or never use) in `02-Areas/writing/voice.md`.
- `portrait`: see step 9.

## Procedure

1. Read `progress.yaml`. If `not_started`, say the welcome in `99-Meta/onboarding/welcome.md`. If `in_progress`, say where you stopped ("Last time we finished 'Your hard rules'. Next is 'Current projects'. Continue?").
2. Set `mode`, `answer_style` and `language` from the welcome module. Load that mode's module list from `questions.yaml`. In deep mode, pick the role pack by `identity.role`, or ask which fits.
3. For each question: ask it, record the answer in working notes, then immediately update `progress.yaml` (`current_module`, `current_question`, `completed_modules`, `skipped`). Progress is saved after every answer, so nothing is lost if the session ends.
4. At the end of each module, draft the exact lines for its `writes_to` file and show them: "I'll add this to USER_PROFILE, section Communication: ... OK?" Write only after yes. Unapproved drafts go to `pending_writes`.
5. Rules module: BOUNDARIES is owner-edited only. Show the diff and wait for an explicit yes before writing the owner section.
6. Projects: one hub per project from `templates/project-hub.md`, five at most. Hand the new hubs to [[librarian]].
7. Recurring: write each recurring task to today's journal and one `PATTERN_LOG.md` row with shape `seed`, so skill-creator has something to count from day one.
8. Replace `{{OWNER_NAME}}` in FOUNDATION, BOUNDARIES and USER_PROFILE frontmatter once known.
9. Portrait: fill `99-Meta/onboarding/portrait-template.md` from the owner's answers only, one page, in plain words, and show it: "Here's who I think you are, from what you told me. What's wrong, missing or overstated?" Apply their corrections and save as `99-Meta/onboarding/portrait.md`. This is the most important step; people correct a portrait far more readily than they answer abstract questions.
10. First win: offer to do the task now.
11. Set `status: complete` (or leave `in_progress` with a `next_sitting_note`). Report in [[brief]] format: files written, questions skipped, modules left, first-win task.

## Privacy rules (from questions.yaml and BOUNDARIES)

- Never ask about health, religion, politics, sexuality, ethnicity or caste, immigration status, personal finances, ID or account numbers, passwords, or family matters beyond what affects the schedule.
- If the owner volunteers one of these, do not write it anywhere. Say once, kindly, that it will not be stored, and move on.
- Never label the owner with a personality type or psychological trait. Record only what they said about themselves, in their words.
- Names of other people: roles only, unless the owner asks to store names for drafting.

## Migrate mode (a vault that already has a profile)

For an existing vault, or an owner upgrading from an older template, `/onboard migrate` avoids asking what is already known.

1. Read USER_PROFILE, BOUNDARIES (owner section), project hubs, the last month of journal entries and PATTERN_LOG.
2. Map what exists to modules in `questions.yaml`. A module counts as covered when its key questions are already answered in the owner's own words. List covered, partly covered and missing modules for the owner in one short table.
3. Draft the portrait from the existing files only and show it for correction. Quote the source line for anything non-obvious.
4. Set `progress.yaml` to `mode: deep`, `status: in_progress`, with covered modules in `completed_modules`, and `migrated: <date>`.
5. Hand over to [[calibrate]] for the first round, which picks from the missing modules and from corrections visible in the journal.
6. The remaining missing modules are asked a few at a time in later calibrate rounds, never as one long interview, unless the owner asks for `/onboard deep`.

## Setting it up for someone else

If the person running the session is helping someone else onboard (a parent, a colleague), interview the owner, not the helper. Their words go into their profile. Their copy, their account, their machine.

## Style rules

- Plain, warm, short. No em dashes, no emoji.
- Use their words in the profile, not a polished paraphrase.

## Example opening

```text
Claude: Hi, I'm the brain in this folder. Right now I know nothing about you...
        How much time do you have today?
        1. Quick, about 15 minutes   2. Standard, about 45 minutes (recommended)
        3. Deep, over a few sittings 4. Just ask me a few and see
Owner:  3
Claude: Deep it is. We can stop anytime. How do you like to answer?
        1. Give me options  2. Let me type freely  3. Mix  4. I'll paste or dictate
Owner:  mix
Claude: First one. What should I call you?
        1. First name  2. Full name  3. A nickname  4. A title
        ...or tell me in your own words.
```

## Links

- [[calibrate]]
- [[USER_PROFILE]]
- [[BOUNDARIES]]
- [[daily]]
- [[librarian]]
- [[skill-creator]]
