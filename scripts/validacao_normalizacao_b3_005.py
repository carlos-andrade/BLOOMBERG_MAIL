#!/usr/bin/env python3
"""BLOOMBERG_MAIL — validação independente da normalização B3 COTAHIST 005N."""
from __future__ import annotations
import gzip, hashlib, json, re
from pathlib import Path
from datetime import datetime

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"EMAILS_RECEBIDOS/INGESTAO/005"
RAW=BASE/"RAW"/"COTAHIST_A2026.ZIP"
OUT=BASE/"NORMALIZADO"/"B3"
MANIFEST=OUT/"b3_cotahist_normalizado.json"
REPORT=OUT/"VALIDACAO_NORMALIZACAO_B3_A2026.json"
RAW_SHA="c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f"
EXPECTED_RECORDS=3070831
EXPECTED_021=1696
PARSER="normalizacao-005-b3-v1.0"
REQUIRED_RAW=[
"tipreg","data_pregao_raw","codbdi","codneg","tpmerc","nomres","especi","prazot","modref",
"preabe_raw","premax_raw","premin_raw","premed_raw","preult_raw","preofc_raw","preofv_raw",
"totneg_raw","quatot_raw","voltot_raw","preexe_raw","indopc","datven_raw","fatcot_raw",
"ptoexe_raw","codisi","dismes"]
DECIMALS={"preabe":2,"premax":2,"premin":2,"premed":2,"preult":2,"preofc":2,"preofv":2,
"voltot":2,"preexe":2,"ptoexe":6}

def sha256(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()

def valid_date(s):
 return s is None or bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}",s)) and datetime.strptime(s,"%Y-%m-%d")

def valid_decimal(s, decimals):
 if s is None: return True
 return bool(re.fullmatch(r"-?\d+(?:\.\d{%d})?" % decimals,s))

def main():
 m=json.loads(MANIFEST.read_text(encoding="utf-8"))
 assert m["raw_sha256"]==RAW_SHA
 assert sha256(RAW)==RAW_SHA
 assert m["parser_version"]==PARSER
 files=sorted(OUT.glob("cotahist_a2026_part_*.jsonl.gz"))
 assert [p.name for p in files]==m["output_files"]
 keys=set(); duplicates=0; count=0; c021=0; invalid=0; missing=0; bad_dates=0; bad_decimals=0; bad_semantics=0
 for path in files:
  with gzip.open(path,"rt",encoding="utf-8") as f:
   for line in f:
    if not line.strip(): continue
    count+=1
    try: x=json.loads(line)
    except Exception: invalid+=1; continue
    if any(k not in x for k in REQUIRED_RAW): invalid+=1; continue
    if any(x[k]=="" for k in REQUIRED_RAW): missing+=1
    if not valid_date(x["data_pregao"]) or not valid_date(x["datven"]): bad_dates+=1
    for k,d in DECIMALS.items():
     if not valid_decimal(x[k],d): bad_decimals+=1
    if x["tpmerc"]=="021":
     c021+=1
     if x["tpmerc_semantica"]!="BLOCK LOT / BBT" or x["tpmerc_reconciliacao"]!="CONTROLLED_RECONCILIATION_2026-10-08": bad_semantics+=1
    else:
     if x["tpmerc_semantica"] is not None or x["tpmerc_reconciliacao"] is not None: bad_semantics+=1
    key=(x["data_pregao"],x["codbdi"],x["codneg"],x["tpmerc"])
    if key in keys: duplicates+=1
    else: keys.add(key)
 assert count==EXPECTED_RECORDS
 assert c021==EXPECTED_021
 assert invalid==0 and missing==0 and bad_dates==0 and bad_decimals==0 and bad_semantics==0
 assert duplicates==m["duplicate_count"]
 assert m["record_count"]==count and m["tpmerc_021_count"]==c021
 report={"schema_version":"1.0-b3-normalization-validation","status":"PASS","dataset_id":"B3_COTAHIST_A2026",
 "raw_path":str(RAW.relative_to(ROOT)),"raw_sha256":RAW_SHA,"parser_version":PARSER,
 "manifest_path":str(MANIFEST.relative_to(ROOT)),"checks":{
 "raw_sha_match":True,"manifest_parser_match":True,"partition_count":len(files),
 "record_count":count,"record_count_expected":EXPECTED_RECORDS,"tpmerc_021_count":c021,
 "tpmerc_021_expected":EXPECTED_021,"duplicate_count":duplicates,"missing_field_count":missing,
 "invalid_json_records":invalid,"invalid_dates":bad_dates,"invalid_decimals":bad_decimals,
 "tpmerc_021_semantics_errors":bad_semantics},
 "policy":{"raw_immutable":True,"economic_adjustment":False,"interpolation":False,"invention":False}}
 REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
