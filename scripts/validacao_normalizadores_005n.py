from pathlib import Path
import json, hashlib, gzip
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"EMAILS_RECEBIDOS/INGESTAO/005"; RAW=BASE/"RAW"; N=BASE/"NORMALIZADO"; OUT=N/"VALIDACAO_NORMALIZADORES_005N.json"
EXPECTED={"BCB_SGS_1178":("bcb_sgs_1178_ultimos_10.json","7343beba0c0d8fad8593bf7d4d74746f7981fd186bc1b25bece94a6d3bd71f36","bcb_sgs_1178_normalizado.json"),"VIX":("VIX_History.csv","cfcb9dce25bbbbd83aedca9a1480468bb25db2e988b3e893a4eebabb1905e1ab","vix_normalizado.json"),"CVM_OFERTAS":("oferta_distribuicao.zip","72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306","cvm_ofertas_normalizado.json"),"TESOURO_HISTORICO":("precotaxatesourodireto.csv","8c0aa0c51b23d49843bf8c912adec1eb8fc959755f3a671e319c98a692b83d4e","tesouro_normalizado.json")}
def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()
def gzip_ok(p):
 with gzip.open(p,"rt",encoding="utf-8") as f:
  for _ in range(3): 
   if not f.readline(): break
 return True
def main():
 checks={}
 for ds,(raw,expected,out) in EXPECTED.items():
  rp=RAW/raw; op=N/out; assert rp.exists(),f"missing RAW {ds}"; assert op.exists(),f"missing normalized {ds}"
  actual=sha(rp); data=json.loads(op.read_text(encoding="utf-8")); linked=data.get("raw_sha256")
  assert actual==expected and linked==expected and data.get("quality_status")=="NORMALIZED_DERIVED"
  files=[]
  if ds=="CVM_OFERTAS":
   for m in data["members"]:
    p=N/m["output_file"]; assert p.exists(),m["output_file"]; assert gzip_ok(p); files.append(p.name)
  elif ds=="TESOURO_HISTORICO":
   p=N/data["output_file"]; assert p.exists(); assert gzip_ok(p); files.append(p.name)
  checks[ds]={"raw_sha_match":True,"normalized_raw_link_match":True,"quality_status":data["quality_status"],"output_exists":True,"derived_files":files}
 payload={"schema_version":"1.1-normalizer-validation","status":"PASS","raw_policy":"IMMUTABLE","checks":checks,"dataset_count":len(checks),"integration_gate":"BLOCKED_UNTIL_B3_NORMALIZER_AND_ALL_FIVE_VALIDATED","notes":"Validates persisted derived outputs and compressed JSONL manifests; does not execute or modify RAW."}
 OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("JOINT NORMALIZER VALIDATION: PASS")
if __name__=="__main__": main()
