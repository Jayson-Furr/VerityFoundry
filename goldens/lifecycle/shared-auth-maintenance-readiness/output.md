# Shared Auth Library Maintenance-Readiness Candidate Output

This is a golden output fixture for
`lifecycle.shipped-product.interview-high.maintenance-ready.v1`. It shows how
VerityFoundry should interview for a shipped shared-library maintenance state
while leaving sensitive operational commitments unresolved.

## Maintenance-Readiness Summary

The shared authentication library draft can support a maintenance interview,
but it is not maintenance-ready. The draft identifies package, consumer,
security, API, and readiness-gap records, but it lacks approved patch policy,
security-response policy, dependency-update policy, consumer communication
rules, evidence records, and VeritySpec maintenance readiness output.

## Maintenance Interview Questions

1. Who owns routine patch releases?
2. Who owns emergency security releases?
3. Which consumer teams must be notified before breaking changes?
4. What semantic-versioning and deprecation rules apply?
5. What test evidence is required before patch publication?
6. What security review evidence is required?
7. How are dependency updates reviewed and rolled out?
8. What support channel receives consumer incidents?
9. What telemetry, package download, or issue signals define a watchlist?
10. What records prove maintenance readiness in VeritySpec?

## Support Handoff Gaps

- Support owner is unknown.
- Consumer escalation path is missing.
- Breaking-change communication policy is missing.
- Vulnerability disclosure path is unresolved.
- Patch release announcement process is unresolved.

## Operational Evidence Gaps

- No CI build evidence.
- No unit or integration test evidence.
- No dependency audit evidence.
- No security review evidence.
- No consumer compatibility evidence.
- No package publication smoke-test evidence.

## Human-Provided Decisions

- The artifact is a shared authentication library.
- The library has consumer applications.
- Authentication and authorization behavior are high-risk maintenance areas.

## AI-Inferred Decisions

- Maintenance readiness should include dependency update policy, security
  response, compatibility testing, consumer communication, and support handoff.
- Breaking changes require stronger approval than routine patch changes.
- Evidence should be linked to the library record and consumer contract
  records.

## AI-Defaulted Decisions

- Maintenance status remains `draft`.
- Support and security owners remain `unknown`.
- Security posture defaults to unverified.
- Consumer compatibility defaults to unproven.

## Unresolved Decisions

- Patch cadence.
- Security response owner.
- Consumer notification list.
- Deprecation window.
- Supported runtime versions.
- Dependency update policy.
- Package publishing authority.
- Incident support process.

## Human Approval Requirements

- Security response commitments.
- Supported version policy.
- Breaking-change policy.
- Consumer communication commitments.
- Maintenance readiness claim.
- Package publishing policy.

## Suggested VeritySpec Validation Loop

After maintenance records and evidence are added, run:

```bash
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

Use missing or failed readiness gates as follow-up interview questions, not as
permission for the AI agent to invent support or security commitments.
