from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/"EMAILS_RECEBIDOS/INGESTAO/005"; RAW=BASE/"RAW"; N=BASE/"NORMALIZADO"; OUT=N/"VALIDACAO_NORMALIZADORES_005N.json"
EXPECTED={"BCB_SGS_1178":("bcb_sgs_1178_ultimos_10.json","7343beba0c0d8fad8593bf7d4d74746f7981fd186bc1b25bece94a6d3bd71f36","bcb_sgs_1178_normalizado.json"),"VIX":("VIX_History.csv","cfcb9dce25bbbbd83aedca9a1480468bb25db2e988b3e893a4eebabb1905e1ab","vix_normalizado.json"),"CVM_OFERTAS":("oferta_distribuicao.zip","72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306","cvm_ofertas_normalizado.json"),"TESOURO_HISTORICO":("precotaxatesourodireto.csv","8c0aa0c51b23d49843bf8c912adec1eb8fc959755f3a671e319c98a692b83d4e","tesouro_normalizado.json")}
def sha(p):
 h=hashlib.sha256(); f=p.open("rb")
 for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()
def main():
 checks={}
 for ds,(raw,expected,out) in EXPECTED.items():
  rp=RAW/raw; op=N/out; assert rp.exists(),f"missing RAW {ds}"; assert op.exists(),f"missing normalized {ds}"
  actual=sha(rp); data=json.loads(op.read_text(encoding="utf-8")); linked=data.get("raw_sha256")
  checks[ds]={"raw_sha_match":actual==expected,"normalized_raw_link_match":linked==expected,"quality_status":data.get("quality_status"),"output_exists":True}
  assert actual==expected and linked==expected and data.get("quality_status")=="NORMALIZED_DERIVED"
 payload={"schema_version":"1.0-normalizer-validation","status":"PASS","raw_policy":"IMMUTABLE","checks":checks,"dataset_count":len(checks),"integration_gate":"BLOCKED_UNTIL_B3_NORMALIZER_AND_ALL_FIVE_VALIDATED","notes":"This workflow validates persisted derived outputs; it does not execute or modify RAW."}
 OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("JOINT NORMALIZER VALIDATION: PASS")
if __name__=="__main__": main()
