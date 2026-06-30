"""Deterministic prompt rendering."""

from __future__ import annotations

from pathlib import Path

from .manifests import by_id, load_prompt_manifests


RENDER_PROFILES: dict[str, dict[str, object]] = {
    "default": {
        "name": "Default",
        "guidance": [],
    },
    "codex": {
        "name": "Codex",
        "guidance": [
            "Treat this as bounded repository context for a concrete implementation task.",
            "Preserve assumptions, unresolved decisions, provenance, and human approval requirements.",
            "When editing a repository, update tests, docs, examples, and changelog together.",
            "Run local validation before handing off generated VeritySpec workspace drafts.",
        ],
    },
    "claude-code": {
        "name": "Claude Code",
        "guidance": [
            "Use this prompt as structured coding-agent context, not as final product truth.",
            "Keep uncertainty, source references, and approval gates visible in generated artifacts.",
            "Prefer small verifiable edits and report exact validation commands.",
            "Do not certify readiness without VeritySpec validation and human review.",
        ],
    },
    "chatgpt": {
        "name": "ChatGPT",
        "guidance": [
            "Use this prompt for candidate workspace drafting, gap review, and interview planning.",
            "Separate user-provided facts from AI inferences, defaults, and suggestions.",
            "Return unresolved questions and readiness gaps instead of inventing sensitive commitments.",
            "Treat generated records as drafts pending VeritySpec validation and human approval.",
        ],
    },
    "gemini": {
        "name": "Gemini",
        "guidance": [
            "Use this prompt for candidate workspace outlines and multimodal source-note review.",
            "Mark image or document interpretation as interpretation, not objective fact.",
            "Do not claim compliance, platform approval, licensing, privacy posture, or archival completion.",
            "Preserve provenance and recommend VeritySpec validation after drafting.",
        ],
    },
    "github-copilot": {
        "name": "GitHub Copilot",
        "guidance": [
            "Use this prompt as bounded repository context for Copilot-assisted edits.",
            "Preserve source references, assumptions, unresolved decisions, and approval gates in generated output.",
            "Keep changes aligned with repository tests, docs, examples, changelog, and roadmap expectations.",
            "Do not treat Copilot-generated VeritySpec workspace drafts as validated product truth.",
        ],
    },
    "unity-ai": {
        "name": "Unity AI",
        "guidance": [
            "Use this prompt to structure Unity game or shared-library workspace drafts.",
            "Keep Unity version, package, asset, scene, prefab, save, input, and telemetry assumptions explicit.",
            "Do not claim licensing, store approval, platform certification, or production readiness.",
            "Surface implementation, QA, liveops, maintenance, decommissioning, and archive gaps.",
        ],
    },
}


def render_profiles() -> list[dict[str, str]]:
    """Return available render profiles for CLI listing."""

    return [
        {"id": profile_id, "name": str(profile["name"])}
        for profile_id, profile in sorted(RENDER_PROFILES.items())
    ]


def render_prompt(root: str | Path, prompt_id: str, profile: str = "default") -> str:
    """Render a prompt with its included common sections."""

    prompts = by_id(load_prompt_manifests(root))
    if prompt_id not in prompts:
        known = ", ".join(sorted(prompts))
        raise KeyError(f"unknown prompt id {prompt_id!r}; known prompts: {known}")
    if profile not in RENDER_PROFILES:
        known_profiles = ", ".join(sorted(RENDER_PROFILES))
        raise KeyError(f"unknown render profile {profile!r}; known profiles: {known_profiles}")

    prompt = prompts[prompt_id]
    manifest = prompt.manifest
    profile_config = RENDER_PROFILES[profile]
    parts = [
        "# VerityFoundry Rendered Prompt",
        "",
        f"Prompt ID: `{prompt_id}`",
        f"Name: {manifest.get('name', prompt_id)}",
        f"Version: {manifest.get('version', 'unknown')}",
        f"Profile: {profile_config['name']}",
        f"Interview mode: {manifest.get('interviewMode', 'unspecified')}",
        f"Target readiness: {manifest.get('targetReadiness', 'unspecified')}",
        "",
    ]

    guidance = profile_config.get("guidance", [])
    if guidance:
        parts.extend(["## Agent Handoff Profile", ""])
        for item in guidance:
            parts.append(f"- {item}")
        parts.append("")

    for include_ref in manifest.get("includeRefs", []):
        included = prompts.get(include_ref)
        if included is None:
            continue
        parts.extend(
            [
                f"## Included: {included.manifest.get('name', include_ref)}",
                "",
                included.body.strip(),
                "",
            ]
        )

    parts.extend(["## Prompt Workflow", "", prompt.body.strip(), ""])
    return "\n".join(parts)
