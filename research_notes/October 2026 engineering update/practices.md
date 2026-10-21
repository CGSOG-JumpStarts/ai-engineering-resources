# Context, skills and evaluation practices

Checked 2026-10-21 against public primary sources. These are notes for the repository update, not results from a live agent benchmark. Dates below distinguish publication from retrieval. Mutable documentation inspected now is not an archived reconstruction of every earlier October revision. No credentials, enterprise services, installers or model calls were used. No source code was copied.

## How should context, instructions and reusable skills be organized?

### Takeaway

Keep the reviewed agreement and execution evidence in durable repository artifacts. Load the portion needed for the current task; treat summaries as navigation aids that can omit details.

### Cited Findings

- Agent Skills defines metadata, activated instructions and on-demand resources as separate loading levels. A skill is a folder with `SKILL.md`; scripts, references and assets are optional. Its `allowed-tools` field is experimental and implementation support varies. [Agent Skills specification](https://agentskills.io/specification), checked 2026-10-21.
- VS Code distinguishes task-specific skills from coding guidelines in instructions, and warns that skill locations and optional features vary across compatible agents. Its controls generally describe Copilot rather than every harness. [VS Code skills](https://code.visualstudio.com/docs/agent-customization/agent-skills), checked 2026-10-21.
- Anthropic recommends relevant context retrieval, compaction and persisted notes, while warning that aggressive compaction can discard details that become important later. This is engineering guidance, not a universal quantitative claim about token savings. [Context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents), published 2025-09-29, checked 2026-10-21.
- Anthropic's April 2026 Managed Agents account distinguishes durable session history from the model's current context and discusses retrieving earlier events after compaction. It also says harness assumptions should be reconsidered as models improve. [Managed Agents architecture](https://www.anthropic.com/research/managed-agents), published 2026-04-08, checked 2026-10-21.
- Its March 2026 harness experiment uses structured handoffs and separate generation/evaluation roles, but explicitly reports that a newer model let it remove context resets needed in earlier work. This does not establish that multiple agents or session resets always improve results. [Harness design for long-running apps](https://www.anthropic.com/research/harness-design-long-running-apps), published 2026-03-24, checked 2026-10-21.

### Inferences

- Add a division of responsibilities to the skill/context guides: stable repo rules in `AGENTS.md`, agreed behavior in specs, current scope in plans/tasks, procedures in skills, callable capabilities in tools. Host loading and permissions still differ. Use a task context packet containing the approved revision/IDs, affected interfaces, relevant tests, unresolved decisions, allowed actions and evidence links.
- Preserve canonical specs and evidence outside summaries. A fresh session verifies working-tree state and reopens authoritative files. Try one bounded worker before adding orchestration; measure whether additional coordination justifies repeated discovery and review. These are recommendations, not measured gains.

### Gaps

- No host-by-host skill behavior tests or precedence checks were run. Do not label a copied skill interoperable across all products solely because its metadata conforms to the open format.
- The repository's local deterministic lab cannot measure context-management gains for a model.

## How should token use, tool responses and bounded execution be measured?

### Takeaway

Measure the full accepted outcome, including retries and review. Prompt caching can change billing and reported usage without removing irrelevant material from the context; record provider semantics rather than comparing ambiguous totals.

### Cited Findings

- Claude's prompt caching docs require identical cached prefix segments. They expose cache writes, cache reads and uncached input separately; its `input_tokens` alone does not represent all processed input when caching is used. The docs state caching does not change output generation. [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), checked 2026-10-21. Avoid copying prices, TTL defaults or model-specific examples into a company-agnostic guide.
- Anthropic's tool-design guidance recommends clear parameter names, useful bounded responses and pagination/filtering for large results. Errors and truncated responses should explain how the caller can recover. [Writing effective tools](https://www.anthropic.com/research/writing-tools-for-agents), published 2025-09-11, checked 2026-10-21.
- Anthropic's earlier agent-pattern article describes environmental feedback, human checkpoints and stopping conditions such as iteration limits. The page now warns that its tooling discussion has changed since publication; use it for the control principle, not current product setup. [Building effective agents](https://www.anthropic.com/research/building-effective-agents), published 2024-12-19, checked 2026-10-21.

### Inferences

- Distinguish removing irrelevant context, caching prompt prefixes and caching tool results. Scope result caches by identity, permissions and freshness. Configure elapsed-time/call limits, timeouts, safe retries and escalation before execution. Budget exhaustion reports incomplete work rather than success.
- Record provider-native usage categories and normalized totals with cost per accepted outcome, including failures and review. Label undefined denominators. Return filtered/paginated tool results to the model while retaining approved audit evidence separately; context truncation should not silently truncate evidence retention.

### Gaps

- No cache implementation or billed usage was tested. No quantified percentage saving can be claimed.
- Retention, cache pricing and provider counters are provider/contract-specific; the notes do not establish a universal schema or price.

## What should an agent evaluation prove?

### Takeaway

Inspect both final environment state and the steps taken to reach it. Repeat variable tasks and calibrate graders; a persuasive answer or self-reported tool label cannot establish that an action happened safely.

### Cited Findings

- Anthropic defines trials, trajectories and outcomes separately: an asserted booking differs from a reservation present in the database. Its January 2026 evaluation guidance recommends repeated trials, deterministic checks where suitable, and human calibration of model graders. It distinguishes at-least-one success in several attempts (`pass@k`) from success on every attempt (`pass^k`). It also separates exploratory capability suites from regression checks. [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), published 2026-01-09, checked 2026-10-21.
- The long-running coding harness account reports premature completion claims when only narrow tests were run, and uses artifacts plus end-to-end interaction to check progress. Its results concern a particular experiment, not proof that this repository's UI was browser-tested. [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents), published 2025-11-26, checked 2026-10-21.

### Inferences

- Add three checks with a synthetic example: intended final backend state, authorized trajectory and truthful response. Exact call ordering is only necessary when the contract requires it. Report first-attempt success separately from eventual success after retries; a best-of-several demonstration does not establish repeatability.
- Keep regression and improvement/holdout cases separate, balance tool-use and no-tool cases, and review grader assumptions when results look wrong. Retain critical authorization failures as blockers regardless of aggregate scores. Calibrate subjective rubrics with people and permit an insufficient-evidence verdict.

### Gaps

- No statistical claim about this repo, real models or universal sample size is supported. Counts such as 30–100 cases in the existing guide should stay illustrative; adequacy depends on failure rarity and decision risk.
- The existing fixture scorer is exact-match and fabricated; these recommendations do not change its runtime or turn its zero exit code into a release gate.

Writer note: all source text above is paraphrased. Keep final prose compact and do not reproduce extensive article summaries; each web source has a 200-word summarization limit. No edits were made outside this notes file.
