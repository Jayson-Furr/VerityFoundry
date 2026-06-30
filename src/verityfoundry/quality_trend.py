"""Prompt quality trend reporting."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .manifests import read_json
from .quality import generate_prompt_quality_report


def generate_prompt_quality_trend_report(root: str | Path) -> dict[str, Any]:
    """Compare current prompt quality with checked-in snapshots."""

    root_path = Path(root)
    current = generate_prompt_quality_report(root_path)
    snapshots = _load_snapshots(root_path)
    latest = snapshots[-1] if snapshots else None

    return {
        "snapshotCount": len(snapshots),
        "snapshots": snapshots,
        "latestSnapshot": latest,
        "current": _summary("current", current),
        "deltaFromLatest": _delta(current, latest) if latest else None,
    }


def format_prompt_quality_trend_report(report: dict[str, Any]) -> str:
    """Format a prompt quality trend report for humans."""

    current = report["current"]
    lines = [
        "Prompt Quality Trend Report",
        "",
        f"Snapshots: {report['snapshotCount']}",
        (
            "Current: "
            f"{current['score']}/{current['maxScore']} ({current['percent']}%), "
            f"{current['promptCount']} prompts"
        ),
    ]

    latest = report["latestSnapshot"]
    if latest:
        delta = report["deltaFromLatest"]
        lines.extend(
            [
                (
                    "Latest snapshot: "
                    f"{latest['label']} "
                    f"{latest['score']}/{latest['maxScore']} ({latest['percent']}%)"
                ),
                (
                    "Delta: "
                    f"{_signed(delta['score'])} score, "
                    f"{_signed(delta['percent'])} percentage points, "
                    f"{_signed(delta['promptCount'])} prompts"
                ),
            ]
        )
    else:
        lines.append("Latest snapshot: none")

    return "\n".join(lines) + "\n"


def _load_snapshots(root: Path) -> list[dict[str, Any]]:
    snapshot_dir = root / "snapshots" / "prompt-quality"
    if not snapshot_dir.exists():
        return []

    snapshots = []
    for path in sorted(snapshot_dir.glob("*.json")):
        data = read_json(path)
        snapshots.append(
            {
                "label": data.get("label", path.stem),
                "path": str(path.relative_to(root)),
                "promptCount": int(data.get("promptCount", 0)),
                "score": int(data.get("score", 0)),
                "maxScore": int(data.get("maxScore", 0)),
                "percent": float(data.get("percent", 0.0)),
                "uncertaintyPercent": float(
                    data.get("uncertaintyPreservation", {}).get("percent", 0.0)
                ),
                "provenancePercent": float(
                    data.get("provenanceCompleteness", {}).get("percent", 0.0)
                ),
            }
        )
    return snapshots


def _summary(label: str, report: dict[str, Any]) -> dict[str, Any]:
    return {
        "label": label,
        "promptCount": int(report["promptCount"]),
        "score": int(report["score"]),
        "maxScore": int(report["maxScore"]),
        "percent": float(report["percent"]),
        "uncertaintyPercent": float(report["uncertaintyPreservation"]["percent"]),
        "provenancePercent": float(report["provenanceCompleteness"]["percent"]),
    }


def _delta(current: dict[str, Any], latest: dict[str, Any]) -> dict[str, Any]:
    return {
        "promptCount": int(current["promptCount"]) - int(latest["promptCount"]),
        "score": int(current["score"]) - int(latest["score"]),
        "maxScore": int(current["maxScore"]) - int(latest["maxScore"]),
        "percent": round(float(current["percent"]) - float(latest["percent"]), 1),
        "uncertaintyPercent": round(
            float(current["uncertaintyPreservation"]["percent"])
            - float(latest["uncertaintyPercent"]),
            1,
        ),
        "provenancePercent": round(
            float(current["provenanceCompleteness"]["percent"])
            - float(latest["provenancePercent"]),
            1,
        ),
    }


def _signed(value: int | float) -> str:
    if isinstance(value, float):
        return f"{value:+.1f}"
    return f"{value:+d}"
