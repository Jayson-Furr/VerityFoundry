# Roadmap

VerityFoundry is the prompt workflow companion to VeritySpec. It fabricates,
interviews for, refines, and gap-reviews candidate VeritySpec workspace drafts
while preserving uncertainty and human approval requirements.

## v0.1.0

The `v0.1.0` milestone establishes the public repository foundation.

| Sprint | Status | Focus |
|---:|---|---|
| 1 | Planned | Repository scaffold, AI-agent entry point, prompt manifest schema, and basic validation CLI |
| 2 | Planned | Interview modes and readiness target documentation |
| 3 | Planned | Unity game prompt matrix and examples |
| 4 | Planned | Unity shared-library prompt matrix and examples |
| 5 | Planned | Decision policy and provenance rules hardening |
| 6 | Planned | Golden output examples and prompt quality rubric |
| 7 | Planned | VeritySpec integration documentation and generated workspace validation notes |
| 8 | Planned | v0.1.0 release preparation |

## Sprint 1 Priorities

- Create the installable `verityfoundry` package and CLI.
- Add machine-checkable prompt, matrix, example, and decision-policy schemas.
- Add the canonical `AGENTS.md` entry point and thin agent adapters.
- Add CI and local tests for deterministic repository validation.
- Add public project metadata and basic documentation.

## Later Candidates

These are intentionally not committed to a release until the initial scaffold
is complete:

- Golden prompt output fixtures for selected workflows.
- Optional VeritySpec workspace generation fixtures.
- VeritySpec validation integration when `verity` is available locally.
- Richer prompt rendering profiles for specific AI-agent surfaces.

## Next 20 Roadmap Points

These points define the next backlog once the active roadmap is caught up. They
are planning inputs, not release commitments. Convert each point into a GitHub
issue and milestone before implementation begins.

AI agents must keep this section populated with up to 20 concrete points when
the active roadmap is caught up. The points should balance fixes,
improvements, continuation work, and expansion.

1. Add golden output fixtures for the Unity game implementation-ready prompt.
2. Add golden output fixtures for the Unity shared-library implementation prompt.
3. Add a prompt quality report that scores uncertainty preservation and
   provenance completeness.
4. Add a local VeritySpec integration smoke check that runs only when `verity`
   is available.
5. Add a software-library example for a shared authentication package.
6. Add a product example for a customer portal.
7. Add prompt manifests for operations-ready and archival-ready Unity game
   workflows.
8. Add a decision-policy linter for high-stakes invention risks.
9. Add Markdown rendering profiles for Codex, Claude Code, ChatGPT, Gemini,
   and Unity AI prompt handoff.
10. Add matrix coverage reports showing domains, interview modes, targets, and
    missing prompt combinations.
11. Add example manifests that reference candidate VeritySpec workspace files
    once workspace fixtures exist.
12. Add generated workspace outline validators for expected record categories.
13. Add image-input manifest fixtures for concept art and identity images.
14. Add provenance examples aligned with future VeritySpec evidence records.
15. Add cross-workspace dependency prompt guidance for shared Unity libraries
    and game portfolios.
16. Add portfolio triage prompts for batches of many game concepts.
17. Add release-readiness gap review prompts for generated VeritySpec
    workspaces.
18. Add maintenance and decommissioning interview flows for shipped products.
19. Add contributor docs for proposing new prompt workflows.
20. Add release-integrity checks for README, changelog, roadmap, package
    metadata, and release notes.

## Working Rule

No sprint is complete unless:

- Tests pass.
- CI passes or an external platform issue is recorded with local verification.
- Documentation and examples match the implemented behavior.
- New behavior has at least one executable test or CLI smoke check.
- The Next 20 roadmap points remain populated when the active roadmap is
  caught up.
