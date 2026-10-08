#!/usr/bin/env python3
import hashlib, json, os, tempfile, urllib.request, zipfile
from datetime import datetime

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
        with z.open(n) as f:
            count=0; dates=[]; generation=None; record01_hash=hashlib.sha256()
            for raw in f:
                line=raw.rstrip(b"\r\n")
                if len(line)!=245: raise RuntimeError(f"invalid record length {len(line)}")
                if line[:2]==b"00":
                    generation=line[24:32].decode("ascii",errors="replace").strip()
                elif line[:2]==b"01":
                    count += 1; dates.append(line[2:10].decode("ascii",errors="replace"))
                    record01_hash.update(raw)
            return {"member":n,"record01_count":count,"date_min":min(dates),"date_max":max(dates),
                    "generation_date":generation,"record01_stream_sha256":record01_hash.hexdigest()}

def compare_common_date_multiset(a,b,common_max):
    def records(path):
        with zipfile.ZipFile(path) as z:
            n=next(x for x in z.namelist() if x.upper().endswith("COTAHIST_A2026.TXT"))
            with z.open(n) as f:
                for raw in f:
                    line=raw.rstrip(b"\r\n")
                    if line[:2]==b"01" and line[2:10].decode("ascii",errors="replace") <= common_max:
                        yield raw
    # COTAHIST is sorted, but cross-repo snapshots may have different ordering.
    # Compare the complete 245-byte record multiset for the common trading-date range.
    ha=hashlib.sha256(); hb=hashlib.sha256()
    ca=cb=0
    only_a=[]; only_b=[]
    with tempfile.TemporaryDirectory() as td:
        pa=os.path.join(td,"a.records"); pb=os.path.join(td,"b.records")
        with open(pa,"wb") as fa:
            for r in records(a):
                fa.write(hashlib.sha256(r).digest()); ca+=1
        with open(pb,"wb") as fb:
            for r in records(b):
                fb.write(hashlib.sha256(r).digest()); cb+=1
        # Sort fixed 32-byte digests externally without loading raw records into memory.
        sa=sorted(open(pa,"rb").read()[i:i+32] for i in range(0,os.path.getsize(pa),32))
        sb=sorted(open(pb,"rb").read()[i:i+32] for i in range(0,os.path.getsize(pb),32))
        ia=ib=0
        while ia<len(sa) and ib<len(sb):
            if sa[ia]==sb[ib]: ia+=1; ib+=1
            elif sa[ia]<sb[ib]:
                if len(only_a)<10: only_a.append(sa[ia].hex())
                ia+=1
            else:
                if len(only_b)<10: only_b.append(sb[ib].hex())
                ib+=1
        while ia<len(sa):
            if len(only_a)<10: only_a.append(sa[ia].hex())
            ia+=1
        while ib<len(sb):
            if len(only_b)<10: only_b.append(sb[ib].hex())
            ib+=1
        for d in sa: ha.update(d)
        for d in sb: hb.update(d)
    return {
        "comparison_method":"order_independent_full_record_multiset",
        "record_identity":"complete 245-byte record type 01",
        "common_date_max":common_max,
        "bloom_common_record01_count":ca,
        "b3_common_record01_count":cb,
        "bloom_common_multiset_sha256":ha.hexdigest(),
        "b3_common_multiset_sha256":hb.hexdigest(),
        "bloom_only_record_hash_samples":only_a,
        "b3_only_record_hash_samples":only_b,
        "exact_common_multiset":ca==cb and not only_a and not only_b
    }

def main():
    with open(MANIFEST,encoding="utf-8") as f: manifest=json.load(f)
    bloom_meta=next(d for d in manifest["datasets"] if d["id"]=="B3_COTACOES")
    with tempfile.TemporaryDirectory() as td:
        b3=os.path.join(td,"COTAHIST_A2026.ZIP")
        req=urllib.request.Request(B3URL,headers={"User-Agent":"BLOOMBERG_MAIL-REC001/1.3"})
        with urllib.request.urlopen(req,timeout=300) as r, open(b3,"wb") as f:
            for x in iter(lambda:r.read(1024*1024),b""): f.write(x)
        bs=inspect(BLOOM); ss=inspect(b3)
        common_max=min(bs["date_max"],ss["date_max"])
        cmp=compare_common_date_multiset(BLOOM,b3,common_max)
        if cmp["exact_common_multiset"] and ss["date_max"] < bs["date_max"]:
            result="PASS_OVERLAP_EXACT"
        elif cmp["exact_common_multiset"] and ss["date_max"] == bs["date_max"]:
            result="PASS_EXACT"
        else:
            result="FAIL_CONTENT_DIVERGENCE"
        evidence={
          "schema_version":"1.3-rec001-b3-cross-repo",
          "result":result,"raw_preserved":True,
          "comparison_scope":"COTAHIST record type 01; order-independent full-record multiset over common trading-date range; headers/trailers excluded",
          "bloomberg_mail":{"path":BLOOM,"zip_sha256":sha(BLOOM),"retrieval_timestamp_utc":bloom_meta.get("retrieval_timestamp_utc"),
                            "source_url":bloom_meta.get("source_url"),"stats":bs},
          "b3":{"url":B3URL,"zip_sha256":sha(b3),"stats":ss},
          "temporal_evidence":{"bloomberg_mail_generation_date":bs["generation_date"],"b3_generation_date":ss["generation_date"],
                               "common_date_min":bs["date_min"],"common_date_max":common_max},
          "comparison":cmp,
          "promotion_impact":"REC001_B3_PASS_OVERLAP" if result=="PASS_OVERLAP_EXACT" else ("REC001_B3_PASS" if result=="PASS_EXACT" else "BLOCKED_CONTENT_DIVERGENCE")
        }
        try:
            evidence["temporal_evidence"]["generation_date_difference_days"]=(datetime.strptime(bs["generation_date"],"%Y%m%d")-datetime.strptime(ss["generation_date"],"%Y%m%d")).days
        except Exception: evidence["temporal_evidence"]["generation_date_difference_days"]=None
        os.makedirs(os.path.dirname(OUT),exist_ok=True)
        with open(OUT,"w",encoding="utf-8") as f: json.dump(evidence,f,ensure_ascii=False,indent=2); f.write("\n")

if __name__=="__main__": main()
