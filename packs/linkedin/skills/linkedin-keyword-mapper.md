---
name: linkedin-keyword-mapper
version: 1.0.0
trigger: before or after a headline or About rewrite, or whenever "will recruiters find this?" needs an answer
inputs: target-role keyword bank, linkedin-profile.md, inventory and CORRECTIONS
outputs: two lists, recommend (missing and true) and do-not-add (missing but untrue or dropped), each with a reason
depends_on: linkedin-strategist
---

# LinkedIn Keyword Mapper

## Procedure

1. Read the keyword bank for the owner's target roles (from the job-search pack's role bundles, or a list the owner gives).
2. Read the current headline, About, skills and experience in `linkedin-profile.md`.
3. List terms already present, and terms frequent in target-role postings but missing.
4. Check every missing term against the inventory and CORRECTIONS. True terms go to "recommend"; untrue or dropped ones go to "do not add" with the reason.
5. Hand both lists to the strategist, or to the bio writer mid-rewrite.

## Style

Flat list, one line of reason per term. Never pad a skill the owner does not have to hit a keyword.
