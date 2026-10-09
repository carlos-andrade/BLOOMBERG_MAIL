import json
import tempfile
import unittest
from pathlib import Path

from WATCHDOG.adapters.replay import ReplayError, replay


def event(event_id="evt-1"):
    return {
        "event_id": event_id,
        "observed_at_utc": "2026-10-09T10:00:00+00:00",
        "source": "fixture_sintetica",
        "asset_class": "test",
        "symbol": None,
        "session": None,
        "event_type": "TEST_EVENT",
        "severity": "INFO",
        "state": "UP",
        "latency_ms": 1,
        "quality": "SYNTHETIC_TEST",
        "payload": {"synthetic": True},
        "schema_version": "1.0",
    }


class ReplayTests(unittest.TestCase):
    def test_validate_only_does_not_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "input.jsonl"
            target = Path(tmp) / "out.jsonl"
            source.write_text(json.dumps(event()) + "\n", encoding="utf-8")
            result = replay(source, target, validate_only=True)
            self.assertEqual(result["accepted"], 1)
            self.assertFalse(target.exists())

    def test_append_and_deduplicate_existing_event_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "input.jsonl"
            target = Path(tmp) / "out.jsonl"
            source.write_text(json.dumps(event()) + "\n" + json.dumps(event("evt-2")) + "\n", encoding="utf-8")
            target.write_text(json.dumps(event()) + "\n", encoding="utf-8")
            result = replay(source, target)
            rows = [json.loads(line) for line in target.read_text(encoding="utf-8").splitlines()]
            self.assertEqual(result["accepted"], 1)
            self.assertEqual(result["duplicates"], 1)
            self.assertEqual([row["event_id"] for row in rows], ["evt-1", "evt-2"])

    def test_invalid_severity_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "input.jsonl"
            bad = event()
            bad["severity"] = "PANIC"
            source.write_text(json.dumps(bad) + "\n", encoding="utf-8")
            with self.assertRaises(ReplayError):
                replay(source)

    def test_malformed_json_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "input.jsonl"
            source.write_text("{not-json}\n", encoding="utf-8")
            with self.assertRaises(ReplayError):
                replay(source)


if __name__ == "__main__":
    unittest.main()
