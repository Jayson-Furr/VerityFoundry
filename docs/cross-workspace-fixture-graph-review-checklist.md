# Cross-Workspace Fixture Graph Review Checklist

Cross-workspace fixture graph review should focus on dependency clarity and
impact, not on making unsupported certainty claims.

## Checklist

- Identify each local workspace in the graph.
- Identify each external workspace dependency.
- List every friendly cross-workspace reference.
- Record the canonical VeritySpec URI if one is known.
- Mark missing dependency versions as unresolved.
- Mark private, deprecated, or removed dependency records as blockers or
  warnings according to human policy.
- Check whether a shared dependency change affects multiple generated
  workspaces.
- Keep VeritySpec graph validation as the authority when dependency graph
  tooling is available.

## Boundary

VerityFoundry can help produce graph-review prompts and fixture notes.
VeritySpec must resolve and validate the actual graph, and human reviewers must
approve release-impacting dependency decisions.
