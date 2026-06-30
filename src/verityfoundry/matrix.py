"""Prompt matrix helpers."""

from __future__ import annotations

from pathlib import Path

from .manifests import load_matrix_manifests


def render_matrix(root: str | Path, matrix_name: str) -> str:
    """Render a matrix by ID or filename stem."""

    matrices = load_matrix_manifests(root)
    for matrix in matrices:
        matrix_id = matrix.manifest.get("id")
        if matrix_id == matrix_name or matrix.path.stem == matrix_name:
            title = matrix.manifest.get("name", matrix_name)
            return f"# {title}\n\n{matrix.body.strip()}\n"

    known = ", ".join(sorted(str(item.manifest.get("id", item.path.stem)) for item in matrices))
    raise KeyError(f"unknown matrix {matrix_name!r}; known matrices: {known}")
