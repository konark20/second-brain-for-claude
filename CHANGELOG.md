# Changelog

## 1.1.0 (2026-10-01)

- First-run onboarding: a fresh vault greets the owner and starts the interview by itself (SessionStart hook in Claude Code; first-run rule in CLAUDE.md, AGENTS.md and START_HERE for every other surface).
- `99-Meta/onboarding/questions.yaml`: 21 modules, 75 questions with suggested answers, 30 role-pack questions across 9 roles. Quick, standard and deep modes.
- Resumable: progress saved after every answer in `progress.yaml`.
- Calibration exercises (tone A/B, voice A/B) and a corrected one-page portrait.
- `onboard` skill 2.0.0; new `calibrate` skill; new `/calibrate` and `/portrait` commands.
- USER_PROFILE gains thinking, working style, people, goals and growth sections.

## 1.0.0 (2026-09-30)

First public release.

- Four-layer operating charter (FOUNDATION, USER_PROFILE, BOUNDARIES, maps) as a fill-in template.
- 14 agents: navigator, architect, builder, coder, janitor, librarian, sentinel, reaper, git-sync, github-manager, researcher, skill-creator, capability-auditor, deck-builder.
- 24 vault, workflow, coding and presentation skills plus 15 portable Claude skills.
- New `onboard` skill and `/onboard` command with a 9-block interview.
- 18 slash commands for Claude Code.
- Optional packs: job-search, LinkedIn, trading (3 agents, 21 skills).
- `version:` line on every agent and skill.
- Diagrams on a light background.
- Documentation in `docs/` with diagrams, a prompt library, use cases, roadmap and a launch kit.
