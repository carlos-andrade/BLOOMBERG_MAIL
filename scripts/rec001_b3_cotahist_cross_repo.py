#!/usr/bin/env python3
import hashlib, json, os, sqlite3, tempfile, urllib.request, zipfile
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
                typ=line[:2]
                if typ==b"00":
                    generation=line[24:32].decode("ascii",errors="replace").strip()
                elif typ==b"01":
                    count += 1; dates.append(line[2:10].decode("ascii",errors="replace"))
                    record01_hash.update(raw)
            return {"member":n,"record01_count":count,"date_min":min(dates),"date_max":max(dates),
                    "generation_date":generation,"record01_stream_sha256":record01_hash.hexdigest()}

def key(line):
    return (line[2:10], line[10:12], line[12:24], line[24:27])

def build_index(path, db_path, table):
    conn=sqlite3.connect(db_path)
    conn.execute(f"CREATE TABLE {table} (k BLOB NOT NULL, rh BLOB NOT NULL, c INTEGER NOT NULL, PRIMARY KEY(k,rh))")
    conn.execute(f"CREATE INDEX idx_{table}_k ON {table}(k)")
    with zipfile.ZipFile(path) as z:
        n=next(x for x in z.namelist() if x.upper().endswith("COTAHIST_A2026.TXT"))
        with z.open(n) as f:
            pending={}
            for raw in f:
                line=raw.rstrip(b"\r\n")
                if line[:2]!=b"01": continue
                k=line[2:27]
                rh=hashlib.sha256(raw).digest()
                pair=(k,rh); pending[pair]=pending.get(pair,0)+1
                if len(pending)>=10000:
                    conn.executemany(f"INSERT INTO {table}(k,rh,c) VALUES(?,?,?) ON CONFLICT(k,rh) DO UPDATE SET c=c+excluded.c",
                                     [(k,rh,c) for (k,rh),c in pending.items()])
                    conn.commit(); pending.clear()
            if pending:
                conn.executemany(f"INSERT INTO {table}(k,rh,c) VALUES(?,?,?) ON CONFLICT(k,rh) DO UPDATE SET c=c+excluded.c",
                                 [(k,rh,c) for (k,rh),c in pending.items()])
                conn.commit()
    return conn

def compare_by_key(a,b):
    with tempfile.TemporaryDirectory() as td:
        db=os.path.join(td,"rec001.sqlite")
        ca=build_index(a,db,"a")
        ca.close()
        cb=sqlite3.connect(db)
        build_index(b,db,"b").close()
        # Multiset comparison by logical instrument/date key + complete record hash.
        common_keys=cb.execute("SELECT COUNT(*) FROM (SELECT k FROM a INTERSECT SELECT k FROM b)").fetchone()[0]
        a_keys=cb.execute("SELECT COUNT(DISTINCT k) FROM a").fetchone()[0]
        b_keys=cb.execute("SELECT COUNT(DISTINCT k) FROM b").fetchone()[0]
        mismatches=[]
        for k,rha,ca_count,rhb,cb_count in cb.execute("""
            SELECT a.k,a.rh,a.c,b.rh,b.c
            FROM a JOIN b USING(k)
            WHERE a.rh<>b.rh OR a.c<>b.c
            LIMIT 10
        """):
            mismatches.append({
                "logical_key":k.decode("ascii","replace"),
                "bloom_hash":rha.hex(),"bloom_count":ca_count,
                "b3_hash":rhb.hex(),"b3_count":cb_count
            })
        # Exact multiset equality over the common logical-key universe.
        divergence=cb.execute("""
            SELECT COUNT(*) FROM (
              SELECT k,rh,c FROM a
              EXCEPT
              SELECT k,rh,c FROM b
            )
        """).fetchone()[0]
        reverse=cb.execute("""
            SELECT COUNT(*) FROM (
              SELECT k,rh,c FROM b
              EXCEPT
              SELECT k,rh,c FROM a
            )
        """).fetchone()[0]
        return {
            "comparison_method":"logical_key_multiset",
            "logical_key":"DATA DO PREGAO + CODBDI + CODNEG + TPMERC",
            "bloom_distinct_logical_keys":a_keys,
            "b3_distinct_logical_keys":b_keys,
            "common_logical_keys":common_keys,
            "bloom_only_key_hash_rows":divergence,
            "b3_only_key_hash_rows":reverse,
            "content_mismatch_samples":mismatches
        }

def main():
    with open(MANIFEST,encoding="utf-8") as f: manifest=json.load(f)
    bloom_meta=next(d for d in manifest["datasets"] if d["id"]=="B3_COTACOES")
    with tempfile.TemporaryDirectory() as td:
        b3=os.path.join(td,"COTAHIST_A2026.ZIP")
        req=urllib.request.Request(B3URL,headers={"User-Agent":"BLOOMBERG_MAIL-REC001/1.2"})
        with urllib.request.urlopen(req,timeout=300) as r, open(b3,"wb") as f:
            for x in iter(lambda:r.read(1024*1024),b""): f.write(x)
        bs=inspect(BLOOM); ss=inspect(b3); cmp=compare_by_key(BLOOM,b3)
        exact=cmp["bloom_only_key_hash_rows"]==0 and cmp["b3_only_key_hash_rows"]==0
        if exact and ss["date_max"] < bs["date_max"]:
            result="PASS_OVERLAP_EXACT"
        elif exact and ss["date_max"] == bs["date_max"]:
            result="PASS_EXACT"
        else:
            result="FAIL_CONTENT_DIVERGENCE"
        evidence={
          "schema_version":"1.2-rec001-b3-cross-repo",
          "result":result,"raw_preserved":True,
          "comparison_scope":"COTAHIST record type 01; logical-key multiset comparison; headers/trailers excluded",
          "bloomberg_mail":{"path":BLOOM,"zip_sha256":sha(BLOOM),"retrieval_timestamp_utc":bloom_meta.get("retrieval_timestamp_utc"),
                            "source_url":bloom_meta.get("source_url"),"stats":bs},
          "b3":{"url":B3URL,"zip_sha256":sha(b3),"stats":ss},
          "temporal_evidence":{"bloomberg_mail_generation_date":bs["generation_date"],"b3_generation_date":ss["generation_date"]},
          "comparison":cmp,
          "promotion_impact":"REC001_B3_PASS_OVERLAP" if result=="PASS_OVERLAP_EXACT" else ("REC001_B3_PASS" if result=="PASS_EXACT" else "BLOCKED_CONTENT_DIVERGENCE")
        }
        try:
            evidence["temporal_evidence"]["generation_date_difference_days"]=(datetime.strptime(bs["generation_date"],"%Y%m%d")-datetime.strptime(ss["generation_date"],"%Y%m%d")).days
        except Exception: evidence["temporal_evidence"]["generation_date_difference_days"]=None
        os.makedirs(os.path.dirname(OUT),exist_ok=True)
        with open(OUT,"w",encoding="utf-8") as f: json.dump(evidence,f,ensure_ascii=False,indent=2); f.write("\n")

if __name__=="__main__": main()
