# FAQ and troubleshooting

## General

**Do I need Obsidian?**
No. Obsidian is a nice way to browse the vault (backlinks, graph view, Mermaid rendering), but Claude only needs the folder.

**Do I need to know how to code?**
No. The desktop app path needs no terminal. The ticket pipeline and coding skills are there if you build things; you can ignore them otherwise.

**Does it work on Windows, macOS and Linux?**
Yes. It is Markdown. The three small Python tools in `code/` need Python 3.

**Which Claude plan do I need?**
Any plan that lets Claude read your files in the surface you choose. Claude Code needs a plan or API access that includes it. On a single-model plan, ignore the model tiers.

**Is my data sent anywhere?**
The template itself sends nothing anywhere. When you work with Claude, the files it reads go to Claude as part of the conversation, under your account's settings. Backups go only where you set them up. See [safety.md](safety.md).

**Can I use it with another AI tool?**
Yes. `AGENTS.md` gives other assistants the same rules. Use `ACTIVE_SESSION.md` if two tools write to the same folder.

## Setup problems

**Claude answered without a routing line.**
It skipped the boot. In Claude Code use `/brain <task>`. Elsewhere paste the boot prompt at the start of the conversation. You can also just say "route that through the skill map".

**Claude says USER_PROFILE has placeholders.**
You have not onboarded yet, or skipped questions. Run `/onboard`, or "redo block 2".

**Slash commands do not appear.**
They only exist in Claude Code, and only when you start `claude` from the vault root. Everywhere else, say the command in words.

**The janitor reports lots of broken links after I moved files.**
Expected. Run `/janitor`; if there are more than 20 issues it will list them and wait. Approve fixes in batches.

**Sentinel blocked my push and I think it is wrong.**
It shows false positives rather than silently passing them. Look at the file and pattern it named. If it is a false positive (a product code that looks like an ID), move on with your explicit ok, or tighten the pattern in `99-Meta/agents/sentinel.md`.

**claude.ai cannot write files.**
Correct, a browser Project cannot write to your disk. Use it for reading and drafting, and paste results into your copy, or use the desktop app or Claude Code.

## Using it well

**It keeps asking me questions.**
It asks one question when routing or scope is genuinely ambiguous. Add the four parts (goal, home, stakes, constraints) to your request and it will ask less. You can also say in onboarding Block 2 that it should make the call and flag it.

**It is too verbose.**
Tell it once in your profile ("short answers by default"). For quick lookups the compressed-response skill applies automatically; `/caveman` makes it ultra-short.

**It did something by hand that should have been a skill.**
Say "log this as a pattern". After three, skill-creator drafts it. Or ask directly: "make me a skill for this".

**How do I stop scheduled jobs quickly?**
Create an empty file at `_local-only/AUTONOMY_OFF`. Delete it to resume.

**Can it send emails or post for me?**
No, by design. It drafts; you send. This is a universal boundary.

**How big can the vault get?**
Large. The system reads only the operating files at boot and opens other notes on demand. The reaper and archive-stale keep the active folders lean.

## Contributing

**I built a great skill. How do I share it?**
Open a pull request with the skill file and a SKILL_MAP row, using fictional examples. See [CONTRIBUTING.md](../CONTRIBUTING.md).

**Can I sell workshops or services built on this?**
Yes, it is MIT licensed. Keep the licence notice.
