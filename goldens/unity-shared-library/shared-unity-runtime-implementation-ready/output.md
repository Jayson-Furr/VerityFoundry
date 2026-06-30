# Shared Unity Runtime Implementation-Ready Candidate Output

This is a golden output fixture for
`unity-library.description.interview-medium.implementation-ready.v1`. It
demonstrates the expected shape and uncertainty posture for a shared Unity
library workspace draft.

## Candidate Workspace Outline

- `core.product`: Shared Unity Runtime.
- `source.brief`: source brief at
  `examples/unity-shared-library/shared-unity-runtime/inputs/brief.md`.
- `unity.library`: reusable Unity package family for multiple consumer games.
- `unity.package.save-system`: candidate save-system helper package.
- `unity.package.telemetry-client`: candidate telemetry client integration
  package.
- `unity.package.liveops-config-loader`: candidate remote/liveops config
  loading package.
- `unity.package.addressables-helpers`: candidate addressables helper package.
- `unity.package.localization-runtime`: candidate localization helper package.
- `unity.package.platform-services`: candidate platform-service wrapper
  package.
- `unity.capability.save-system`: suggested exported capability, pending public
  API approval.
- `unity.capability.telemetry-client`: suggested exported capability, pending
  data-collection and schema approval.
- `unity.capability.liveops-config`: suggested exported capability, pending
  operations and rollback policy approval.
- `unity.compatibility.policy`: unresolved compatibility contract for Unity
  versions, package versions, semantic versioning, and consumer migration.
- `unity.consumer-contract`: future-facing notes for game workspaces that may
  depend on this shared runtime.
- `evidence.gap`: CI, Unity edit mode, Unity play mode, package import,
  integration, compatibility, and release evidence are not present.
- `agent.context`: bounded implementation context can be generated after
  package names, Unity versions, public exports, consumers, and compatibility
  policy are clarified.

## Source Material Summary

The supplied brief describes Shared Unity Runtime as a reusable Unity package
family for multiple games. It is expected to cover save-system helpers,
telemetry client integration, liveops config loading, addressables helpers,
localization helpers, and platform-service wrappers. The brief intentionally
leaves target Unity versions, package names, consumer game list, public versus
internal exported records, compatibility policy, deprecation policy, and
evidence requirements unspecified.

## Human-Provided Decisions

- Library name: Shared Unity Runtime.
- Domain: reusable Unity package family.
- Intended consumers: multiple games, with the specific game list unresolved.
- Candidate shared systems: save-system helpers, telemetry client integration,
  liveops config loading, addressables helpers, localization helpers, and
  platform-service wrappers.
- Known gaps: Unity versions, package names, exports, compatibility,
  deprecation, and evidence are not provided.

## AI-Inferred Decisions

- Candidate record categories include product, source, Unity library, Unity
  package, capability, compatibility policy, consumer contract, evidence gap,
  and agent context records.
- The save-system, telemetry, liveops config, addressables, localization, and
  platform-service areas are likely separate package or module contracts.
- Public capability records should be separated from internal implementation
  records so consuming game workspaces do not rely on private details.
- Future VeritySpec workspace dependencies may allow consumer games to
  reference exported records from this library workspace.

## AI-Defaulted Decisions

- Record status should default to `draft`.
- Owner should default to `unknown` until engineering, platform, liveops, and
  QA owners are supplied.
- Visibility should default to unresolved, not public, until the exported API
  surface is approved.
- Compatibility should default to `uncommitted` until Unity version ranges,
  package versioning, and migration policy are supplied.

## AI-Suggested Decisions

- Consider modeling each shared system as both a Unity package record and an
  exported capability record after human approval.
- Consider defining public/exported records separately from internal/private
  records before any consumer game depends on this workspace.
- Consider adding a compatibility policy for supported Unity versions,
  package semantic versioning, deprecation windows, breaking-change notices,
  and migration expectations.
- Consider adding evidence records for CI, Unity package import tests, edit
  mode tests, play mode tests, sample consumer integration, and release
  package hashes.

## Unresolved Decisions

- Target Unity versions.
- Concrete Unity package names.
- Package boundaries.
- Consumer game list.
- Public/exported records versus internal/private records.
- Compatibility and semantic versioning policy.
- Deprecation and removal policy.
- Data collection constraints for telemetry client integration.
- Liveops config rollback and failure behavior.
- Addressables and localization versioning expectations.
- Platform-service wrapper scope.
- CI and Unity test evidence requirements.
- Release artifact and package distribution process.
- Support, maintenance, decommissioning, and archival policy.

## Human Approval Requirements

- Supported Unity version ranges.
- Public API and exported capability surface.
- Consumer compatibility claims.
- Telemetry and player data collection behavior.
- Liveops remote config behavior, rollback expectations, and operational
  ownership.
- Platform-service wrapper responsibilities.
- Versioning, deprecation, removal, and migration policies.
- Release readiness, production readiness, package approval, and archival
  completion claims.

## Readiness Gaps

The workspace draft may be suitable for architecture discussion after human
review, but it is not implementation-ready. It lacks approved Unity versions,
package names, package boundaries, exported API surface, consumer list,
compatibility policy, deprecation policy, telemetry constraints, liveops
rollback behavior, CI and Unity test evidence, release artifact policy,
support policy, and archival policy.

## Suggested Next Interview Questions

1. Which Unity versions must this shared runtime support?
2. What are the concrete Unity package names and package boundaries?
3. Which records or capabilities are public exports for consumer games?
4. Which records are internal implementation details?
5. Which games are expected consumers for the first release?
6. What compatibility and semantic versioning policy should consumers rely on?
7. What deprecation window is required before removing an exported capability?
8. What telemetry data may the telemetry client collect?
9. What rollback behavior is required for liveops config loading?
10. What Unity test, CI, package import, and integration evidence is required?

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
