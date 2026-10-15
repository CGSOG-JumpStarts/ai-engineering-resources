# Context management and token usage

The team raised token usage as a practical concern. The correct unit of comparison is the **fully reviewed change**, including retries, tests and rework, not the first AI response.

## Avoid unnecessary context

- Keep repo maps and general rules short. Make package/domain-specific instructions opt-in through portable skills.
- Supply related contracts, error cases, tests and a reviewed feature spec rather than unfiltered historical chats.
- Store resolved decisions as ADRs, known API contracts, executable tests and small stable reference files.
- Search code symbolically and open targeted files instead of putting the entire repository in the model context.
- Separate a short "what and why" spec from a technical implementation plan; regenerate only the outdated portion.
- Run deterministic validators locally. Do not spend model tokens asking whether a JSON schema, unit test or lint result passes when a tool can determine it.
- Preserve a concise post-task handoff: what changed, why, tests run, known risks and next owner. Avoid duplicating the full transcript.

## Measurement sheet

Capture one row per change and agent/model configuration:

| Metric | Definition |
|---|---|
| `input_tokens` | Model input usage reported by provider, including cached tokens separately if available |
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

Use smaller models for classification/extraction and larger models only where quality data justify them. Cache identical deterministic results. Stop after repeated tool failures rather than blindly retrying. Reduce irrelevant source material and redundant evaluations, but preserve security checks, negative tests, audit and review. See `05-evaluation/model-selection.md` for the scoring method.
