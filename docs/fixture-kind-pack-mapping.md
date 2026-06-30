# Fixture Kind Pack Mapping

`verityfoundry report fixture-inventory` maps candidate workspace fixture record
kinds to recommended VeritySpec packs.

The mapping is intentionally advisory. VerityFoundry examples may include
future-facing record kinds for game, Unity, product, software-library, and
authoring-output workflows before VeritySpec has built-in packs for every
domain.

Current mapping categories include:

- `core.product` -> `verity.core`
- `api.interface` -> `verity.pack.api`
- `security.decision` -> `verity.pack.security`
- `telemetry.intent` -> `verity.pack.observability`
- `game.*` -> future game and game-assets packs
- `unity.*` -> future Unity pack
- `product.*` -> future product pack
- `software.*` -> future software pack
- `foundry.readiness-gap` -> VerityFoundry authoring output

Use the report to answer:

- which candidate record kinds appear in examples
- which VeritySpec packs would eventually own those kinds
- whether new examples are expanding the fixture vocabulary intentionally
- whether release notes and roadmap entries need to mention new fixture kinds

The mapping does not validate generated workspaces. VeritySpec remains the
authority for schema, reference, readiness, graph, and generator behavior once a
workspace is materialized.
