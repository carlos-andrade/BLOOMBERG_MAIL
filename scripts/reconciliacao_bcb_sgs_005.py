#!/usr/bin/env python3
"""BLOOMBERG_MAIL — REC-001 BCB SGS 1178 — independent reconciliation."""

from __future__ import annotations
import hashlib, json, tempfile, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ENDPOINT = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados?formato=json&dataInicial=23/09/2026&dataFinal=06/10/2026"
RAW = Path("EMAILS_RECEBIDOS/INGESTAO/005/RAW/bcb_sgs_1178_ultimos_10.json")
OUT_JSON = Path("EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/EXECUCAO_AUTOMATICA/rec001_bcb_sgs_1178.json")
OUT_MD = Path("EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/EXECUCAO_AUTOMATICA/rec001_bcb_sgs_1178.md")

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def canonical(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    return sorted({"data": x["data"], "valor": x.get("valor", x.get("value"))} for x in data)

def main() -> int:
    observed_at = datetime.now(timezone.utc).isoformat()
    if not RAW.exists():
        result = {"dataset":"BCB_SGS_1178","result":"FAIL","reason":"RAW_NOT_FOUND","observed_at_utc":observed_at}
    else:
        raw_sha = sha256(RAW)
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "bcb.json"
            req = urllib.request.Request(ENDPOINT, headers={"User-Agent":"BLOOMBERG_MAIL-REC001/1.0","Accept":"application/json"})
            with urllib.request.urlopen(req, timeout=120) as r, p.open("wb") as f:
                f.write(r.read())
            endpoint_sha = sha256(p)
            remote = canonical(p)
        local = canonical(RAW)
        same = local == remote
        result = {
            "dataset":"BCB_SGS_1178",
            "series_code":"1178",
            "result":"PASS" if same else "SOURCE_UPDATED_OR_REPRESENTATION_DIFFERENT",
            "endpoint":ENDPOINT,
            "observed_at_utc":observed_at,
            "raw_sha256":raw_sha,
            "endpoint_sha256":endpoint_sha,
            "raw_preserved":True,
            "raw_records":len(local),
            "endpoint_records":len(remote),
            "semantic_records_equal":same,
            "promotion_impact":"BCB_REC_RECONCILED" if same else "BLOCKED_REVIEW_REQUIRED"
        }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    status = result["result"]
    OUT_MD.write_text(
        "# BLOOMBERG_MAIL — INGESTÃO 005 — REC-001 BCB SGS 1178\n\n"
        "> Cabeçalho histórico — 2026-10-07.\n\n"
        f"- Endpoint oficial: {result.get('endpoint', ENDPOINT)}\n"
        f"- Observado UTC: {result.get('observed_at_utc')}\n"
        f"- RAW preservado: {result.get('raw_preserved', False)}\n"
        f"- SHA RAW: {result.get('raw_sha256','N/A')}\n"
        f"- SHA endpoint: {result.get('endpoint_sha256','N/A')}\n"
        f"- Registros RAW: {result.get('raw_records','N/A')}\n"
        f"- Registros endpoint: {result.get('endpoint_records','N/A')}\n"
        f"- Igualdade semântica: {result.get('semantic_records_equal','N/A')}\n"
        f"- Resultado: **{status}**\n\n"
        "## Regra\n\n"
        "A fonte oficial é consultada em área temporária. O RAW nunca é substituído. A decisão usa comparação semântica dos registros; SHA-256 é preservado como evidência de bytes. Divergência bloqueia promoção."
        "\n",
        encoding="utf-8"
    )
    return 0 if status == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
