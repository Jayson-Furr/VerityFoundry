"""Command-line interface for VerityFoundry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from . import __version__
from .manifests import find_project_root, load_matrix_manifests, load_prompt_manifests
from .matrix import render_matrix
from .rendering import render_prompt
from .validation import validate_all, validate_examples, validate_matrices, validate_prompts

EXIT_OK = 0
EXIT_VALIDATION_FAILED = 1
EXIT_USAGE_ERROR = 2
EXIT_INTERNAL_ERROR = 3


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="verityfoundry")
    parser.add_argument("--version", action="version", version=f"verityfoundry {__version__}")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to the current directory.")

    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser("list", help="List prompt workflow artifacts.")
    list_parser.add_argument("artifact", choices=["prompts", "matrices"])
    list_parser.add_argument("--format", choices=["text", "json"], default="text")

    validate_parser = subparsers.add_parser("validate", help="Validate prompt workflow artifacts.")
    validate_parser.add_argument("target", nargs="?", choices=["all", "prompts", "matrices", "examples"], default="all")
    validate_parser.add_argument("--format", choices=["text", "json"], default="text")

    render_parser = subparsers.add_parser("render", help="Render a prompt workflow by ID.")
    render_parser.add_argument("--prompt", required=True, help="Prompt ID to render.")
    render_parser.add_argument("--out", help="Optional output path.")

    matrix_parser = subparsers.add_parser("matrix", help="Render a prompt matrix by ID.")
    matrix_parser.add_argument("name", help="Matrix ID or filename stem.")
    matrix_parser.add_argument("--out", help="Optional output path.")

    return parser


def _root(value: str) -> Path:
    return find_project_root(value)


def _write_or_print(content: str, out: str | None) -> None:
    if out:
        output = Path(out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(content, encoding="utf-8")
        print(f"Wrote {output}")
    else:
        print(content, end="")


def _cmd_list(args: argparse.Namespace) -> int:
    root = _root(args.root)
    if args.artifact == "prompts":
        items = [
            {
                "id": item.manifest.get("id"),
                "name": item.manifest.get("name"),
                "domain": item.manifest.get("domain"),
                "interviewMode": item.manifest.get("interviewMode"),
                "targetReadiness": item.manifest.get("targetReadiness"),
                "path": str(item.path.relative_to(root)),
            }
            for item in load_prompt_manifests(root)
        ]
    else:
        items = [
            {
                "id": item.manifest.get("id"),
                "name": item.manifest.get("name"),
                "domain": item.manifest.get("domain"),
                "path": str(item.path.relative_to(root)),
            }
            for item in load_matrix_manifests(root)
        ]

    if args.format == "json":
        print(json.dumps(items, indent=2, sort_keys=True))
    else:
        for item in items:
            print(f"{item['id']}\t{item['name']}\t{item['path']}")
    return EXIT_OK


def _cmd_validate(args: argparse.Namespace) -> int:
    root = _root(args.root)
    if args.target == "prompts":
        issues = validate_prompts(root)
    elif args.target == "matrices":
        issues = validate_matrices(root)
    elif args.target == "examples":
        issues = validate_examples(root)
    else:
        issues = validate_all(root)

    if args.format == "json":
        payload = {
            "status": "failed" if issues else "passed",
            "issueCount": len(issues),
            "issues": [issue.__dict__ for issue in issues],
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        if issues:
            print("Validation failed.")
            for issue in issues:
                print(f"- {issue.format()}")
        else:
            print("Validation passed.")

    return EXIT_VALIDATION_FAILED if issues else EXIT_OK


def _cmd_render(args: argparse.Namespace) -> int:
    content = render_prompt(_root(args.root), args.prompt)
    _write_or_print(content, args.out)
    return EXIT_OK


def _cmd_matrix(args: argparse.Namespace) -> int:
    content = render_matrix(_root(args.root), args.name)
    _write_or_print(content, args.out)
    return EXIT_OK


def run(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return EXIT_USAGE_ERROR

    try:
        if args.command == "list":
            return _cmd_list(args)
        if args.command == "validate":
            return _cmd_validate(args)
        if args.command == "render":
            return _cmd_render(args)
        if args.command == "matrix":
            return _cmd_matrix(args)
    except KeyError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return EXIT_USAGE_ERROR
    except Exception as exc:  # pragma: no cover - defensive CLI boundary
        print(f"ERROR: {exc}", file=sys.stderr)
        return EXIT_INTERNAL_ERROR

    parser.print_help()
    return EXIT_USAGE_ERROR


def main(argv: list[str] | None = None) -> int:
    return run(argv)
