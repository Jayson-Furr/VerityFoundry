# Portfolio Workflows

Portfolio workflows help teams turn many rough product or game ideas into
candidate VeritySpec workspace plans without erasing uncertainty.

The first supported portfolio workflows are:

- `portfolio.games.interview-low.concept-complete.v1`
- `portfolio.dependencies.interview-medium.implementation-ready.v1`

Render them with:

```bash
verityfoundry render --prompt portfolio.games.interview-low.concept-complete.v1 --profile codex
verityfoundry render --prompt portfolio.dependencies.interview-medium.implementation-ready.v1 --profile codex
verityfoundry matrix portfolio
```

## Game Portfolio Triage

Use game portfolio triage when the inputs are many rough game briefs, GDD
summaries, source-material indexes, concept-art indexes, identity-art indexes,
or shared-runtime assumptions.

Expected candidate outputs include:

- portfolio triage table
- candidate priority groups
- source-material coverage gaps
- shared dependency assumptions
- unresolved interview questions
- VeritySpec workspace drafting recommendations

The workflow should group concepts without claiming that any game is
implementation-ready, commercially cleared, licensed, platform approved,
funded, or liveops-ready unless the input evidence proves it.

The checked example at
`examples/portfolio/game-portfolio-triage/` demonstrates this workflow with a
small game portfolio sample. It includes inputs, expected outputs, a candidate
workspace fixture, and provenance examples.

## Cross-Workspace Dependency Mapping

Use dependency mapping when a portfolio contains multiple workspaces, such as
games, shared Unity runtimes, liveops SDKs, telemetry SDKs, platform services,
backend services, design systems, or event-contract workspaces.

Expected candidate outputs include:

- consuming workspace
- provider workspace
- proposed dependency alias
- source path or repository assumption
- version constraint assumption
- exported/public record candidates
- internal/private record risks
- deprecated or removed record risks
- lockfile and reproducibility questions
- future impact-analysis questions

Friendly references such as `sharedUnity::unity.package.save_system` should be
treated as illustrative authoring syntax. Canonical URI forms, lockfiles,
export visibility, transitive dependency policy, and compatibility reports
remain future VeritySpec responsibilities unless the input proves they already
exist.

See
[cross-workspace-reference-guidance.md](cross-workspace-reference-guidance.md)
for candidate reference syntax guidance, and use
`verityfoundry report portfolio-coverage` to inspect checked portfolio fixture
coverage by game concept and dependency assumption.

The checked example at
`examples/portfolio/shared-unity-dependency-map/` demonstrates this workflow
with game workspaces that may consume a shared Unity runtime workspace. It
keeps dependency aliases, version constraints, exported-record status,
lockfiles, and canonical URI forms unresolved unless source inputs prove them.

## Authority Boundary

VerityFoundry creates candidate plans and prompt outputs. VeritySpec remains
the validation authority for actual workspaces, record references, dependency
graphs, readiness, and release gates.
