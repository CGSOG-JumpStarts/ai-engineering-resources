# Spec-driven delivery review checklist

- Is every requirement testable, with no ambiguous words such as "properly" or "smart" left undefined?
- Are the actor, authorization source, denial path and data permissions explicit?
- Are out-of-scope actions and the existing compatibility surface documented?
- Are negative, empty-data, error, timeout and cross-tenant cases covered?
- Is each FR/NFR mapped to a unit, integration, security or human acceptance check?
- Do tasks name edit boundaries and a reviewable done condition?
- Is the decision to use an LLM in each step warranted by ambiguity or benefit?
- Is there evidence from executed tests, not just an agent assertion?
- Have model/SDK and dependency updates been reviewed separately?
