---
tags: [skill, coding]
name: context-management
version: 1.0.0
description: Use this skill when working with a large or unfamiliar codebase where loading everything into context at once would be wasteful or impossible. Trigger this for requests like "help me understand this repo," "look through this project," "find where X is implemented," "navigate this codebase," or any task that requires exploring a multi-file project incrementally rather than reading it all upfront. Also trigger when a task on a large project is about to start (a bug fix, feature addition, or review) and understanding the relevant parts of the codebase is a prerequisite. Applies to any language. This skill governs how to explore, not what to build, so it works alongside other skills (architecture-review, TDD, data-analysis-coding) rather than replacing them.
---

# Context Management

This skill governs how to navigate and build understanding of a large codebase incrementally, without loading everything into memory at once. The core problem it solves: dumping an entire repo into context wastes tokens on irrelevant files, hits context limits on big projects, and makes it harder to reason clearly about the parts that actually matter. Instead, explore selectively, track what you've already read, and only pull in what's needed for the current question.

This applies to any language and any repo size where reading everything upfront would be wasteful. For small projects (a handful of files, a few hundred lines total), this overhead isn't worth it, just read the files directly.

## Step 1: Start with the directory tree

When dropped into an unfamiliar repo, the first move is always to get the directory tree structure (typically 2 levels deep) to understand how the project is organized. Don't read any files yet. The tree tells you where to look; individual files tell you what's there.

From the tree, identify:
- **Entry points** (main files, app entry, CLI scripts, test runners)
- **Configuration** (package.json, pyproject.toml, requirements.txt, Makefile, Dockerfile, etc.) to understand dependencies, build process, and project conventions
- **Directory groupings** that suggest architecture (src/, tests/, lib/, utils/, models/, routes/, etc.)

Read the README if one exists, since it's usually the cheapest way to get project-level context (what the project does, how it's structured, how to run it).

## Step 2: Navigate by relevance, not by order

Don't read files sequentially or exhaustively. Navigate based on what the current task actually needs. If the task is "fix the order parser," trace from the entry point to the parsing code and read only the files in that path, not every module in the project.

At each step, ask: "Do I have enough context to answer the current question or complete the current task?" If yes, stop reading. If no, identify the specific gap (a function that's imported but not yet read, a config value that's referenced but not yet seen) and read just that file or section.

For very large files (500+ lines), read strategically rather than dumping the whole file: check the top-level structure first (class names, function signatures, imports), then read the specific section that's relevant. Most of a large file is usually irrelevant to any single task.

## Step 3: Maintain a running context map

As files are read, keep a running mental index of what's been explored. For each file that's been read, track:

- **Filename and path**
- **Purpose** (one line: what this file is responsible for)
- **Key functions/classes** (the important exports or entry points, not every helper)
- **Dependencies** (what it imports from other files in the project, and what imports it)

This index serves two purposes: it prevents re-reading files that have already been explored (if you need to recall what a file does, check the index first rather than reading the file again), and it builds a picture of how the codebase fits together (which modules depend on which) that grows incrementally as more files are visited.

Don't dump the full index into every response. Reference it when relevant (e.g. "I've already seen that the parser module depends on the schema definitions in models/schema.py") and use it internally to decide what to read next. If the owner asks "what have you looked at so far," surface the full index at that point.

## Navigation patterns

Different tasks call for different navigation strategies. Pick the one that fits:

**Tracing a feature or bug:** Start from where the symptom appears (the error, the broken output, the entry point the user mentions) and trace backward through the call chain: what calls this function, where does this data come from, what config controls this behavior. Read files along that chain only.

**Understanding overall architecture:** Start from entry points and configuration, then read one representative file from each major directory/module to understand the pattern. Don't read every file in a module if the first two follow the same structure, note the pattern and move on.

**Finding where something is implemented:** Use grep/search first rather than reading files one by one. A targeted search for a function name, class name, or string literal is almost always faster than sequential file reading. Once the search narrows the location, read just that file.

**Preparing for a change:** Identify the file(s) that will need to change, then read their direct dependencies (imports and importers) to understand what might break. The context map's dependency tracking is specifically useful here since it shows the blast radius of a change without re-reading everything.

## What not to do

- **Don't read the entire repo upfront.** This is the single most common failure mode. Even if it seems faster, it wastes context on files that turn out to be irrelevant and makes reasoning harder by flooding working memory.
- **Don't re-read files already in the context map.** Check the map first. If the summary is insufficient for the current question, re-read selectively (a specific function, not the whole file).
- **Don't read test files unless the task involves tests.** Test directories are often the largest part of a repo. Skip them unless the task specifically requires understanding or running tests.
- **Don't read generated files, build artifacts, or vendored dependencies.** node_modules/, dist/, build/, .git/, __pycache__/, lock files, etc. are noise. Skip them during tree exploration and never read them unless explicitly asked to.
