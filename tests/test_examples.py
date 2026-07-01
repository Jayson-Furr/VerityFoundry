from pathlib import Path
import json
import shutil
import tempfile
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
                "example.portfolio.game-portfolio-triage",
                "example.portfolio.shared-unity-dependency-map",
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

    def test_expected_image_input_manifests_exist(self) -> None:
        manifests = {
            manifest["id"]: manifest
            for _, manifest in load_example_manifests(ROOT)
        }

        for example_id in (
            "example.product.customer-portal",
            "example.software-library.shared-auth-library",
            "example.unity-game.dream-extraction",
        ):
            with self.subTest(example=example_id):
                self.assertIn("inputs/image-manifest.json", manifests[example_id]["inputs"])

    def test_image_input_manifest_schema_is_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            shutil.copytree(ROOT / "schemas", temp_root / "schemas")
            shutil.copytree(ROOT / "prompts", temp_root / "prompts")
            shutil.copytree(ROOT / "examples", temp_root / "examples")

            image_manifest_path = (
                temp_root
                / "examples"
                / "unity-game"
                / "dream-extraction"
                / "inputs"
                / "image-manifest.json"
            )
            image_manifest = read_json(image_manifest_path)
            del image_manifest["images"][0]["interpretationLimits"]
            image_manifest_path.write_text(
                json.dumps(image_manifest, indent=2) + "\n",
                encoding="utf-8",
            )

            issues = validate_examples(temp_root)
            self.assertTrue(
                any(issue.code == "example.image-manifest.schema" for issue in issues),
                [issue.format() for issue in issues],
            )


if __name__ == "__main__":
    unittest.main()
