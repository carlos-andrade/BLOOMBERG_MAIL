#!/usr/bin/env python3
"""REC-001 incremental reconciliation against the current official B3 annual COTAHIST endpoint.

This run is deliberately separate from the immutable 2026-10-09 overlap diagnostic.
It tests dates after the last reconciled B3 snapshot (2026-09-23) and records the
official endpoint's current SHA-256 rather than silently replacing the historical
manifest reference.
"""
import hashlib
import json
import os
import tempfile
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone

BLOOM = "EMAILS_RECEBIDOS/INGESTAO/005/RAW/COTAHIST_A2026.ZIP"
MANIFEST = "EMAILS_RECEBIDOS/INGESTAO/005/manifesto_aquisicao.json"
OFFICIAL_URL = "https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A2026.ZIP"
BASELINE_END = "20260923"
OUT = "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_INCREMENTAL_2026-10-09.json"

def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

def read_records(path):
    by_date = defaultdict(Counter)
    generation_date = None
    total = 0
    with zipfile.ZipFile(path) as archive:
        corrupt = archive.testzip()
        if corrupt:
            raise RuntimeError(f"ZIP corrompido: {corrupt}")
        member = next((name for name in archive.namelist()
                      if name.upper().endswith("COTAHIST_A2026.TXT")), None)
        if not member:
            raise RuntimeError("membro COTAHIST_A2026.TXT ausente")
        with archive.open(member) as stream:
            for raw in stream:
                line = raw.rstrip(b"\r\n")
                if len(line) != 245:
                    raise RuntimeError(f"registo com comprimento {len(line)}; esperado 245")
                if line[:2] == b"00":
                    generation_date = line[23:31].decode("ascii", "replace").strip()
                elif line[:2] == b"01":
                    date = line[2:10].decode("ascii", "replace")
                    if len(date) != 8 or not date.isdigit():
                        raise RuntimeError(f"data inválida em registo tipo 01: {date!r}")
                    by_date[date][hashlib.sha256(line).hexdigest()] += 1
                    total += 1
    if not by_date:
        raise RuntimeError("nenhum registo tipo 01 encontrado")
    return {"member": member, "record01_count": total,
            "date_min": min(by_date), "date_max": max(by_date),
            "generation_date": generation_date, "by_date": by_date}

def compare_incremental(left, right, baseline_end=BASELINE_END):
    # Reconcile the full incremental period represented by BLOOMBERG_MAIL.
    # A newer official endpoint may contain later dates; report that separately
    # rather than misclassifying ordinary source freshness as a missing local date.
    target_end = max(left) if left else baseline_end
    dates = sorted(d for d in (set(left) | set(right)) if baseline_end < d <= target_end)
    divergences = []
    for date in dates:
        a, b = left.get(date), right.get(date)
        if a != b:
            divergences.append({
                "date": date,
                "bloomberg_mail_records": sum(a.values()) if a else 0,
                "official_b3_records": sum(b.values()) if b else 0,
                "reason": "DATE_MISSING_ON_ONE_SIDE" if a is None or b is None else "MULTISET_MISMATCH",
            })
    return dates, divergences

def main():
    with open(MANIFEST, encoding="utf-8") as stream:
        manifest = json.load(stream)
    dataset = next(item for item in manifest["datasets"] if item["id"] == "B3_COTACOES")
    bloom_hash = sha256_file(BLOOM)
    expected_bloom = dataset.get("checksum_sha256")
    if expected_bloom and bloom_hash != expected_bloom:
        raise RuntimeError("SHA-256 do RAW BLOOMBERG_MAIL diverge do manifesto; comparação bloqueada")

    with tempfile.TemporaryDirectory() as tmp:
        official_path = os.path.join(tmp, "COTAHIST_A2026.ZIP")
        request = urllib.request.Request(OFFICIAL_URL, headers={"User-Agent": "BLOOMBERG_MAIL-REC001/1.6"})
        with urllib.request.urlopen(request, timeout=300) as response, open(official_path, "wb") as target:
            for block in iter(lambda: response.read(1024 * 1024), b""):
                target.write(block)
        official_hash = sha256_file(official_path)
        bloom = read_records(BLOOM)
        official = read_records(official_path)
        dates, divergences = compare_incremental(bloom["by_date"], official["by_date"])
        tested = len(dates)
        matched = tested - len(divergences)
        has_new_data = any(date > BASELINE_END for date in dates)
        if not has_new_data:
            result = "BLOCKED_NO_INCREMENTAL_DATES"
        elif divergences:
            result = "FAIL_INCREMENTAL_DIVERGENCE"
        elif official["date_max"] < bloom["date_max"]:
            result = "PASS_INCREMENTAL_OVERLAP_ONLY"
        else:
            result = "PASS_INCREMENTAL_EXACT"

        evidence = {
            "schema_version": "1.0-rec001-b3-incremental",
            "created_at_utc": datetime.now(timezone.utc).isoformat(),
            "result": result,
            "baseline_last_reconciled_date": BASELINE_END,
            "comparison_scope": "registos COTAHIST tipo 01 completos de 245 bytes; multiconjunto de hashes por data; multiplicidade preservada; apenas datas posteriores à linha de base",
            "raw_policy": "immutable; nenhum RAW ou manifesto histórico foi substituído",
            "bloomberg_mail": {"path": BLOOM, "zip_sha256": bloom_hash, "manifest_sha256": expected_bloom,
                               "record01_count": bloom["record01_count"], "date_min": bloom["date_min"],
                               "date_max": bloom["date_max"], "generation_date": bloom["generation_date"]},
            "official_b3": {"url": OFFICIAL_URL, "zip_sha256": official_hash,
                            "manifest_reference_sha256": dataset.get("reference_sha256"),
                            "current_hash_equals_historical_manifest_reference": official_hash == dataset.get("reference_sha256"),
                            "record01_count": official["record01_count"], "date_min": official["date_min"],
                            "date_max": official["date_max"], "generation_date": official["generation_date"]},
            "comparison": {"dates_tested_after_baseline": tested, "target_period_end": bloom["date_max"],
                           "convergent_dates": matched, "divergent_dates_count": len(divergences),
                           "divergent_dates": divergences[:200], "incremental_dates_present": has_new_data,
                           "official_dates_after_local_period": sum(1 for date in official["by_date"] if date > bloom["date_max"])},
            "interpretation": "O hash atual do endpoint oficial é registado como nova observação de proveniência; não é exigido que coincida com o hash histórico do manifesto. Divergências ou datas ausentes bloqueiam a aprovação.",
            "promotion_impact": "REVIEW_FOR_PROMOTION" if result.startswith("PASS_") else "BLOCKED"
        }
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "w", encoding="utf-8") as stream:
            json.dump(evidence, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        print(json.dumps({"result": result, "dates_tested_after_baseline": tested,
                          "convergent_dates": matched, "divergent_dates_count": len(divergences),
                          "official_hash": official_hash, "official_date_max": official["date_max"],
                          "output": OUT}, ensure_ascii=False))

if __name__ == "__main__":
    main()
