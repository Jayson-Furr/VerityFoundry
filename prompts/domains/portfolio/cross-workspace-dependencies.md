---
{
  "id": "portfolio.dependencies.interview-medium.implementation-ready.v1",
  "name": "Cross-Workspace Dependency Mapping",
  "version": "0.1.0",
  "kind": "domain-prompt",
  "domain": "portfolio",
  "interviewMode": "interview-medium-stakes",
  "targetReadiness": "implementation-ready",
  "inputTypes": [
    "portfolio-index",
    "game-workspace-summaries",
    "shared-library-workspace-summaries",
    "dependency-notes",
    "package-version-notes"
  ],
  "outputs": [
    "workspace-dependency-map",
    "cross-workspace-reference-candidates",
    "exported-record-assumptions",
    "version-and-lockfile-questions",
    "impact-analysis-questions"
  ],
  "decisionPolicyRef": "decision-policy.medium-stakes.v1",
  "includeRefs": [
    "common.verityspec-context.v1",
    "common.safety-and-uncertainty.v1",
    "common.provenance-rules.v1",
    "common.output-contract.v1",
    "target.implementation-ready.v1",
    "interview.medium-stakes.v1"
  ],
  "requiresHumanApproval": true,
  "notes": "Drafts dependency assumptions for future VeritySpec cross-workspace support while keeping unresolved dependency and lockfile decisions visible."
}
---

Map candidate dependencies between VeritySpec workspaces in a portfolio.

Identify workspace-level dependency candidates, such as games depending on a
shared Unity runtime, liveops SDK, telemetry SDK, localization runtime,
platform services library, backend service contract, design system, or shared
event-contract workspace.

For each dependency candidate, report:

- consuming workspace
- provider workspace
- proposed alias
- source path or repository assumption
- version constraint assumption
- candidate exported/public record references
- internal/private record risks
- deprecated or removed record risks
- lockfile and reproducibility questions
- impact-analysis questions for future diffs

Use friendly reference examples only as illustrative authoring syntax, such as
`sharedUnity::unity.package.save_system`. Mark canonical URI forms, lockfiles,
visibility rules, and transitive dependency policy as future VeritySpec
capabilities unless the input explicitly proves they already exist.

Do not silently invent compatibility, exported record status, package versions,
lockfile state, licensing rights, or implementation readiness. Leave missing
dependency facts unresolved and require human approval before implementation
or release decisions use the dependency map.
