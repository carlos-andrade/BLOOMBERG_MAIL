#!/usr/bin/env python3
# controlled execution trigger 2026-10-08
import hashlib, json, os, tempfile, urllib.request, zipfile

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
                if len(line)!=245:
                    raise RuntimeError(f"invalid record length {len(line)}")
                typ=line[:2]
                if typ==b"00":
                    generation=line[24:32].decode("ascii",errors="replace")
                elif typ==b"01":
                    count += 1
                    dates.append(line[2:10].decode("ascii",errors="replace"))
                    record01_hash.update(raw)
            return {
                "member":n,
                "record01_count":count,
                "date_min":min(dates),
                "date_max":max(dates),
                "generation_date":generation,
                "record01_stream_sha256":record01_hash.hexdigest()
            }

def compare_common_records(a,b):
    def stream(path):
        z=zipfile.ZipFile(path)
        n=next(x for x in z.namelist() if x.upper().endswith("COTAHIST_A2026.TXT"))
        return z, z.open(n)
    za,fa=stream(a); zb,fb=stream(b)
    try:
        # Compare only COTAHIST record type 01. Headers/trailers can legitimately
        # differ because they carry file-level generation/count metadata.
        def next01(f):
            for raw in f:
                line=raw.rstrip(b"\r\n")
                if line[:2]==b"01":
                    return raw
            return b""
        i=0
        while True:
            ra=next01(fa); rb=next01(fb)
            if not ra or not rb:
                return {
                    "common_record01_count":i,
                    "bloom_record01_exhausted":not ra,
                    "b3_record01_exhausted":not rb,
                    "first_difference":None
                }
            i += 1
            if ra != rb:
                return {
                    "common_record01_count":i-1,
                    "bloom_record01_exhausted":False,
                    "b3_record01_exhausted":False,
                    "first_difference":{
                        "position_record01":i,
                        "bloom_sha256":hashlib.sha256(ra).hexdigest(),
                        "b3_sha256":hashlib.sha256(rb).hexdigest(),
                        "bloom_prefix":ra[:40].decode("latin1"),
                        "b3_prefix":rb[:40].decode("latin1")
                    }
                }
    finally:
        fa.close(); fb.close(); za.close(); zb.close()

def main():
    with open(MANIFEST,encoding="utf-8") as f:
        manifest=json.load(f)
    bloom_meta=next(d for d in manifest["datasets"] if d["id"]=="B3_COTACOES")
    with tempfile.TemporaryDirectory() as td:
        b3=os.path.join(td,"COTAHIST_A2026.ZIP")
        req=urllib.request.Request(B3URL,headers={"User-Agent":"BLOOMBERG_MAIL-REC001/1.1"})
        with urllib.request.urlopen(req,timeout=300) as r, open(b3,"wb") as f:
            for x in iter(lambda:r.read(1024*1024),b""): f.write(x)
        bs=inspect(BLOOM); ss=inspect(b3)
        cmp=compare_common_records(BLOOM,b3)
        if cmp["first_difference"] is not None:
            result="FAIL_CONTENT_DIVERGENCE"
        elif cmp["b3_record01_exhausted"] and not cmp["bloom_record01_exhausted"]:
            result="PASS_OVERLAP_EXACT"
        elif cmp["b3_record01_exhausted"] and cmp["bloom_record01_exhausted"]:
            result="PASS_EXACT"
        else:
            result="FAIL_CONTENT_DIVERGENCE"
        evidence={
            "schema_version":"1.1-rec001-b3-cross-repo",
            "result":result,
            "raw_preserved":True,
            "comparison_scope":"COTAHIST record type 01 only; file headers/trailers excluded from equality test",
            "bloomberg_mail":{
                "path":BLOOM,
                "zip_sha256":sha(BLOOM),
                "retrieval_timestamp_utc":bloom_meta.get("retrieval_timestamp_utc"),
                "source_url":bloom_meta.get("source_url"),
                "stats":bs
            },
            "b3":{
                "url":B3URL,
                "zip_sha256":sha(b3),
                "stats":ss
            },
            "temporal_evidence":{
                "bloomberg_mail_generation_date":bs["generation_date"],
                "b3_generation_date":ss["generation_date"],
                "generation_date_difference_days":None
            },
            "comparison":cmp,
            "promotion_impact":"REC001_B3_PASS_OVERLAP" if result=="PASS_OVERLAP_EXACT" else ("REC001_B3_PASS" if result=="PASS_EXACT" else "BLOCKED_CONTENT_DIVERGENCE")
        }
        from datetime import datetime
        try:
            a=datetime.strptime(bs["generation_date"],"%Y%m%d")
            b=datetime.strptime(ss["generation_date"],"%Y%m%d")
            evidence["temporal_evidence"]["generation_date_difference_days"]=(a-b).days
        except Exception:
            pass
        os.makedirs(os.path.dirname(OUT),exist_ok=True)
        with open(OUT,"w",encoding="utf-8") as f:
            json.dump(evidence,f,ensure_ascii=False,indent=2); f.write("\n")

if __name__=="__main__":
    main()
