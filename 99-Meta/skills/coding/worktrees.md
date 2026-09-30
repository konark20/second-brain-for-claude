---
name: worktrees
version: 1.0.0
trigger: a ticket needs an isolated branch to build on, or two tickets could run in parallel without colliding
inputs: the ticket id, the vault or project repo, git
outputs: an isolated git worktree on a new branch, clean test baseline verified
depends_on: 99-Meta/agents/git-sync.md, sentinel, BOUNDARIES.md
---

# Worktrees

## Purpose

Isolate each ticket's work on its own branch in its own working directory, so an in-progress build can never half-break the main tree and two tickets can run in parallel without conflict. Idea borrowed from superpowers' using-git-worktrees and claude-squad's per-task isolation, rebuilt as a documented vault skill rather than an installed tool. Pairs with [[git-sync]]: worktrees isolate the work, git-sync commits and pushes the result.

## When to use

- A ticket at `coding` will touch several files and you want the main branch untouched until review passes.
- Two tickets have no shared files and could be built at the same time.
- The owner asks to try an approach without risking the working tree.

## When NOT to use

- A one-file, one-line fix. Branch ceremony is not worth it; edit, review, commit.
- Before `.git` exists. Worktrees need a repo; stand up git-sync's first-time setup first.
- Anything that would touch real sensitive or regulated data (BOUNDARIES). Isolation does not make that allowed.

## Procedure

1. Confirm the repo has a clean status. If not, stop and report; do not stash silently.
2. Create the worktree on a new branch named for the ticket: `git worktree add ../<repo>-TICK-NNN -b tick-NNN`.
3. Run the project's test baseline in the new worktree. It must be green before any new code. If red, stop and report; do not build on a broken baseline.
4. Build the ticket there (coder does the work; this skill only sets up and tears down).
5. On review pass: merge or hand to [[git-sync]] for the sentinel-gated push, then `git worktree remove` the directory.
6. On abandon: `git worktree remove --force` and delete the branch only on the owner's say-so (no destructive git without explicit instruction, BOUNDARIES).

## Style rules

- One worktree per ticket, named for the ticket. No anonymous branches.
- Never force-remove a worktree with uncommitted changes without flagging what would be lost.
- No em dashes, no AI-sounding language.

## Links

- [[git-sync]]
- [[coder]]
- [[code-review]]
- [[BOUNDARIES]]
