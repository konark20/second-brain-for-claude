---
name: resume-critic
version: 1.0.0
trigger: after a resume compiles and passes layout, before it is marked ready or sent
inputs: the compiled PDF, the JD, the role bundle, RESUME_RULES, resume-rating-rubric
outputs: a scored critique with blocking and non-blocking findings
depends_on: RESUME_RULES, resume-rating-rubric, ROLE_BUNDLES
constraint: READ-ONLY. This skill never edits the resume.
---

# Resume Critic (the fresh-eyes gate)

One job: judge a finished resume as a reader would, not as its author. Runs **after** [[resume-layout]] passes and **before** [[interview-defender]].

## Two hard constraints, both structural

**1. Fresh context.** This skill runs in a NEW session or a subagent that has not seen the build. It receives only: the compiled PDF, the JD, the bundle, and the rules. It does not receive the reasoning, the drafts, or the decision log.

**2. Read-only.** The critic never edits the resume, never rewrites a bullet, never recompiles. It reports. [[job-coordinator]] decides what to act on. (Pattern taken from academic-research-skills, whose reviewer agents carry the same constraint.)

> **Why both.** On 2026-09-20 the same agent that built a resume scored it 88, then 90, while its Word export was two pages with the dates broken. A builder grading itself grades generously and cannot see what it already decided to stop seeing. The fix is structural, not a reminder to be objective.

## The five readers

Score the document as each, in order. Each gets a time budget, because that is the real constraint.

| Reader | Time | Question | Fails if |
|---|---|---|---|
| **ATS parser** | instant | Does the text extract cleanly and linearly? | Headers split or missing, dates orphaned from employers, contact unparseable, any table or column |
| **Recruiter** | 10 seconds | Company names, titles, dates, school. Is this person plausibly right? | Cannot tell what they do, gaps unexplained, title buried, most relevant role not visible in the top third |
| **HR screener** | 30 seconds | Does this match the JD's stated requirements? | Named requirements absent with no adjacent evidence, keywords missing, availability unclear |
| **Hiring manager** | 2 minutes | Can this person do the job? Is any of it interesting? | Bullets are duties not outcomes, no numbers, nothing they would want to ask about |
| **Technical reviewer** | 10 minutes | Would each claim survive a question? | Any claim that cannot be traced to the record, overstated scope, a number with no source |

## Procedure

1. Extract the PDF with `pdftotext` and read only that first. If it does not make sense as linear text, the ATS reader has already failed.
2. Run each of the five passes. Write findings per reader, quoting the exact line at fault.
3. Score against [[resume-rating-rubric]].
4. Compare against the previous score for this application if one exists. **Any dimension that dropped is reported explicitly, even if the total went up.** (Score trajectory, from academic-research-skills. On 2026-09-20 a total went 88 to 90 while keyword coverage fell 15 to 14, and the drop was glossed over.)
5. Check [[CORRECTIONS]]: has any known-wrong fact been reintroduced?
6. Emit the report.

## Output shape

```
VERDICT: ship | fix-first | rebuild
SCORE: nn/100  (previous: nn, deltas per dimension)

BLOCKING
  - [reader] finding, with the offending line quoted, and which rule it breaks

NON-BLOCKING
  - [reader] finding

REGRESSIONS
  - dimension: was nn, now nn, cause

CORRECTIONS CHECK: clean | reintroduced: <fact>
```

## Anti-patterns

| Anti-pattern | Why it fails | Correct behaviour |
|---|---|---|
| Critiquing in the same session that built it | The critic inherits the builder's blind spots and its sunk cost | Fresh context, always |
| Fixing what you find | Conflates judging with building, and the fix is unreviewed | Report only; job-coordinator acts |
| Reporting only the total score | Hides per-dimension regressions | Always report deltas |
| Being generous because the build was hard | Effort is not quality | Score the artifact, not the process |
| Softening a finding after pushback | Persistence is not evidence | Hold the finding unless given new facts |

## When NOT to use

- Mid-build. It gates a finished document, not a draft.
- For content selection or wording. That is [[bullet-writer]] and [[project-organiser]].

## Links

- [[RESUME_RULES]] [[resume-rating-rubric]] [[job-coordinator]] [[resume-layout]] [[interview-defender]] [[ROLE_BUNDLES]] [[CORRECTIONS]]
