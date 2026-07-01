# Generated Workspace Unresolved-Decision Report

Generated workspace validation-result snapshots should keep unresolved
decisions visible. This prevents a successful structural validation from being
mistaken for design, implementation, release, operations, or archive readiness.

## Expected Report Content

A future unresolved-decision report should summarize:

- unresolved decisions by generated workspace
- unresolved decisions by readiness target
- decisions requiring human approval
- decisions that block implementation readiness
- decisions that block release, liveops, maintenance, decommissioning, or
  archive readiness
- source references that explain why the decision is unresolved

## Current Snapshot Pattern

For now, each `validation-result.json` includes an `unresolvedDecisions` array.
Release reviewers should inspect it before treating a generated workspace
fixture as stable evidence.

## Authority Boundary

VerityFoundry can report unresolved decisions and prompt for follow-up
interviews. VeritySpec remains the authority for product-contract validation
and readiness gates. Human owners remain responsible for approval.
