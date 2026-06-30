from pathlib import Path
import unittest

from verityfoundry.manifests import load_example_manifests
from verityfoundry.validation import validate_examples


ROOT = Path(__file__).resolve().parents[1]


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


if __name__ == "__main__":
    unittest.main()
