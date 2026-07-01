"""Release integrity checks for public version bookkeeping."""

from __future__ import annotations

from dataclasses import dataclass
import re
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ReleaseIntegrityIssue:
    """A deterministic release-integrity issue."""

    code: str
    path: str
    message: str

    def to_dict(self) -> dict[str, str]:
        return {
            "code": self.code,
            "path": self.path,
            "message": self.message,
        }


def check_release_integrity(root: str | Path, expected_version: str | None = None) -> dict[str, Any]:
    """Check that release-facing version references agree."""

    root_path = Path(root)
    version = expected_version or _read_pyproject_version(root_path)
    tag = f"v{version}"
    issues: list[ReleaseIntegrityIssue] = []

    _expect_match(
        issues,
        root_path / "pyproject.toml",
        r'^version = "([^"]+)"',
        version,
        "release.pyproject-version",
        "pyproject.toml package version must match expected version",
    )
    _expect_match(
        issues,
        root_path / "src" / "verityfoundry" / "__init__.py",
        r'^__version__ = "([^"]+)"',
        version,
        "release.init-version",
        "package __version__ must match expected version",
    )
    _expect_contains(
        issues,
        root_path / "README.md",
        f"release-{tag}-blue",
        "release.readme-badge",
        "README release badge must reference the expected tag",
    )
    _expect_contains(
        issues,
        root_path / "README.md",
        f"Latest release: `{tag}`",
        "release.readme-latest",
        "README latest release text must reference the expected tag",
    )
    _expect_contains(
        issues,
        root_path / "README.md",
        f"verity-foundry.git@{tag}",
        "release.readme-install",
        "README install command must pin the expected tag",
    )
    _expect_contains(
        issues,
        root_path / "README.md",
        f"docs/release-notes-{tag}.md",
        "release.readme-release-notes",
        "README documentation links must include release notes for the expected tag",
    )
    _expect_latest_changelog(issues, root_path / "CHANGELOG.md", version)
    _expect_contains(
        issues,
        root_path / "ROADMAP.md",
        f"## {tag}",
        "release.roadmap-version",
        "ROADMAP must include a section for the expected tag",
    )
    _expect_contains(
        issues,
        root_path / "ROADMAP.md",
        f"The `{tag}` milestone is released.",
        "release.roadmap-released",
        "ROADMAP must mark the expected milestone as released",
    )
    _expect_contains(
        issues,
        root_path / "docs" / "release-checklist.md",
        f"VERSION={tag}",
        "release.checklist-version",
        "release checklist tag command must use the expected tag",
    )

    release_notes = root_path / "docs" / f"release-notes-{tag}.md"
    _expect_contains(
        issues,
        release_notes,
        f"# VerityFoundry {tag} Release Notes",
        "release.notes-title",
        "release notes must exist and use the expected title",
    )
    _expect_contains(
        issues,
        release_notes,
        f"Package version: `{version}`.",
        "release.notes-version",
        "release notes must mention the expected package version",
    )
    _expect_contains(
        issues,
        release_notes,
        f"verity-foundry.git@{tag}",
        "release.notes-install",
        "release notes install command must pin the expected tag",
    )

    return {
        "status": "failed" if issues else "passed",
        "expectedVersion": version,
        "expectedTag": tag,
        "issueCount": len(issues),
        "issues": [issue.to_dict() for issue in issues],
    }


def format_release_integrity_report(report: dict[str, Any]) -> str:
    """Format a release-integrity report for humans."""

    lines = [
        "Release Integrity Check",
        "",
        f"Expected version: {report['expectedVersion']}",
        f"Expected tag: {report['expectedTag']}",
    ]

    if report["issueCount"]:
        lines.extend(["", "Issues:"])
        for issue in report["issues"]:
            lines.append(f"- {issue['code']}: {issue['path']}: {issue['message']}")
    else:
        lines.extend(["", "Release integrity check passed."])

    return "\n".join(lines) + "\n"


def _read_pyproject_version(root: Path) -> str:
    path = root / "pyproject.toml"
    text = path.read_text(encoding="utf-8")
    match = re.search(r'^version = "([^"]+)"', text, re.MULTILINE)
    if not match:
        raise ValueError(f"{path}: missing project version")
    return match.group(1)


def _expect_match(
    issues: list[ReleaseIntegrityIssue],
    path: Path,
    pattern: str,
    expected: str,
    code: str,
    message: str,
) -> None:
    if not path.exists():
        issues.append(ReleaseIntegrityIssue(code, str(path), f"{message}; file is missing"))
        return
    text = path.read_text(encoding="utf-8")
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        issues.append(ReleaseIntegrityIssue(code, str(path), f"{message}; value not found"))
        return
    actual = match.group(1)
    if actual != expected:
        issues.append(
            ReleaseIntegrityIssue(
                code,
                str(path),
                f"{message}; expected {expected!r}, found {actual!r}",
            )
        )


def _expect_contains(
    issues: list[ReleaseIntegrityIssue],
    path: Path,
    expected_text: str,
    code: str,
    message: str,
) -> None:
    if not path.exists():
        issues.append(ReleaseIntegrityIssue(code, str(path), f"{message}; file is missing"))
        return
    if expected_text not in path.read_text(encoding="utf-8"):
        issues.append(
            ReleaseIntegrityIssue(
                code,
                str(path),
                f"{message}; missing {expected_text!r}",
            )
        )


def _expect_latest_changelog(
    issues: list[ReleaseIntegrityIssue], path: Path, expected_version: str
) -> None:
    if not path.exists():
        issues.append(
            ReleaseIntegrityIssue(
                "release.changelog-latest",
                str(path),
                "CHANGELOG must include the expected latest release; file is missing",
            )
        )
        return

    headings = re.findall(r"^## (.+)$", path.read_text(encoding="utf-8"), re.MULTILINE)
    releases = [heading.strip() for heading in headings if heading.strip() != "Unreleased"]
    if not releases:
        issues.append(
            ReleaseIntegrityIssue(
                "release.changelog-latest",
                str(path),
                "CHANGELOG must include at least one release heading",
            )
        )
        return
    latest = releases[0]
    if latest != expected_version:
        issues.append(
            ReleaseIntegrityIssue(
                "release.changelog-latest",
                str(path),
                f"latest CHANGELOG release must be {expected_version!r}; found {latest!r}",
            )
        )
