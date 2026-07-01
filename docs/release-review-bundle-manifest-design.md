# Release-Review Bundle Manifest Design

A release-review bundle manifest should describe what a deterministic bundle
contains before or after the bundle is generated.

The manifest should answer:

- Which repository, ref, commit, and release tag produced the bundle?
- Which reports, snapshots, fixtures, or metadata files are included?
- Which command produced each generated report?
- Are checksums planned or computed?
- What retention context applies?
- What human review and VeritySpec authority boundaries remain?

## Modes

`planned-dry-run` means the manifest describes expected files before the
export command writes them. Artifact checksums should use `state: planned` and
`digest: null`.

`generated` means the bundle exists. Artifact checksums should use
`state: computed` and a SHA-256 digest for every included artifact.

## Boundary

The bundle manifest is release-review metadata for VerityFoundry. It does not
certify generated workspace truth. VeritySpec remains the authority for
workspace validation, graph checks, readiness, and product-contract behavior,
and human approval remains required for release decisions.
