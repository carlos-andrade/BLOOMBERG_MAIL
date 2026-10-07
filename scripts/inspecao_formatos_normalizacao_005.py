#!/usr/bin/env python3
from pathlib import Path
import csv, json, zipfile, hashlib

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/"EMAILS_RECEBIDOS/INGESTAO/005/RAW"
OUT=ROOT/"EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO"
OUT.mkdir(parents=True,exist_ok=True)

def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()

def zip_inspect(name):
 p=RAW/name
 with zipfile.ZipFile(p) as z:
  members=[]
  for i in z.infolist():
   members.append({"name":i.filename,"size":i.file_size,"compressed_size":i.compress_size,"crc":f"{i.CRC:08x}"})
 return {"file":name,"sha256":sha(p),"members":members}

report={"schema_version":"1.0-format-inspection","raw_policy":"IMMUTABLE",
 "b3":zip_inspect("COTAHIST_A2026.ZIP"),
 "cvm":zip_inspect("oferta_distribuicao.zip")}

p=RAW/"precotaxatesourodireto.csv"
with p.open("r",encoding="utf-8-sig",newline="") as f:
 r=csv.reader(f)
 header=next(r)
 samples=[next(r) for _ in range(3)]
report["tesouro"]={"file":p.name,"sha256":sha(p),"header":header,"sample_rows":samples}

(OUT/"INSPECAO_FORMATOS_005.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k: (len(v["members"]) if "members" in v else len(v["header"])) for k,v in report.items() if isinstance(v,dict) and k in ["b3","cvm","tesouro"]}))
