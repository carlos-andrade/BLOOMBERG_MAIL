"""
BLOOMBERG_MAIL — protótipo offline de comparação de snapshots RTD.

IMPORTANTE:
- Apenas dados sintéticos.
- Não liga ao Excel/Profit.
- Não lê nem escreve ficheiros.
- Não grava histórico e não ativa captura persistente.
Executar: python TESTES_RTD_DD/prototipo_comparacao_snapshots_sinteticos.py
"""

from dataclasses import dataclass
from typing import Any, Mapping, Optional, Tuple


@dataclass(frozen=True)
class CellError:
    """Representa um erro RTD/Excel sintético; nunca é convertido em zero/vazio."""
    code: str


@dataclass(frozen=True)
class Comparison:
    status: str
    changed_fields: Tuple[str, ...] = ()
    reason: str = ""


class SnapshotComparator:
    """
    Compara snapshots completos em memória.

    A primeira leitura válida estabelece referência e não conta como alteração.
    Snapshots com erros são rejeitados e não substituem a última referência válida.
    A classe não executa qualquer persistência.
    """

    def __init__(self) -> None:
        self._previous: Optional[dict[str, Any]] = None

    @staticmethod
    def _validate(snapshot: Mapping[str, Any]) -> Optional[str]:
        if not snapshot:
            return "snapshot vazio"
        if any(not isinstance(key, str) or not key for key in snapshot):
            return "nome de campo inválido"
        if any(isinstance(value, CellError) for value in snapshot.values()):
            return "snapshot contém erro de célula"
        return None

    def observe(self, snapshot: Mapping[str, Any]) -> Comparison:
        reason = self._validate(snapshot)
        if reason:
            return Comparison("INVALID", reason=reason)

        current = dict(snapshot)

        if self._previous is None:
            self._previous = current
            return Comparison("BASELINE", reason="referência inicial; sem registo")

        if current.keys() != self._previous.keys():
            return Comparison(
                "INVALID",
                reason="esquema de campos alterado; referência mantida",
            )

        changed = tuple(
            key for key in current
            if current[key] != self._previous[key]
        )

        if not changed:
            return Comparison("UNCHANGED", reason="snapshot idêntico")

        # Neste protótipo, a aceitação é apenas em memória.
        # Em produção, a referência só avançará após confirmação da escrita.
        self._previous = current
        return Comparison("CHANGED", changed_fields=changed,
                          reason="diferença detetada em memória")


if __name__ == "__main__":
    import unittest

    class SnapshotComparatorTests(unittest.TestCase):
        def setUp(self):
            self.detector = SnapshotComparator()
            self.base = {
                "asset": "SYNTHETIC_ASSET",
                "last": 100.0,
                "bid": 99.5,
                "quantity": 10,
                "state": "OK",
            }

        def test_first_snapshot_sets_baseline_only(self):
            result = self.detector.observe(self.base)
            self.assertEqual(result.status, "BASELINE")

        def test_identical_snapshot_is_unchanged(self):
            self.detector.observe(self.base)
            self.assertEqual(self.detector.observe(dict(self.base)).status,
                             "UNCHANGED")

        def test_single_field_change(self):
            self.detector.observe(self.base)
            changed = dict(self.base, last=100.25)
            result = self.detector.observe(changed)
            self.assertEqual(result.status, "CHANGED")
            self.assertEqual(result.changed_fields, ("last",))

        def test_multiple_fields_make_one_comparison_event(self):
            self.detector.observe(self.base)
            changed = dict(self.base, bid=100.0, quantity=12)
            result = self.detector.observe(changed)
            self.assertEqual(result.status, "CHANGED")
            self.assertEqual(set(result.changed_fields), {"bid", "quantity"})

        def test_quantity_change_detected_when_last_is_same(self):
            self.detector.observe(self.base)
            changed = dict(self.base, quantity=11)
            result = self.detector.observe(changed)
            self.assertEqual(result.status, "CHANGED")
            self.assertEqual(result.changed_fields, ("quantity",))

        def test_transition_to_empty_is_a_change(self):
            self.detector.observe(self.base)
            changed = dict(self.base, bid="")
            result = self.detector.observe(changed)
            self.assertEqual(result.status, "CHANGED")
            self.assertEqual(result.changed_fields, ("bid",))

        def test_error_snapshot_is_rejected_and_baseline_preserved(self):
            self.detector.observe(self.base)
            bad = dict(self.base, last=CellError("#N/A"))
            self.assertEqual(self.detector.observe(bad).status, "INVALID")
            self.assertEqual(self.detector.observe(self.base).status,
                             "UNCHANGED")

        def test_empty_snapshot_rejected(self):
            self.assertEqual(self.detector.observe({}).status, "INVALID")

        def test_schema_change_rejected_without_advancing_baseline(self):
            self.detector.observe(self.base)
            altered_schema = dict(self.base)
            del altered_schema["state"]
            self.assertEqual(self.detector.observe(altered_schema).status,
                             "INVALID")
            self.assertEqual(self.detector.observe(self.base).status,
                             "UNCHANGED")

        def test_new_valid_snapshot_becomes_next_reference(self):
            self.detector.observe(self.base)
            next_snapshot = dict(self.base, last=101.0)
            self.assertEqual(self.detector.observe(next_snapshot).status,
                             "CHANGED")
            self.assertEqual(self.detector.observe(next_snapshot).status,
                             "UNCHANGED")

    unittest.main(verbosity=2)
