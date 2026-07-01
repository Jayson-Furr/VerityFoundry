# Release-Review Bundle Dry-Run CLI Design

This is a design note for a future command. It is not implemented yet.

Potential command:

```bash
verityfoundry export release-review-bundle --out build/release-review --dry-run
```

## Desired Behavior

The dry-run mode should:

- render a bundle manifest without writing report artifacts
- validate the manifest against the bundle manifest schema
- list every planned artifact and producer command
- mark checksums as planned with `digest: null`
- fail if a required producer command is unknown
- remain deterministic and local-only

## Non-Goals

- Do not call external AI APIs.
- Do not publish artifacts.
- Do not perform VeritySpec workspace validation.
- Do not replace human release review.

The dry-run should be a planning and validation aid for release reviewers, not
a release authority.
