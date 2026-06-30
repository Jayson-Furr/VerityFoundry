"""Deterministic prompt quality reporting."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .manifests import load_prompt_manifests
from .rendering import render_prompt


UNCERTAINTY_CHECKS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("assumptions-or-defaults", ("assumption", "default")),
    ("ai-decision-separation", ("ai-inferred", "ai inference", "ai-defaulted", "ai-suggested")),
    ("unresolved-decisions", ("unresolved", "unknown")),
    ("human-approval", ("human approval", "humanapprovalrequired", "requireshumanapproval")),
    ("readiness-caveat", ("candidate draft", "not implementation-ready", "do not imply final readiness")),
    ("high-stakes-invention-guard", ("must not invent", "do not claim", "legal", "privacy", "certification")),
)

PROVENANCE_CHECKS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("source-references", ("sourcerefs", "source refs", "source material", "source references")),
    ("decision-provenance", ("provenance", "decisionsource", "decision provenance")),
    ("confidence", ("confidence",)),
    ("human-vs-ai-sources", ("human-provided", "user-provided", "ai-inferred", "ai default")),
    (
        "verityspec-validation-authority",
        ("verity validate", "verityspec remains", "validation authority", "suggested verityspec validation"),
    ),
)


def _normalized(value: str) -> str:
    return value.lower().replace("_", "-")


def _matched_checks(text: str, checks: tuple[tuple[str, tuple[str, ...]], ...]) -> list[str]:
    normalized = _normalized(text)
    compact = normalized.replace("-", "")
    matched: list[str] = []
    for name, terms in checks:
        if any(term in normalized or term.replace("-", "") in compact for term in terms):
            matched.append(name)
    return matched


def _score(text: str, checks: tuple[tuple[str, tuple[str, ...]], ...]) -> dict[str, Any]:
    matched = _matched_checks(text, checks)
    missing = [name for name, _ in checks if name not in matched]
    max_score = len(checks)
    score = len(matched)
    return {
        "score": score,
        "maxScore": max_score,
        "percent": round((score / max_score) * 100, 1) if max_score else 100.0,
        "matched": matched,
        "missing": missing,
    }


def generate_prompt_quality_report(root: str | Path) -> dict[str, Any]:
    """Score prompt workflows for uncertainty and provenance evidence."""

    root_path = Path(root)
    prompt_items = []
    for prompt in load_prompt_manifests(root_path):
        prompt_id = str(prompt.manifest.get("id", prompt.path.stem))
        rendered = render_prompt(root_path, prompt_id)
        uncertainty = _score(rendered, UNCERTAINTY_CHECKS)
        provenance = _score(rendered, PROVENANCE_CHECKS)
        combined_score = uncertainty["score"] + provenance["score"]
        combined_max = uncertainty["maxScore"] + provenance["maxScore"]
        prompt_items.append(
            {
                "id": prompt_id,
                "name": prompt.manifest.get("name", prompt_id),
                "kind": prompt.manifest.get("kind", "unknown"),
                "domain": prompt.manifest.get("domain", "unknown"),
                "path": str(prompt.path.relative_to(root_path)),
                "uncertaintyPreservation": uncertainty,
                "provenanceCompleteness": provenance,
                "score": combined_score,
                "maxScore": combined_max,
                "percent": round((combined_score / combined_max) * 100, 1) if combined_max else 100.0,
            }
        )

    prompt_items.sort(key=lambda item: (item["percent"], item["id"]))
    prompt_count = len(prompt_items)
    total_score = sum(int(item["score"]) for item in prompt_items)
    total_max = sum(int(item["maxScore"]) for item in prompt_items)
    uncertainty_score = sum(int(item["uncertaintyPreservation"]["score"]) for item in prompt_items)
    uncertainty_max = sum(int(item["uncertaintyPreservation"]["maxScore"]) for item in prompt_items)
    provenance_score = sum(int(item["provenanceCompleteness"]["score"]) for item in prompt_items)
    provenance_max = sum(int(item["provenanceCompleteness"]["maxScore"]) for item in prompt_items)

    return {
        "promptCount": prompt_count,
        "score": total_score,
        "maxScore": total_max,
        "percent": round((total_score / total_max) * 100, 1) if total_max else 100.0,
        "uncertaintyPreservation": {
            "score": uncertainty_score,
            "maxScore": uncertainty_max,
            "percent": round((uncertainty_score / uncertainty_max) * 100, 1) if uncertainty_max else 100.0,
        },
        "provenanceCompleteness": {
            "score": provenance_score,
            "maxScore": provenance_max,
            "percent": round((provenance_score / provenance_max) * 100, 1) if provenance_max else 100.0,
        },
        "weakestPrompts": prompt_items[:5],
        "prompts": prompt_items,
    }


def format_prompt_quality_report(report: dict[str, Any]) -> str:
    """Format a prompt quality report for humans."""

    lines = [
        "Prompt Quality Report",
        "",
        f"Prompts: {report['promptCount']}",
        f"Overall score: {report['score']}/{report['maxScore']} ({report['percent']}%)",
        (
            "Uncertainty preservation: "
            f"{report['uncertaintyPreservation']['score']}/"
            f"{report['uncertaintyPreservation']['maxScore']} "
            f"({report['uncertaintyPreservation']['percent']}%)"
        ),
        (
            "Provenance completeness: "
            f"{report['provenanceCompleteness']['score']}/"
            f"{report['provenanceCompleteness']['maxScore']} "
            f"({report['provenanceCompleteness']['percent']}%)"
        ),
        "",
        "Weakest prompts:",
    ]

    for prompt in report["weakestPrompts"]:
        lines.append(
            f"- {prompt['id']}: {prompt['score']}/{prompt['maxScore']} "
            f"({prompt['percent']}%) at {prompt['path']}"
        )
        missing_uncertainty = prompt["uncertaintyPreservation"]["missing"]
        missing_provenance = prompt["provenanceCompleteness"]["missing"]
        if missing_uncertainty:
            lines.append(f"  Missing uncertainty checks: {', '.join(missing_uncertainty)}")
        if missing_provenance:
            lines.append(f"  Missing provenance checks: {', '.join(missing_provenance)}")

    return "\n".join(lines) + "\n"
