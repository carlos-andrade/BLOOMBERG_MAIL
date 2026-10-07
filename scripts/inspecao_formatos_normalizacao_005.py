#!/usr/bin/env python3
"""BLOOMBERG_MAIL — inspeção determinística dos formatos RAW da INGESTÃO 005N.

Não altera RAW. Produz somente evidência estrutural suficiente para definir
os layouts derivados sem adivinhar schemas.
"""
from pathlib import Path
import csv, hashlib, io, json, zipfile

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "EMAILS_RECEBIDOS/INGESTAO/005/RAW"
OUT = ROOT / "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO"
OUT.mkdir(parents=True, exist_ok=True)

TEXT_ENCODINGS = ("utf-8-sig", "latin-1", "cp1252")

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def decode_preview(data: bytes):
    for enc in TEXT_ENCODINGS:
        try:
            return enc, data.decode(enc)
        except UnicodeDecodeError:
            continue
    return None, None

def text_structure(data: bytes):
    enc, text = decode_preview(data)
    if text is None:
        return {"text_decodable": False}
    lines = text.splitlines()
    sample = lines[:5]
    delimiters = {d: max((line.count(d) for line in sample), default=0) for d in [",", ";", "|", "\t"]}
    return {
        "text_decodable": True,
        "encoding_candidate": enc,
        "line_count_sampled": min(len(lines), 5),
        "first_lines": sample,
        "delimiter_counts_sample": delimiters,
        "first_line_length": len(lines[0]) if lines else 0,
    }

def zip_inspect(name: str):
    p = RAW / name
    members = []
    with zipfile.ZipFile(p) as z:
        bad = z.testzip()
        for info in z.infolist():
            item = {
                "name": info.filename,
                "size": info.file_size,
                "compressed_size": info.compress_size,
                "crc": f"{info.CRC:08x}",
            }
            if not info.is_dir():
                with z.open(info) as fh:
                    data = fh.read(min(info.file_size, 65536))
                item["preview_sha256"] = hashlib.sha256(data).hexdigest()
                item["structure"] = text_structure(data)
            members.append(item)
    return {
        "file": name,
        "sha256": sha256(p),
        "zip_integrity": "PASS" if bad is None else f"FAIL:{bad}",
        "members": members,
    }

report = {
    "schema_version": "1.1-format-inspection",
    "raw_policy": "IMMUTABLE",
    "inspection_scope": "member_metadata_plus_bounded_text_preview; no RAW modification",
    "b3": zip_inspect("COTAHIST_A2026.ZIP"),
    "cvm": zip_inspect("oferta_distribuicao.zip"),
}

p = RAW / "precotaxatesourodireto.csv"
with p.open("rb") as fb:
    raw_bytes = fb.read()
enc, text = decode_preview(raw_bytes[:1048576])
if text is None:
    raise RuntimeError("Tesouro CSV não pôde ser decodificado pelos encodings permitidos")
lines = text.splitlines()
reader = csv.reader(lines)
header = next(reader, [])
samples = [next(reader, []) for _ in range(3)]
report["tesouro"] = {
    "file": p.name,
    "sha256": sha256(p),
    "encoding_candidate": enc,
    "header": header,
    "sample_rows": samples,
    "sample_structure": text_structure(raw_bytes[:1048576]),
}

(OUT / "INSPECAO_FORMATOS_005.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print("FORMAT INSPECTION: PASS")
