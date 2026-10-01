"""Print a first-run or resume notice for Claude at session start.

Wired as a Claude Code SessionStart hook in .claude/settings.json. Whatever this
prints is added to the session's context, so a brand-new vault always opens
with the onboarding welcome, and an interrupted interview offers to resume.
Standard library only; safe to run anywhere; prints nothing once onboarding is complete.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
PROGRESS = ROOT / "99-Meta" / "onboarding" / "progress.yaml"


def field(text, name):
    match = re.search(rf"^{name}:\s*(\S+)", text, re.M)
    return match.group(1) if match else ""


def main():
    if not PROGRESS.exists():
        return
    text = PROGRESS.read_text(encoding="utf-8")
    status = field(text, "status")
    if status == "not_started":
        print("FIRST RUN: this vault has not been onboarded. Before any other work, "
              "follow 99-Meta/skills/vault/onboard.md and greet the owner with "
              "99-Meta/onboarding/welcome.md, unless they ask to skip.")
    elif status == "in_progress":
        module = field(text, "current_module")
        print(f"ONBOARDING IN PROGRESS: stopped at module '{module}'. At a natural moment, "
              "offer to resume with /onboard resume (see 99-Meta/onboarding/progress.yaml).")


if __name__ == "__main__":
    main()
