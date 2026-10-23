# Context management and token usage

Repeated discovery, oversized context and retries can increase token usage. The correct unit of comparison is the **fully reviewed change**, including retries, tests and rework, not the first AI response.

## Avoid unnecessary context

- Keep repo maps and general rules short. Make package/domain-specific instructions opt-in through portable skills.
- Supply related contracts, error cases, tests and a reviewed feature spec rather than unfiltered historical chats.
- Store resolved decisions as ADRs, known API contracts, executable tests and small stable reference files.
- Search code symbolically and open targeted files instead of putting the entire repository in the model context.
- Separate a short "what and why" spec from a technical implementation plan; regenerate only the outdated portion.
- Run deterministic validators locally. Do not spend model tokens asking whether a JSON schema, unit test or lint result passes when a tool can determine it.
- Preserve a concise post-task handoff: what changed, why, tests run, known risks and next owner. Avoid duplicating the full transcript.

## Carry a task context packet

Start with the approved spec revision and IDs, the current task, affected interface contracts, relevant tests, unresolved decisions and allowed actions. Link the evidence and decisions needed for that task. Keep repository conventions in instructions, agreed behavior in specs, current edit scope in tasks and reusable procedures in skills. A tool supplies a capability; a skill does not grant its permissions.

Agent Skills supports [progressive loading](https://agentskills.io/specification), but discovery and execution behavior still depend on the coding host. Verify the files the host actually loaded before diagnosing a missed instruction.

Conversation history, an audit trail and the model's current context are separate records. A compacted summary can omit a constraint. Preserve authoritative specs and execution evidence outside summaries, then reopen them when resuming. [Context-engineering guidance](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) describes this risk. Start with one bounded worker; add orchestration only when measured coordination benefits justify its extra discovery and review.

## Separate context reduction from caching

| Technique | What to check |
|---|---|
| Remove irrelevant context | The task still has its required contracts, failure cases and decisions |
| Cache a prompt prefix | Provider cache-write/read/uncached counters, invalidation and billing semantics |
| Cache tool results | Caller identity, permission scope, freshness and whether reuse is safe |

A cache hit does not establish that the prompt contains only relevant material. Provider counters differ: for example, Claude reports cache reads and writes separately from uncached input in its [prompt-cache documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching). Retain provider-native counters and label any normalized total. Do not compare ambiguous `input_tokens` values across providers as if their definitions were identical.

Return bounded, filtered or paginated tool results to the model while retaining approved audit evidence separately. Set elapsed-time and call budgets, tool timeouts and safe retry rules before execution. At a budget limit, report incomplete work and the next decision; do not turn exhaustion into a success claim.

## Measurement sheet

Capture one row per change and agent/model configuration:

| Metric | Definition |
|---|---|
| `input_tokens` | Provider-native uncached/cache-read/cache-write categories where available; keep definitions with normalized totals |
| `output_tokens` | Provider-reported model output usage |
| `tool_calls` | Count by tool and successful/failed status |
| `model_spend` | Provider-billed usage at the contract's actual price, never assumed public list price |
| `human_minutes` | Prep, review, debugging and handoff work |
| `elapsed_minutes` | Wall-clock time through accepted PR |
| `acceptance_pass_rate` | Required acceptance cases passing first and final review |
| `rework_count` | Changes requested after the first submitted implementation |
| `escaped_defects` | Issues found after acceptance within a defined window |

A sensible comparison is two comparable tasks or an A/B crossover with the same developer group. Record model IDs, prompts, software versions, cache policy and environment. Include any human-only baseline where appropriate. Do not present unmeasured token or time savings as fact.

## Token budgeting without unsafe shortcuts

Use smaller models for classification/extraction and larger models only where quality data justify them. Cache identical deterministic results. Stop after repeated tool failures rather than blindly retrying. Reduce irrelevant source material and redundant evaluations, but preserve security checks, negative tests, audit and review. See [model selection](../05-evaluation/model-selection.md) for the scoring method. Use the [session handoff template](session-handoff-template.md) to carry decisions into a fresh session.
