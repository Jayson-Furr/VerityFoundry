# Lifecycle Readiness Workflows

VerityFoundry lifecycle workflows help AI agents review candidate VeritySpec
workspaces across release, maintenance, and decommissioning stages.

They do not certify readiness.

VerityFoundry may assemble questions, gaps, approval registers, and suggested
next validation loops. VeritySpec validation, readiness gates, CI evidence,
operational evidence, and human approval remain authoritative.

## Prompt Workflows

The lifecycle domain currently provides:

- `lifecycle.workspace.interview-medium.production-ready.release-gap-review.v1`
- `lifecycle.shipped-product.interview-high.maintenance-ready.v1`
- `lifecycle.retiring-product.interview-all.decommission-ready.v1`

Use them when a workspace has moved past initial authoring and the next risk is
not structure alone, but whether the workspace has the evidence, owners,
operational context, support posture, and approval state needed for the next
lifecycle step.

## Release Gap Review

The release gap review workflow expects a candidate VeritySpec workspace plus
validation/readiness output and release notes.

It should identify:

- blocking release gaps
- non-blocking release gaps
- missing or unresolved VeritySpec records
- missing evidence
- missing QA, support, rollback, telemetry, or ownership records
- human approval requirements
- the next VeritySpec validation loop

It should not claim release readiness unless VeritySpec readiness output, CI
evidence, release evidence, and explicit human approval support that claim.

## Maintenance Interview

The maintenance workflow is high-stakes because it touches support, security,
privacy, dependency updates, patching, incident response, and operational
promises.

Agents should ask before filling in:

- support commitments
- security patch obligations
- service-level promises
- customer or player communication policy
- platform obligations
- data-retention obligations
- telemetry monitoring expectations

Unknowns should remain unresolved.

## Decommissioning Interview

The decommissioning workflow uses `interview-all` because shutdown work usually
has legal, privacy, support, platform, data, communication, and archival risks.

Agents must not invent:

- legal clearance
- privacy completion
- data deletion status
- platform approval
- customer or player notification completion
- archival completion

The output should preserve unresolved decisions and human approval markers so
the generated VeritySpec workspace can be validated and reviewed honestly.

## VeritySpec Loop

Recommended handoff loop:

```bash
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

Then rerun the relevant VerityFoundry lifecycle workflow against the new
outputs to identify remaining gaps.
