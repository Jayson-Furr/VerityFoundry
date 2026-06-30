"""Deterministic prompt rendering."""

from __future__ import annotations

from pathlib import Path

from .manifests import by_id, load_prompt_manifests


def render_prompt(root: str | Path, prompt_id: str) -> str:
    """Render a prompt with its included common sections."""

    prompts = by_id(load_prompt_manifests(root))
    if prompt_id not in prompts:
        known = ", ".join(sorted(prompts))
        raise KeyError(f"unknown prompt id {prompt_id!r}; known prompts: {known}")

    prompt = prompts[prompt_id]
    manifest = prompt.manifest
    parts = [
        "# VerityFoundry Rendered Prompt",
        "",
        f"Prompt ID: `{prompt_id}`",
        f"Name: {manifest.get('name', prompt_id)}",
        f"Version: {manifest.get('version', 'unknown')}",
        f"Interview mode: {manifest.get('interviewMode', 'unspecified')}",
        f"Target readiness: {manifest.get('targetReadiness', 'unspecified')}",
        "",
    ]

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
