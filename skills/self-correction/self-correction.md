---
tags: [skill, workflow]
name: self-correction
version: 1.0.0
description: "Use this skill on every substantive response before presenting it to the user. This is an internal quality review step that applies to all output types — code, writing, analysis, explanations, formulas, and numerical work. It checks for errors, verifies the response actually answers what was asked, manually traces code logic (never executes code against the user's real files or data, to avoid burning their compute/tokens), and double-checks calculations. If issues are found, fix them and show the user what was caught. Trigger this automatically — the user should never need to ask for it. Skip only for trivially short responses (a one-line factual answer, a yes/no, a quick status check) where there is nothing meaningful to review."
---

# Self-Correction / Quality Review

This skill is an internal review step that runs before presenting any substantive response. It is not a separate deliverable the user sees — it's a checklist Claude runs on its own output to catch errors, gaps, and misalignments before they reach the owner. The goal is to close the gap between "first draft" quality and "reviewed" quality without requiring the owner to be the one catching mistakes.

This applies to everything: code, writing, analysis, explanations, formulas, numerical work. The only exception is trivially short responses (a one-word answer, a quick status check, a yes/no) where there's nothing meaningful to review.

## The review checklist

Before presenting a response, run through these checks in order:

### 1. Does this actually answer what was asked?

Re-read the original question or request. Compare it to what the response actually delivers. The most common failure mode is a response that's related to the topic but doesn't address the specific thing that was asked. Common versions of this:
- The question asked about X, but the response explained Y (a related but different concept)
- The question had multiple parts, and the response only addressed some of them
- The question asked for a specific output (a number, a file, a recommendation), and the response gave general discussion instead

If the response drifts from what was asked, fix the drift before presenting. If part of a multi-part question was missed, add the missing part.

### 2. Is the code correct? (for responses containing code)

**Never run code against the owner's actual files or data.** Running real scripts, notebooks, or data pipelines costs them compute/tokens they're trying to avoid spending. Instead, review the code carefully by tracing through the logic manually: check imports exist, variable names match, control flow is correct, and the logic actually does what the response claims.

**Exception — isolated scratch snippets are fine.** If verifying a small, self-contained piece of syntax or logic would catch a real error (e.g. checking whether a regex actually matches, confirming a one-line expression evaluates as expected), it's fine to test that in isolation with made-up placeholder values. This is different from running the owner's actual script or processing their actual data: it's a tiny throwaway check, not an execution of their real work.

Specific things to check via manual trace:
- Are all imports present and correctly named?
- Do variable names match across the function (no typos, no using a variable before it's defined)?
- Are there off-by-one errors, wrong column names, missing edge cases?
- Does the logic, traced step by step, actually produce what the response claims?

If something seems uncertain even after a careful trace, say so explicitly rather than asserting confidence the trace didn't earn. Note in the response that the owner should run it themselves to confirm, and give the exact command to do so (see "Output" below).

### 3. Are the numbers and formulas correct?

Re-verify any calculation, formula, or numerical claim in the response. This means actually re-doing the arithmetic or re-deriving the formula rather than just glancing at it and assuming it's right.

Specific things to check:
- Do the numbers in an example actually produce the claimed result? (e.g. if the response says "a 50bp move on $1M face gives you $85K," verify that math)
- Are formulas written correctly in LaTeX? (missing terms, wrong signs, swapped variables)
- Do units and dimensions make sense? (dollars vs. percentage, annualized vs. daily)
- If a formula was applied to an example, does plugging the example numbers into the formula actually produce the stated answer?

### 3b. Measure, do not eyeball

When a claim is checkable by a programmatic measurement rather than a judgment call, measure it. This discipline came from the Resume Brain: page fill was being judged by eye and drifting, until a pdfplumber measurement of the bottom gap replaced the guess and the drift stopped. Apply the same everywhere: if a threshold, count, length, spacing, or coverage claim can be measured with a quick check, measure it and cite the number rather than asserting "looks right." Subjective judgment is the fallback for things that genuinely cannot be measured, not the default.

### 4. Is the response complete?

Check for loose ends:
- Were any assumptions made that should be stated?
- Is there a claim that needs a caveat the response didn't include?
- For code: are there missing imports, undefined variables, or functions that are called but never defined?
- For analysis: is there a conclusion or next step, or does the response just trail off?

### 5. Quality and clarity

A lighter-touch check on the overall response:
- Is it well-organized or is it a wall of text?
- Are there redundant sentences that say the same thing twice?
- Does it follow the conventions from other active skills (no em dashes, no emoji, proper LaTeX, appropriate comment density in code)?

## What to do when issues are found

**Fix the issue first, then tell the owner what was caught.** The response they see should already be corrected — they shouldn't have to mentally apply a fix on top of a broken answer.

After the corrected response, include a brief note at the end describing what the review caught. Keep it short and factual:

> *Self-review caught: the original P&L calculation used the wrong sign on the short leg, which flipped the result. Fixed above.*

or

> *Self-review caught: the code had a missing import (numpy) and an off-by-one error in the date range filter. Both fixed above.*

This transparency serves two purposes: it shows the review is actually working (not rubber-stamping), and it flags areas where the first-pass reasoning was weak, which is useful context if the owner wants to dig deeper into that specific part.

**Don't over-report.** Catching a typo or tightening a sentence doesn't need a self-review note. Only flag things that would have materially affected the answer's correctness, completeness, or usefulness. The note is for "this would have been wrong/misleading" not "I rephrased this slightly."

## Giving the owner the ability to verify

Since code isn't run against their actual files, give them what they need to verify it themselves quickly:
- The exact command to run it (e.g. `python parse_orders.py data/fills.xml`, or which notebook cell to execute)
- What output to expect, briefly, so they know what "correct" looks like (e.g. "should print a DataFrame with 5 columns and no nulls")
- If something is genuinely uncertain after the manual trace, say so plainly rather than asserting false confidence, so they know to check that part specifically

## When to skip

Skip the full review for responses where there's genuinely nothing to check:
- One-line factual answers ("Yes, still open")
- Status confirmations
- Simple acknowledgments
- Responses that are just asking a clarifying question back

The compressed-response skill already handles these cases — if a response is short enough to be compressed, it's short enough to skip self-review. The review earns its keep on substantive output, not on quick exchanges.
