#!/usr/bin/env python3
# INGESTAO-005F: SHA-256 determinístico corrigido e validado.
import csv, hashlib, json, os, sys, tempfile  # deterministic acquisition
from datetime import datetime, timezone
from urllib.request import Request, urlopen

ENDPOINT="https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/precotaxatesourodireto.csv"
RAW="EMAILS_RECEBIDOS/INGESTAO/005/RAW/precotaxatesourodireto.csv"
SHA_FILE=RAW+".sha256"
EVIDENCE_JSON="EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/EXECUCAO_AUTOMATICA/aquisicao_tesouro_direto_005.json"
EVIDENCE_MD="EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/EXECUCAO_AUTOMATICA/aquisicao_tesouro_direto_005.md"

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as fh:
        for chunk in iter(lambda: fh.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def validate(path):
    if os.path.getsize(path)==0: raise ValueError("arquivo vazio")
    with open(path,"r",encoding="utf-8-sig",newline="") as f: rows=list(csv.reader(f,delimiter=";"))
    if len(rows)<2: raise ValueError("CSV sem registros")
    header=rows[0]
    if len(header)<8: raise ValueError(f"schema inesperado: {len(header)} colunas")
    records=rows[1:]
    for i,r in enumerate(records,2):
        if len(r)!=len(header): raise ValueError(f"linha {i}: {len(r)} colunas; esperado {len(header)}")
    dates=[r[2] for r in records if len(r)>2 and r[2]]
    if not dates: raise ValueError("Data Base ausente")
    return {"bytes":os.path.getsize(path),"rows":len(records),"columns":len(header),"header":header,
            "first_data_base":min(dates),"last_data_base":max(dates),
            "missing_rows":sum(1 for r in records if any(x.strip()=="" for x in r)),
            "duplicate_rows":len(records)-len({tuple(r) for r in records})}

def main():
    os.makedirs(os.path.dirname(EVIDENCE_JSON),exist_ok=True)
    os.makedirs(os.path.dirname(RAW),exist_ok=True)
    observed=datetime.now(timezone.utc).isoformat()
    result={"dataset":"TESOURO_HISTORICO","source":"Tesouro Direto/Tesouro Transparente","endpoint":ENDPOINT,
            "observed_at_utc":observed,"raw_preserved":False,"result":"FAIL"}
    tmp_path=None
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp: tmp_path=tmp.name
        req=Request(ENDPOINT,headers={"User-Agent":"BLOOMBERG_MAIL/INGESTAO-005"})
        with urlopen(req,timeout=120) as resp, open(tmp_path,"wb") as out:
            while True:
                chunk=resp.read(1024*1024)
                if not chunk: break
                out.write(chunk)
        meta=validate(tmp_path)
        endpoint_sha=sha256(tmp_path)
        existing_sha=sha256(RAW) if os.path.exists(RAW) and os.path.getsize(RAW)>0 else None
        if existing_sha and existing_sha!=endpoint_sha:
            result.update({"result":"FAIL_RAW_IMMUTABILITY_CONFLICT","endpoint_sha256":endpoint_sha,
                           "existing_raw_sha256":existing_sha,"validation":meta,
                           "error":"Existing non-empty RAW differs from current official endpoint; no overwrite permitted.",
                           "promotion_impact":"BLOCKED_RAW_IMMUTABILITY"})
        else:
            os.replace(tmp_path,RAW)
            with open(SHA_FILE,"w",encoding="utf-8") as f: f.write(endpoint_sha+"  precotaxatesourodireto.csv\n")
            result.update({"result":"PASS","endpoint_sha256":endpoint_sha,"raw_sha256":endpoint_sha,
                           "raw_preserved":True,"validation":meta,"promotion_impact":"TESOURO_ACQUIRED_RAW_VALIDATED"})
        with open(EVIDENCE_JSON,"w",encoding="utf-8") as f: json.dump(result,f,ensure_ascii=False,indent=2)
        with open(EVIDENCE_MD,"w",encoding="utf-8") as f:
            f.write("# BLOOMBERG_MAIL — INGESTÃO 005 — Aquisição Tesouro Direto\n\n")
            f.write("## Cabeçalho histórico\n- Projeto: BLOOMBERG_MAIL\n- Ingestão: 005\n- Fonte: Tesouro Direto / Tesouro Transparente\n\n")
            f.write("Resultado: "+result["result"]+"\n\n")
            f.write(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
        return 0 if result["result"]=="PASS" else 1
    except Exception as e:
        result.update({"result":"FAIL_SOURCE_ACCESS_OR_VALIDATION","error_type":type(e).__name__,
                       "error":str(e),"promotion_impact":"BLOCKED_SOURCE_ACCESS"})
        with open(EVIDENCE_JSON,"w",encoding="utf-8") as f: json.dump(result,f,ensure_ascii=False,indent=2)
        with open(EVIDENCE_MD,"w",encoding="utf-8") as f: f.write("# BLOOMBERG_MAIL — INGESTÃO 005 — Aquisição Tesouro Direto\n\n"+json.dumps(result,ensure_ascii=False,indent=2)+"\n")
        return 1
    finally:
        if tmp_path:
            try: os.unlink(tmp_path)
            except FileNotFoundError: pass

if __name__=="__main__": sys.exit(main())
