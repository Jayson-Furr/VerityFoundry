# Generated Workspace Fixture Provenance Schema

[`schemas/generated-workspace-fixture-provenance.schema.json`](../schemas/generated-workspace-fixture-provenance.schema.json)
documents the provenance block used by generated workspace fixture manifests.

The schema requires:

- `decisionSource`
- `confidence`
- `sourceRefs`
- `humanApprovalRequired`

This keeps generated workspace fixtures from hiding whether a decision came
from user input, AI inference, AI suggestion, a prior VeritySpec record, an
external documented source, or an unresolved assumption.

## Boundary

The schema validates VerityFoundry provenance metadata only. It does not prove
that a generated VeritySpec workspace is true, complete, or ready. VeritySpec
validation and human review remain required.
