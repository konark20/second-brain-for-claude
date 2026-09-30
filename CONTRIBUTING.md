# Contributing

Thanks for wanting to make this better. The project is Markdown instructions plus a few small Python scripts, so most contributions are writing, not code.

## Good first contributions

- A new portable skill in `skills/<name>/<name>.md` that is useful to people outside your own job.
- A clearer procedure in an existing agent or skill, with a short note on what went wrong without it.
- A new onboarding question that would have saved you time, in `docs/onboarding-interview.md`.
- A worked example in `examples/` (fictional people and companies only).
- Translations of the docs.

## Rules for every pull request

1. Never include content from your own vault: no journal lines, project notes, client names, profile answers. Use made-up examples.
2. Follow the skill format in `99-Meta/FOUNDATION.md` section 3. One skill, one job.
3. Add a row to `99-Meta/SKILL_MAP.md` and `99-Meta/SKILL_INDEX.md` for anything new, or it does not exist.
4. No em dashes, no emoji, plain language. Read `skills/professional-writing/professional-writing.md` for the style.
5. Do not loosen the universal section of `99-Meta/BOUNDARIES.md`. Tightening it is welcome.
6. Run a secrets scan before you push (`/sentinel`, or `grep -rE "api[_-]?key|token|secret" .`).

## Proposing a bigger change

Open an issue first describing the problem, the proposed change, and which layer it touches (profile, mapping, tools, interface, loop). Changes to FOUNDATION or BOUNDARIES need discussion before a PR.
