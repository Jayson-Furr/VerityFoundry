# Golden Output Guidelines

Golden outputs should be deterministic examples of expected prompt behavior.
They should not call external AI APIs in tests or CI.

Good golden outputs include:

- Source summary.
- Candidate workspace outline.
- Assumptions.
- AI-inferred decisions.
- AI-defaulted decisions.
- Unresolved questions.
- Human approval requirements.
- Readiness gaps.
- Suggested VeritySpec validation commands.

Do not create golden outputs that imply AI-generated records are final truth.
