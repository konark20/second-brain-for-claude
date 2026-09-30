---
tags: [skill, coding]
name: data-analysis-coding
version: 1.0.0
description: Use this skill whenever writing Python code for data analysis, data cleaning, data exploration, or building data pipelines and tools. Also trigger for general Python coding tasks where readability and good commenting matter, or when the user asks to process, transform, visualize, or analyze data in any format (CSV, Excel, XML, JSON, databases). Trigger for requests like "clean this data," "analyze this dataset," "write a script to parse," "plot this," "build a pipeline for," or when the user shares data and wants something done with it. This skill also applies to non-Python coding tasks where the same principles (readable, well-commented, practical) are relevant, though Python is the default. Prefers Jupyter-style structure for exploratory analysis and .py scripts for production tools.
---

# Data Analysis & Coding

This skill governs how to write code for data analysis and general coding tasks. The priority is code that another person can read, understand, and modify without needing to reverse-engineer what it does. That means inline comments on non-obvious logic, docstrings on every function, and structure that follows the shape of the problem rather than being clever for cleverness's sake.

Python is the default language. The default data analysis stack is pandas, numpy, matplotlib/seaborn, and scipy. Reach for other tools when they genuinely fit better (e.g. polars for very large datasets, plotly for interactive plots if requested), but don't switch away from the default stack without reason.

## Before writing code: the laziness ladder

Before writing any new code, run through this checklist in order and stop at the first rung that holds:

1. **Does this need to exist at all?** If the task can be solved without new code (a config change, an existing CLI tool, a one-off manual step), skip writing code entirely.
2. **Already in this codebase?** If the function, pattern, or utility already exists in the project, reuse it rather than writing a duplicate.
3. **Standard library does it?** Python's stdlib is large. `pathlib`, `csv`, `json`, `itertools`, `collections`, `datetime`, `re` — check before reaching for a third-party library.
4. **Native platform feature?** For web/UI work: use native browser features (`<input type="date">`, CSS grid) before installing a component library. For CLI: use argparse before click.
5. **Already-installed dependency handles it?** If pandas is already in the project and can do the job, don't add a new library for the same task.
6. **Can it be one line?** If the entire operation fits cleanly in one readable line, write one line, not a helper function wrapping one line.
7. **Only then: write the minimum that works.** No speculative features, no "might need this later" abstractions, no wrapper classes around simple operations.

This ladder is about the *decision* to write code, not about the code itself. Once you're past the ladder and actually writing, the rest of this skill's rules (readability, comments, structure) apply fully. The ladder prevents over-building; the other rules prevent under-documenting.

**Exception: never skip validation, error handling, or security.** The ladder cuts unnecessary code, not necessary safety. Input validation, error handling, and data checks are never "over-building."

## Jupyter vs. scripts

Pick the format based on what the task actually is:

**Jupyter-style (cell-by-cell with markdown headers between sections)** for exploratory analysis, data investigation, one-off analysis tasks, and anything where seeing intermediate results matters. Structure the notebook as a sequence of logical steps, each in its own cell, with a markdown header or brief markdown cell explaining what the next cell does before the code runs. This makes the analysis readable as a narrative, not just a wall of code.

**Python scripts (.py)** for production tools, reusable utilities, CLI scripts, parsers, pipelines, and anything meant to be run repeatedly or imported by other code. These get proper function/class structure, `if __name__ == "__main__"` blocks, and argument handling where appropriate.

If it's genuinely unclear which format fits, default to Jupyter for analysis tasks and scripts for everything else.

## Code readability

**Docstrings:** every function gets a docstring at the top explaining what it does, what it takes, and what it returns. Keep them concise but complete. For short helper functions, a one-liner docstring is fine.

**Inline comments:** comment non-obvious logic, business rules, and anything where the "why" isn't self-evident from the code. Don't comment self-explanatory lines (e.g. `# import pandas` above `import pandas` adds nothing). The test is: would someone unfamiliar with this specific task understand why this line exists? If not, comment it.

**Plotting and visualization code is an exception: comment every line.** Plot code is where tweaking happens most, and parameters like `figsize`, `rotation`, `color`, `alpha`, axis limits, and layout calls are not self-explanatory. Comment each line briefly — just enough to know what it controls and what changing it does, not a full explanation. Keep comments short and compressed (a few words, not a sentence).

**Variable naming:** use descriptive names over abbreviations. `daily_returns` not `dr`. `cleaned_orders` not `co`. The name should tell you what the variable contains without needing to trace back to where it was assigned.

**Structure:** break long operations into named steps rather than chaining everything into one unreadable expression. A 15-line pipeline split into 3 clearly-named intermediate variables is more readable than 1 giant chain, even if the chain is technically more "Pythonic."

## Shortcut techniques and efficient patterns

Use the most efficient, modern approach Claude knows rather than the safe/verbose way. This includes things like pandas method chaining, vectorized operations instead of loops, `assign()` for adding columns in a chain, `query()` for readable filtering, `pipe()` for composable transforms, and numpy broadcasting.

**The first time a shortcut or less-common pattern appears in a conversation, explain it briefly in a comment or a short note.** This is so the owner learns the technique, not just gets the output. After the first use, the technique can appear without re-explanation.

Example of a first-time explanation:
```python
# .assign() adds new columns while keeping the chain going
# — avoids breaking into separate df['new_col'] = ... lines
df = (
    df
    .assign(
        pnl=lambda x: x['exit_price'] - x['entry_price'],
        pnl_pct=lambda x: x['pnl'] / x['entry_price'] * 100
    )
    .query('pnl_pct > 0')  # .query() filters with a string expression — more readable than boolean indexing for simple conditions
)
```

After this has appeared once in the conversation, subsequent uses of `.assign()` and `.query()` don't need the explanation comment.

## Data sanity checks

After loading data and after each major transformation step, include a brief sanity check: shape and null count. Keep it lightweight, not a full profiling report.

```python
# Sanity check
print(f"Shape: {df.shape}, Nulls: {df.isnull().sum().sum()}")
```

This catches silent data loss (unexpected row drops), unexpected nulls introduced by joins or transforms, and schema changes (column count drift) early rather than at the end when the source of the problem is hard to trace back.

Don't overdo it. One line per major step is enough. Don't add a sanity check after every single operation, only after the ones that could meaningfully change the data's shape or introduce nulls (loading, merging, filtering, pivoting, filling/dropping).

## Data cleaning patterns

When cleaning data, follow a consistent order that makes the pipeline predictable:

1. **Load and inspect** (shape, dtypes, head, nulls)
2. **Fix types** (parse dates, cast numerics, handle categoricals) before any logic that depends on correct types
3. **Handle nulls** (drop, fill, or flag, depending on what makes sense for the analysis, don't just silently drop rows without noting how many were removed)
4. **Filter** (remove irrelevant rows, outliers if warranted, with the filter criteria made explicit in comments or variable names)
5. **Transform** (add computed columns, reshape, aggregate)

Each step should be a clearly separated cell (Jupyter) or a clearly named function (scripts), not all blended into one block.

## Error handling in scripts

For production scripts and tools (not Jupyter exploration), handle errors explicitly rather than letting them crash silently. At minimum: wrap file I/O in try/except with a clear error message about what went wrong (e.g. "File not found: {path}" rather than a raw traceback), validate inputs early (check that expected columns exist, that files aren't empty), and fail loudly rather than silently producing wrong output.

For Jupyter exploration, exceptions can propagate naturally since the user is watching the output cell by cell. Don't clutter exploratory code with defensive error handling that makes it harder to read.

## Editing existing code

When modifying code that the owner has already shared or that was written earlier in the conversation, don't reprint the entire script or notebook to show a change. Show only the changed section with enough surrounding context (2-3 lines) to locate where it goes, or use a diff format. If the owner pastes a 50-line script and asks to fix one line, the output should be that one fix with context, not the full 50 lines reprinted.

Similarly, don't mirror code back before answering a question about it. If they ask "what does line 12 do," answer directly rather than reprinting the file first.

The exception is when changes are extensive enough that a diff would be harder to follow than the full rewritten version (e.g. restructuring most of the script). In that case, showing the full version is fine.

## Execution policy

Claude writes the code; the owner runs it. Don't execute code against their actual files, data, or notebooks, doing so spends their compute/tokens unnecessarily when they can run it themselves in seconds.

When delivering code, include the exact command or step to run it:
- For scripts: the command line invocation (e.g. `python clean_fills.py data/orders.csv`)
- For notebooks: which cell(s) to run, in order, if it's not simply top to bottom
- Briefly note what correct output looks like (shape, key values) so the owner can confirm it worked without needing to ask

**Exception:** a tiny, isolated, self-contained snippet can be sanity-checked with placeholder/made-up values if that's genuinely useful for catching an error (e.g. confirming a regex pattern matches, or that a one-line expression evaluates correctly). This is not the same as running their actual script or processing their actual data, it's a throwaway check on a fragment, and should be used sparingly, only when it meaningfully reduces the risk of a real mistake.

## Non-Python tasks

This skill's principles (readability, comments, practical structure) apply to any language, not just Python. When writing code in other languages, follow the same standards: docstrings/comments on non-obvious logic, descriptive variable names, and structure that matches the problem. The Python-specific patterns (pandas, Jupyter, etc.) obviously don't apply, but the readability and commenting standards do.
