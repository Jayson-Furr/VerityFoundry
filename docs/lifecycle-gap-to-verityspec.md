# Lifecycle Gap Reports To VeritySpec Records

VerityFoundry lifecycle prompts produce interview outputs and readiness-gap
reviews. They do not certify readiness. Convert their output into VeritySpec
records before treating the result as part of a product contract.

## Translation Pattern

Use this mapping when a lifecycle prompt identifies a gap:

| VerityFoundry output | VeritySpec follow-up |
|---|---|
| Blocking gap | Add or update a readiness gate, release record, evidence record, or unresolved decision record |
| Non-blocking gap | Add a tracked follow-up, advisory readiness item, or documentation task |
| Missing record | Create the missing VeritySpec record in the appropriate pack or mark the concept unsupported |
| Missing evidence | Add an evidence record with URI, owner, status, and subject reference |
| Human approval requirement | Add an approval/evidence record or keep the related decision unresolved |
| Suggested decision | Convert only after human approval or keep it as a proposal |
| AI-inferred/defaulted decision | Preserve provenance and avoid promotion to approved state |

## Lifecycle Targets

Release-readiness gaps commonly map to:

- `release.milestone`
- `release.rollback-plan`
- `evidence.qa`
- `evidence.security-review`
- `evidence.privacy-review`
- `support.handoff`
- `observability.alerting-plan`

Maintenance-readiness gaps commonly map to:

- `maintenance.policy`
- `maintenance.patch-process`
- `maintenance.dependency-update-policy`
- `support.escalation-path`
- `evidence.ci-build`
- `evidence.security-review`
- `evidence.compatibility-test`

Decommissioning and archival gaps commonly map to:

- `decommission.plan`
- `decommission.communication-plan`
- `decommission.consumer-impact`
- `archive.manifest`
- `archive.artifact-hash`
- `evidence.license-review`
- `evidence.consumer-migration`

These kind names are directional until VeritySpec owns the corresponding
packs. VerityFoundry should preserve the intended record shape and authority
boundary rather than pretending the records already exist in VeritySpec.

## Required Provenance

When a prompt output is translated into a VeritySpec record, preserve:

- source references
- decision source
- confidence
- human approval requirement
- unresolved questions
- related readiness gap
- generated-by workflow or prompt ID

AI-inferred, AI-defaulted, and AI-suggested values should not be promoted to
approved decisions without human review.

## Verification Loop

After translation, run VeritySpec checks against the generated workspace:

```bash
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

Use failures as interview inputs. Do not patch over failed readiness by
inventing evidence, approvals, compliance claims, release claims, maintenance
commitments, decommission completion, or archive completion.
