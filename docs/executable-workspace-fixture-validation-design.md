# Executable Workspace Fixture Validation Design

VerityFoundry currently validates prompt, matrix, example, golden, and
release-review artifacts. It also provides `verityfoundry check verityspec` as
an optional smoke check when the `verity` CLI is installed.

Executable workspace fixture validation is a possible future enhancement. The
goal would be to verify converted fixture workspaces locally without making
VeritySpec a required dependency of VerityFoundry.

## Proposed Boundary

VerityFoundry should continue to own:

- prompt workflow manifests
- candidate workspace fixtures
- provenance examples
- release-review snapshots
- conversion guidance
- optional local integration checks

VeritySpec should continue to own:

- workspace schemas
- pack semantics
- graph validation
- readiness gates
- lint policies
- executable product-contract authority

## Candidate Workflow

A future fixture validation loop could be:

```bash
verityfoundry validate examples
verityfoundry report fixture-inventory
verityfoundry check verityspec --workspace fixtures/generated/dream-extraction-spec
verity validate fixtures/generated/dream-extraction-spec
verity lint fixtures/generated/dream-extraction-spec --strict
verity readiness fixtures/generated/dream-extraction-spec --strict
verity graph fixtures/generated/dream-extraction-spec
```

The `verityfoundry check verityspec` command should keep its current behavior:
pass when VeritySpec validation passes, fail when VeritySpec validation fails,
and skip cleanly when `verity` is not installed.

## Future Fixture Shape

Executable fixtures should be separate from current candidate fixtures. A
future layout could be:

```text
fixtures/generated-workspaces/
  customer-portal/
    verityspec.json
    records/
  dream-extraction/
    verityspec.json
    records/
```

Each generated workspace should keep links back to:

- source example manifest
- candidate workspace fixture
- provenance examples
- unresolved decision list
- readiness-gap report
- conversion checklist notes

## Non-Goals

Do not make VeritySpec a mandatory Python dependency of VerityFoundry.

Do not weaken VeritySpec validation so generated fixtures pass.

Do not treat a generated fixture as approved product truth just because the
fixture is structurally valid.

Do not run external AI APIs in fixture validation.

## Acceptance Criteria for a Future Sprint

A future implementation sprint should include:

- at least one generated workspace fixture that can be validated by VeritySpec
  when `verity` is installed
- a skip-safe local check when `verity` is unavailable
- documentation for generated fixture maintenance
- CI behavior that remains deterministic and does not require external AI APIs
- release-review notes explaining VeritySpec validation results separately
  from VerityFoundry authoring-quality reports
