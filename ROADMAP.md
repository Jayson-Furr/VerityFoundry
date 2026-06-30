# Roadmap

VerityFoundry is the prompt workflow companion to VeritySpec. It fabricates,
interviews for, refines, and gap-reviews candidate VeritySpec workspace drafts
while preserving uncertainty and human approval requirements.

## v0.1.0

The `v0.1.0` milestone is released.

| Sprint | Status | Focus |
|---:|---|---|
| 1 | Complete | Repository scaffold, AI-agent entry point, prompt manifest schema, and basic validation CLI |
| 2 | Complete | Interview modes and readiness target documentation |
| 3 | Complete | Unity game prompt matrix and examples |
| 4 | Complete | Unity shared-library prompt matrix and examples |
| 5 | Complete | Decision policy and provenance rules hardening |
| 6 | Complete | Golden output examples and prompt quality rubric |
| 7 | Complete | VeritySpec integration documentation and generated workspace validation notes |
| 8 | Complete | v0.1.0 release preparation |

## Sprint 1 Priorities

- Create the installable `verityfoundry` package and CLI.
- Add machine-checkable prompt, matrix, example, and decision-policy schemas.
- Add the canonical `AGENTS.md` entry point and thin agent adapters.
- Add CI and local tests for deterministic repository validation.
- Add public project metadata and basic documentation.

## Sprint 8 Priorities

Sprint 8 should release the completed `v0.1.0` scope:

- Add v0.1.0 release notes.
- Update README release badge, latest-release text, install guidance, and
  release-notes link to `v0.1.0`.
- Add a GitHub release workflow that builds, checks, smoke-tests, uploads
  release assets, and creates the GitHub release on tags.
- Run local release verification, package build checks, `twine check`, wheel
  smoke tests, and GitHub Actions.
- Tag and publish the v0.1.0 GitHub release when checks pass.
- Close the v0.1.0 milestone after release verification.

## v0.2.0

The `v0.2.0` milestone is in progress.

| Sprint | Status | Focus |
|---:|---|---|
| 9 | Complete | Unity game implementation-ready golden output fixture |

## Sprint 9 Priorities

Sprint 9 should add the first deterministic golden output fixture:

- Add a golden output manifest schema and validator.
- Add `verityfoundry validate goldens`.
- Add a Unity game implementation-ready golden output fixture for Dream
  Extraction.
- Require golden outputs to preserve assumptions, unresolved decisions, human
  approval requirements, readiness gaps, and the VeritySpec validation loop.
- Add tests for golden manifest validation and CLI coverage.
- Update README, changelog, roadmap, and golden output guidance.
- Keep the Next 20 roadmap points populated after converting this item.

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

1. Add golden output fixtures for the Unity shared-library implementation prompt.
2. Add a prompt quality report that scores uncertainty preservation and
   provenance completeness.
3. Add a local VeritySpec integration smoke check that runs only when `verity`
   is available.
4. Add a software-library example for a shared authentication package.
5. Add a product example for a customer portal.
6. Add prompt manifests for operations-ready and archival-ready Unity game
   workflows.
7. Add a decision-policy linter for high-stakes invention risks.
8. Add Markdown rendering profiles for Codex, Claude Code, ChatGPT, Gemini,
   and Unity AI prompt handoff.
9. Add matrix coverage reports showing domains, interview modes, targets, and
    missing prompt combinations.
10. Add example manifests that reference candidate VeritySpec workspace files
    once workspace fixtures exist.
11. Add generated workspace outline validators for expected record categories.
12. Add image-input manifest fixtures for concept art and identity images.
13. Add provenance examples aligned with future VeritySpec evidence records.
14. Add cross-workspace dependency prompt guidance for shared Unity libraries
    and game portfolios.
15. Add portfolio triage prompts for batches of many game concepts.
16. Add release-readiness gap review prompts for generated VeritySpec
    workspaces.
17. Add maintenance and decommissioning interview flows for shipped products.
18. Add contributor docs for proposing new prompt workflows.
19. Add release-integrity checks for README, changelog, roadmap, package
    metadata, and release notes.
20. Add golden output drift review documentation for maintainers.

## Working Rule

No sprint is complete unless:

- Tests pass.
- CI passes or an external platform issue is recorded with local verification.
- Documentation and examples match the implemented behavior.
- New behavior has at least one executable test or CLI smoke check.
- The Next 20 roadmap points remain populated when the active roadmap is
  caught up.
