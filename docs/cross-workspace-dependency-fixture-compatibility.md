# Cross-Workspace Dependency Fixture Compatibility

Cross-workspace dependency fixtures should make dependency assumptions visible
without pretending VerityFoundry can resolve every workspace graph itself.

## Compatibility Questions

For a generated workspace fixture that references another workspace, reviewers
should ask:

- Is the dependency represented as a workspace, not a pack?
- Is the dependency alias stable and human-readable?
- Is the expected VeritySpec version documented?
- Are referenced records intended to be public or exported?
- Are deprecated or removed records explicitly called out?
- Does the fixture explain what should happen when the dependency is missing?
- Is the validation path skip-safe when VeritySpec dependency support is not
  available?

## Boundary

VerityFoundry can preserve dependency assumptions and prompt workflows.
VeritySpec remains the authority for dependency resolution, graph validation,
readiness, lockfiles, and cross-workspace reference semantics. Human review is
required before treating a dependency fixture as a real contract.
