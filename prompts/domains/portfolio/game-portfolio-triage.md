---
{
  "id": "portfolio.games.interview-low.concept-complete.v1",
  "name": "Game Portfolio Triage",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "portfolio",
  "interviewMode": "interview-low-stakes",
  "targetReadiness": "concept-complete",
  "inputTypes": [
    "game-briefs",
    "gdd-index",
    "concept-art-index",
    "identity-art-index",
    "shared-runtime-assumptions"
  ],
  "outputs": [
    "portfolio-triage-table",
    "candidate-priority-groups",
    "coverage-gaps",
    "shared-dependency-assumptions",
    "unresolved-questions"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1",
    "common.output-contract.v1",
    "target.concept-complete.v1",
    "interview.low-stakes.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Triages many game concepts without inventing production readiness, commercial approval, or implementation commitments."
}
---

Triage a portfolio of game concepts into candidate VeritySpec workspace
priorities.

For each game concept, identify candidate records or workspace areas for
product identity, GDD/source material, visual identity, concept art coverage,
core loop, target platforms, Unity/shared-runtime assumptions, telemetry
questions, prototype scope, and readiness gaps.

Group games by concept coverage and handoff readiness:

- strong candidate for immediate VeritySpec workspace drafting
- needs short interview before workspace drafting
- needs GDD/art/source-material cleanup
- blocked by missing ownership, platform, licensing, or strategic decisions

Preserve uncertainty. Do not claim a game is implementation-ready,
commercially cleared, platform approved, licensed, production funded, or
liveops-ready unless those facts are explicitly provided with evidence.
