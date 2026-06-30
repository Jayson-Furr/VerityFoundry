# Dream Extraction Implementation-Ready Candidate Output

This is a golden output fixture for
`unity-game.gdd-art.interview-medium.implementation-ready.v1`. It demonstrates
the expected shape and uncertainty posture for a Unity game workspace draft.

## Candidate Workspace Outline

- `core.product`: Dream Extraction.
- `source.gdd`: rough GDD source at
  `examples/unity-game/dream-extraction/inputs/rough-gdd.md`.
- `source.image-notes`: concept and identity image notes at
  `examples/unity-game/dream-extraction/inputs/images.md`.
- `game.visual-identity`: surreal, liminal, high-contrast direction with logo
  unresolved.
- `game.loop.core`: enter dream zone, collect memory shards, manage pressure,
  escape before collapse.
- `game.loop.session`: one dream-zone run from entry through extraction or
  failure.
- `game.loop.progression`: upgrade loop between runs.
- `game.mode.coop-extraction`: co-op extraction mode with networking model
  unresolved.
- `game.feature.memory-shards`: collectible resource and reward driver.
- `game.feature.zone-collapse`: timed extraction pressure.
- `game.feature.escape-portal`: run completion objective.
- `game.feature.contract-board`: optional objective surface.
- `unity.project`: Unity project record with Unity version unresolved.
- `unity.dependency.shared-runtime`: suggested shared Unity runtime dependency,
  not approved.
- `telemetry.intent`: suggested events for run started, shard collected,
  contract completed, collapse warning, and extraction outcome.
- `qa.gap`: QA evidence is not present.
- `agent.context`: bounded implementation context can be generated after
  platform, Unity version, save model, networking, and prototype scope are
  clarified.

## Source Material Summary

The supplied brief describes a co-op extraction roguelite about entering
unstable dream zones, collecting memory shards, fighting manifestations, and
escaping before collapse. The rough GDD lists candidate systems but leaves
platform, Unity version, networking, save model, telemetry payloads, liveops,
and monetization unspecified. Image notes describe dream-zone ruins, hostile
shadow-like manifestations, cooperative player silhouettes, and a surreal
liminal identity direction.

## Human-Provided Decisions

- Game name: Dream Extraction.
- Genre framing: co-op extraction roguelite.
- Primary loop concept: enter dream zones, collect memory shards, escape before
  collapse.
- Candidate systems: dream-zone run loop, memory shard collection,
  manifestation enemy pressure, escape portal objective, upgrade loop, and
  contract board.
- Image-note themes: dream-zone ruins, floating memory fragments, hostile
  manifestations, cooperative silhouettes, surreal and liminal mood.

## AI-Inferred Decisions

- Candidate record categories include product, source, visual identity, loop,
  mode, feature, Unity dependency, telemetry intent, QA gap, and agent context
  records.
- `memory_shard` is likely a resource or reward concept.
- `zone_collapse` is likely a timed pressure mechanic.
- `escape_portal` is likely the completion condition for a session.
- `contract_board` is likely an optional objective system.

## AI-Defaulted Decisions

- Record status should default to `draft`.
- Owner should default to `unknown` until the team supplies owners.
- Prototype platform may be suggested as PC for local prototyping, but this is
  not a production platform decision.
- Monetization should default to `undecided`.

## AI-Suggested Decisions

- Consider declaring a shared Unity runtime dependency only after the human
  confirms which shared systems are mandatory.
- Consider telemetry events for run lifecycle and reward collection, but do
  not treat event schemas as approved.
- Consider an initial prototype scope limited to one dream-zone scene, one
  resource loop, one enemy pressure archetype, one extraction objective, and
  one upgrade decision.

## Unresolved Decisions

- Unity version.
- Prototype and production target platforms.
- Networking model.
- Save model.
- Shared Unity runtime requirements.
- Telemetry payload schemas.
- Content pipeline.
- QA evidence requirements.
- Licensing and commercial clearance for visual inputs.
- Liveops expectations.
- Monetization model.
- Release milestone.
- Decommissioning and archival policy.

## Human Approval Requirements

- Target platform decisions.
- Multiplayer and networking architecture.
- Save-system requirements.
- Telemetry and player data collection.
- Monetization.
- Liveops or remote configuration.
- Image ownership, licensing, and commercial clearance.
- Production readiness, release readiness, platform approval, and archival
  completion claims.

## Readiness Gaps

The workspace draft may be suitable for concept and prototype discussion after
human review, but it is not implementation-ready. It lacks approved platform,
Unity version, networking, save-system, telemetry schema, QA evidence,
licensing evidence, release milestone, liveops model, and archival policy
decisions.

## Suggested Next Interview Questions

1. What Unity version should the project target?
2. What platforms are in scope for prototype and production?
3. What networking model is expected?
4. What save model is required for the prototype?
5. Which shared Unity runtime systems are mandatory?
6. What is the first prototype scope?
7. Which telemetry events are required, and what data can they collect?
8. Are the concept and identity images owned or licensed for commercial use?
9. Is liveops expected?
10. What release milestone should this draft support?

## Suggested VeritySpec Validation Loop

After generating a concrete VeritySpec workspace from this draft, run:

```bash
verity validate <generated-workspace>
verity lint <generated-workspace> --strict
verity readiness <generated-workspace> --strict
verity graph <generated-workspace>
```

Treat validation failures and readiness gaps as interview inputs, not as
permission for the AI agent to invent missing decisions.
