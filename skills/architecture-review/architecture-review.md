---
tags: [skill, coding]
name: architecture-review
version: 1.0.0
description: Use this skill when asked to review, restructure, refactor, or improve the architecture of an existing codebase or module — requests like "can you review the structure of this project," "this code is getting messy, help me clean it up," "refactor this module," "make this more testable," or "how would you re-architect this." Applies to genuinely large or complex code (multi-file projects, modules with tangled dependencies, growing scripts that have become hard to follow), not small standalone scripts. Always runs or checks existing tests before proposing changes and again after, to verify nothing broke; if no tests exist, stop and flag this before proceeding rather than refactoring without a safety net. Works across languages (Python, and others depending on the project). Proposes specific changes for approval rather than rewriting code unprompted.
---

# Architecture Review

This skill governs how to review and propose improvements to existing code structure: thin interfaces, separation of concerns, reduced coupling, improved testability. The job is not to write new features, it's to make existing code easier to understand, change safely, and test. This only applies when the code has actually grown complex enough to need it. A 50-line script with one clear job doesn't need an architecture review, it needs maybe a few targeted comments at most. Reserve this full process for multi-file projects, modules with tangled dependencies, or code that's grown organically to the point where it's genuinely hard to follow.

## Step 1: Establish a test baseline before touching anything

Before reviewing structure or proposing any change, check whether tests exist for the code in question.

**If tests exist:** run them and record the result (pass/fail, and which ones, if any fail already before any changes are made). This is the baseline every later change gets checked against. If something is already failing before any refactor, note that clearly. It's not this skill's job to fix unrelated failures, but proceeding without knowing about them is how a refactor gets wrongly blamed for a pre-existing bug.

**If no tests exist:** stop here. Do not propose or make structural changes without a safety net. Tell the owner plainly that there's no existing test coverage for this code, and ask how they want to proceed. The most common good options are: write a minimal set of tests covering current behavior first (treat this as a quick, separate sub-task), or proceed without tests but with explicit acknowledgment that changes can't be automatically verified and will need manual checking. Don't pick one of these unilaterally, since the right tradeoff (time available vs. risk tolerance) is their call, not a default to assume.

**Override:** if the owner says up front to skip the test check (e.g. "don't worry about tests," "just go ahead without tests," "skip the test step"), respect that for the rest of the conversation without asking again. The default is to stop and ask, but once they're told you to proceed without tests, don't re-ask on subsequent reviews in the same session.

## Step 2: Understand before restructuring

Read enough of the codebase to understand why it's shaped the way it currently is before proposing changes. Code that looks messy from a glance sometimes has a reason (a workaround for an external constraint, a deliberate tradeoff made under time pressure). The goal here is genuine understanding, not a surface pass: trace how the main pieces depend on each other, notice where responsibilities overlap or where one module is doing several unrelated jobs, and notice where interfaces between components are wide (lots of shared state, deep knowledge of internals) versus thin (a clean, small contract).

This step produces the actual findings. Useful things to look for and note:
- **Tangled dependencies** — modules that know too much about each other's internals, making changes in one place ripple unpredictably elsewhere
- **Mixed responsibilities** — a single function, class, or file doing several unrelated jobs, making it hard to test or change one without affecting the other
- **Untestable seams** — code that's hard to test in isolation because it's tightly coupled to I/O, global state, or another module, rather than having a clean interface that could be tested with simple inputs
- **Duplicated logic** — the same pattern reimplemented in multiple places, suggesting a shared abstraction is missing

## Step 3: Propose specific changes, don't just rewrite

Once the findings are clear, propose concrete refactors for approval rather than silently rewriting the code. For each proposed change, state: what the change is, why it addresses a specific finding from Step 2 (not just "this is cleaner," tie it to the actual problem), and what risk or tradeoff it carries (a bigger restructure carries more risk of subtle breakage than a small one, and that's worth surfacing explicitly rather than presenting every change as equally safe).

Order proposals from lowest-risk/highest-value to highest-risk, so the easy, clearly-beneficial changes can be approved and made first, and the more invasive ones (or ones that touch a lot of surface area) get a clear separate decision point rather than being bundled in with everything else.

Wait for approval before implementing. This skill proposes; it doesn't assume approval and start rewriting on its own.

## Step 4: Implement approved changes incrementally

Make approved changes one at a time rather than all at once, where practical. After each change (or each small batch of related changes), re-run the tests from Step 1 and compare to the baseline. If something that passed before now fails, stop and fix or revert that specific change before moving to the next one, rather than continuing to stack changes on top of a broken state.

If no tests exist and the owner chose to proceed without them anyway (per Step 1), be explicit at each step about what was changed and what would need manual verification, since there's no automated way to confirm correctness here.

## Step 5: Summarize what changed and why

After implementing, give a short summary: what was restructured, what specifically improved (testability, reduced coupling, removed duplication), and the test results before and after. This is the record of what happened and why, useful both for the owner's own understanding and for anyone else who later looks at the diff and wonders why it was done this way.
