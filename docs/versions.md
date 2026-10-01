# Versions

Two kinds of version matter here: the version of each agent or skill file, and the Claude model each agent runs on.

## Release

| Item | Version | Date |
|---|---|---|
| Template | 1.1.0 | 2026-10-01 |
| FOUNDATION | 1.0-template | 2026-10-01 |
| Every agent and skill file | 1.0.0 (the `version:` line in its frontmatter); onboard 2.0.0, calibrate 1.0.0 | 2026-10-01 |

Versioning rule for contributors: bump the patch number (1.0.1) for wording fixes, the minor number (1.1.0) when a procedure step changes, and the major number (2.0.0) when a trigger, input or output changes, because that can change routing. Log it in [CHANGELOG.md](../CHANGELOG.md).

## Model tiers and current Claude models

Agent files name a tier in their `model:` line. This is the mapping the original vault used, with the models available as of October 2026. Your plan may differ; edit `99-Meta/MODEL_SELECTOR.md`.

| Tier name in files | Role | Model the author mapped it to | API id | If you do not have it |
|---|---|---|---|---|
| `sonnet` | Fast default: routing, scoping, mechanical and well-specced work | Claude Sonnet 5.5 | `claude-sonnet-5-5` | Any current Sonnet or Haiku |
| `fable` | Careful judgment: ambiguity, research, synthesis, noticing its own uncertainty | Claude Fable 5.1 | `claude-fable-5-1` | Claude Opus 5.5 |
| `opus` | High stakes: real data, money, irreversible actions | Claude Opus 5.5 | `claude-opus-5-5` | Your strongest available model |

Model availability changes. Check [docs.claude.com](https://docs.claude.com) for the current list before relying on an id. On a single-model plan, ignore the tiers; the decision rule in MODEL_SELECTOR still tells you where to slow down.

## Every agent

| Agent | File version | Tier | Model (author's mapping) | Where |
|---|---|---|---|---|
| navigator | 1.0.0 | sonnet | Claude Sonnet 5.5 | core |
| architect | 1.0.0 | sonnet | Claude Sonnet 5.5 | core |
| builder | 1.0.0 | fable | Claude Fable 5.1 | core |
| coder | 1.0.0 | sonnet, opus on flagged tickets | Sonnet 5.5 / Opus 5.5 | core |
| researcher | 1.0.0 | fable | Claude Fable 5.1 | core |
| librarian | 1.0.0 | sonnet | Claude Sonnet 5.5 | core |
| deck-builder | 1.0.0 | fable | Claude Fable 5.1 | core |
| janitor | 1.0.0 | sonnet | Claude Sonnet 5.5 | core |
| reaper | 1.0.0 | sonnet | Claude Sonnet 5.5 | core |
| sentinel | 1.0.0 | sonnet | Claude Sonnet 5.5 | core |
| git-sync | 1.0.0 | sonnet | Claude Sonnet 5.5 | core |
| github-manager | 1.0.0 | sonnet | Claude Sonnet 5.5 | core |
| skill-creator | 1.0.0 | fable | Claude Fable 5.1 | core |
| capability-auditor | 1.0.0 | fable | Claude Fable 5.1 | core |
| job-coordinator | 1.0.0 | fable | Claude Fable 5.1 | job-search pack |
| dossier-keeper | 1.0.0 | sonnet | Claude Sonnet 5.5 | job-search pack |
| linkedin-strategist | 1.0.0 | fable | Claude Fable 5.1 | linkedin pack |

Skills do not carry a tier; they run on whatever model the calling agent or session uses.

## Why these tiers

The author compared tiers on real tasks (a concept note, a bounded coding ticket, a debugging ticket). The fast tier matched the top tier on every well-specced coding and debugging ticket, so coder defaults to it. The careful tier was the most likely to flag its own uncertainty on underspecified writing and research, so builder, researcher and skill-creator default to it. Run your own comparison and log it in MODEL_SELECTOR's evidence table; the defaults should follow evidence, not habit.

## History of the design

| Date | Change |
|---|---|
| 2026-07-01 | Private vault bootstrapped: foundation, profile, boundaries, maps, navigator, janitor, first skills |
| 2026-07-02 | Architect, builder, coder pipeline and ticket files; first model comparisons |
| 2026-07-08 | Agent roster grows from 2 to 10, including sentinel; boundaries amended for plugins, money, ID numbers and git |
| 2026-07-16 | Researcher agent and web-research skill; trading skills promoted |
| 2026-07-22 | Job-search sub-brain; sub-brain pattern written down |
| 2026-07-28 | Reaper, autonomous-run rules and kill switch, maestro |
| 2026-09-20 | Capability auditor; punch-list and runbook-writeback; agent-builder merged into skill-creator |
| 2026-09-23 | Routing line required as the first line of every reply; LinkedIn sub-brain |
| 2026-10-01 | Public template 1.0.0: onboarding, packs, docs |
| 2026-10-01 | 1.1.0: first-run interview with modes, suggestions, resume, portrait and calibrate |
