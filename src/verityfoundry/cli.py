"""Command-line interface for VerityFoundry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from . import __version__
from .integration import check_verityspec, format_verityspec_check_result
from .inventory import (
    format_example_inventory_report,
    format_golden_inventory_report,
    generate_example_inventory_report,
    generate_golden_inventory_report,
)
from .manifests import find_project_root, load_matrix_manifests, load_prompt_manifests
from .matrix import render_matrix
from .matrix_coverage import format_matrix_coverage_report, generate_matrix_coverage_report
from .policy_lint import (
    SEVERITY_ERROR,
    SEVERITY_WARNING,
    count_policy_lint_severities,
    format_policy_lint_issues,
    lint_decision_policy,
)
from .quality import format_prompt_quality_report, generate_prompt_quality_report
from .quality_trend import (
    format_prompt_quality_trend_report,
    generate_prompt_quality_trend_report,
)
from .rendering import render_profiles, render_prompt
from .release_integrity import check_release_integrity, format_release_integrity_report
from .thresholds import check_quality_thresholds, format_quality_threshold_report
from .validation import (
    validate_all,
    validate_examples,
    validate_goldens,
    validate_matrices,
    validate_prompts,
)
from .workflow_hygiene import check_workflow_hygiene, format_workflow_hygiene_report

EXIT_OK = 0
EXIT_VALIDATION_FAILED = 1
EXIT_USAGE_ERROR = 2
EXIT_INTERNAL_ERROR = 3


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="verityfoundry")
    parser.add_argument("--version", action="version", version=f"verityfoundry {__version__}")
    parser.add_argument(
        "--root",
        help="Artifact root. Defaults to the current checkout or installed prompt library.",
    )

    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser("list", help="List prompt workflow artifacts.")
    list_parser.add_argument("artifact", choices=["prompts", "matrices", "profiles"])
    list_parser.add_argument("--format", choices=["text", "json"], default="text")

    validate_parser = subparsers.add_parser("validate", help="Validate prompt workflow artifacts.")
    validate_parser.add_argument(
        "target",
        nargs="?",
        choices=["all", "prompts", "matrices", "examples", "goldens"],
        default="all",
    )
    validate_parser.add_argument("--format", choices=["text", "json"], default="text")

    render_parser = subparsers.add_parser("render", help="Render a prompt workflow by ID.")
    render_parser.add_argument("--prompt", required=True, help="Prompt ID to render.")
    render_parser.add_argument(
        "--profile",
        choices=[profile["id"] for profile in render_profiles()],
        default="default",
        help="Optional agent handoff profile.",
    )
    render_parser.add_argument("--out", help="Optional output path.")

    matrix_parser = subparsers.add_parser("matrix", help="Render a prompt matrix by ID.")
    matrix_parser.add_argument("name", help="Matrix ID or filename stem.")
    matrix_parser.add_argument("--out", help="Optional output path.")

    report_parser = subparsers.add_parser("report", help="Generate deterministic local reports.")
    report_parser.add_argument(
        "target",
        choices=[
            "prompt-quality",
            "prompt-quality-trend",
            "matrix-coverage",
            "golden-inventory",
            "example-inventory",
        ],
    )
    report_parser.add_argument("--format", choices=["text", "json"], default="text")

    check_parser = subparsers.add_parser("check", help="Run optional local integration checks.")
    check_subparsers = check_parser.add_subparsers(dest="check_target", required=True)
    verityspec_parser = check_subparsers.add_parser(
        "verityspec",
        help="Run an optional VeritySpec smoke check when `verity` is available.",
    )
    verityspec_parser.add_argument(
        "--workspace",
        help="Optional VeritySpec workspace path to validate when `verity` is available.",
    )
    verityspec_parser.add_argument(
        "--verity",
        help="Path or command name for the VeritySpec CLI. Defaults to `verity` on PATH.",
    )
    verityspec_parser.add_argument("--format", choices=["text", "json"], default="text")

    release_integrity_parser = check_subparsers.add_parser(
        "release-integrity",
        help="Check release/version bookkeeping across package metadata and docs.",
    )
    release_integrity_parser.add_argument(
        "--expected-version",
        help="Expected package version. Defaults to the version in pyproject.toml.",
    )
    release_integrity_parser.add_argument("--format", choices=["text", "json"], default="text")

    quality_thresholds_parser = check_subparsers.add_parser(
        "quality-thresholds",
        help="Check prompt quality and matrix coverage against release thresholds.",
    )
    quality_thresholds_parser.add_argument(
        "--config",
        help="Optional threshold config path. Defaults to config/release-quality-thresholds.json.",
    )
    quality_thresholds_parser.add_argument("--format", choices=["text", "json"], default="text")

    workflow_hygiene_parser = check_subparsers.add_parser(
        "workflow-hygiene",
        help="Check GitHub Actions workflow action versions for known hygiene risks.",
    )
    workflow_hygiene_parser.add_argument("--format", choices=["text", "json"], default="text")

    lint_parser = subparsers.add_parser("lint", help="Run deterministic local linters.")
    lint_parser.add_argument("target", choices=["decision-policy"])
    lint_parser.add_argument("--format", choices=["text", "json"], default="text")

    return parser


def _root(value: str | None) -> Path:
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
    elif args.artifact == "matrices":
        items = [
            {
                "id": item.manifest.get("id"),
                "name": item.manifest.get("name"),
                "domain": item.manifest.get("domain"),
                "path": str(item.path.relative_to(root)),
            }
            for item in load_matrix_manifests(root)
        ]
    else:
        items = render_profiles()

    if args.format == "json":
        print(json.dumps(items, indent=2, sort_keys=True))
    else:
        for item in items:
            if "path" in item:
                print(f"{item['id']}\t{item['name']}\t{item['path']}")
            else:
                print(f"{item['id']}\t{item['name']}")
    return EXIT_OK


def _cmd_validate(args: argparse.Namespace) -> int:
    root = _root(args.root)
    if args.target == "prompts":
        issues = validate_prompts(root)
    elif args.target == "matrices":
        issues = validate_matrices(root)
    elif args.target == "examples":
        issues = validate_examples(root)
    elif args.target == "goldens":
        issues = validate_goldens(root)
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
    content = render_prompt(_root(args.root), args.prompt, profile=args.profile)
    _write_or_print(content, args.out)
    return EXIT_OK


def _cmd_matrix(args: argparse.Namespace) -> int:
    content = render_matrix(_root(args.root), args.name)
    _write_or_print(content, args.out)
    return EXIT_OK


def _cmd_report(args: argparse.Namespace) -> int:
    root = _root(args.root)
    if args.target == "matrix-coverage":
        report = generate_matrix_coverage_report(root)
        formatted = format_matrix_coverage_report(report)
    elif args.target == "prompt-quality":
        report = generate_prompt_quality_report(root)
        formatted = format_prompt_quality_report(report)
    elif args.target == "prompt-quality-trend":
        report = generate_prompt_quality_trend_report(root)
        formatted = format_prompt_quality_trend_report(report)
    elif args.target == "golden-inventory":
        report = generate_golden_inventory_report(root)
        formatted = format_golden_inventory_report(report)
    else:
        report = generate_example_inventory_report(root)
        formatted = format_example_inventory_report(report)

    if args.format == "json":
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(formatted, end="")
    return EXIT_OK


def _cmd_check(args: argparse.Namespace) -> int:
    root = _root(args.root)
    if args.check_target == "verityspec":
        result = check_verityspec(root, workspace=args.workspace, executable=args.verity)
        if args.format == "json":
            print(json.dumps(result.to_dict(), indent=2, sort_keys=True))
        else:
            print(format_verityspec_check_result(result), end="")
        return EXIT_VALIDATION_FAILED if result.status == "failed" else EXIT_OK
    if args.check_target == "release-integrity":
        report = check_release_integrity(root, expected_version=args.expected_version)
        if args.format == "json":
            print(json.dumps(report, indent=2, sort_keys=True))
        else:
            print(format_release_integrity_report(report), end="")
        return EXIT_VALIDATION_FAILED if report["status"] == "failed" else EXIT_OK
    if args.check_target == "quality-thresholds":
        report = check_quality_thresholds(root, config_path=args.config)
        if args.format == "json":
            print(json.dumps(report, indent=2, sort_keys=True))
        else:
            print(format_quality_threshold_report(report), end="")
        return EXIT_VALIDATION_FAILED if report["status"] == "failed" else EXIT_OK
    if args.check_target == "workflow-hygiene":
        report = check_workflow_hygiene(root)
        if args.format == "json":
            print(json.dumps(report, indent=2, sort_keys=True))
        else:
            print(format_workflow_hygiene_report(report), end="")
        return EXIT_VALIDATION_FAILED if report["status"] == "failed" else EXIT_OK
    return EXIT_USAGE_ERROR


def _cmd_lint(args: argparse.Namespace) -> int:
    root = _root(args.root)
    if args.target == "decision-policy":
        issues = lint_decision_policy(root)
        counts = count_policy_lint_severities(issues)
        if args.format == "json":
            payload = {
                "status": "failed" if counts[SEVERITY_ERROR] else "passed",
                "issueCount": len(issues),
                "errorCount": counts[SEVERITY_ERROR],
                "warningCount": counts[SEVERITY_WARNING],
                "issues": [issue.to_dict() for issue in issues],
            }
            print(json.dumps(payload, indent=2, sort_keys=True))
        else:
            print(format_policy_lint_issues(issues), end="")
        return EXIT_VALIDATION_FAILED if counts[SEVERITY_ERROR] else EXIT_OK
    return EXIT_USAGE_ERROR


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
        if args.command == "report":
            return _cmd_report(args)
        if args.command == "check":
            return _cmd_check(args)
        if args.command == "lint":
            return _cmd_lint(args)
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
