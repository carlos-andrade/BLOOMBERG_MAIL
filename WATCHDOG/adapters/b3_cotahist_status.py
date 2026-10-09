#!/usr/bin/env python3
"""Converte evidências persistidas do COTAHIST num evento de qualidade histórica."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULTS = {
    "manifest": "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/b3_cotahist_normalizado.json",
    "layout": "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/VALIDACAO_LAYOUT_COTAHIST_A2026.json",
    "normalization": "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/VALIDACAO_NORMALIZACAO_B3_A2026.json",
    "reconciliation": "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_CROSS_REPO_2026-10-08.json",
}


class EvidenceError(ValueError):
    pass


def read_json(root: Path, relative: str) -> dict:
    path = root / relative
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise EvidenceError(f"evidência ausente: {relative}") from exc
    except json.JSONDecodeError as exc:
        raise EvidenceError(f"JSON inválido em {relative}: {exc.msg}") from exc
    if not isinstance(value, dict):
        raise EvidenceError(f"evidência não é objeto JSON: {relative}")
    return value


def build_event(root: Path) -> dict:
    manifest = read_json(root, DEFAULTS["manifest"])
    layout = read_json(root, DEFAULTS["layout"])
    normalization = read_json(root, DEFAULTS["normalization"])
    reconciliation = read_json(root, DEFAULTS["reconciliation"])

    raw_sha = manifest.get("raw_sha256")
    if not isinstance(raw_sha, str) or len(raw_sha) != 64:
        raise EvidenceError("manifesto sem SHA-256 RAW válido")
    for label, report in (("layout", layout), ("normalization", normalization)):
        if report.get("raw_sha256") != raw_sha:
            raise EvidenceError(f"SHA-256 RAW divergente no relatório de {label}")
        if report.get("status") != "PASS":
            raise EvidenceError(f"validação de {label} não está PASS")

    rec_result = reconciliation.get("result")
    allowed = {"PASS_EXACT", "PASS_OVERLAP_EXACT", "FAIL_CONTENT_DIVERGENCE", "BLOCKED_EXECUTION"}
    if rec_result not in allowed:
        raise EvidenceError(f"resultado REC-001 ausente ou desconhecido: {rec_result!r}")

    quality_pass = rec_result in {"PASS_EXACT", "PASS_OVERLAP_EXACT"}
    state = "UP" if quality_pass else "DEGRADED"
    severity = "INFO" if quality_pass else "HIGH"
    dataset_id = str(manifest.get("dataset_id", "B3_COTAHIST_A2026"))
    stable_material = "|".join((dataset_id, raw_sha, str(rec_result)))
    event_id = hashlib.sha256(stable_material.encode("utf-8")).hexdigest()

    return {
        "event_id": event_id,
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "b3_cotahist_historical_quality",
        "asset_class": "historical_market_data",
        "symbol": None,
        "session": None,
        "event_type": "HISTORICAL_DATASET_QUALITY",
        "severity": severity,
        "state": state,
        "latency_ms": None,
        "quality": "VALIDATED_HISTORICAL_DATASET" if quality_pass else "RECONCILIATION_BLOCKED_OR_DIVERGENT",
        "payload": {
            "dataset_id": dataset_id,
            "reference_period": manifest.get("reference_period"),
            "raw_sha256": raw_sha,
            "record_count": manifest.get("record_count"),
            "layout_status": layout.get("status"),
            "normalization_status": normalization.get("status"),
            "reconciliation_result": rec_result,
            "reconciliation_scope": reconciliation.get("comparison_scope"),
            "is_realtime_feed": False,
            "economic_adjustment": False,
        },
        "schema_version": "1.0",
    }


def append_once(path: Path, event: dict) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        with path.open("r", encoding="utf-8") as stream:
            for line_number, line in enumerate(stream, 1):
                if not line.strip():
                    continue
                try:
                    existing = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise EvidenceError(f"JSONL destino inválido na linha {line_number}") from exc
                if isinstance(existing, dict) and existing.get("event_id") == event["event_id"]:
                    return False
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, help="JSONL append-only para eventos")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args(argv)
    try:
        event = build_event(args.root)
        written = False
        if args.output and not args.validate_only:
            written = append_once(args.output, event)
        print(json.dumps({"status": "VALIDADO", "written": written, "event": event}, ensure_ascii=False, sort_keys=True))
    except (OSError, EvidenceError) as exc:
        print(json.dumps({"status": "ERRO", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
