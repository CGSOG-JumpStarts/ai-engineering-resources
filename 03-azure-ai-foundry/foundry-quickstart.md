# Foundry hands-on checklist for an existing advisory-agent project

This is a guided **manual verification checklist**, not a script that grants permissions or provisions production resources. Follow current Microsoft documentation for portal steps and SDK examples.

## 1. Establish the environment

Record subscription and tenant, Foundry project type, region, deployment names, allowed outbound connectivity, identity model, tool connections and owners. Have the cloud administrator confirm least-privilege access for any new role assignment. Check Foundry Hosted Agent [prerequisites and deployment documentation](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent).

## 2. Select a bounded test

Use a synthetic dealer question with a known allowed response and a deliberately unsupported policy question. Keep the model evaluation set and tool schemas under version control. Do not upload real dealer data into the portal for a workshop without its approved data handling assessment.

## 3. Choose a hosting approach

Document whether the existing code runs in a normal enterprise application service, a Foundry Hosted Agent, or another orchestrator. Hosted GA availability is **not** permission to deploy in any region without checking. See [Agent Framework hosting models](https://learn.microsoft.com/en-us/agent-framework/hosting/).

## 4. Connect only approved tools

Start with read-only synthetic knowledge. Use server-side authz even when a tool is called by an agent. Confirm the correct Foundry connection auth mode and the principal receiving resource permissions using [MCP authentication](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/mcp-authentication).

## 5. Capture traces and evaluate

Configure Application Insights in the Foundry project, verify who can read traces and which content fields are captured, and run at least one successful and one unsupported question. Use [tracing guidance](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup) and [agent evaluator documentation](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators); select evaluators only if supported for the tool type and release status.

## 6. Compare versions using an identical test set

Run a fixed model baseline and optional model router comparison where supported. Capture actual tokens, cost, p50/p95, success and tool accuracy across repeated runs. Do not assume a less expensive model is suitable without quality evidence. [Model routing reference](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses-model-routing).

## 7. Decide on rollout

A human owner signs off on coverage, access boundaries, failure handling, evaluation results, budget, support plan, deployment/version strategy and rollback. Start read-only or with tightly restricted action scope; no autonomous destructive changes.
