#!/usr/bin/env python3
"""BLOOMBERG_MAIL — normalização determinística INGESTÃO 005.
Produz saídas derivadas a partir de RAW; nunca altera RAW.
"""
from __future__ import annotations
import csv, hashlib, json, os, zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "EMAILS_RECEBIDOS/INGESTAO/005/RAW"
OUT = ROOT / "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO"
OUT.mkdir(parents=True, exist_ok=True)
PARSER_VERSION = "normalizacao-005-v1.1"
SCHEMA_VERSION = "1.0-normalized"

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def write_json(name, obj):
    p = OUT / name
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return p

processed = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

# BCB: canonicalize exact current RAW observations, without changing values.
bcb = RAW / "bcb_sgs_1178_ultimos_10.json"
raw_bcb = json.loads(bcb.read_text(encoding="utf-8"))
obs = []
for x in raw_bcb:
    parsed = datetime.strptime(x["data"], "%d/%m/%Y").date()
    obs.append({
        "date": parsed.isoformat(),
        "date_raw": x["data"],
        "value": x["valor"],
        "value_raw": x["valor"]
    })
obs = sorted(obs, key=lambda x: x["date"])
write_json("bcb_sgs_1178_normalizado.json", {
    "schema_version": SCHEMA_VERSION, "dataset_id": "BCB_SGS_1178",
    "source": "Banco Central do Brasil — SGS",
    "source_url": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados?formato=json&dataInicial=23%2F09%2F2026&dataFinal=06%2F10%2F2026",
    "raw_path": "EMAILS_RECEBIDOS/INGESTAO/005/RAW/bcb_sgs_1178_ultimos_10.json",
    "raw_sha256": sha256(bcb), "retrieval_timestamp_utc": "2026-10-07T10:34:56Z",
    "reference_period": "2026-09-23/2026-10-06", "processed_at_utc": processed,
    "date_representation": "ISO-8601 derived from RAW DD/MM/YYYY; date_raw preserved",
    "value_representation": "RAW decimal string preserved; no numeric coercion",
    "frequency": "daily", "unit": "percent_per_year",
    "parser_version": PARSER_VERSION, "quality_status": "NORMALIZED_DERIVED",
    "record_count": len(obs), "duplicate_count": 0,
    "missing_count": sum(1 for x in obs if not x["date"] or x["value"] is None),
    "observations": obs
})

# VIX: canonicalize source CSV fields without economic transformation.
vix = RAW / "VIX_History.csv"
rows = []
with vix.open("r", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        rows.append({k.strip(): r[k].strip() for k in r})
write_json("vix_normalizado.json", {
    "schema_version": SCHEMA_VERSION, "dataset_id": "VIX",
    "source": "Cboe",
    "source_url": "https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv",
    "raw_path": "EMAILS_RECEBIDOS/INGESTAO/005/RAW/VIX_History.csv",
    "raw_sha256": sha256(vix), "retrieval_timestamp_utc": "2026-10-07T13:59:08Z",
    "reference_period": "1990-01-02/2026-10-06", "processed_at_utc": processed,
    "schema_fields": ["DATE","OPEN","HIGH","LOW","CLOSE"],
    "parser_version": PARSER_VERSION, "quality_status": "NORMALIZED_DERIVED",
    "record_count": len(rows),
    "duplicate_count": len(rows) - len({r["DATE"] for r in rows}),
    "missing_count": sum(1 for r in rows for k in ["DATE","OPEN","HIGH","LOW","CLOSE"] if not r.get(k)),
    "records": rows
})

print("NORMALIZATION DERIVED outputs created for BCB_SGS_1178 and VIX.")
