#!/usr/bin/env python3
"""BLOOMBERG_MAIL — validação determinística do layout B3 COTAHIST 005.

Lê somente o RAW COTAHIST_A2026.ZIP. Não altera RAW nem produz dados normalizados.
Valida estrutura física e campos contra o mapeamento oficial B3 v2.0/rev.02.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "EMAILS_RECEBIDOS/INGESTAO/005/RAW/COTAHIST_A2026.ZIP"
OUT = ROOT / "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3"
OUT.mkdir(parents=True, exist_ok=True)
REPORT = OUT / "VALIDACAO_LAYOUT_COTAHIST_A2026.json"

EXPECTED_RAW_SHA = "c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f"
RECORD_LEN = 245
PRICE_FIELDS = [(57,69),(70,82),(83,95),(96,108),(109,121),(122,134),(135,147),(189,201)]
INT_FIELDS = [(148,152),(153,170),(243,245)]
DATE_FIELDS = [(3,10),(203,210)]
VALID_TYPES = {b"00", b"01", b"99"}
VALID_TPMERC = {b"010", b"012", b"013", b"017", b"020", b"030", b"050", b"060", b"070", b"080"}
VALID_INDOPC = {b" ", b"0", b"1", b"2", b"8", b"9"}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def field(rec: bytes, start: int, end: int) -> bytes:
    return rec[start-1:end]

def digits_or_blank(v: bytes) -> bool:
    s = v.decode("ascii", errors="strict")
    return s.strip() == "" or s.strip().isdigit()

def fixed_numeric_ok(v: bytes, decimals: int = 0) -> bool:
    s = v.decode("ascii", errors="strict")
    return s.strip() == "" or bool(re.fullmatch(r"[ 0-9+-]+", s))

def valid_date(v: bytes) -> bool:
    s = v.decode("ascii", errors="strict").strip()
    if not s or s == "00000000":
        return True
    try:
        dt.datetime.strptime(s, "%Y%m%d")
        return True
    except ValueError:
        return False

raw_sha = sha256(RAW)
assert raw_sha == EXPECTED_RAW_SHA, f"RAW SHA mismatch: {raw_sha}"

checks = {
    "raw_sha_match": True,
    "zip_integrity": False,
    "member_count": None,
    "member_name": None,
    "record_count_physical": 0,
    "record_00": 0,
    "record_01": 0,
    "record_99": 0,
    "record_other": 0,
    "record_length_245": 0,
    "record_length_invalid": 0,
    "header_valid": False,
    "trailer_valid": False,
    "record_01_fields_valid": 0,
    "record_01_fields_invalid": 0,
    "date_invalid": 0,
    "numeric_invalid": 0,
    "tpmec_invalid": 0,
    "codbdi_blank_count": 0,
    "indopc_invalid": 0,
    "trailer_total_records": None,
    "trailer_count_matches_record01": False,
    "trailer_count_matches_total_physical": False,
}

with zipfile.ZipFile(RAW, "r") as z:
    bad = z.testzip()
    assert bad is None, f"ZIP CRC failure at member {bad}"
    checks["zip_integrity"] = True
    members = z.infolist()
    checks["member_count"] = len(members)
    assert len(members) == 1, f"Expected 1 member, found {len(members)}"
    checks["member_name"] = members[0].filename
    with z.open(members[0], "r") as f:
        first = f.readline()
        assert first, "Empty COTAHIST member"
        pending = first
        trailer_raw = None
        header_raw = None
        while pending:
            line = pending
            pending = f.readline()
            # Physical line ending is not part of the 245-byte record.
            rec = line.rstrip(b"\r\n")
            checks["record_count_physical"] += 1
            if len(rec) != RECORD_LEN:
                checks["record_length_invalid"] += 1
                continue
            checks["record_length_245"] += 1
            typ = rec[:2]
            if typ not in VALID_TYPES:
                checks["record_other"] += 1
                continue
            if typ == b"00":
                checks["record_00"] += 1
                header_raw = rec
                ok = (
                    rec[:2] == b"00"
                    and bool(rec[2:15].strip())
                    and bool(rec[15:23].strip())
                    and bool(re.fullmatch(rb"\d{8}", rec[23:31]))
                    and len(rec[31:]) == 214
                )
                checks["header_valid"] = checks["header_valid"] or ok
            elif typ == b"01":
                checks["record_01"] += 1
                ok = True
                try:
                    ok &= bool(re.fullmatch(rb"\d{8}", field(rec,3,10)))
                    ok &= bool(re.fullmatch(rb"[ -~]{2}", field(rec,11,12)))
                    if not field(rec,11,12).strip():
                        checks["codbdi_blank_count"] += 1
                        ok = False
                    ok &= bool(re.fullmatch(rb"[ -~]{12}", field(rec,13,24)))
                    ok &= field(rec,25,27) in VALID_TPMERC
                    if field(rec,25,27) not in VALID_TPMERC:
                        checks["tpmec_invalid"] += 1
                    for s,e in PRICE_FIELDS:
                        ok &= fixed_numeric_ok(field(rec,s,e))
                    for s,e in INT_FIELDS:
                        ok &= digits_or_blank(field(rec,s,e))
                    ok &= valid_date(field(rec,3,10))
                    ok &= valid_date(field(rec,203,210))
                    if field(rec,202,202) not in VALID_INDOPC:
                        checks["indopc_invalid"] += 1
                        ok = False
                except UnicodeDecodeError:
                    ok = False
                if not ok:
                    checks["record_01_fields_invalid"] += 1
                else:
                    checks["record_01_fields_valid"] += 1
                if not valid_date(field(rec,3,10)) or not valid_date(field(rec,203,210)):
                    checks["date_invalid"] += 1
                if any(not fixed_numeric_ok(field(rec,s,e)) for s,e in PRICE_FIELDS):
                    checks["numeric_invalid"] += 1
            elif typ == b"99":
                checks["record_99"] += 1
                trailer_raw = rec

assert checks["record_length_invalid"] == 0, "Found physical records different from 245 bytes"
assert checks["record_other"] == 0, "Found unsupported record type"
assert checks["record_00"] == 1, f"Expected exactly one header, found {checks['record_00']}"
assert checks["record_99"] == 1, f"Expected exactly one trailer, found {checks['record_99']}"
assert checks["record_01"] > 0, "No quotation records found"
assert checks["header_valid"], "Header validation failed"
assert trailer_raw is not None, "Trailer missing"

trailer_total = int(field(trailer_raw,32,42).decode("ascii").strip() or "0")
checks["trailer_total_records"] = trailer_total
checks["trailer_valid"] = bool(
    trailer_raw[:2] == b"99"
    and bool(trailer_raw[2:15].strip())
    and bool(trailer_raw[15:23].strip())
    and bool(re.fullmatch(rb"\d{8}", trailer_raw[23:31]))
    and digits_or_blank(field(trailer_raw,32,42))
)

# B3 trailer count is the number of quotation records (01), excluding 00 and 99.
checks["trailer_count_matches_record01"] = trailer_total == checks["record_01"]
checks["trailer_count_matches_total_physical"] = trailer_total == checks["record_count_physical"]

status = "PASS" if all([
    checks["raw_sha_match"], checks["zip_integrity"], checks["record_length_invalid"] == 0,
    checks["record_other"] == 0, checks["record_00"] == 1, checks["record_99"] == 1,
    checks["header_valid"], checks["trailer_valid"], checks["record_01_fields_invalid"] == 0,
    checks["date_invalid"] == 0, checks["numeric_invalid"] == 0,
    checks["tpmec_invalid"] == 0, checks["codbdi_blank_count"] == 0,
    checks["indopc_invalid"] == 0, checks["trailer_count_matches_record01"],
]) else "FAIL"

report = {
    "schema_version": "1.1-b3-layout-validation",
    "status": status,
    "dataset_id": "B3_COTAHIST_A2026",
    "source": "B3 — Cotações Históricas",
    "layout_reference": "SeriesHistoricas_Layout.pdf — versão 2.0, revisão 02, atualização 05/10/2020",
    "raw_path": "EMAILS_RECEBIDOS/INGESTAO/005/RAW/COTAHIST_A2026.ZIP",
    "raw_sha256": raw_sha,
    "checks": checks,
    "policy": {
        "raw_immutable": True,
        "economic_adjustment": False,
        "interpolation": False,
        "invention": False,
        "normalization_executed": False,
    },
}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
if status != "PASS":
    raise SystemExit(1)
