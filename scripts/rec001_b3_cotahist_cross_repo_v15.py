#!/usr/bin/env python3
"""REC-001 diagnostic: order-independent multiset comparison of complete COTAHIST records per date."""
import hashlib
import json
import os
import tempfile
import urllib.request
import zipfile
from collections import defaultdict

BLOOM = "EMAILS_RECEBIDOS/INGESTAO/005/RAW/COTAHIST_A2026.ZIP"
MANIFEST = "EMAILS_RECEBIDOS/INGESTAO/005/manifesto_aquisicao.json"
B3_URL = "https://raw.githubusercontent.com/carlos-andrade/B3/main/dados/cotahist/raw/anual/COTAHIST_A2026.ZIP"
OUT = "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_DIAGNOSTICO_MULTICONJUNTO_2026-10-09.json"

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def inspect_zip(path):
    with zipfile.ZipFile(path) as z:
        bad = z.testzip()
        if bad:
            raise RuntimeError(f"ZIP corrompido no membro {bad}")
        member = next((n for n in z.namelist() if n.upper().endswith("COTAHIST_A2026.TXT")), None)
        if not member:
            raise RuntimeError("COTAHIST_A2026.TXT ausente")
        dates, count, generation = [], 0, None
        with z.open(member) as f:
            for raw in f:
                line = raw.rstrip(b"\r\n")
                if len(line) != 245:
                    raise RuntimeError(f"registo com comprimento inválido: {len(line)}")
                if line[:2] == b"00":
                    generation = line[23:31].decode("ascii", "replace").strip()
                elif line[:2] == b"01":
                    count += 1
                    dates.append(line[2:10].decode("ascii", "replace"))
        if not dates:
            raise RuntimeError("nenhum registo tipo 01 encontrado")
        return {
            "member": member, "record01_count": count,
            "date_min": min(dates), "date_max": max(dates),
            "generation_date": generation,
        }

def per_date_multiset(path, lo, hi):
    by_date = defaultdict(list)
    with zipfile.ZipFile(path) as z:
        member = next(n for n in z.namelist() if n.upper().endswith("COTAHIST_A2026.TXT"))
        with z.open(member) as f:
            for raw in f:
                line = raw.rstrip(b"\r\n")
                if line[:2] != b"01":
                    continue
                date = line[2:10].decode("ascii", "replace")
                if lo <= date <= hi:
                    by_date[date].append(hashlib.sha256(line).digest())
    result = {}
    for date, digests in by_date.items():
        digests.sort()
        aggregate = hashlib.sha256()
        for digest in digests:
            aggregate.update(digest)
        result[date] = {"count": len(digests), "multiset_sha256": aggregate.hexdigest()}
    return result

def compare_date_maps(bloom_days, b3_days):
    # Union catches dates present in only one source; a shared-key-only comparison would miss them.
    all_dates = sorted(set(bloom_days) | set(b3_days))
    divergent = []
    for date in all_dates:
        a, b = bloom_days.get(date), b3_days.get(date)
        if a != b:
            divergent.append({
                "date": date,
                "bloomberg_mail": a,
                "b3": b,
                "reason": "DATE_MISSING_ON_ONE_SIDE" if a is None or b is None else "MULTISET_MISMATCH",
            })
    return all_dates, divergent

def main():
    with open(MANIFEST, encoding="utf-8") as f:
        manifest = json.load(f)
    dataset = next(d for d in manifest["datasets"] if d["id"] == "B3_COTACOES")
    bloom_sha = sha256_file(BLOOM)
    expected_bloom_sha = dataset.get("checksum_sha256")
    if expected_bloom_sha and bloom_sha != expected_bloom_sha:
        raise RuntimeError("SHA-256 do RAW BLOOMBERG_MAIL não coincide com o manifesto; comparação bloqueada")

    with tempfile.TemporaryDirectory() as td:
        b3_path = os.path.join(td, "COTAHIST_A2026.ZIP")
        req = urllib.request.Request(B3_URL, headers={"User-Agent": "BLOOMBERG_MAIL-REC001/1.5"})
        with urllib.request.urlopen(req, timeout=300) as response, open(b3_path, "wb") as out:
            for block in iter(lambda: response.read(1024 * 1024), b""):
                out.write(block)
        b3_sha = sha256_file(b3_path)
        expected_b3_sha = dataset.get("reference_sha256")
        b3_snapshot_matches_manifest = not expected_b3_sha or b3_sha == expected_b3_sha
        bloom_stats = inspect_zip(BLOOM)
        b3_stats = inspect_zip(b3_path)
        lo = max(bloom_stats["date_min"], b3_stats["date_min"])
        hi = min(bloom_stats["date_max"], b3_stats["date_max"])
        bloom_days = per_date_multiset(BLOOM, lo, hi)
        b3_days = per_date_multiset(b3_path, lo, hi)
        tested_dates, divergent_dates = compare_date_maps(bloom_days, b3_days)
        exact_overlap = not divergent_dates
        if not b3_snapshot_matches_manifest:
            result = "BLOCKED_B3_SNAPSHOT_CHANGED"
        elif exact_overlap and b3_stats["date_max"] < bloom_stats["date_max"]:
            result = "PASS_OVERLAP_EXACT"
        elif exact_overlap and b3_stats["date_max"] == bloom_stats["date_max"]:
            result = "PASS_EXACT"
        else:
            result = "FAIL_CONTENT_DIVERGENCE"

        evidence = {
            "schema_version": "1.0-rec001-b3-multiset-diagnostic",
            "created_at_utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
            "result": result,
            "raw_preserved": True,
            "comparison_scope": "COTAHIST tipo 01; registo completo de 245 bytes; multiconjunto de SHA-256 por pregão; ordem física ignorada; cabeçalho/trailer excluídos",
            "bloomberg_mail": {"path": BLOOM, "zip_sha256": bloom_sha, "expected_sha256": expected_bloom_sha, "stats": bloom_stats},
            "b3": {"url": B3_URL, "zip_sha256": b3_sha, "expected_sha256": expected_b3_sha, "snapshot_hash_matches_manifest_reference": b3_snapshot_matches_manifest, "stats": b3_stats},
            "temporal_evidence": {"common_date_min": lo, "common_date_max": hi, "bloomberg_mail_generation_date": bloom_stats["generation_date"], "b3_generation_date": b3_stats["generation_date"]},
            "comparison": {"dates_tested": len(tested_dates), "convergent_dates": len(tested_dates) - len(divergent_dates), "divergent_dates_count": len(divergent_dates), "divergent_dates": divergent_dates[:100], "exact_common_period": exact_overlap, "bloomberg_dates_present": len(bloom_days), "b3_dates_present": len(b3_days)},
            "diagnostic_conclusion": "A comparação por data usa a união das datas presentes nas duas fontes e preserva a multiplicidade de registos. Resultado diagnóstico; o REC-001 original é preservado.",
            "promotion_impact": "REVIEW_REC001_FOR_SUPERSESSION" if result.startswith("PASS_") else "BLOCKED_CONTENT_DIVERGENCE"
        }
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "w", encoding="utf-8") as f:
            json.dump(evidence, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(json.dumps({"result": result, "dates_tested": len(tested_dates), "convergent_dates": len(tested_dates)-len(divergent_dates), "divergent_dates_count": len(divergent_dates), "b3_snapshot_matches_manifest_reference": b3_snapshot_matches_manifest, "output": OUT}, ensure_ascii=False))

if __name__ == "__main__":
    main()
