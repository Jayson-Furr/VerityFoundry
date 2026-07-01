# Release-Review Bundle Checksums

Release-review bundle checksums should make generated review artifacts easier
to compare and audit.

## Checksum Rules

- Use SHA-256 for bundle artifacts.
- Record one checksum entry for every generated file.
- Use lowercase hexadecimal digests.
- Use `state: planned` with `digest: null` in dry-run manifests.
- Use `state: computed` with a concrete digest in generated manifests.
- Recompute checksums whenever bundle contents change.

## Review Use

Checksums help a human reviewer detect accidental artifact changes between
local generation, CI, and release upload. They do not prove that prompt outputs
are true or that a generated VeritySpec workspace is ready. VeritySpec checks
and human approval remain separate.
