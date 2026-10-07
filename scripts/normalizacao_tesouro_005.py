from __future__ import annotations
import csv, hashlib, json
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"EMAILS_RECEBIDOS/INGESTAO/005"; RAW=BASE/"RAW"; OUT=BASE/"NORMALIZADO"/"tesouro_normalizado.json"
RAWFILE=RAW/"precotaxatesourodireto.csv"; SHA="8c0aa0c51b23d49843bf8c912adec1eb8fc959755f3a671e319c98a692b83d4e"
def sha(p):
 h=hashlib.sha256(); f=p.open("rb")
 for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()
def main():
 assert sha(RAWFILE)==SHA
 text=RAWFILE.read_text(encoding="utf-8-sig")
 reader=csv.DictReader(text.splitlines(),delimiter=";"); headers=reader.fieldnames or []; assert len(headers)==8
 records=[]
 for row in reader:
  out=dict(row)
  for k in ("Data Vencimento","Data Base"):
   if row[k]: out[k+"_ISO"]=datetime.strptime(row[k],"%d/%m/%Y").date().isoformat()
  records.append(out)
 payload={"schema_version":"1.0-normalized-tesouro","dataset_id":"TESOURO_HISTORICO","source":"Tesouro Direto","raw_path":str(RAWFILE.relative_to(ROOT)),"raw_sha256":SHA,"processed_at_utc":"2026-10-07","parser_version":"normalizacao-005-tesouro-v1.0","quality_status":"NORMALIZED_DERIVED","field_names":headers,"record_count":len(records),"records":records}
 OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
 print("TESOURO NORMALIZATION: PASS")
if __name__=="__main__": main()
