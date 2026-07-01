# VerityFoundry Rendered Prompt

Prompt ID: `unity-game.gdd-art.interview-medium.implementation-ready.v1`
Name: Unity Game GDD and Art to Implementation-Ready Workspace
Version: 0.1.0
Profile: GitHub Copilot
Interview mode: interview-medium-stakes
Target readiness: implementation-ready

## Agent Handoff Profile

- Use this prompt as bounded repository context for Copilot-assisted edits.
- Preserve source references, assumptions, unresolved decisions, and approval gates in generated output.
- Keep changes aligned with repository tests, docs, examples, changelog, and roadmap expectations.
- Do not treat Copilot-generated VeritySpec workspace drafts as validated product truth.

## Included: VeritySpec Context

VeritySpec is the executable product-contract framework. VerityFoundry is the
AI-assisted authoring and prompt workflow layer.

Use this relationship:

```text
VeritySpec    = contract engine
VerityFoundry = candidate authoring workflow
```

Do not claim that VerityFoundry validates final product truth. It may create a
candidate workspace draft, but VeritySpec validation, linting, readiness, graph
checks, and human review remain required.

## Included: Safety and Uncertainty Rules

Preserve uncertainty. Separate facts from assumptions.

Bad posture:

```text
The game is implementation-ready.
```

Better posture:

```text
The workspace draft is structurally organized for prototype review. It is not
implementation-ready because platform, save-system, telemetry, QA, liveops,
and production ownership decisions remain unresolved.
```

Unknown sensitive commitments must remain unknown until a human provides and
approves them.

## Included: Provenance Rules

Every candidate output should identify whether information came from a
user-provided field, rough design document, concept art interpretation,
identity image interpretation, AI inference, AI default, human interview
answer, prior VeritySpec record, or documented external source.

Recommended provenance fields:

```json
{
  "sourceRefs": ["source.gdd.main"],
  "fabricationMode": "interview-medium-stakes",
  "decisionSource": "ai-inferred",
  "confidence": "medium",
  "humanApprovalRequired": true
}
```

If a source is unclear, mark it as unresolved instead of fabricating certainty.

## Included: Candidate Output Contract

When producing candidate VeritySpec authoring output, include these sections:

1. Candidate workspace outline.
2. Source material summary.
3. Human-provided decisions.
4. AI-inferred decisions.
5. AI-defaulted decisions.
6. AI-suggested decisions.
7. Unresolved decisions.
8. Human approval requirements.
9. Readiness gaps.
10. Suggested next interview questions.
11. Suggested VeritySpec validation loop.

Use precise language. Do not imply final readiness when the output is only a
candidate draft.

## Included: Implementation Ready Target

Implementation-ready drafts should give a human engineer or AI coding agent
bounded context: source records, constraints, dependencies, affected surfaces,
files or artifact classes, validation commands, evidence expectations, and
decisions that must not be invented.

## Included: Interview Medium Stakes

Ask questions that affect architecture, implementation, telemetry, production,
or team handoff. Clarify save model, platforms, liveops expectations,
telemetry, content pipeline, shared systems, release milestone, and ownership.

## Prompt Workflow

Create a candidate VeritySpec workspace outline for a Unity game from the
provided GDD and art notes.

Include candidate records for game identity, GDD source, visual identity,
concept art, core loop, session loop, progression loop, game modes, features,
Unity project assumptions, Unity package dependencies, shared runtime
assumptions, telemetry intent, QA gaps, implementation context, and readiness
gaps.

Ask or mark unresolved any production platform, save model, multiplayer,
telemetry, content pipeline, monetization, liveops, legal, licensing,
certification, privacy, or archival decision that is not provided.
