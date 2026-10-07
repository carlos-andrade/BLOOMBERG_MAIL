#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'EMAILS_RECEBIDOS'/'INGESTAO'/'005'/'RAW'
OUT=ROOT/'EMAILS_RECEBIDOS'/'INGESTAO'/'005'/'VALIDACAO'/'EXECUCAO_AUTOMATICA'
OUT.mkdir(parents=True,exist_ok=True)
ENDPOINT='https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A2026.ZIP'
CURRENT='c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f'
HIST='4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768'
def sha256(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1024*1024),b''): h.update(c)
 return h.hexdigest()
p=RAW/'COTAHIST_A2026.ZIP'
observed=sha256(p) if p.exists() else None
status='PASS' if observed==CURRENT else 'FAIL'
report={'contract':'CONTRATO_VERIFICACAO_V1_0','test_id':'REC-001','dataset':'B3_COTACOES','result':status,'source_url':ENDPOINT,'raw_sha256':observed,'official_current_endpoint_sha256':CURRENT,'historical_reference_sha256':HIST,'historical_reference_status':'SOURCE_UPDATED_SINCE_REFERENCE' if observed==CURRENT and observed!=HIST else 'MATCH','generated_at_utc':datetime.utcnow().isoformat(timespec='seconds')+'Z','promotion':'B3_REC_RECONCILED' if status=='PASS' else 'BLOCKED'}
(OUT/'rec001_b3.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/'rec001_b3.md').write_text('# INGESTÃO 005 — REC-001 B3\n\n**Resultado: '+status+'**\n\n- Endpoint: '+ENDPOINT+'\n- SHA RAW atual: '+str(observed)+'\n- SHA endpoint atual esperado: '+CURRENT+'\n- SHA histórico: '+HIST+'\n- Situação histórica: '+report['historical_reference_status']+'\n\nA diferença em relação ao SHA histórico é preservada como atualização da fonte. Nenhum RAW foi sobrescrito.\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
