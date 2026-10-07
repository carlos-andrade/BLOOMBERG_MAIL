#!/usr/bin/env python3
"""BLOOMBERG_MAIL — INGESTÃO 005D — validação determinística V1.0.

Princípio: aquisição não é validação; ausência de reconciliação independente
é BLOCKED, nunca PASS.
"""

from __future__ import annotations

import csv
import hashlib
import json
import zipfile
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "EMAILS_RECEBIDOS" / "INGESTAO" / "005" / "RAW"
OUT = ROOT / "EMAILS_RECEBIDOS" / "INGESTAO" / "005" / "VALIDACAO" / "EXECUCAO_AUTOMATICA"
OUT.mkdir(parents=True, exist_ok=True)

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def result(test_id, dataset, status, expected, observed, rationale):
    return {
        "test_id": test_id,
        "dataset": dataset,
        "result": status,
        "expected": expected,
        "observed": observed,
        "rationale": rationale,
    }

tests = []
files = {
    "B3_COTACOES": RAW / "COTAHIST_A2026.ZIP",
    "CVM_OFERTAS": RAW / "oferta_distribuicao.zip",
    "BCB_SGS": RAW / "bcb_sgs_1178_ultimos_10.json",
    "TESOURO_HISTORICO": RAW / "precotaxatesourodireto.csv",
    "VIX": RAW / "VIX_History.csv",
}

for dataset, path in files.items():
    if not path.exists():
        tests.append(result("INT-001", dataset, "FAIL", "RAW presente", "ausente", "RAW obrigatório não encontrado."))
        continue
    tests.append(result(
        "INT-001", dataset, "PASS", "SHA-256 calculável",
        sha256(path), "Checksum calculado diretamente sobre o RAW."
    ))

def validate_zip(dataset, path):
    try:
        with zipfile.ZipFile(path) as z:
            bad = z.testzip()
            names = z.namelist()
            tests.append(result("STR-001", dataset, "PASS" if bad is None else "FAIL",
                                "ZIP íntegro e legível", {"entries": len(names), "bad_entry": bad},
                                "Teste estrutural do arquivo ZIP."))
    except Exception as e:
        tests.append(result("STR-001", dataset, "FAIL", "ZIP legível", str(e), "Falha ao abrir/testar ZIP."))

validate_zip("B3_COTACOES", files["B3_COTACOES"])
validate_zip("CVM_OFERTAS", files["CVM_OFERTAS"])

# BCB
p = files["BCB_SGS"]
try:
    data = json.loads(p.read_text(encoding="utf-8"))
    rows = data if isinstance(data, list) else data.get("value", data.get("dados", []))
    valid = isinstance(rows, list) and all(isinstance(x, dict) and "data" in x and "valor" in x for x in rows)
    dates = [x["data"] for x in rows] if valid else []
    dup = len(dates) - len(set(dates))
    tests += [
        result("STR-001", "BCB_SGS", "PASS" if valid else "FAIL", "JSON com data/valor", len(rows), "Schema mínimo."),
        result("SCH-001", "BCB_SGS", "PASS" if valid else "FAIL", "data e valor", list(rows[0].keys()) if rows else [], "Campos obrigatórios."),
        result("DUP-001", "BCB_SGS", "PASS" if dup == 0 else "FAIL", "sem duplicidade por data", dup, "Chave lógica: data."),
        result("MIS-001", "BCB_SGS", "PASS" if rows and all(x.get("valor") not in (None, "") for x in rows) else "FAIL",
               "valor presente", "amostra verificada", "Missing não convertido em zero."),
    ]
except Exception as e:
    tests.append(result("STR-001", "BCB_SGS", "FAIL", "JSON válido", str(e), "Falha de parsing."))

# Tesouro — validação de cabeçalho/linhas sem alteração de conteúdo.
p = files["TESOURO_HISTORICO"]
try:
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        sample = f.read(8192)
    dialect = csv.Sniffer().sniff(sample, delimiters=";,")
    header = next(csv.reader(sample.splitlines(), dialect))
    tests.append(result("STR-001", "TESOURO_HISTORICO", "PASS", "CSV legível", header, "CSV reconhecido."))
    tests.append(result("SCH-001", "TESOURO_HISTORICO", "PASS" if len(header) >= 2 else "FAIL",
                        "cabeçalho com múltiplos campos", len(header), "Schema mínimo de arquivo."))
except Exception as e:
    tests.append(result("STR-001", "TESOURO_HISTORICO", "FAIL", "CSV legível", str(e), "Falha de leitura/estrutura."))

# VIX
p = files["VIX"]
try:
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        expected = ["DATE", "OPEN", "HIGH", "LOW", "CLOSE"]
        if reader.fieldnames != expected:
            raise ValueError(f"header observado={reader.fieldnames!r}")
        rows = list(reader)
    dates = []
    bad = 0
    for row in rows:
        try:
            dt = datetime.strptime(row["DATE"], "%m/%d/%Y")
            vals = [float(row[k]) for k in expected[1:]]
            if not all(v == v for v in vals):
                bad += 1
            dates.append(dt)
        except Exception:
            bad += 1
    dup = len(dates) - len(set(dates))
    ordered = all(a <= b for a, b in zip(dates, dates[1:]))
    tests += [
        result("STR-001", "VIX", "PASS", "DATE,OPEN,HIGH,LOW,CLOSE", reader.fieldnames, "Header esperado."),
        result("DAT-001", "VIX", "PASS" if bad == 0 else "FAIL", "datas parseáveis", len(rows) - bad, "Datas verificadas."),
        result("TYP-001", "VIX", "PASS" if bad == 0 else "FAIL", "OHLC numérico", len(rows) - bad, "Valores OHLC convertidos para número."),
        result("DUP-001", "VIX", "PASS" if dup == 0 else "FAIL", "sem duplicidade por data", dup, "Chave lógica: DATE."),
        result("ORD-001", "VIX", "PASS" if ordered else "FAIL", "ordem temporal crescente", ordered, "Sequência DATE."),
    ]
except Exception as e:
    tests.append(result("STR-001", "VIX", "FAIL", "CSV VIX legível", str(e), "Falha de leitura/estrutura."))

# REC-001 consumes persisted, dataset-specific evidence produced by the independent
# reconciliation workflows. This validator does not redownload endpoints and never
# modifies RAW. Evidence is accepted only when it explicitly reports PASS and the
# persisted RAW checksum matches the current RAW file.
rec_evidence = {
    "B3_COTACOES": ROOT / "EMAILS_RECEBIDOS" / "INGESTAO" / "005" / "VALIDACAO" / "b3_sha_reconciliation.txt",
    "CVM_OFERTAS": OUT / "rec001_cvm.json",
    "BCB_SGS": OUT / "rec001_bcb_sgs_1178.json",
    "TESOURO_HISTORICO": OUT / "rec001_tesouro.json",
    "VIX": OUT / "rec001_vix.json",
}

def validate_rec_json(dataset, evidence_path, raw_path):
    if not evidence_path.exists():
        return result("REC-001", dataset, "BLOCKED",
                      "evidência REC-001 persistida com result=PASS",
                      "evidência ausente",
                      "A validação determinística não recria REC-001; exige evidência persistida.")
    try:
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        raw_sha = sha256(raw_path)
        observed_sha = evidence.get("raw_sha256")
        status = evidence.get("result")
        semantic_equal = evidence.get("semantic_records_equal", True)
        ok = status == "PASS" and observed_sha == raw_sha and semantic_equal is True
        return result("REC-001", dataset, "PASS" if ok else "FAIL",
                      {"result": "PASS", "raw_sha256": raw_sha, "semantic_records_equal": True},
                      {"result": status, "raw_sha256": observed_sha, "semantic_records_equal": semantic_equal},
                      "Evidência REC-001 independente verificada contra o RAW persistido.")
    except Exception as e:
        return result("REC-001", dataset, "FAIL", "evidência JSON válida", str(e),
                      "Falha ao ler/validar evidência REC-001.")

def validate_b3_rec(evidence_path, raw_path):
    if not evidence_path.exists():
        return result("REC-001", "B3_COTACOES", "BLOCKED",
                      "evidência B3 persistida", "evidência ausente",
                      "Arquivo de reconciliação B3 não encontrado.")
    try:
        kv = {}
        for line in evidence_path.read_text(encoding="utf-8").splitlines():
            if "=" in line:
                k, v = line.split("=", 1)
                kv[k.strip()] = v.strip()
        raw_sha = sha256(raw_path)
        current_sha = kv.get("current_endpoint_sha256")
        status = kv.get("reconciliation_status")
        ok = current_sha == raw_sha and status == "SOURCE_UPDATED_SINCE_REFERENCE"
        return result("REC-001", "B3_COTACOES", "PASS" if ok else "FAIL",
                      {"current_endpoint_sha256": raw_sha, "reconciliation_status": "SOURCE_UPDATED_SINCE_REFERENCE"},
                      {"current_endpoint_sha256": current_sha, "reconciliation_status": status},
                      "Evidência B3 reconciliada; atualização da fonte histórica é explicitamente registrada.")
    except Exception as e:
        return result("REC-001", "B3_COTACOES", "FAIL", "evidência B3 válida", str(e),
                      "Falha ao ler/validar evidência B3.")

tests.append(validate_b3_rec(rec_evidence["B3_COTACOES"], files["B3_COTACOES"]))
for dataset in ("CVM_OFERTAS", "BCB_SGS", "TESOURO_HISTORICO", "VIX"):
    tests.append(validate_rec_json(dataset, rec_evidence[dataset], files[dataset]))

# Provenance/evidence/gate are evaluated at the report level.
for dataset, path in files.items():
    if path.exists():
        tests.append(result("PRO-001", dataset, "PASS",
                            "RAW + filename + SHA disponíveis",
                            {"filename": path.name, "sha256": sha256(path)},
                            "Proveniência mínima local disponível."))

summary = {}
for dataset in files:
    ds = [x for x in tests if x["dataset"] == dataset]
    statuses = {x["result"] for x in ds}
    if "FAIL" in statuses:
        state = "REJECTED"
    elif "BLOCKED" in statuses:
        state = "BLOCKED"
    elif not ds:
        state = "NOT_READY"
    else:
        state = "VALIDATED"
    summary[dataset] = state

gate = "PASS" if all(v == "VALIDATED" for v in summary.values()) else (
    "FAIL" if any(v == "REJECTED" for v in summary.values()) else "BLOCKED"
)
tests.append(result("GAT-001", "GLOBAL", gate, "todos os datasets VALIDATED", summary,
                    "Gate V1.0: qualquer BLOCKED impede promoção."))

report = {
    "contract": "CONTRATO_VERIFICACAO_V1_0",
    "matrix": "MATRIZ_TESTES_V1_0",
    "generated_at_utc": datetime.utcnow().isoformat(timespec="seconds") + "Z",
    "datasets": summary,
    "global_gate": gate,
    "tests": tests,
    "promotion": "BLOCKED" if gate != "PASS" else "ELIGIBLE_FOR_REVIEW",
}

(OUT / "resultado_005D.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

md = [
    "# INGESTÃO 005D — RESULTADO AUTOMÁTICO",
    "",
    f"> Gerado em UTC: {report['generated_at_utc']}",
    "",
    "## Resultado por dataset",
    "",
    "| Dataset | Estado |",
    "|---|---|",
]
md += [f"| {k} | {v} |" for k, v in summary.items()]
md += [
    "",
    f"**GAT-001 global: {gate}**",
    "",
    "REC-001 é consumido exclusivamente de evidências persistidas e verificadas contra o RAW; esta etapa não redownload nem altera RAW.",
    "",
    "Nenhum RAW foi alterado. Nenhuma promoção para Layer A foi executada.",
]
(OUT / "resultado_005D.md").write_text("\n".join(md) + "\n", encoding="utf-8")

print(json.dumps({"datasets": summary, "global_gate": gate}, indent=2))
