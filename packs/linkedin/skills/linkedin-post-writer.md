---
name: linkedin-post-writer
version: 1.0.0
trigger: the owner wants a post about something specific: a milestone, a project, a lesson, a thank-you
inputs: the topic and the one point to make, confirmed facts
outputs: one post draft in posts/<slug>.md
depends_on: professional-writing, self-correction
---

# LinkedIn Post Writer

## Procedure

1. Confirm the topic and the single point. If vague, ask.
2. Check every fact against the inventory or CORRECTIONS.
3. Pick a shape if one helps: a milestone, a specific result, a named thank-you, a plain explanation, an anecdote plus evidence.
4. Draft short by default (under about 150 words; up to about 1,300 characters for a project write-up). First person, one point, lead with a specific fact, a natural close.
5. De-slop pass and self-correction: no em dashes, no emoji, no hashtag stuffing, no corporate voice, no unconfirmed claim.
6. Save to `posts/<slug>.md` with the topic in frontmatter.
7. The owner edits and posts. The brain never posts, schedules or saves a LinkedIn draft.
