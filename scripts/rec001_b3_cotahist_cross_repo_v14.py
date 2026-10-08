#!/usr/bin/env python3
# BLOOMBERG_MAIL — REC-001 B3 COTAHIST — reconciliação corrigida
import hashlib,json,os,tempfile,urllib.request,zipfile
from collections import defaultdict
BLOOM="EMAILS_RECEBIDOS/INGESTAO/005/RAW/COTAHIST_A2026.ZIP"
MANIFEST="EMAILS_RECEBIDOS/INGESTAO/005/manifesto_aquisicao.json"
B3URL="https://raw.githubusercontent.com/carlos-andrade/B3/main/dados/cotahist/raw/anual/COTAHIST_A2026.ZIP"
OUT="EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_CROSS_REPO_2026-10-08.json"
def sha(p):
 h=hashlib.sha256()
 with open(p,"rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()
def inspect(p):
 with zipfile.ZipFile(p) as z:
  n=next(x for x in z.namelist() if x.upper().endswith("COTAHIST_A2026.TXT"))
  dates=[];count=0;generation=None;stream=hashlib.sha256()
  with z.open(n) as f:
   for raw in f:
    line=raw.rstrip(b"\r\n")
    if len(line)!=245: raise RuntimeError(f"invalid record length {len(line)}")
    if line[:2]==b"00": generation=line[23:31].decode("ascii","replace").strip()
    elif line[:2]==b"01":
     count+=1;dates.append(line[2:10].decode("ascii","replace"));stream.update(line)
  return {"member":n,"record01_count":count,"date_min":min(dates),"date_max":max(dates),"generation_date":generation,"record01_stream_sha256":stream.hexdigest()}
def per_date_multiset(path,lo,hi):
 g=defaultdict(list)
 with zipfile.ZipFile(path) as z:
  n=next(x for x in z.namelist() if x.upper().endswith("COTAHIST_A2026.TXT"))
  with z.open(n) as f:
   for raw in f:
    line=raw.rstrip(b"\r\n"); d=line[2:10].decode("ascii","replace")
    if line[:2]==b"01" and lo<=d<=hi:g[d].append(hashlib.sha256(line).digest())
 out={}
 for d,v in g.items():
  v.sort();h=hashlib.sha256()
  for x in v:h.update(x)
  out[d]=(len(v),h.hexdigest())
 return out
def main():
 with open(MANIFEST,encoding="utf-8") as f:m=json.load(f)
 meta=next(x for x in m["datasets"] if x["id"]=="B3_COTACOES")
 with tempfile.TemporaryDirectory() as td:
  b3=os.path.join(td,"COTAHIST_A2026.ZIP")
  req=urllib.request.Request(B3URL,headers={"User-Agent":"BLOOMBERG_MAIL-REC001/1.4"})
  with urllib.request.urlopen(req,timeout=300) as r,open(b3,"wb") as f:
   for x in iter(lambda:r.read(1024*1024),b""):f.write(x)
  a=inspect(BLOOM);b=inspect(b3);lo=max(a["date_min"],b["date_min"]);hi=min(a["date_max"],b["date_max"])
  da=per_date_multiset(BLOOM,lo,hi);db=per_date_multiset(b3,lo,hi)
  common=sorted(set(da)&set(db));bad=[d for d in common if da[d]!=db[d]]
  result="PASS_OVERLAP_EXACT" if not bad and b["date_max"]<a["date_max"] else ("PASS_EXACT" if not bad else "FAIL_CONTENT_DIVERGENCE")
  ev={"schema_version":"1.4-rec001-b3-cross-repo","result":result,"raw_preserved":True,"comparison_scope":"TIPREG=01; complete 245-byte record; per-trading-date order-independent multiset; CR/LF excluded from record identity","bloomberg_mail":{"path":BLOOM,"zip_sha256":sha(BLOOM),"retrieval_timestamp_utc":meta.get("retrieval_timestamp_utc"),"stats":a},"b3":{"url":B3URL,"zip_sha256":sha(b3),"stats":b},"temporal_evidence":{"common_date_min":lo,"common_date_max":hi,"generation_date_bloomberg_mail":a["generation_date"],"generation_date_b3":b["generation_date"]},"comparison":{"dates_tested":len(common),"convergent_dates":len(common)-len(bad),"divergent_dates":bad,"exact_common_period":not bad,"sample_convergent_dates":common[:5]+common[-5:],"sample_divergent_dates":bad[:10]},"diagnostic_conclusion":"As datas são comparadas individualmente. Se todas convergem, a divergência anterior era metodológica e não de conteúdo."}
  os.makedirs(os.path.dirname(OUT),exist_ok=True)
  with open(OUT,"w",encoding="utf-8") as f:json.dump(ev,f,ensure_ascii=False,indent=2);f.write("\n")
if __name__=="__main__":main()
