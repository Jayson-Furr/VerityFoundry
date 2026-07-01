# Cross-Workspace Reference Guidance

VerityFoundry can draft cross-workspace dependency assumptions for future
VeritySpec workspaces, but it does not resolve or validate those references.
VeritySpec remains responsible for workspace dependency semantics, lockfiles,
export visibility, compatibility checks, and graph validation.

## Authoring Syntax

Use friendly authoring syntax only when the input supports a dependency
assumption:

```text
sharedUnity::unity.package.save_system
```

The left side is a dependency alias. The right side is the candidate record ID
in the provider workspace.

Generated records should preserve uncertainty:

```json
{
  "id": "xref.dream_extraction.save_system",
  "kind": "workspace.cross-reference",
  "status": "illustrative",
  "sourceRecord": "game.feature.cloud_save",
  "target": "sharedUnity::unity.package.save_system",
  "summary": "Illustrative friendly reference only; canonical URI resolution is a future VeritySpec responsibility.",
  "provenance": {
    "decisionSource": "ai-suggested",
    "confidence": "low",
    "humanApprovalRequired": true
  }
}
```

## Canonical URI Shape

When documenting future intent, use canonical URI examples as non-binding
guidance:

```text
verity://workspace/studio.library.shared_unity_runtime@1.2.4/record/unity.package.save_system
```

Do not claim that canonical URI resolution, dependency locking, or exported
record validation exists unless the target VeritySpec version supports it.

## Required Uncertainty

Generated cross-workspace records should identify:

- consumer workspace
- provider workspace
- dependency alias
- version constraint or unresolved version decision
- source record
- friendly target reference
- public/exported versus internal/private uncertainty
- lockfile and reproducibility gaps
- human approval requirement

Leave these unresolved unless the input evidence proves them:

- exact provider version
- exported record status
- compatibility guarantee
- lockfile hash
- transitive dependency policy
- migration or breaking-change status

## Verification Loop

Use VerityFoundry to inspect the candidate dependency map:

```bash
verityfoundry report portfolio-coverage
verityfoundry report provenance-distribution
```

Then convert the fixture into a real VeritySpec workspace and validate it:

```bash
verity validate <generated-workspace>
verity graph <generated-workspace>
verity readiness <generated-workspace> --strict
```

If VeritySpec cannot resolve or validate the reference, keep the candidate
record as a dependency assumption or readiness gap until the workspace and
pack support exist.
