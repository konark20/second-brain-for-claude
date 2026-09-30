---
name: runbook-writeback
version: 1.0.0
trigger: an unattended or scheduled run works around a defect in the script or procedure file it was executing
inputs: the failing step, the workaround actually used, the procedure file or script that was wrong
outputs: a diff against the procedure/script written to 99-Meta/generated/writeback/, plus one journal line naming it; never an in-place edit to an operating-layer file
depends_on: PATTERN_LOG.md, punch-list, tdd, architect, sentinel
status: active
promoted: 2026-09-20
proposed: 2026-08-02
proposed_by: skill-sweep (acting as skill-creator)
---

# Runbook Writeback

## Purpose

Scheduled runs keep hitting defects in their own instructions, working around them in-session, writing "worth baking into the procedure" in the journal, and then not baking it in. The next night's run hits the identical defect and re-derives the identical workaround.

The evidence is three sweeps deep. `GIT_SYNC.md` specifies a fixed `/tmp/vault.git` path; on 2026-07-31 that path collided with a leftover root-owned directory and the run improvised timestamped paths. On 2026-08-02 the same collision happened again and the same improvisation was made again. The stale-index mode churn (146 spurious `100755 -> 100644` entries, fixed with `git read-tree HEAD` plus `core.fileMode false`) has now been discovered and re-solved twice, and the 2026-08-02 entry says outright that it "will recur every night until the procedure in GIT_SYNC.md picks up those two steps." Earlier the same shape produced `sweep_tickets.py` silently dropping TICK-010 on a status vocabulary miss, `target.cmd` swallowing its arguments, and `herdr agent start` breaking under PowerShell 5.1.

The gap is not knowledge and it is not testing. The run already knows the exact fix, in the exact file, at the moment it works around it. What is missing is a required, bounded step that captures the fix as a reviewable diff before the session ends. [[tdd]] covers writing tests for `code/`; this covers the narrower case where a runbook or script is provably wrong and the correction is already in hand.

## When to use

- A scheduled or background run deviates from its written procedure to get past an error.
- A deterministic script in `code/` produces a wrong or silently incomplete result and the cause is identified.
- A path, flag, or status vocabulary in a procedure file does not match reality on the machine.
- A journal entry is about to contain the phrase "worth baking into", "will recur until", "worked around", or equivalent.

## When NOT to use

- The run failed for an environmental reason with no defect behind it (network down, file locked by Obsidian). Note it, do not propose a diff.
- The fix is not actually known. Then it is a [[PATTERN_LOG]] row and possibly a ticket, not a writeback.
- The file to correct is `FOUNDATION.md` or `BOUNDARIES.md`. Those are the owner-edited only. Report and stop.
- The correction is a design change rather than a defect fix. That goes to [[architect]] as a ticket.
- One-off exploratory work. This is for procedures that run again on a schedule.

## Procedure

1. Name the defect as an identity, the same convention [[punch-list]] uses: file plus defect. `GIT_SYNC.md fixed /tmp/vault.git path collides across runs`, not `git backup had a problem`.
2. Record the workaround that actually worked, verbatim, including exact commands and flags. If it was not run and verified this session, it is not a writeback.
3. Write the correction as a unified diff against the target file. Diff only, per [[USER_PROFILE]]. Never restate the whole file.
4. Save it to `99-Meta/generated/writeback/YYYY-MM-DD-<slug>.diff` with a three-line header: what broke, what fixed it, which run found it.
5. Do not apply the diff. Operating-layer procedure files and `code/` scripts change on the owner's review. The one exception is a file the run itself owns and regenerates.
6. Append or bump the matching [[punch-list]] row with owner set to whoever can apply the diff, and the writeback path in the description.
7. Append one [[PATTERN_LOG]] row only if this is a new shape. A second sighting of a defect that already has a writeback bumps the punch-list row instead.
8. In the journal, one line: `writeback: <identity> -> <path>`. Not the diff, not the narrative.
9. If the same defect gets a third writeback without the diff being applied, stop proposing and escalate: it is a ticket for [[architect]], not a nightly note.

## Style rules

- Diffs, not prose descriptions of diffs.
- Exact paths, exact commands, exact flag names.
- No adjectives about severity. The sighting count carries the weight.
- No em dashes, no emoji.
- Never claim a fix works unless this run executed it.

## Example

Before, two nights running:

```
2026-07-31 git-backup: note on the index: the first `git add -A` staged 146 spurious
  mode-only changes... Worth baking into the procedure so future runs do not commit
  mode churn.
2026-08-02 git-backup: issue: The bundle carries a stale index, so the first
  `git add -A` staged 146 mode-only changes... This will recur every night until
  the procedure in GIT_SYNC.md picks up those two steps.
```

After:

```
writeback: GIT_SYNC.md missing read-tree/fileMode guard -> 99-Meta/generated/writeback/2026-08-02-gitsync-mode-churn.diff
punch list: 1 new (owner: The owner, applies the diff)
```

with the diff itself carrying the two lines that belong in the procedure:

```diff
@@ restore step
   git clone --bare _local-only/vault-repo.bundle "$WORKDIR"
+  git -C "$WORKDIR" read-tree HEAD
+  git -C "$WORKDIR" config core.fileMode false
```

## Links

- [[PATTERN_LOG]]
- [[punch-list]]
- [[tdd]]
- [[architect]]
