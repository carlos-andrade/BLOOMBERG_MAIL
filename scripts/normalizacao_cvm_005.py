from __future__ import annotations
import csv, gzip, hashlib, json
from pathlib import Path
from zipfile import ZipFile
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"EMAILS_RECEBIDOS/INGESTAO/005"; RAW=BASE/"RAW"; OUT=BASE/"NORMALIZADO"
RAWFILE=RAW/"oferta_distribuicao.zip"; SHA="72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306"

def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()

def write_member(z, name):
 source=OUT/(Path(name).stem+".jsonl.gz")
 count=0; headers=[]
 with z.open(name) as raw, gzip.GzipFile(filename="",mode="wb",fileobj=source.open("wb"),mtime=0) as gz:
  import io
  text=io.TextIOWrapper(raw,encoding="latin-1",newline="")
  reader=csv.DictReader(text,delimiter=";")
  headers=reader.fieldnames or []; assert headers
  for row in reader:
   gz.write((json.dumps(row,ensure_ascii=False,separators=(",",":"))+"\n").encode("utf-8")); count+=1
 return source,count,headers

def main():
 assert sha(RAWFILE)==SHA
 OUT.mkdir(parents=True,exist_ok=True)
 members=[]
 with ZipFile(RAWFILE) as z:
  assert z.testzip() is None
  for name in ("oferta_distribuicao.csv","oferta_resolucao_160.csv"):
   path,count,headers=write_member(z,name)
   members.append({"source_member":name,"output_file":path.name,"encoding":"latin-1","delimiter":";","field_names":headers,"record_count":count,"compression":"gzip","record_format":"jsonl"})
 payload={"schema_version":"1.1-normalized-cvm","dataset_id":"CVM_OFERTAS","source":"CVM","raw_path":str(RAWFILE.relative_to(ROOT)),"raw_sha256":SHA,"processed_at_utc":"2026-10-07","parser_version":"normalizacao-005-cvm-v1.1","quality_status":"NORMALIZED_DERIVED","storage_policy":"CHUNKED_COMPRESSED_JSONL","members":members}
 (OUT/"cvm_ofertas_normalizado.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print("CVM NORMALIZATION: PASS")
if __name__=="__main__": main()
