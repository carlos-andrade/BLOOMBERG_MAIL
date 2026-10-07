from __future__ import annotations
import csv, gzip, hashlib, json, io
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"EMAILS_RECEBIDOS/INGESTAO/005"; RAW=BASE/"RAW"; OUT=BASE/"NORMALIZADO"
RAWFILE=RAW/"precotaxatesourodireto.csv"; SHA="8c0aa0c51b23d49843bf8c912adec1eb8fc959755f3a671e319c98a692b83d4e"

def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()

def main():
 assert sha(RAWFILE)==SHA
 OUT.mkdir(parents=True,exist_ok=True)
 output=OUT/"tesouro_normalizado.jsonl.gz"; count=0; headers=[]
 with RAWFILE.open("rb") as raw, gzip.GzipFile(filename="",mode="wb",fileobj=output.open("wb"),mtime=0) as gz:
  text=io.TextIOWrapper(raw,encoding="utf-8-sig",newline="")
  reader=csv.DictReader(text,delimiter=";"); headers=reader.fieldnames or []; assert len(headers)==8
  for row in reader:
   out=dict(row)
   for k in ("Data Vencimento","Data Base"):
    if row[k]: out[k+"_ISO"]=datetime.strptime(row[k],"%d/%m/%Y").date().isoformat()
   gz.write((json.dumps(out,ensure_ascii=False,separators=(",",":"))+"\n").encode("utf-8")); count+=1
 payload={"schema_version":"1.1-normalized-tesouro","dataset_id":"TESOURO_HISTORICO","source":"Tesouro Direto","raw_path":str(RAWFILE.relative_to(ROOT)),"raw_sha256":SHA,"processed_at_utc":"2026-10-07","parser_version":"normalizacao-005-tesouro-v1.1","quality_status":"NORMALIZED_DERIVED","storage_policy":"COMPRESSED_JSONL","field_names":headers,"record_count":count,"output_file":output.name,"compression":"gzip","record_format":"jsonl"}
 (OUT/"tesouro_normalizado.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print("TESOURO NORMALIZATION: PASS")
if __name__=="__main__": main()
