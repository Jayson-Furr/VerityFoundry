# Workspace Fixtures

Workspace fixtures are candidate VeritySpec workspace drafts attached to
examples. They make expected outputs more concrete while preserving the core
VerityFoundry rule: generated records are not final product truth.

An example manifest may declare:

```json
{
  "workspaceFixtures": [
    "expected/candidate-workspace.json"
  ],
  "expectedRecordCategories": [
    "core.product",
    "foundry.readiness-gap"
  ],
  "provenanceExamples": [
    "expected/provenance.json"
  ]
}
```

`workspaceFixtures` are local files under the example directory. The first
fixture shape is intentionally simple:

```json
{
  "workspace": {
    "id": "foundry.example.product.customer_portal",
    "specVersion": "candidate",
    "status": "draft"
  },
  "records": [
    {
      "id": "product.customer_portal",
      "kind": "core.product",
      "status": "draft",
      "provenance": {
        "sourceRefs": ["inputs/brief.md"],
        "decisionSource": "user-provided",
        "confidence": "medium",
        "humanApprovalRequired": true
      }
    }
  ]
}
```

`verityfoundry validate examples` checks that every declared fixture file
exists and that every `expectedRecordCategories` entry appears as a `kind` in
the fixture records.

`provenanceExamples` document how decisions should stay traceable. Each
decision entry should include:

- `recordRef`
- `field`
- `decisionSource`
- `sourceRefs`
- `confidence`
- `humanApprovalRequired`

These fixtures are not a replacement for VeritySpec validation. To convert one
into a concrete workspace:

1. Create a real VeritySpec workspace directory.
2. Split fixture records into the record-file layout expected by that
   workspace.
3. Replace `specVersion: "candidate"` with a supported VeritySpec workspace
   version.
4. Map candidate `kind` values to installed VeritySpec packs.
5. Preserve provenance, assumptions, unresolved questions, and human approval
   requirements.
6. Run `verity validate`, `verity lint --strict`, and `verity readiness`.

If VeritySpec rejects the converted workspace, VeritySpec is authoritative.
