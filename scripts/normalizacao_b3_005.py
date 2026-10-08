#!/usr/bin/env python3
"""BLOOMBERG_MAIL — normalização determinística B3 COTAHIST 005N.

RAW permanece imutável. Parser baseado exclusivamente no layout B3 COTAHIST
v2.0/rev.02 (245 bytes) e na reconciliação controlada de TPMERC=021.
Saída particionada em JSONL gzip para evitar arquivos monolíticos.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "EMAILS_RECEBIDOS/INGESTAO/005"
RAW = BASE / "RAW" / "COTAHIST_A2026.ZIP"
OUT = BASE / "NORMALIZADO" / "B3"
RAW_SHA = "c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f"
PARSER_VERSION = "normalizacao-005-b3-v1.0"
SCHEMA_VERSION = "1.0-normalized-b3-cotahist"
RECORD_LEN = 245
CHUNK_RECORDS = 100_000
TPMERC_021 = "021"

FIELDS = [
    ("tipreg",1,2),("data_pregao_raw",3,10),("codbdi",11,12),("codneg",13,24),
    ("tpmerc",25,27),("nomres",28,39),("especi",40,49),("prazot",50,52),
    ("modref",53,56),("preabe_raw",57,69),("premax_raw",70,82),
    ("premin_raw",83,95),("premed_raw",96,108),("preult_raw",109,121),
    ("preofc_raw",122,134),("preofv_raw",135,147),("totneg_raw",148,152),
    ("quatot_raw",153,170),("voltot_raw",171,188),("preexe_raw",189,201),
    ("indopc",202,202),("datven_raw",203,210),("fatcot_raw",211,217),
    ("ptoexe_raw",218,230),("codisi",231,242),("dismes",243,245),
]

DECIMAL_FIELDS = {
    "preabe_raw": 2, "premax_raw": 2, "premin_raw": 2, "premed_raw": 2,
    "preult_raw": 2, "preofc_raw": 2, "preofv_raw": 2, "voltot_raw": 2,
    "preexe_raw": 2, "ptoexe_raw": 6,
}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def raw_field(rec: bytes, start: int, end: int) -> str:
    return rec[start-1:end].decode("ascii", errors="strict")

def canonical_date(value: str) -> str | None:
    s = value.strip()
    if not s or s == "00000000":
        return None
    return datetime.strptime(s, "%Y%m%d").date().isoformat()

def canonical_decimal(value: str, decimals: int) -> str | None:
    s = value.strip()
    if not s:
        return None
    if not re.fullmatch(r"[+-]?\d+", s):
        raise ValueError(f"invalid fixed numeric field: {value!r}")
    sign = "-" if s.startswith("-") else ""
    digits = s.lstrip("+-")
    if len(digits) <= decimals:
        digits = digits.zfill(decimals + 1)
    if decimals:
        return sign + digits[:-decimals] + "." + digits[-decimals:]
    return sign + digits

def normalize_record(rec: bytes) -> dict:
    if len(rec) != RECORD_LEN or rec[:2] != b"01":
        raise ValueError("expected 245-byte record 01")
    out = {}
    for name, start, end in FIELDS:
        out[name] = raw_field(rec, start, end)
    out["data_pregao"] = canonical_date(out["data_pregao_raw"])
    out["datven"] = canonical_date(out["datven_raw"])
    for name, decimals in DECIMAL_FIELDS.items():
        out[name[:-4]] = canonical_decimal(out[name], decimals)
    out["tpmerc_semantica"] = "BLOCK LOT / BBT" if out["tpmerc"] == TPMERC_021 else None
    out["tpmerc_reconciliacao"] = (
        "CONTROLLED_RECONCILIATION_2026-10-08"
        if out["tpmerc"] == TPMERC_021 else None
    )
    return out

def main() -> None:
    assert sha256(RAW) == RAW_SHA, "RAW SHA mismatch"
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("cotahist_a2026_part_*.jsonl.gz"):
        old.unlink()

    processed_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    counts = {"physical": 0, "record_01": 0, "record_00": 0, "record_99": 0}
    missing = 0
    tpmerc_021 = 0
    part_no = 0
    part_count = 0
    part_paths = []
    seen_keys = set()
    duplicate_count = 0

    def open_part():
        nonlocal part_no, part_count
        part_no += 1
        part_count = 0
        path = OUT / f"cotahist_a2026_part_{part_no:03d}.jsonl.gz"
        part_paths.append(path)
        return gzip.GzipFile(filename="", mode="wb", fileobj=path.open("wb"), mtime=0)

    with zipfile.ZipFile(RAW, "r") as z:
        assert z.testzip() is None
        members = z.infolist()
        assert len(members) == 1 and members[0].filename == "COTAHIST_A2026.TXT"
        with z.open(members[0], "r") as f:
            gz = None
            try:
                for line in f:
                    rec = line.rstrip(b"\r\n")
                    counts["physical"] += 1
                    if len(rec) != RECORD_LEN:
                        raise ValueError(f"record length != 245 at physical record {counts['physical']}")
                    typ = rec[:2]
                    if typ == b"00":
                        counts["record_00"] += 1
                        continue
                    if typ == b"99":
                        counts["record_99"] += 1
                        continue
                    if typ != b"01":
                        raise ValueError(f"unsupported record type {typ!r}")
                    counts["record_01"] += 1
                    obj = normalize_record(rec)
                    if any(obj[k] == "" for k,_,_ in FIELDS):
                        missing += 1
                    key = (obj["data_pregao"], obj["codbdi"], obj["codneg"], obj["tpmerc"])
                    if key in seen_keys:
                        duplicate_count += 1
                    else:
                        seen_keys.add(key)
                    if obj["tpmerc"] == TPMERC_021:
                        tpmerc_021 += 1
                    if gz is None or part_count >= CHUNK_RECORDS:
                        if gz is not None:
                            gz.close()
                        gz = open_part()
                    gz.write((json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8"))
                    part_count += 1
            finally:
                if gz is not None:
                    gz.close()

    assert counts["record_00"] == 1
    assert counts["record_99"] == 1
    assert counts["record_01"] > 0

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "dataset_id": "B3_COTAHIST_A2026",
        "source": "B3 — Cotações Históricas",
        "source_url": "https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/",
        "raw_path": "EMAILS_RECEBIDOS/INGESTAO/005/RAW/COTAHIST_A2026.ZIP",
        "raw_sha256": RAW_SHA,
        "reference_period": "2026",
        "processed_at_utc": processed_at,
        "parser_version": PARSER_VERSION,
        "layout_reference": "SeriesHistoricas_Layout.pdf v2.0/rev.02; TPMERC=021 controlled reconciliation 2026-10-08",
        "quality_status": "NORMALIZED_DERIVED",
        "storage_policy": "PARTITIONED_COMPRESSED_JSONL",
        "record_length_bytes": RECORD_LEN,
        "chunk_records": CHUNK_RECORDS,
        "physical_counts": counts,
        "record_count": counts["record_01"],
        "duplicate_count": duplicate_count,
        "missing_record_field_count": missing,
        "tpmerc_021_count": tpmerc_021,
        "tpmerc_021_semantics": "BLOCK LOT / BBT",
        "tpmerc_021_reconciliation": "RECONCILIACAO_TPMERC021_COM_REPOSITORIO_B3_2026-10-08.md",
        "field_count": len(FIELDS),
        "field_names": [x[0] for x in FIELDS],
        "output_files": [p.name for p in part_paths],
    }
    (OUT / "b3_cotahist_normalizado.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
