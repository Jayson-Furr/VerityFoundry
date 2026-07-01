# Customer Portal Archival-Readiness Candidate Output

This is a golden output fixture for
`lifecycle.archived-product.interview-all.archival-ready.v1`. It shows how
VerityFoundry should ask exhaustive archival questions without claiming that a
retired product archive is complete, legally cleared, privacy-safe, or
approved.

## Archival-Readiness Summary

The customer portal draft can seed an archival interview. It is not archival-ready.
It lacks final source and build manifests, artifact hashes, archive storage
location, license review, data-retention evidence, support handoff evidence,
dashboard shutdown evidence, and human approval.

## Archival Interview Questions

1. Which source repositories, build artifacts, configuration files, and docs
   are final?
2. Which archive location, retention policy, and archive owner are approved?
3. What artifact hashes prove final build and package integrity?
4. Which third-party licenses, UI assets, icons, and dependencies require
   review?
5. What customer data must be retained, deleted, anonymized, or exported?
6. Which support notes, known issues, and historical decisions must be
   preserved?
7. Which telemetry dashboards, alerts, billing integrations, and service
   monitors were shut down?
8. Which domains, app listings, package registries, or distribution channels
   remain active?
9. Which legal, privacy, finance, product, support, and engineering approvals
   are required?
10. What evidence records should VeritySpec validate before any archival-ready
    claim?

## Archive Manifest Gaps

- Final source manifest is missing.
- Final build manifest is missing.
- Artifact hash manifest is missing.
- Documentation archive manifest is missing.
- License review is missing.
- Data-retention and deletion evidence is missing.
- Support handoff note is missing.
- Archive owner and archive location are unresolved.

## Evidence Gap Register

- No evidence proves final source completeness.
- No evidence proves final build reproducibility.
- No evidence proves data-retention obligations are satisfied.
- No evidence proves telemetry, billing, or support systems are shut down.
- No evidence proves legal, privacy, or finance approval.

## Human-Provided Decisions

- The subject is a customer portal product.
- Candidate source material references account status, user management,
  invoices, support requests, and service health.

## AI-Inferred Decisions

- Archival readiness requires preserving final product, support, data, and
  integration state.
- Data-retention evidence is high-impact and cannot be inferred from product
  brief material.
- Support handoff and final known-issues records should be preserved with the
  archive.

## AI-Suggested Decisions

- Create archive manifest records for source, build, docs, and artifacts.
- Create evidence records for artifact hashes, data-retention review, and
  support handoff.
- Create approval records for legal, privacy, finance, product, support, and
  engineering signoff.

## Unresolved Decisions

- Final archive owner.
- Final archive storage location.
- Artifact hashing policy.
- Data-retention policy.
- License review owner.
- Support handoff owner.
- Telemetry and billing shutdown evidence.
- Archive approval authority.

## Human Approval Requirements

- Archive completion claim.
- Legal and license review.
- Privacy and data-retention review.
- Final artifact integrity.
- Support handoff completion.
- Finance or billing shutdown confirmation.

## Suggested VeritySpec Validation Loop

After adding archive, evidence, approval, and support records, run:

```bash
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

Treat archival readiness as incomplete until VeritySpec readiness output,
archive evidence, data-retention evidence, support handoff evidence, and human
approval support the claim.
