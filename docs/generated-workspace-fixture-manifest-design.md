# Generated Workspace Fixture Manifest Design

Generated workspace fixtures are VeritySpec-shaped directories produced from
VerityFoundry examples. Their fixture manifests preserve the conversion context
that should not be embedded into VeritySpec records.

## Manifest Responsibilities

A generated fixture manifest should identify:

- the source VerityFoundry example
- the candidate workspace fixture that was converted
- the generated workspace directory
- the intended VeritySpec workspace format version
- the packs expected by the generated workspace
- the optional local validation command
- whether validation should skip when `verity` is unavailable
- human-review and VeritySpec authority boundaries
- source references, confidence, and unresolved approval requirements

## Boundary

The generated workspace files are candidate VeritySpec workspaces. The manifest
is VerityFoundry metadata for human reviewers and AI agents. VeritySpec remains
the authority for workspace validation, graph checks, readiness, and release
claims.
