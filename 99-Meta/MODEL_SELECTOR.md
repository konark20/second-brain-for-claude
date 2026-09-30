---
type: meta
layer: 2
status: active
tags: [model-selection, routing]
---

# Model Selector

> Consulted by [[navigator]] before dispatching an agent, by [[architect]] when scoping a ticket, and by [[skill-creator]] when drafting a new agent. Decides which model tier a task runs on. Keep it a living record: when you compare models on a real task, log the result below.

## Three tiers

Agent files name a tier in their `model:` line. The names are the original author's; map them to whatever models your plan offers.

| Tier in agent files | Role | Map it to |
|---|---|---|
| `sonnet` | Fast default. Routing, scoping, mechanical and well-specced work | Your fastest capable model |
| `fable` | Careful judgment. Ambiguity, research, synthesis, anything that must notice its own uncertainty | Your strongest model for reasoning |
| `opus` | High stakes. Real data, money, hard-to-undo actions, large blast radius | Your strongest model, used sparingly |

If your plan has only one model, ignore the tiers. The rule below still tells you where to slow down and double-check.

## Decision rule (apply in order, stop at the first match)

1. High stakes: real data, credentials, money, or hard to undo if wrong? Use the high-stakes tier regardless of how well specced it looks.
2. Genuinely ambiguous: something has to be interpreted, not just executed? Use the careful tier.
3. Well specced and mechanical: clear spec, clear pass or fail, bounded scope? Use the fast tier.
4. Pure routing or triage? Fast tier.
5. None of these resolve cleanly? Fast tier, and flag it to the owner. That is a sign this rule needs another data point.

## Agent roster

| Agent | Job | Default tier |
|---|---|---|
| [[navigator]] | Routes every request | sonnet |
| [[janitor]] | Session-end and weekly hygiene | sonnet |
| [[librarian]] | Tags and indexes new content | sonnet |
| [[architect]] | Goal to ordered tickets | sonnet |
| [[builder]] | Ticket to exact plan | fable |
| [[coder]] | Plan to diff | sonnet, opus on flagged tickets |
| [[researcher]] | Web research with sources | fable |
| [[skill-creator]] | Patterns to new skills and agents | fable |
| [[capability-auditor]] | Audits the toolkit as a system | fable |
| [[deck-builder]] | Slide-deck lifecycle | fable |
| [[sentinel]] | Secrets and ID firewall | sonnet |
| [[reaper]] | Archive-then-delete lifecycle | sonnet |
| [[git-sync]] | Scheduled private backup | sonnet |
| [[github-manager]] | Project repos | sonnet |

Update this table whenever skill-creator promotes a new agent.

## Evidence log

One entry per comparison. Append, never overwrite.

The original author ran three comparisons (a concept note, a bounded coding ticket, a debugging ticket). The fast tier matched the top tier on every bounded coding and debugging task. The careful tier was most likely to flag its own uncertainty on underspecified writing. That is why coder defaults to the fast tier and builder to the careful one.

| Date | Task | Tiers compared | Result |
|---|---|---|---|
