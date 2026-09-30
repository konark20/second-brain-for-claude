# Launch kit

How to explain, share and grow this project. For the maintainer and for anyone who wants to spread the word. All copy below is ready to paste; edit freely.

## Positioning

**One line.** A second brain that Claude actually runs: it reads who you are, follows your rules, does the work through written procedures, and learns new skills from what you repeat.

**Who it is for.** People who already use Claude every day and are tired of re-explaining themselves: managers, consultants, professionals with clients, writers, researchers, students, developers.

**What makes it different.**
1. It is instructions, not software. No plugins, no servers, plain Markdown.
2. Visible discipline. Every reply names the agent or skill that handled it.
3. It learns you. Repeats become skills, only with your approval.
4. Safety built in. Nothing deleted, nothing sent, nothing leaks past the sentinel.
5. It survives model changes. State lives in files, so any session or model can continue.

**What it is not.** Not a note-taking app, not an autonomous agent that acts without you, not a hosted service.

## Taglines

- Stop re-briefing your AI.
- Your rules. Your memory. Claude does the work.
- A second brain that gets more like you every week.
- Fourteen specialists, one folder, zero plugins.
- It drafts. You decide.

## Launch posts

### LinkedIn

```text
For three months I ran my work through a folder of Markdown files that Claude
reads before it does anything.

It knows who I am and how I want things written. It has 14 "agents", each with
one job: one routes requests, one plans projects into tickets, one does sourced
research, one keeps the notes clean, one blocks anything with an ID number or a
password from ever leaving my machine.

The part I did not expect: it learns. Every time I do something by hand that no
skill covers, it logs it. Three times, and it drafts a new skill for me to
approve.

I've extracted the engine into an open-source template. Nine-question
onboarding, and it becomes yours, not mine.

Free, MIT licensed, works with Claude Code, the Claude app and Obsidian:
<repo link>

If you try it, tell me what your first learned skill was.
```

### X / Twitter thread

```text
1/ I open-sourced the "second brain" I run with Claude. It's not an app.
It's a folder of Markdown that tells Claude who I am, what it must never do,
and which specialist handles each request. <repo link>

2/ Every reply starts with a routing line, e.g.
"Routing: client email -> professional-writing"
so you can see it followed the system instead of improvising.

3/ Big work goes through architect -> builder -> coder tickets. The thinking
happens before the typing, and any session or model can pick up a ticket.

4/ Safety: nothing deleted (archive first), nothing sent (drafts only),
and a sentinel blocks ID numbers and keys before any push.

5/ The fun bit: repeats get logged. Three of the same shape and it drafts a
new skill for you to approve. It gets more like you each week.

6/ /onboard interviews you in 9 short blocks. MIT licensed. Diagrams, 70
prompts and worked examples in the repo.
```

### Reddit (r/ClaudeAI, r/ObsidianMD, r/PKMS)

```text
Title: I turned my Claude + Obsidian setup into an open template: 14 agents,
39 skills, an onboarding interview, and a loop that learns new skills from
what you repeat

Body: what it is (3 lines), the anatomy diagram, what's different (routing
line, drafts only, sentinel, learning loop), how to try it in 5 minutes, and
an honest "known gaps" list. Link at the end. Ask for feedback on the
onboarding questions specifically.
```

### Hacker News (Show HN)

```text
Show HN: Second Brain for Claude, an operating charter for your notes in plain Markdown

Plain text title, first comment explains: why files instead of a plugin, how
routing is made visible, how the learning loop works, what it deliberately
refuses to do, and what I'd like feedback on.
```

## Demo script (3 minutes, screen recording)

| Time | Show |
|---|---|
| 0:00 | The anatomy diagram. "This is a folder. Each part does what its brain region does." |
| 0:20 | `/onboard`, answer two questions, show the diff before it writes |
| 0:50 | `/capture` a thought, then `/inbox` and approve its home |
| 1:10 | A real request; point at the routing line |
| 1:30 | `/plan` a small tool; show the ticket file |
| 2:00 | Try to push a file with a fake ID number; sentinel blocks it |
| 2:20 | PATTERN_LOG with three rows; skill-creator's draft in proposed/ |
| 2:45 | "Use this template" button |

Record the GIF for the README from 0:50 to 1:30.

## Where to share

| Channel | Why | Notes |
|---|---|---|
| r/ClaudeAI, r/ObsidianMD, r/PKMS | Exact audience | Lead with the diagram |
| Hacker News, Show HN | Builders who like plain-text systems | Weekday morning US time |
| LinkedIn | Professionals, managers, consultants | Personal story first |
| X / Twitter | AI builders | Thread with the diagrams |
| Obsidian forum, Share and showcase | Obsidian users | Mention it needs no plugins |
| awesome lists (awesome-claude, awesome-obsidian, awesome-pkm) | Long-tail discovery | Pull request with one line |
| Workshops at work or college | Warm audience, real feedback | Use the demo script |

## Grow it

- Add GitHub topics: `claude`, `claude-code`, `second-brain`, `obsidian`, `pkm`, `ai-agents`, `prompt-engineering`, `productivity`, `markdown`, `template`.
- Pin a "Show us your first learned skill" discussion.
- Label easy issues `good first issue`: new portable skills, onboarding translations, sentinel pattern sets.
- Publish the optional skill packs one at a time; each is its own small launch.
- Write one short case study per pilot (with permission, no personal details).

## What to measure

| Metric | Where | Healthy sign |
|---|---|---|
| Template uses | GitHub insights | Rising, not just stars |
| Issues from real use | Issues | Questions about skills, not setup |
| Pull requests with new skills | PRs | At least one a month after launch |
| Pilot retention | Pilot notes | Used 3+ days a week at week 4 |

## Brand basics

- Name: Second Brain for Claude.
- Colours: amber `#f59e0b` (tools), blue `#3b82f6` (mapping), purple `#a855f7` (inner self), green `#10b981` (interface), red `#ef4444` (loop), slate `#94a3b8` (core), on navy `#0b1022`.
- Images: `assets/hero-banner.svg`, `assets/brain-anatomy.svg`, `assets/agent-departments.svg`, `assets/request-lifecycle.svg`, `assets/learning-loop.svg`.
- Say "built with and for Claude"; do not imply it is an official Anthropic project.
