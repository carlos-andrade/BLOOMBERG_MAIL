#!/usr/bin/env python3
"""BLOOMBERG_MAIL — REC-001 CVM — independent endpoint reconciliation."""

from __future__ import annotations
import hashlib, json, tempfile, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ENDPOINT = "https://dados.cvm.gov.br/dados/OFERTA/DISTRIB/DADOS/oferta_distribuicao.zip"
RAW = Path("EMAILS_RECEBIDOS/INGESTAO/005/RAW/oferta_distribuicao.zip")
OUT_JSON = Path("EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/EXECUCAO_AUTOMATICA/rec001_cvm.json")
OUT_MD = Path("EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/EXECUCAO_AUTOMATICA/rec001_cvm.md")

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    observed_at=datetime.now(timezone.utc).isoformat()
    if not RAW.exists():
        result={"dataset":"CVM_OFERTAS","result":"FAIL","reason":"RAW_NOT_FOUND","observed_at_utc":observed_at}
    else:
        raw_sha=sha256(RAW)
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"oferta_distribuicao.zip"
            req=urllib.request.Request(ENDPOINT, headers={"User-Agent":"BLOOMBERG_MAIL-REC001/1.0"})
            with urllib.request.urlopen(req, timeout=120) as r, p.open("wb") as f:
                while True:
                    b=r.read(1024*1024)
                    if not b: break
                    f.write(b)
            endpoint_sha=sha256(p)
        same=raw_sha==endpoint_sha
        result={
            "dataset":"CVM_OFERTAS","result":"PASS" if same else "SOURCE_UPDATED_SINCE_RAW",
            "endpoint":ENDPOINT,"observed_at_utc":observed_at,
            "raw_sha256":raw_sha,"endpoint_sha256":endpoint_sha,
            "raw_preserved":True,
            "promotion_impact":"CVM_REC_RECONCILED" if same else "BLOCKED_NEWER_ENDPOINT"
        }
    OUT_JSON.parent.mkdir(parents=True,exist_ok=True)
    OUT_JSON.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    status=result["result"]
    OUT_MD.write_text(f"""# BLOOMBERG_MAIL — INGESTÃO 005 — REC-001 CVM

> Cabeçalho histórico — 2026-10-07.

- Endpoint oficial: {result.get("endpoint", ENDPOINT)}
- Observado UTC: {result.get("observed_at_utc")}
- RAW preservado: {result.get("raw_preserved", False)}
- SHA RAW: {result.get("raw_sha256","N/A")}
- SHA endpoint independente: {result.get("endpoint_sha256","N/A")}
- Resultado: **{status}**

## Regra

A reconciliação baixa o arquivo atual para área temporária, calcula SHA-256 independentemente e nunca substitui o RAW. Igualdade é PASS; divergência é classificada como atualização da fonte e mantém a promoção bloqueada.
""",encoding="utf-8")
    return 0 if status == "PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
