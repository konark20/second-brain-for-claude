---
name: number-miner
version: 1.0.0
trigger: a bullet lacks a number, or a new artifact (repository, notebook, report, deck) enters the record
inputs: project artifacts: result files, notebooks, CSVs, reports, decks, older resumes
outputs: verified figures added to the PROJECT_BANK box, each with its source path
depends_on: PROJECT_BANK, RESUME_RULES
---

# Number Miner

One job: dig real, defensible numbers out of artifacts so nobody has to guess.

## Procedure

1. Find result artifacts: summary CSVs, results files, executed notebook outputs, report text, dashboards.
2. Extract candidates: scale (rows, users, clients, days, dollars handled) and outcome (percent change, time saved, accuracy, revenue, error rate).
3. Record each figure in the box with its exact source and the configuration or scenario it belongs to.
4. Never combine figures from different scenarios or configurations into one claim.
5. If nothing usable exists, say so. Proposing a hypothetical number is the owner's call, never the skill's.

## Tools

- Notebooks: read the JSON and walk cell outputs for metrics.
- PDFs and reports: `pdfplumber`. CSVs: pandas.
- Older resumes: extract stated figures but mark them CONFIRM until the owner verifies.

## Rule

No project bullet ships without at least one real number. Dig the outputs, not just the README.
