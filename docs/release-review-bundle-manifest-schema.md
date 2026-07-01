# Release-Review Bundle Manifest Schema

[`schemas/release-review-bundle-manifest.schema.json`](../schemas/release-review-bundle-manifest.schema.json)
defines the machine-readable shape for release-review bundle manifests.

The schema currently supports:

- `planned-dry-run` manifests for future export-command validation.
- `generated` manifests for concrete bundle artifacts.
- repository source metadata
- retention context
- artifact producer commands
- planned or computed SHA-256 checksums
- local-only, no-external-AI validation boundaries
- human-review and VeritySpec authority notes

Example fixture:

```text
fixtures/release-review/bundle/manifest.example.json
```

This schema is intentionally about VerityFoundry release-review artifacts. It
does not certify generated VeritySpec workspaces.
