from pathlib import Path
from typing import Any
import unittest

from verityfoundry.manifests import load_example_manifests, read_json
from verityfoundry.validation import validate_examples


ROOT = Path(__file__).resolve().parents[1]


def fixture_categories(value: dict[str, Any]) -> set[str]:
    categories = set()
    for record in value.get("records", []):
        if isinstance(record, dict) and isinstance(record.get("kind"), str):
            categories.add(record["kind"])
    return categories


class ExampleTests(unittest.TestCase):
    def test_examples_validate(self) -> None:
        self.assertEqual(validate_examples(ROOT), [])

    def test_expected_examples_exist(self) -> None:
        ids = {manifest["id"] for _, manifest in load_example_manifests(ROOT)}
        self.assertEqual(
            ids,
            {
                "example.product.customer-portal",
                "example.software-library.shared-auth-library",
                "example.unity-game.dream-extraction",
                "example.unity-shared-library.shared-unity-runtime",
            },
        )

    def test_examples_declare_workspace_fixtures_and_provenance(self) -> None:
        for manifest_path, manifest in load_example_manifests(ROOT):
            with self.subTest(example=manifest["id"]):
                self.assertTrue(manifest.get("workspaceFixtures"))
                self.assertTrue(manifest.get("expectedRecordCategories"))
                self.assertTrue(manifest.get("provenanceExamples"))

                categories: set[str] = set()
                for relative in manifest["workspaceFixtures"]:
                    fixture = read_json(manifest_path.parent / relative)
                    categories.update(fixture_categories(fixture))

                self.assertTrue(
                    set(manifest["expectedRecordCategories"]).issubset(categories)
                )


if __name__ == "__main__":
    unittest.main()
