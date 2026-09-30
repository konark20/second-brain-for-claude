---
tags: [skill, workflow]
name: project-planner
version: 1.0.0
description: "Use this skill when planning, scoping, or designing something that doesn't exist yet — a new coding project, an AI agent, a model, a skill set, a pipeline, or a tool. Trigger for 'I want to build,' 'help me plan,' 'how should I architect,' 'what would I need to build X,' 'design an agent that,' 'scope this out,' or any request where the goal is to figure out what to build and how before writing any code. This skill is the thinking-before-building step. It walks through the design conversationally, then produces a structured YAML plan that feeds directly into development (compatible with HANDOFF.yaml). Does not write implementation code — that's for the coding and TDD skills once the plan is approved."
---

# Project Planner

This skill helps plan and architect something that doesn't exist yet. It covers any kind of project: a coding tool, a data pipeline, a trading strategy implementation, an AI agent with specific capabilities, a new set of skills for Claude, or a full system with multiple moving parts. The key distinction from other skills: this one produces a *plan*, not code. Implementation happens after the plan is approved, using the appropriate coding/TDD/architecture skills.

The workflow is conversational first, structured output second. Talk through the design with the owner to make sure the scope, architecture, and task breakdown are right before committing to a plan document. A plan that's wrong is worse than no plan, so the conversation matters more than the document.

## Step 1: Understand the goal

Before decomposing anything, get clear on what this project actually needs to accomplish. Ask the owner directly if any of these are unclear:

- **What does it do?** The core capability in one or two sentences. "An agent that calibrates SVI models to market vol surfaces" is clear. "Something for options" is not.
- **Who/what uses it?** Is this for the owner personally, for a team, for another agent to consume, or for production use? This changes the quality bar and the architecture.
- **What does success look like?** What's the minimum version that's actually useful? This prevents scope creep by establishing a clear "done" criteria before the plan expands.

Don't skip this step even if the goal seems obvious. Restating it back to the owner in concrete terms catches misalignments early.

## Step 2: Decompose into capabilities

Break the goal into the concrete capabilities the project needs. Each capability is a thing the project must be able to *do*, not a component or file name.

Example for an SVI calibration agent:
- Read and parse a vol surface from market data (option chain with strikes, expiries, mid-IVs)
- Fit SVI parameters to each expiry slice
- Validate the fit (no-arbitrage constraints, goodness-of-fit metrics)
- Visualize the fitted surface vs. market data
- Report parameter values and fit quality in a structured output
- Persist calibration results for later comparison

Each capability becomes a building block that maps to one or more implementation tasks later. Order them by dependency (you can't validate a fit before you can produce one).

## Step 3: Inventory what already exists

Before planning new work, actively check what's already available rather than relying on memory alone:

- **Search past conversations:** use conversation_search to find related past work. The owner has worked on many projects across sessions (trading strategies, data pipelines, coursework, skill building) and may not remember to mention all relevant prior work. Search for keywords related to the current project before asking them to list everything manually.
- **Existing skills:** which of the owner's current skills cover parts of this? Map capabilities from Step 2 to skills that already handle them.
- **Existing code:** has the owner already built anything related? Check both Claude.ai history and ask about Claude Code / VS Code sessions (those are separate and can't be searched from here, so ask explicitly).
- **Available tools and connectors:** MCP connectors (Gmail for email, Claude in Chrome for browser automation), libraries, APIs that could be wired in rather than built from scratch. Use tool_search to check what's actually available rather than guessing.
- **External resources:** papers, documentation, reference implementations that inform the design.

The point is to avoid building what already exists. Map each capability from Step 2 to either "already have this" or "need to build this."

## Step 4: Architecture decisions

For each capability that needs building, work through the key design decisions conversationally. These are the choices that are expensive to change later:

- **Data flow:** where does data come from, how does it move through the system, where does output go?
- **Component boundaries:** what are the distinct modules/pieces, and what's the interface between them? Thin interfaces (clear inputs/outputs, minimal shared state) are almost always better than tightly coupled components.
- **Technology choices:** what language, libraries, frameworks? Default to the owner's standard stack (Python, pandas/numpy/scipy/matplotlib) unless there's a reason not to.
- **Agent-specific decisions (if building an agent):** what skills does it need, what tools/connectors, what's its system prompt, how does it interact with users or other agents?
- **Skill-set decisions (if designing skills):** how many skills, what triggers each one, where do they overlap, how do they interact?

Surface tradeoffs explicitly. "We could do X (simpler, less flexible) or Y (more complex, handles edge cases). X is probably fine for v1." Let the owner make the call rather than choosing silently.

## Step 5: Task breakdown

Once the architecture is agreed, decompose into concrete, ordered tasks. Each task should be:

- **Specific enough to act on.** "Build the SVI parameter fitting function using scipy.optimize.minimize with the SLSQP method" not "implement fitting."
- **Ordered by dependency.** Tasks that produce inputs for other tasks come first.
- **Estimated roughly.** Not time estimates (those are usually wrong), but complexity: small (a function, an hour of work), medium (a module, a session), large (a multi-session effort).
- **Assigned to a skill.** Which of the owner's skills governs how this task gets implemented? (e.g. data-analysis-coding for data pipeline tasks, tdd for core logic, architecture-review if restructuring existing code)

## Step 6: Produce the plan document

After the conversational walkthrough is done and the plan is agreed, produce a structured YAML document. This is the artifact that gets saved and used to drive implementation. It's designed to be compatible with `HANDOFF.yaml` so it can evolve into a handoff file once implementation starts.

```yaml
project_plan:
  name: <project name>
  purpose: <what it does and why, 1-2 sentences>
  created: <date>
  status: planned
  success_criteria: <what "done" looks like for v1>

capabilities:
  - name: <capability name>
    description: <what it does>
    status: <planned | have_already | in_progress>
    depends_on: <other capabilities this requires>

architecture:
  overview: <prose summary of how the pieces fit together>
  components:
    - name: <component/module name>
      role: <what it's responsible for>
      interfaces: <what it takes in, what it produces>
      technology: <language, key libraries>
  data_flow: <how data moves through the system, source to output>
  decisions:
    - decision: <what was decided>
      reason: <why, alternatives considered>

existing_resources:
  skills: <which existing skills apply>
  code: <any existing code to reuse or build on>
  tools: <MCP connectors, APIs, libraries>
  references: <papers, docs, repos to reference>

tasks:
  - task: <concrete action>
    capability: <which capability this serves>
    skill: <which skill governs implementation>
    complexity: <small | medium | large>
    depends_on: <other tasks that must be done first>
    notes: <any gotchas, context, or specific approach>
  # ordered by execution sequence

open_questions:
  - <anything unresolved that needs answering before or during implementation>
```

Save this as `PROJECT_PLAN.yaml` in the project root. This file is only for multi-session building projects (coding, agent development, system design), not for regular chats or one-off questions.

**Lifecycle:** PROJECT_PLAN.yaml is the "before" document (what to build). Once implementation begins, it evolves into `HANDOFF.yaml` (what's been built) by adding `current_state`, `error_log`, and `changelog` sections as work progresses. The project-handoff skill governs that transition. Don't maintain both files separately once implementation starts — merge the plan into the handoff file so there's one source of truth, not two competing documents.

## What to avoid

- **Don't plan in the abstract.** Every capability, component, and task should be concrete enough that someone (or an agent) could start working on it without asking clarifying questions. "Handle edge cases" is not a task.
- **Don't over-plan.** A plan for a small tool (one script, one purpose) shouldn't have 20 tasks and an architecture diagram. Scale the plan to the project's actual complexity.
- **Don't write implementation code in this skill.** The plan says *what* to build and *how the pieces fit*. Actual code is written using the coding/TDD skills once the plan is approved. Mixing planning and implementation in the same step produces messy plans and messy code.
- **Don't skip the conversation.** Jumping straight to the YAML plan without talking through the design misses the main value: catching bad decisions before they're committed. The conversation is where the real planning happens; the YAML is just the record of it.
