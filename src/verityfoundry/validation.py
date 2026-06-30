"""Local validation for VerityFoundry prompt workflow artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from .manifests import (
    ManifestError,
    example_manifest_paths,
    load_example_manifests,
    load_matrix_manifests,
    load_prompt_manifests,
    read_json,
)


@dataclass(frozen=True)
class ValidationIssue:
    """A deterministic validation issue."""

    code: str
    message: str
    path: str

    def format(self) -> str:
        return f"{self.code}: {self.path}: {self.message}"


def _schema(root: Path, name: str) -> Draft202012Validator:
    return Draft202012Validator(read_json(root / "schemas" / name))


def _jsonschema_issues(
    validator: Draft202012Validator, data: dict[str, Any], path: Path, code: str
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.path)):
        location = "/".join(str(part) for part in error.path)
        suffix = f" at {location}" if location else ""
        issues.append(ValidationIssue(code, f"{error.message}{suffix}", str(path)))
    return issues


def validate_prompts(root: str | Path) -> list[ValidationIssue]:
    """Validate prompt markdown manifests and references."""

    root_path = Path(root)
    issues: list[ValidationIssue] = []
    try:
        prompts = load_prompt_manifests(root_path)
    except ManifestError as exc:
        return [ValidationIssue("prompt.parse", str(exc), str(root_path / "prompts"))]

    if not prompts:
        issues.append(ValidationIssue("prompt.missing", "no prompt markdown files found", str(root_path / "prompts")))
        return issues

    validator = _schema(root_path, "prompt-manifest.schema.json")
    ids: dict[str, Path] = {}

    for prompt in prompts:
        manifest = prompt.manifest
        prompt_id = manifest.get("id")
        issues.extend(_jsonschema_issues(validator, manifest, prompt.path, "prompt.schema"))

        if isinstance(prompt_id, str):
            if prompt_id in ids:
                issues.append(
                    ValidationIssue(
                        "prompt.duplicate-id",
                        f"duplicate prompt id {prompt_id!r}; first declared in {ids[prompt_id]}",
                        str(prompt.path),
                    )
                )
            ids[prompt_id] = prompt.path

        if not prompt.body.strip():
            issues.append(ValidationIssue("prompt.empty-body", "prompt body is empty", str(prompt.path)))

    known_ids = set(ids)
    for prompt in prompts:
        for include_ref in prompt.manifest.get("includeRefs", []):
            if include_ref not in known_ids:
                issues.append(
                    ValidationIssue(
                        "prompt.missing-include",
                        f"includeRefs references unknown prompt {include_ref!r}",
                        str(prompt.path),
                    )
                )

        policy_ref = prompt.manifest.get("decisionPolicyRef")
        if policy_ref and policy_ref not in known_ids:
            issues.append(
                ValidationIssue(
                    "prompt.missing-policy",
                    f"decisionPolicyRef references unknown prompt {policy_ref!r}",
                    str(prompt.path),
                )
            )

    return issues


def validate_matrices(root: str | Path) -> list[ValidationIssue]:
    """Validate matrix markdown manifests and prompt references."""

    root_path = Path(root)
    issues: list[ValidationIssue] = []
    try:
        matrices = load_matrix_manifests(root_path)
        prompts = load_prompt_manifests(root_path)
    except ManifestError as exc:
        return [ValidationIssue("matrix.parse", str(exc), str(root_path / "matrices"))]

    if not matrices:
        issues.append(ValidationIssue("matrix.missing", "no matrix markdown files found", str(root_path / "matrices")))
        return issues

    validator = _schema(root_path, "matrix-manifest.schema.json")
    prompt_ids = {
        prompt.manifest["id"]
        for prompt in prompts
        if isinstance(prompt.manifest.get("id"), str)
    }
    ids: dict[str, Path] = {}

    for matrix in matrices:
        manifest = matrix.manifest
        matrix_id = manifest.get("id")
        issues.extend(_jsonschema_issues(validator, manifest, matrix.path, "matrix.schema"))

        if isinstance(matrix_id, str):
            if matrix_id in ids:
                issues.append(
                    ValidationIssue(
                        "matrix.duplicate-id",
                        f"duplicate matrix id {matrix_id!r}; first declared in {ids[matrix_id]}",
                        str(matrix.path),
                    )
                )
            ids[matrix_id] = matrix.path

        if not matrix.body.strip():
            issues.append(ValidationIssue("matrix.empty-body", "matrix body is empty", str(matrix.path)))

        for row in manifest.get("rows", []):
            prompt_id = row.get("promptId")
            if prompt_id and prompt_id not in prompt_ids:
                issues.append(
                    ValidationIssue(
                        "matrix.unknown-prompt",
                        f"row references unknown prompt {prompt_id!r}",
                        str(matrix.path),
                    )
                )

    return issues


def validate_examples(root: str | Path) -> list[ValidationIssue]:
    """Validate example manifests and referenced files."""

    root_path = Path(root)
    issues: list[ValidationIssue] = []
    paths = example_manifest_paths(root_path)
    if not paths:
        return [ValidationIssue("example.missing", "no example manifest files found", str(root_path / "examples"))]

    validator = _schema(root_path, "example-manifest.schema.json")
    try:
        examples = load_example_manifests(root_path)
        prompts = load_prompt_manifests(root_path)
    except ManifestError as exc:
        return [ValidationIssue("example.parse", str(exc), str(root_path / "examples"))]

    prompt_ids = {
        prompt.manifest["id"]
        for prompt in prompts
        if isinstance(prompt.manifest.get("id"), str)
    }
    ids: dict[str, Path] = {}
    for path, manifest in examples:
        example_id = manifest.get("id")
        issues.extend(_jsonschema_issues(validator, manifest, path, "example.schema"))

        if isinstance(example_id, str):
            if example_id in ids:
                issues.append(
                    ValidationIssue(
                        "example.duplicate-id",
                        f"duplicate example id {example_id!r}; first declared in {ids[example_id]}",
                        str(path),
                    )
                )
            ids[example_id] = path

        for prompt_ref in manifest.get("promptRefs", []):
            if prompt_ref not in prompt_ids:
                issues.append(
                    ValidationIssue(
                        "example.unknown-prompt",
                        f"promptRefs references unknown prompt {prompt_ref!r}",
                        str(path),
                    )
                )

        base = path.parent
        for section in ("inputs", "expectedOutputs"):
            for relative in manifest.get(section, []):
                candidate = base / relative
                if not candidate.exists():
                    issues.append(
                        ValidationIssue(
                            "example.missing-file",
                            f"{section} references missing file {relative!r}",
                            str(path),
                        )
                    )

    return issues


def validate_all(root: str | Path) -> list[ValidationIssue]:
    """Validate all VerityFoundry managed artifacts."""

    issues: list[ValidationIssue] = []
    issues.extend(validate_prompts(root))
    issues.extend(validate_matrices(root))
    issues.extend(validate_examples(root))
    return issues
