# Dependency Brief

The studio wants to map candidate dependencies between game workspaces and a
shared Unity runtime workspace.

Consumer workspaces:

- `studio.game.dream_extraction`
- `studio.game.space_runners`

Provider workspace:

- `studio.library.shared_unity_runtime`

Candidate dependency alias:

- `sharedUnity`

Known candidate capabilities:

- save system
- telemetry client
- liveops config loader

Unknowns:

- exact shared runtime version
- exported/public record list
- lockfile state
- canonical cross-workspace URI syntax
- whether save system and telemetry client are public or internal records
