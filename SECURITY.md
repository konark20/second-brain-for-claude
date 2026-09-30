# Security and privacy

This repository is a template. Your own copy will hold personal and possibly confidential material. Treat it that way.

- Keep your own vault in a private repository or on your machine only. Never push it to a fork of this public repo.
- Never paste vault content into a public issue, discussion or pull request.
- The `sentinel` agent blocks commits and pushes that contain credentials or government ID numbers. It pattern-matches, so it can miss things. Review what you push.
- `_local-only/` is gitignored and is where sentinel quarantines anything it catches.
- If you find a way the template leaks data or bypasses a boundary, open a private security advisory on GitHub instead of a public issue.
