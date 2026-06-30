from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReleaseReviewDocsTests(unittest.TestCase):
    def test_release_review_docs_are_linked_from_readme(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        expected = [
            "docs/lifecycle-gap-to-verityspec.md",
            "docs/release-integrity-report-schema.md",
            "docs/report-schema-stability.md",
            "docs/release-reviewer-checklist.md",
        ]

        for target in expected:
            with self.subTest(target=target):
                self.assertIn(target, readme)

    def test_release_review_docs_preserve_authority_boundary(self) -> None:
        for relative in (
            "docs/lifecycle-gap-to-verityspec.md",
            "docs/report-schema-stability.md",
            "docs/release-reviewer-checklist.md",
        ):
            with self.subTest(relative=relative):
                text = (ROOT / relative).read_text(encoding="utf-8")
                self.assertIn("VeritySpec", text)
                self.assertIn("human", text.lower())


if __name__ == "__main__":
    unittest.main()
