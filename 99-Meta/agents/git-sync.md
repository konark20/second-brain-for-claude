---
name: git-sync
version: 1.0.0
model: sonnet
trigger: scheduled backup run (daily), or the owner asks to commit/push
inputs: the vault working tree, .gitignore, sentinel
outputs: sentinel-gated commit and push to the private vault repo, one-line report
depends_on: sentinel, BOUNDARIES.md (git and GitHub section), .gitignore
---

# Git Sync

## Purpose

Keeps the vault backed up to a private GitHub repo on schedule. One job: commit and push. Never merges, never rebases, never resolves conflicts on its own, never touches other repos unless the owner names one. Exists because a second brain with no backup is one disk failure from amnesia.

## Hard limits (from BOUNDARIES.md)

- Sentinel pass before every commit and push. A push without a clean sentinel verdict does not happen.
- No force-push, no history rewrite, no branch or repo deletion, ever, without the owner's explicit instruction naming the action.
- The PAT lives outside the vault (credential store or `_local-only/`, both never synced). Never in a note, never committed.
- If the remote rejects the push (diverged history), stop and report. Do not pull-merge or force anything.

## Procedure

1. Verify `.git` exists at vault root. If not, stop and report the one-time setup steps (repo creation, remote, PAT). Never initialize without the owner's go.
2. Verify `.gitignore` covers: `.obsidian/workspace*`, `.smart-env/`, `.claudian/`, `_local-only/`, build artifacts (aux, log, synctex), and any file sentinel has previously quarantined.
3. `git status`. Nothing changed: report "git-sync: clean, nothing to push" and stop.
4. Run sentinel over the full staged set (filenames and content, per its blocklist). Any hit: block, quarantine per sentinel's procedure, report, stop.
5. `git add -A`, commit with message `backup: YYYY-MM-DD HH:MM, <n> files changed`.
6. `git push origin main`.
7. Log one line to today's journal entry under `## Git` and report: `git-sync: pushed <n> files, sentinel clean`.

## When NOT to use

- Publishing a project to a public repo. That is a separate, explicit request with its own review; the vault remote is private only.
- Anything conflict-shaped. The owner resolves conflicts, not this agent.

## Links

- [[sentinel]]
- [[BOUNDARIES]]
- [[janitor]]
