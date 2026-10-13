import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "validar_cabecalho_documental.py"
SPEC = importlib.util.spec_from_file_location("document_validator", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class GovernanceDocumentValidationTests(unittest.TestCase):
    def test_canonical_hash_ignores_only_control_rows(self):
        sample = (
            "# Titulo\n\n| Campo | Valor |\n|---|---|\n"
            "| **SHA-256 (conteúdo canónico)** | placeholder |\n"
            "| **Commit de referência (versão anterior)** | N/A — documento inicial |\n"
        )
        canonical = MODULE.canonical_document_bytes(sample)
        self.assertIn(b"# Titulo", canonical)
        self.assertNotIn(b"placeholder", canonical)
        self.assertNotIn(b"Commit de refer", canonical)

    def test_canonical_hash_is_stable_for_crlf(self):
        sample = (
            "# Titulo\r\n\r\n| Campo | Valor |\r\n|---|---|\r\n"
            "| **SHA-256 (conteúdo canónico)** | abc |\r\n"
            "| **Commit de referência (versão anterior)** | N/A — documento inicial |\r\n"
        )
        self.assertEqual(
            MODULE.canonical_document_bytes(sample),
            MODULE.canonical_document_bytes(sample.replace("\r\n", "\n")),
        )

    def test_authority_chain_requires_canonical_plural(self):
        self.assertEqual(
            MODULE.CANONICAL_CHAIN, "PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO"
        )
        self.assertNotEqual(
            "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO", MODULE.CANONICAL_CHAIN
        )

    def test_link_scanner_detects_bad_relative_markdown_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.md").write_text("# Index\n\n[Bad](missing.md)\n", encoding="utf-8")
            errors = MODULE.validate_markdown_links(root, [root / "index.md"])
            self.assertTrue(any("missing.md" in error for error in errors))

    def test_duplicate_document_id_is_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "one.md").write_text(
                "# One\n\n| Campo | Valor |\n|---|---|\n| **ID** | SAME-001 |\n",
                encoding="utf-8",
            )
            (root / "two.md").write_text(
                "# Two\n\n| Campo | Valor |\n|---|---|\n| **ID** | SAME-001 |\n",
                encoding="utf-8",
            )
            errors, count = MODULE.scan_document_ids(root, [root / "one.md", root / "two.md"])
            self.assertEqual(count, 2)
            self.assertTrue(any("SAME-001" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
