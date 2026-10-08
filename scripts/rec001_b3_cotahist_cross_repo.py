#!/usr/bin/env python3
import hashlib, json, os, tempfile, urllib.request, zipfile
BLOOM="EMAILS_RECEBIDOS/INGESTAO/005/RAW/COTAHIST_A2026.ZIP"
B3URL="https://raw.githubusercontent.com/carlos-andrade/B3/main/dados/cotahist/raw/anual/COTAHIST_A2026.ZIP"
OUT="EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_CROSS_REPO_2026-10-08.json"
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
 return h.hexdigest()
def stats(p):
 with zipfile.ZipFile(p) as z:
  n=next(x for x in z.namelist() if x.upper().endswith("COTAHIST_A2026.TXT"))
  with z.open(n) as f:
   c=0; d=[]; h=hashlib.sha256(); first=None; last=None
   for r in f:
    h.update(r); line=r.rstrip(b'\r\n')
    if len(line)!=245: raise RuntimeError(f"invalid record length {len(line)}")
    t=line[:2]
    if t==b'00' and first is None: first=line.decode('latin1')
    if t==b'01':
     c+=1; d.append(line[2:10].decode()); 
     if last is None: pass
     last=line.decode('latin1')
   return {'member':n,'member_sha256':h.hexdigest(),'record01_count':c,'date_min':min(d),'date_max':max(d),'first_record00':first,'last_record01':last}
def compare(a,b):
 with zipfile.ZipFile(a) as za, zipfile.ZipFile(b) as zb:
  na=next(x for x in za.namelist() if x.upper().endswith("COTAHIST_A2026.TXT")); nb=next(x for x in zb.namelist() if x.upper().endswith("COTAHIST_A2026.TXT"))
  with za.open(na) as fa, zb.open(nb) as fb:
   i=0
   while True:
    ra=fa.readline(); rb=fb.readline()
    if not ra or not rb: return {'common_prefix_records':i,'bloom_exhausted':not ra,'b3_exhausted':not rb,'first_difference':None}
    i+=1
    if ra!=rb:
     return {'common_prefix_records':i-1,'bloom_exhausted':False,'b3_exhausted':False,'first_difference':{'position':i,'bloom_sha256':hashlib.sha256(ra).hexdigest(),'b3_sha256':hashlib.sha256(rb).hexdigest(),'bloom_prefix':ra[:40].decode('latin1'),'b3_prefix':rb[:40].decode('latin1')}}
def main():
 with tempfile.TemporaryDirectory() as td:
  b3=os.path.join(td,'COTAHIST_A2026.ZIP')
  req=urllib.request.Request(B3URL,headers={'User-Agent':'BLOOMBERG_MAIL-REC001/1.0'})
  with urllib.request.urlopen(req,timeout=180) as r, open(b3,'wb') as f:
   for x in iter(lambda:r.read(1024*1024),b''): f.write(x)
  cmp=compare(BLOOM,b3)
  result='PASS_OVERLAP_EXACT' if cmp['first_difference'] is None and cmp['b3_exhausted'] and not cmp['bloom_exhausted'] else ('PASS_EXACT' if cmp['first_difference'] is None and cmp['b3_exhausted'] and cmp['bloom_exhausted'] else 'FAIL_CONTENT_DIVERGENCE')
  ev={'schema_version':'1.0-rec001-b3-cross-repo','result':result,'raw_preserved':True,'bloomberg_mail':{'path':BLOOM,'zip_sha256':sha(BLOOM),'stats':stats(BLOOM)},'b3':{'url':B3URL,'zip_sha256':sha(b3),'stats':stats(b3)},'comparison':cmp,'promotion_impact':'REC001_B3_PASS_OVERLAP' if result=='PASS_OVERLAP_EXACT' else ('REC001_B3_PASS' if result=='PASS_EXACT' else 'BLOCKED_CONTENT_DIVERGENCE')}
 os.makedirs(os.path.dirname(OUT),exist_ok=True)
 with open(OUT,'w',encoding='utf-8') as f: json.dump(ev,f,ensure_ascii=False,indent=2); f.write('\n')
if __name__=='__main__': main()
