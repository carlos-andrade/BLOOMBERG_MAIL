import json
import tempfile
import unittest
from pathlib import Path

from WATCHDOG.adapters.b3_cotahist_status import EvidenceError, build_event


def write_evidence(root: Path, rec_result="FAIL_CONTENT_DIVERGENCE", raw_sha="a" * 64):
    paths = {
        "manifest": "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/b3_cotahist_normalizado.json",
        "layout": "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/VALIDACAO_LAYOUT_COTAHIST_A2026.json",
        "normalization": "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/VALIDACAO_NORMALIZACAO_B3_A2026.json",
        "reconciliation": "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC-001.json",
        "diagnostic": "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_DIAGNOSTICO_MULTICONJUNTO_2026-10-09.json",
    }
    values = {
        "manifest": {"dataset_id": "B3_COTAHIST_A2026", "raw_sha256": raw_sha, "record_count": 123, "reference_period": "2026"},
        "layout": {"status": "PASS", "raw_sha256": raw_sha},
        "normalization": {"status": "PASS", "raw_sha256": raw_sha},
        "reconciliation": {"result": rec_result, "comparison_scope": "test"},
    }
    for key, rel in paths.items():
        if key not in values:
            continue
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(values[key]), encoding="utf-8")
    return paths


class B3CotaHistStatusTests(unittest.TestCase):
    def test_divergence_is_degraded_not_up(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_evidence(root)
            from WATCHDOG.adapters import b3_cotahist_status as adapter
            original = adapter.DEFAULTS.copy()
            adapter.DEFAULTS.update(paths)
            try:
                event = build_event(root)
            finally:
                adapter.DEFAULTS.update(original)
            self.assertEqual(event["state"], "DEGRADED")
            self.assertEqual(event["severity"], "HIGH")
            self.assertFalse(event["payload"]["is_realtime_feed"])

    def test_exact_reconciliation_is_up(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_evidence(root, "PASS_EXACT")
            from WATCHDOG.adapters import b3_cotahist_status as adapter
            original = adapter.DEFAULTS.copy()
            adapter.DEFAULTS.update(paths)
            try:
                event = build_event(root)
            finally:
                adapter.DEFAULTS.update(original)
            self.assertEqual(event["state"], "UP")
            self.assertEqual(event["severity"], "INFO")

    def test_raw_hash_mismatch_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_evidence(root, raw_sha="a" * 64)
            layout_path = root / paths["layout"]
            layout_path.write_text(json.dumps({"status": "PASS", "raw_sha256": "b" * 64}), encoding="utf-8")
            from WATCHDOG.adapters import b3_cotahist_status as adapter
            original = adapter.DEFAULTS.copy()
            adapter.DEFAULTS.update(paths)
            try:
                with self.assertRaises(EvidenceError):
                    build_event(root)
            finally:
                adapter.DEFAULTS.update(original)


    def test_verified_overlap_diagnostic_supersedes_legacy_false_divergence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_evidence(root, "FAIL_CONTENT_DIVERGENCE", raw_sha="a" * 64)
            diagnostic = {
                "result": "PASS_OVERLAP_EXACT",
                "comparison_scope": "full-record multiset per date",
                "bloomberg_mail": {"zip_sha256": "a" * 64},
                "b3": {"snapshot_hash_matches_manifest_reference": True},
                "comparison": {"exact_common_period": True, "divergent_dates_count": 0, "dates_tested": 182, "convergent_dates": 182},
            }
            diagnostic_path = root / paths["diagnostic"]
            diagnostic_path.parent.mkdir(parents=True, exist_ok=True)
            diagnostic_path.write_text(json.dumps(diagnostic), encoding="utf-8")
            from WATCHDOG.adapters import b3_cotahist_status as adapter
            original = adapter.DEFAULTS.copy()
            adapter.DEFAULTS.update(paths)
            try:
                event = build_event(root)
            finally:
                adapter.DEFAULTS.update(original)
            self.assertEqual(event["state"], "UP")
            self.assertEqual(event["severity"], "INFO")
            self.assertEqual(event["payload"]["reconciliation_result"], "PASS_OVERLAP_EXACT")
            self.assertEqual(event["payload"]["original_reconciliation_result"], "FAIL_CONTENT_DIVERGENCE")
            self.assertEqual(event["quality"], "VALIDATED_HISTORICAL_OVERLAP")

    def test_diagnostic_pass_with_divergent_dates_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_evidence(root, "FAIL_CONTENT_DIVERGENCE", raw_sha="a" * 64)
            diagnostic = {
                "result": "PASS_OVERLAP_EXACT",
                "bloomberg_mail": {"zip_sha256": "a" * 64},
                "b3": {"snapshot_hash_matches_manifest_reference": True},
                "comparison": {"exact_common_period": False, "divergent_dates_count": 1, "dates_tested": 182, "convergent_dates": 181},
            }
            diagnostic_path = root / paths["diagnostic"]
            diagnostic_path.parent.mkdir(parents=True, exist_ok=True)
            diagnostic_path.write_text(json.dumps(diagnostic), encoding="utf-8")
            from WATCHDOG.adapters import b3_cotahist_status as adapter
            original = adapter.DEFAULTS.copy()
            adapter.DEFAULTS.update(paths)
            try:
                with self.assertRaises(EvidenceError):
                    build_event(root)
            finally:
                adapter.DEFAULTS.update(original)


if __name__ == "__main__":
    unittest.main()
