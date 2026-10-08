#!/usr/bin/env python3
# BLOOMBERG_MAIL — REC-001 B3 COTAHIST — diagnóstico de convergência por pregão
import hashlib, json, os, tempfile, urllib.request, zipfile
from collections import defaultdict

BLOOM="EMAILS_RECEBIDOS/INGESTAO/005/RAW/COTAHIST_A2026.ZIP"
MANIFEST="EMAILS_RECEBIDOS/INGESTAO/005/manifesto_aquisicao.json"
B3URL="https://raw.githubusercontent.com/carlos-andrade/B3/main/dados/cotahist/raw/anual/COTAHIST_A2026.ZIP"
OUT="EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_CONVERGENCIA_POR_DATA_2026-10-08.json"

def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def by_date(path):
    groups=defaultdict(list)
    with zipfile.ZipFile(path) as z:
        n=next(x for x in z.namelist() if x.upper().endswith("COTAHIST_A2026.TXT"))
        with z.open(n) as f:
            for raw in f:
                line=raw.rstrip(b"\r\n")
                if len(line)!=245 or line[:2]!=b"01":
                    continue
                d=line[2:10].decode("ascii","replace")
                groups[d].append(hashlib.sha256(line).digest())
    out={}
    for d,vals in groups.items():
        vals.sort()
        h=hashlib.sha256()
        for v in vals: h.update(v)
        out[d]={"count":len(vals),"multiset_sha256":h.hexdigest()}
    return out

def main():
    with open(MANIFEST,encoding="utf-8") as f: manifest=json.load(f)
    meta=next(d for d in manifest["datasets"] if d["id"]=="B3_COTACOES")
    with tempfile.TemporaryDirectory() as td:
        b3=os.path.join(td,"COTAHIST_A2026.ZIP")
        req=urllib.request.Request(B3URL,headers={"User-Agent":"BLOOMBERG_MAIL-REC001-CONVERGENCIA/1.0"})
        with urllib.request.urlopen(req,timeout=300) as r, open(b3,"wb") as f:
            for x in iter(lambda:r.read(1024*1024),b""): f.write(x)
        a=by_date(BLOOM); b=by_date(b3)
        common=sorted(set(a)&set(b))
        matches=[d for d in common if a[d]==b[d]]
        count_matches=[d for d in common if a[d]["count"]==b[d]["count"]]
        evidence={
          "schema_version":"1.0-rec001-b3-convergencia-por-data",
          "purpose":"Encontrar pregões em que BLOOMBERG_MAIL RAW e snapshot B3 possuem exatamente o mesmo multiconjunto de registros 01 completos de 245 bytes.",
          "method":"order-independent full-record multiset per trading date; SHA-256 of each complete 245-byte record; sorted digest multiset hash; no economic adjustment.",
          "raw_preserved":True,
          "bloomberg_mail":{"path":BLOOM,"zip_sha256":sha(BLOOM),"retrieval_timestamp_utc":meta.get("retrieval_timestamp_utc")},
          "b3":{"url":B3URL,"zip_sha256":sha(b3)},
          "overlap":{"date_min":min(common) if common else None,"date_max":max(common) if common else None,"dates_tested":len(common)},
          "convergent_dates":matches,
          "count_only_convergent_dates":count_matches,
          "convergent_date_details":{d:{"bloomberg_mail":a[d],"b3":b[d]} for d in matches},
          "interpretation":"Uma data em convergent_dates prova convergência física exata naquele pregão. Isso permite isolar o problema para diferenças posteriores, snapshot/revisão ou método de comparação, sem inferir divergência econômica."
        }
        os.makedirs(os.path.dirname(OUT),exist_ok=True)
        with open(OUT,"w",encoding="utf-8") as f: json.dump(evidence,f,ensure_ascii=False,indent=2); f.write("\n")
        print(json.dumps({"convergent_dates":matches,"count_only_convergent_dates":count_matches,"dates_tested":len(common)},ensure_ascii=False))

if __name__=="__main__":
    main()
