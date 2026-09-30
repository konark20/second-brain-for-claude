# LinkedIn pack

A small sub-brain that keeps a LinkedIn profile accurate, findable and in your own voice. Pairs well with the job-search pack, which supplies the verified facts.

| File | Kind | Job |
|---|---|---|
| agents/linkedin-strategist.md | agent (careful) | Coordinates the nine profile components and reconciles drafts |
| skills/linkedin-keyword-mapper.md | skill | What recruiters search for that your profile is missing, and what not to add |
| skills/linkedin-bio-writer.md | skill | Headline options and an About section |
| skills/linkedin-post-writer.md | skill | One post, one point |
| skills/linkedin-photo-review.md | skill | Written feedback on a photo, never generation |
| LINKEDIN_RULES.md | rules | The pack's law |

## Install

1. Copy the agent to `99-Meta/agents/`, the skills to `99-Meta/skills/linkedin/`.
2. Create `01-Projects/linkedin/` with `linkedin-profile.md` (paste your current profile), `LINKEDIN_RULES.md`, and a `posts/` folder.
3. Register the agent and skills in `99-Meta/SKILL_MAP.md` and the agent in `MODEL_SELECTOR.md`.
4. Say: "Review my LinkedIn profile against my target roles."

Optional connection: a LinkedIn or profile-lookup connector lets the strategist read your current public profile instead of you pasting it. It never posts.
