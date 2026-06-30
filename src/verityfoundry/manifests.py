"""Manifest discovery and parsing for VerityFoundry."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import sysconfig
from typing import Any, Iterable


class ManifestError(ValueError):
    """Raised when a manifest cannot be parsed."""


@dataclass(frozen=True)
class MarkdownManifest:
    """A parsed markdown file with JSON front matter."""

    path: Path
    manifest: dict[str, Any]
    body: str


def find_project_root(start: str | Path | None = None) -> Path:
    """Find the nearest VerityFoundry artifact root from a starting path."""

    current = Path(start or ".").resolve()
    explicit_start = start is not None
    if current.is_file():
        current = current.parent

    for candidate in [current, *current.parents]:
        if _has_artifact_root(candidate) and (
            (candidate / "pyproject.toml").exists() or explicit_start
        ):
            return candidate

    if not explicit_start:
        bundled = bundled_artifact_root()
        if bundled is not None:
            return bundled

    return current


def _has_artifact_root(path: Path) -> bool:
    """Return whether a path contains the deterministic prompt artifacts."""

    return all(
        (path / name).exists()
        for name in ("prompts", "matrices", "schemas", "examples", "goldens")
    )


def bundled_artifact_root() -> Path | None:
    """Return the installed prompt artifact root when available."""

    override = os.environ.get("VERITYFOUNDRY_ASSET_ROOT")
    candidates = []
    if override:
        candidates.append(Path(override))

    data_root = Path(sysconfig.get_path("data")) / "share" / "verityfoundry"
    candidates.append(data_root)

    for candidate in candidates:
        if _has_artifact_root(candidate):
            return candidate.resolve()
    return None


def read_json(path: Path) -> dict[str, Any]:
    """Read a JSON object from a path."""

    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ManifestError(f"{path}: invalid JSON: {exc.msg}") from exc

    if not isinstance(value, dict):
        raise ManifestError(f"{path}: expected a JSON object")
    return value


def parse_markdown_manifest(path: Path) -> MarkdownManifest:
    """Parse JSON front matter from a markdown file."""

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ManifestError(f"{path}: missing JSON front matter")

    end_index: int | None = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break

    if end_index is None:
        raise ManifestError(f"{path}: unterminated JSON front matter")

    raw_manifest = "\n".join(lines[1:end_index])
    raw_body = "\n".join(lines[end_index + 1 :]).strip() + "\n"
    try:
        manifest = json.loads(raw_manifest)
    except json.JSONDecodeError as exc:
        raise ManifestError(f"{path}: invalid front matter JSON: {exc.msg}") from exc

    if not isinstance(manifest, dict):
        raise ManifestError(f"{path}: front matter must be a JSON object")
    return MarkdownManifest(path=path, manifest=manifest, body=raw_body)


def prompt_paths(root: str | Path) -> list[Path]:
    """Return all prompt markdown paths."""

    base = Path(root) / "prompts"
    if not base.exists():
        return []
    return sorted(base.rglob("*.md"))


def matrix_paths(root: str | Path) -> list[Path]:
    """Return all matrix markdown paths."""

    base = Path(root) / "matrices"
    if not base.exists():
        return []
    return sorted(base.glob("*.md"))


def example_manifest_paths(root: str | Path) -> list[Path]:
    """Return all example manifest paths."""

    base = Path(root) / "examples"
    if not base.exists():
        return []
    return sorted(base.rglob("manifest.json"))


def golden_manifest_paths(root: str | Path) -> list[Path]:
    """Return all golden output manifest paths."""

    base = Path(root) / "goldens"
    if not base.exists():
        return []
    return sorted(base.rglob("manifest.json"))


def load_prompt_manifests(root: str | Path) -> list[MarkdownManifest]:
    """Load all prompt manifests from a project root."""

    return [parse_markdown_manifest(path) for path in prompt_paths(root)]


def load_matrix_manifests(root: str | Path) -> list[MarkdownManifest]:
    """Load all matrix manifests from a project root."""

    return [parse_markdown_manifest(path) for path in matrix_paths(root)]


def load_example_manifests(root: str | Path) -> list[tuple[Path, dict[str, Any]]]:
    """Load all example manifests from a project root."""

    return [(path, read_json(path)) for path in example_manifest_paths(root)]


def load_golden_manifests(root: str | Path) -> list[tuple[Path, dict[str, Any]]]:
    """Load all golden output manifests from a project root."""

    return [(path, read_json(path)) for path in golden_manifest_paths(root)]


def by_id(items: Iterable[MarkdownManifest]) -> dict[str, MarkdownManifest]:
    """Index markdown manifests by their `id` field."""

    indexed: dict[str, MarkdownManifest] = {}
    for item in items:
        item_id = item.manifest.get("id")
        if isinstance(item_id, str):
            indexed[item_id] = item
    return indexed
