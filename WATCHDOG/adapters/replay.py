#!/usr/bin/env python3
"""Replay auditável de eventos canónicos do WATCHDOG; não recolhe cotações."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterator

REQUIRED = {"event_id", "observed_at_utc", "source", "event_type", "severity", "schema_version"}
SEVERITIES = {"INFO", "LOW", "MEDIUM", "HIGH", "CRITICAL"}
STATES = {"UP", "DEGRADED", "DOWN", "STALE", "UNKNOWN"}


class ReplayError(ValueError):
    """Entrada JSONL inválida ou incompatível com o contrato."""


def iter_events(path: Path) -> Iterator[dict]:
    with path.open("r", encoding="utf-8") as stream:
        for line_number, raw in enumerate(stream, start=1):
            if not raw.strip():
                continue
            try:
                event = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise ReplayError(f"linha {line_number}: JSON inválido: {exc.msg}") from exc
            if not isinstance(event, dict):
                raise ReplayError(f"linha {line_number}: cada evento tem de ser um objeto JSON")
            missing = sorted(REQUIRED - event.keys())
            if missing:
                raise ReplayError(f"linha {line_number}: campos obrigatórios ausentes: {', '.join(missing)}")
            if not isinstance(event["event_id"], str) or not event["event_id"].strip():
                raise ReplayError(f"linha {line_number}: event_id tem de ser texto não vazio")
            if event["severity"] not in SEVERITIES:
                raise ReplayError(f"linha {line_number}: severity inválida: {event['severity']}")
            if event.get("state") is not None and event["state"] not in STATES:
                raise ReplayError(f"linha {line_number}: state inválido: {event['state']}")
            if not isinstance(event["source"], str) or not event["source"].strip():
                raise ReplayError(f"linha {line_number}: source tem de ser texto não vazio")
            yield event


def replay(input_path: Path, output_path: Path | None = None, validate_only: bool = False) -> dict:
    seen: set[str] = set()
    if output_path and output_path.exists():
        for existing in iter_events(output_path):
            seen.add(existing["event_id"])

    accepted = 0
    duplicates = 0
    batch: list[dict] = []
    for event in iter_events(input_path):
        if event["event_id"] in seen:
            duplicates += 1
            continue
        seen.add(event["event_id"])
        batch.append(event)
        accepted += 1

    if output_path and not validate_only and batch:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("a", encoding="utf-8") as stream:
            for event in batch:
                stream.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")

    return {
        "status": "VALIDADO" if validate_only else "CONCLUIDO",
        "input": str(input_path),
        "output": str(output_path) if output_path and not validate_only else None,
        "accepted": accepted,
        "duplicates": duplicates,
        "written": 0 if validate_only or not output_path else accepted,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="ficheiro JSONL de eventos canónicos")
    parser.add_argument("--output", type=Path, help="destino JSONL append-only; omitido no modo validação")
    parser.add_argument("--validate-only", action="store_true", help="validar sem escrever")
    args = parser.parse_args(argv)
    try:
        result = replay(args.input, args.output, args.validate_only)
    except (OSError, ReplayError) as exc:
        print(json.dumps({"status": "ERRO", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
