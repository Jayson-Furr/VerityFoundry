# Shared Unity Runtime Decommission-Readiness Candidate Output

This is a golden output fixture for
`lifecycle.retiring-product.interview-all.decommission-ready.v1`. It shows how
VerityFoundry should ask exhaustive decommissioning questions without claiming
that a shared runtime, package, or archive has been safely retired.

## Decommission-Readiness Summary

The shared Unity runtime draft can seed a decommissioning interview, but it is
not decommission-ready. It lacks consumer-game impact evidence, package
deprecation policy, migration path, final artifact manifest, license review,
support handoff, archival plan, and human approval.

## Decommissioning Interview Questions

1. Which Unity games consume this runtime today?
2. Which runtime records are exported and which are internal?
3. What replacement package or migration path is approved?
4. What deprecation version and removal version are planned?
5. Which package registries, Git repositories, or artifact stores must change?
6. Which support and liveops teams must be notified?
7. What final source, package, documentation, and asset manifests are required?
8. What license review is required before archival?
9. What telemetry, crash, or runtime dashboards must be retired?
10. What evidence proves all consuming games have migrated?

## Archive Follow-Up Items

- Final package manifest.
- Source archive manifest.
- Documentation archive manifest.
- Artifact checksums.
- License review record.
- Consumer migration evidence.
- Support handoff note.
- Archive owner and archive location.

## Data And Platform Gaps

- Package registry retention policy is unknown.
- Consumer game migration state is unknown.
- Telemetry/dashboard shutdown requirements are unknown.
- Platform or store impact is unknown.
- Legal, licensing, and archival approval evidence is missing.

## Human-Provided Decisions

- The subject is a shared Unity runtime library.
- Candidate capabilities include save, telemetry, liveops config, and related
  Unity package contracts.

## AI-Inferred Decisions

- Decommissioning a shared runtime requires consumer impact analysis before
  any removal claim.
- Exported versus internal record status matters for migration planning.
- Archive records should link final source, package, documentation, checksum,
  and license evidence.

## AI-Suggested Decisions

- Create a decommission plan record with consumer-game references.
- Create an archive manifest record for final source and package artifacts.
- Create evidence records proving replacement adoption by consumer games.
- Create support and communication records for runtime consumers.

## Unresolved Decisions

- Approved replacement runtime.
- Consumer migration deadline.
- Package deprecation and removal versions.
- Registry retention policy.
- Archive owner.
- Archive storage location.
- License review owner.
- Support handoff owner.
- Telemetry shutdown requirements.

## Human Approval Requirements

- Decommissioning approval.
- Consumer migration completion.
- Legal and license review.
- Archive completion claim.
- Package registry removal or retention policy.
- Support handoff completion.

## Suggested VeritySpec Validation Loop

After adding decommission, migration, evidence, and archive records, run:

```bash
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

Treat decommissioning as incomplete until VeritySpec readiness output,
consumer-impact evidence, archival evidence, and human approval support the
claim.
