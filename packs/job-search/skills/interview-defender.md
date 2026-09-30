---
name: interview-defender
version: 1.0.0
trigger: a resume is marked materials_ready, or the owner asks for prep on a specific application
inputs: the shipped resume, its JD profile, the PROJECT_BANK boxes used
outputs: a defense sheet saved beside the resume
depends_on: PROJECT_BANK, experience archive, trading-finance-tutor or other domain skills for refreshers
---

# Interview Defender

One job: every bullet on a shipped resume gets the follow-up questions an interviewer would ask, answered from what actually happened.

## Procedure

1. For each bullet, write the 2 to 4 natural follow-ups (how did you do X, why that method, what failed, what would you change).
2. Answer each from the record, including honest limits (team project, prototype only, backtest only) and how to state them plainly.
3. Flag any bullet that cannot be defended from the record. It goes back to bullet-writer before the resume ships.
4. Add likely domain questions for the role type.
5. Save as `materials/defense_<company>_<role>.md`.

## Rule

An indefensible bullet is a shipping blocker, same force as the critic's verdict.

## Priority

Prepare first for bullets that describe work still in progress, figures from a specific configuration, and roles that were merged or simplified on the page. Those draw the sharpest questions.
