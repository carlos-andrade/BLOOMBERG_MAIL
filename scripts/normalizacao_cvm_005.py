from __future__ import annotations
import csv, hashlib, io, json
from pathlib import Path
from zipfile import ZipFile
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"EMAILS_RECEBIDOS/INGESTAO/005"; RAW=BASE/"RAW"; OUT=BASE/"NORMALIZADO"/"cvm_ofertas_normalizado.json"
RAWFILE=RAW/"oferta_distribuicao.zip"; SHA="72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306"
def sha(p):
 h=hashlib.sha256(); f=p.open("rb")
 for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()
def main():
 assert sha(RAWFILE)==SHA
 rows=[]
 with ZipFile(RAWFILE) as z:
  assert z.testzip() is None
  for name in ("oferta_distribuicao.csv","oferta_resolucao_160.csv"):
   raw=z.read(name).decode("latin-1")
   reader=csv.DictReader(io.StringIO(raw),delimiter=";")
   headers=reader.fieldnames or []
   assert headers
   data=list(reader)
   rows.append({"source_member":name,"encoding":"latin-1","delimiter":";","field_names":headers,"record_count":len(data),"records":data})
 payload={"schema_version":"1.0-normalized-cvm","dataset_id":"CVM_OFERTAS","source":"CVM","raw_path":str(RAWFILE.relative_to(ROOT)),"raw_sha256":SHA,"processed_at_utc":"2026-10-07","parser_version":"normalizacao-005-cvm-v1.0","quality_status":"NORMALIZED_DERIVED","members":rows}
 OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
 print("CVM NORMALIZATION: PASS")
if __name__=="__main__": main()
