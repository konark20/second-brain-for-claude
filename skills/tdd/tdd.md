---
tags: [skill, coding]
name: tdd
version: 1.0.0
description: "Use this skill when writing important or complex code that benefits from test-driven development — writing tests before implementation. Trigger for requests like 'build this with tests,' 'write tests first,' 'TDD this,' or when the code being written is substantial enough that tests add real value (parsers, pipelines, business logic, algorithms, anything with multiple code paths or edge cases). Do NOT trigger for quick scripts, one-off data exploration, Jupyter notebooks, or simple utilities where TDD overhead isn't worth it. Uses pytest or unittest for Python (whichever fits better); matches whatever the project already uses for other languages."
---

# Test-Driven Development (TDD)

This skill enforces a test-first workflow for substantial code: write the tests that define correct behavior, then write the implementation that passes them, then refactor with confidence. The value of TDD is that it forces clear thinking about what the code should actually do before writing it, catches regressions immediately, and produces code that is testable by construction rather than tested as an afterthought.

This applies to important or complex code only. Quick scripts, one-off analysis, Jupyter exploration, and simple utilities don't need TDD — the overhead isn't worth it for code that's throwaway or trivially verifiable by eye. If it's unclear whether a task is "substantial enough," a good heuristic: if the code has multiple branches, handles different input shapes, or would be painful to debug if it silently produced wrong output, TDD is worth it.

## Framework

**Python:** pytest is the default for its simplicity, but unittest is fine too — use whichever fits the project or the test structure better. pytest for flat, function-based tests; unittest when class-based grouping or setUp/tearDown makes the tests cleaner. Don't mix both in the same project.

**Other languages:** match whatever the project already uses. If starting fresh in a non-Python language and nothing is established, ask which framework to use rather than picking one.

## The workflow

### Step 1: Understand what the code should do

Before writing any tests or implementation, be clear on the requirements: what inputs does this code take, what outputs should it produce, and what are the important behaviors (not just the happy path). This understanding drives what tests to write. If the requirements are ambiguous, ask before writing tests against the wrong specification.

### Step 2: Write all tests for the function/feature first

Write the full set of tests for a function or feature before writing any implementation. This means the tests define the contract: what correct behavior looks like across the relevant cases.

**For simple functions (clear input/output, minimal branching):** happy path tests are enough. Don't manufacture edge cases for a function that adds two numbers.

**For complex logic (multiple code paths, error handling, boundary conditions):** focus on the main paths and critical fields — the things where a silent failure would produce wrong results downstream. Cover the cases that actually matter for correctness, not every theoretical permutation:
- The main success path works and produces correct values in the fields that matter
- Critical fields (price, quantity, side, IDs) are present and correctly typed
- Obvious failure modes that would cause real problems (missing required data, malformed input, empty input)

Name tests descriptively so they read as a specification:
```python
def test_parse_order_returns_correct_fields_for_tt_format():
    ...

def test_parse_order_raises_on_missing_price_field():
    ...

def test_parse_order_handles_empty_xml_gracefully():
    ...
```

At this point, all tests should fail (red) because no implementation exists yet. Don't run them yet — tests are run only when the owner asks or at the end.

### Step 3: Implement to pass the tests

Write the minimum implementation that makes the tests pass. Resist the urge to build extra features, optimizations, or abstractions that no test is asking for. If the tests pass, the implementation is sufficient for now. Additional capability gets added by writing additional tests first, then implementing.

Keep the implementation clean and readable (per the data-analysis-coding skill's standards: docstrings, inline comments on non-obvious logic, descriptive variable names), but don't gold-plate it before confirming the tests actually pass.

### Step 4: Refactor

Once tests pass, look for opportunities to clean up the implementation without changing behavior:
- Extract repeated logic into helper functions
- Rename variables for clarity
- Simplify conditional chains
- Remove dead code

The tests are your safety net here: if a refactor breaks something, the tests catch it. This is the whole reason for writing tests first.

### Step 5: Give the owner what they need to run tests themselves

Claude does not execute tests against the owner's actual project, running code costs them compute/tokens they're trying to avoid spending. Instead, once tests and implementation are written, give them the exact command to run them themselves:

```
pytest tests/parsers/test_tt_parser.py -v
```

or for unittest:
```
python -m unittest tests.parsers.test_tt_parser -v
```

Briefly note what passing output should look like (e.g. "all 5 tests should pass") so they can tell at a glance whether something's wrong. If they report a failure back, debug from the error message and traceback they share, rather than re-running anything directly.

**Exception:** a tiny isolated snippet (not the actual test suite or project files) can be sanity-checked directly if it meaningfully reduces the risk of a real mistake, e.g. confirming a regex or one-line expression behaves as expected. This is a throwaway check on a fragment, not running the owner's real tests.

## Test organization

Keep test files alongside or mirroring the source structure:
```
src/
    parsers/
        tt_parser.py
tests/
    parsers/
        test_tt_parser.py
```

One test file per source file. Test functions grouped logically (all tests for one function together, in the order: happy path first, then edge cases, then error cases).

## What to avoid

- **Don't write implementation first and tests after.** That's not TDD, it's retroactive testing. The test-first order is the point — it forces the interface design to happen before the implementation, which produces cleaner APIs.
- **Don't write tests that test implementation details.** Test behavior (given this input, expect this output) not internals (this private method was called 3 times). Implementation-detail tests break on every refactor and provide no real safety.
- **Don't skip the refactor step.** The first implementation that passes the tests is often messy. The refactor step with passing tests as a safety net is where code quality improves. Skipping it accumulates tech debt.
- **Don't over-test simple code.** A function that returns `a + b` doesn't need 10 test cases. Scale test coverage to the complexity and risk of the code.
