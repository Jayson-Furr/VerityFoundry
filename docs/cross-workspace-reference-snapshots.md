# Cross-Workspace Reference Snapshots

Cross-workspace reference snapshots capture the dependency-assumption subset
from example candidate workspace fixtures.

Current snapshots live under:

```text
snapshots/cross-workspace-references/
```

The initial snapshot is:

```text
snapshots/cross-workspace-references/shared-unity-dependency-map-v0.22.0.json
```

It is derived from:

```text
examples/portfolio/shared-unity-dependency-map/expected/candidate-workspace.json
```

The snapshot includes records with these candidate kinds:

- `workspace.dependency`
- `workspace.cross-reference`
- `workspace.dependency-risk`
- `unity.exported-record-assumption`

## Boundary

These records are illustrative authoring outputs. They are not resolved
VeritySpec dependencies, lockfile entries, exported-record proofs, or graph
validation results.

The snapshot is useful because reviewers can inspect the handoff shape without
mistaking unresolved references for product truth.

## Required Review Checks

Before accepting a cross-workspace reference as product truth, a human or
VeritySpec workflow must confirm:

- provider workspace exists
- dependency alias is declared
- version constraint is intentional
- referenced record exists
- referenced record is public or exported
- status is not removed
- dependency lockfile or reproducibility strategy exists
- graph and readiness checks pass in VeritySpec

Until those checks exist, keep the records as assumptions or readiness gaps.
