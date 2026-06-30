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

## Authority Boundary

VerityFoundry creates candidate plans and prompt outputs. VeritySpec remains
the validation authority for actual workspaces, record references, dependency
graphs, readiness, and release gates.
