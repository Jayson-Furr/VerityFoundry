# VeritySpec Dependency Lockfile Prompt Workflows

Prompt workflows that mention future VeritySpec dependency lockfiles should
preserve uncertainty and avoid fabricating resolved dependency state.

## Prompt Requirements

Prompts should ask for or preserve:

- workspace dependency ID
- dependency alias
- source path or repository
- intended version range
- resolved version if already known
- unresolved record-set hash
- unresolved Git revision or package digest
- pack versions when known
- human approval requirements

Prompts must not invent:

- lockfile hashes
- Git SHAs
- package checksums
- exported-record approval
- production compatibility claims
- VeritySpec validation results

## Boundary

VerityFoundry can draft dependency-lockfile questions, assumptions, and
candidate records. VeritySpec should own the concrete lockfile format,
resolution behavior, graph validation, and readiness impact. Human approval is
required for high-impact dependency decisions.
