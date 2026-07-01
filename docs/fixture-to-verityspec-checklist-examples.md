# Fixture to VeritySpec Checklist Examples

These examples apply the general checklist in
[`fixture-to-verityspec-checklist.md`](fixture-to-verityspec-checklist.md) to
two current fixtures.

The examples are intentionally conservative. VerityFoundry drafts candidate
records; VeritySpec remains the validation authority.

## Product Fixture: Customer Portal

Fixture:

```text
examples/product/customer-portal/expected/candidate-workspace.json
```

Suggested conversion steps:

1. Create a VeritySpec workspace such as `customer-portal-spec/`.
2. Add a workspace manifest with supported VeritySpec format version and packs.
3. Map `core.product` records to the current VeritySpec core product shape.
4. Map `product.audience`, `product.feature`, and
   `product.integration-assumption` to supported product or local extension
   kinds.
5. Preserve `security.decision` as a security pack record or as a readiness
   gap if the target pack is unavailable.
6. Preserve `foundry.readiness-gap` as an issue, evidence gap, or readiness
   blocker instead of hiding it.
7. Preserve every `provenance` object from the fixture.
8. Keep AI-suggested permissions, integrations, and operations assumptions
   marked as human-approval-required until a human approves them.

Useful review commands:

```bash
verityfoundry report fixture-inventory
verityfoundry report provenance-distribution
verity validate customer-portal-spec
verity lint customer-portal-spec --strict
verity readiness customer-portal-spec --strict
```

## Unity Fixture: Dream Extraction

Fixture:

```text
examples/unity-game/dream-extraction/expected/candidate-workspace.json
```

Suggested conversion steps:

1. Create a VeritySpec workspace such as `dream-extraction-spec/`.
2. Add game, asset, Unity, and observability packs when available, or document
   local extension packs for unsupported candidate kinds.
3. Map `core.product`, `game.gdd-source`, `game.loop`, `game.mode`, and
   `game.feature` records into the game workspace.
4. Keep `game.asset.image` and `game.visual-identity` records tied to source
   files; do not claim licensing or commercial clearance unless provided.
5. Keep `unity.package-dependency` unresolved until the shared Unity runtime
   package name, version, exported capabilities, and lockfile policy are known.
6. Keep `telemetry.intent` as telemetry intent until event payloads,
   dashboards, and owner decisions are specified.
7. Preserve unresolved decisions for platform scope, save model, liveops,
   production QA, and release evidence.
8. Re-run VeritySpec graph and readiness checks after every conversion pass.

Useful review commands:

```bash
verityfoundry report portfolio-coverage
verityfoundry report provenance-distribution
verity validate dream-extraction-spec
verity graph dream-extraction-spec
verity readiness dream-extraction-spec --strict
```

If VeritySpec rejects the converted workspace, update the workspace, prompt
workflow, fixture, or example expectations to preserve that feedback.
