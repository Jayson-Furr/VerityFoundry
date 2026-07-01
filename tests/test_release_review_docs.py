from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReleaseReviewDocsTests(unittest.TestCase):
    def test_readme_relative_links_exist(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        missing: list[str] = []
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", readme):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            path_text = target.split("#", 1)[0]
            if not path_text:
                continue
            if not (ROOT / path_text).exists():
                missing.append(target)

        self.assertEqual(missing, [])

    def test_release_review_docs_are_linked_from_readme(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        expected = [
            "docs/lifecycle-gap-to-verityspec.md",
            "docs/release-integrity-report-schema.md",
            "docs/release-summary-report.md",
            "docs/report-schema-stability.md",
            "docs/release-reviewer-checklist.md",
            "docs/policy-lint-trends.md",
            "docs/fixture-inventory-report-schema.md",
            "docs/example-fixture-diff-snapshots.md",
            "docs/release-review-fixture-json-schema.md",
            "docs/release-review-fixture-updates.md",
            "docs/lifecycle-archival-drift-comparison.md",
            "docs/package-data-verification.md",
            "docs/readme-link-coverage.md",
            "docs/provenance-distribution.md",
            "docs/portfolio-coverage-report.md",
            "docs/fixture-to-verityspec-checklist.md",
            "docs/cross-workspace-reference-guidance.md",
            "docs/workflow-hygiene-history.md",
            "docs/action-version-policy.md",
            "docs/quality-threshold-ratcheting.md",
            "docs/render-profile-compatibility.md",
        ]

        for target in expected:
            with self.subTest(target=target):
                self.assertIn(target, readme)

    def test_release_review_docs_preserve_authority_boundary(self) -> None:
        for relative in (
            "docs/lifecycle-gap-to-verityspec.md",
            "docs/report-schema-stability.md",
            "docs/release-reviewer-checklist.md",
            "docs/release-summary-report.md",
            "docs/policy-lint-trends.md",
            "docs/fixture-inventory-report-schema.md",
            "docs/example-fixture-diff-snapshots.md",
            "docs/release-review-fixture-json-schema.md",
            "docs/release-review-fixture-updates.md",
            "docs/lifecycle-archival-drift-comparison.md",
            "docs/package-data-verification.md",
            "docs/readme-link-coverage.md",
            "docs/provenance-distribution.md",
            "docs/portfolio-coverage-report.md",
            "docs/fixture-to-verityspec-checklist.md",
            "docs/cross-workspace-reference-guidance.md",
        ):
            with self.subTest(relative=relative):
                text = (ROOT / relative).read_text(encoding="utf-8")
                self.assertIn("VeritySpec", text)
                self.assertIn("human", text.lower())


if __name__ == "__main__":
    unittest.main()
