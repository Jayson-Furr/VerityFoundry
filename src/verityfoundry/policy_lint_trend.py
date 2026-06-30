"""Policy-lint trend reporting for release review."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

from .manifests import read_json
from .policy_lint import (
    SEVERITY_ERROR,
    SEVERITY_WARNING,
    PolicyLintIssue,
    count_policy_lint_severities,
    lint_decision_policy,
)


def generate_policy_lint_trend_report(root: str | Path) -> dict[str, Any]:
    """Compare current policy-lint counts with checked-in snapshots."""

    root_path = Path(root)
    issues = lint_decision_policy(root_path)
    current = _summary(issues)
    snapshots = _load_snapshots(root_path)
    latest = snapshots[-1] if snapshots else None

    return {
        "status": "passed",
        "snapshotCount": len(snapshots),
        "snapshots": snapshots,
        "current": current,
        "latestSnapshot": latest,
        "deltaFromLatest": _delta(current, latest) if latest else None,
    }


def format_policy_lint_trend_report(report: dict[str, Any]) -> str:
    """Format policy-lint trend results for humans."""

    current = report["current"]
    lines = [
        "Policy Lint Trend Report",
        "",
        f"Snapshots: {report['snapshotCount']}",
        (
            "Current: "
            f"{current['errorCount']} errors, "
            f"{current['warningCount']} warnings"
        ),
    ]

    latest = report["latestSnapshot"]
    if latest:
        lines.append(
            "Latest snapshot: "
            f"{latest['label']} "
            f"{latest['errorCount']} errors, "
            f"{latest['warningCount']} warnings"
        )
        delta = report["deltaFromLatest"]
        lines.append(
            "Delta: "
            f"{delta['errorCount']:+d} errors, "
            f"{delta['warningCount']:+d} warnings"
        )
    else:
        lines.append("Latest snapshot: none")

    return "\n".join(lines) + "\n"


def _summary(issues: list[PolicyLintIssue]) -> dict[str, Any]:
    counts = count_policy_lint_severities(issues)
    code_counts = Counter(issue.code for issue in issues)
    return {
        "issueCount": len(issues),
        "errorCount": counts[SEVERITY_ERROR],
        "warningCount": counts[SEVERITY_WARNING],
        "issueCodeCounts": dict(sorted(code_counts.items())),
    }


def _load_snapshots(root: Path) -> list[dict[str, Any]]:
    snapshot_dir = root / "snapshots" / "policy-lint"
    if not snapshot_dir.exists():
        return []

    snapshots = []
    for path in sorted(snapshot_dir.glob("*.json")):
        data = read_json(path)
        snapshots.append(
            {
                "label": data.get("label", path.stem),
                "issueCount": int(data.get("issueCount", 0)),
                "errorCount": int(data.get("errorCount", 0)),
                "warningCount": int(data.get("warningCount", 0)),
                "issueCodeCounts": data.get("issueCodeCounts", {}),
                "path": str(path.relative_to(root)),
            }
        )
    return snapshots


def _delta(current: dict[str, Any], latest: dict[str, Any]) -> dict[str, int]:
    return {
        "issueCount": int(current["issueCount"]) - int(latest["issueCount"]),
        "errorCount": int(current["errorCount"]) - int(latest["errorCount"]),
        "warningCount": int(current["warningCount"]) - int(latest["warningCount"]),
    }
