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
from datetime import datetime, timezone, date, timedelta

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
                      if name.upper().endswith(".TXT") and "COTAHIST" in name.upper()), None)
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

    bloom = read_records(BLOOM)
    first_month = (int(BASELINE_END[:4]), int(BASELINE_END[4:6]))
    last_date = date(int(bloom["date_max"][:4]), int(bloom["date_max"][4:6]), int(bloom["date_max"][6:]))
    last_month = (last_date.year, last_date.month)
    months = []
    year, month = first_month
    while (year, month) <= last_month:
        months.append((year, month))
        month += 1
        if month == 13:
            year, month = year + 1, 1

    official_days = defaultdict(Counter)
    official_snapshots = []
    unavailable_official_dates = []
    with tempfile.TemporaryDirectory() as tmp:
        for year, month in months:
            if (year, month) < last_month:
                filenames = [("COTAHIST_M{:02d}{}.ZIP".format(month, year), None)]
            else:
                month_start = date(year, month, 1)
                baseline_date = date(int(BASELINE_END[:4]), int(BASELINE_END[4:6]), int(BASELINE_END[6:]))
                day = max(month_start, baseline_date + timedelta(days=1))
                filenames = []
                while day <= last_date:
                    if day.weekday() < 5:
                        filenames.append(("COTAHIST_D{}.ZIP".format(day.strftime("%d%m%Y")), day.isoformat()))
                    day += timedelta(days=1)

            for filename, expected_date in filenames:
                url = "https://bvmf.bmfbovespa.com.br/InstDados/SerHist/{}".format(filename)
                official_path = os.path.join(tmp, filename)
                request = urllib.request.Request(url, headers={
                    "User-Agent": "Mozilla/5.0 (compatible; BLOOMBERG_MAIL-REC001/1.6)",
                    "Accept": "*/*",
                })
                try:
                    with urllib.request.urlopen(request, timeout=45) as response, open(official_path, "wb") as target:
                        for chunk in iter(lambda: response.read(1024 * 1024), b""):
                            target.write(chunk)
                except urllib.error.HTTPError as exc:
                    if exc.code == 404 and expected_date:
                        unavailable_official_dates.append({"date": expected_date, "url": url, "http_status": 404})
                        continue
                    raise
                stats = read_records(official_path)
                if expected_date and any(date_key != expected_date.replace("-", "") for date_key in stats["by_date"]):
                    raise RuntimeError("arquivo diário {} contém data diferente da esperada {}".format(filename, expected_date))
                for date_key, records in stats["by_date"].items():
                    official_days[date_key].update(records)
                official_snapshots.append({
                    "filename": filename, "url": url, "type": "monthly" if expected_date is None else "daily",
                    "zip_sha256": sha256_file(official_path), "record01_count": stats["record01_count"],
                    "date_min": stats["date_min"], "date_max": stats["date_max"],
                    "generation_date": stats["generation_date"],
                })

    dates, divergences = compare_incremental(bloom["by_date"], official_days)
    tested = len(dates)
    matched = tested - len(divergences)
    has_new_data = any(date > BASELINE_END for date in dates)
    if unavailable_official_dates:
        result = "BLOCKED_OFFICIAL_DAILY_UNAVAILABLE"
    elif not has_new_data:
        result = "BLOCKED_NO_INCREMENTAL_DATES"
    elif divergences:
        result = "FAIL_INCREMENTAL_DIVERGENCE"
    elif max((item["date_max"] for item in official_snapshots), default="") < bloom["date_max"]:
        result = "PASS_INCREMENTAL_OVERLAP_ONLY"
    else:
        result = "PASS_INCREMENTAL_EXACT"

    aggregate_hash = hashlib.sha256(
        "".join(item["zip_sha256"] for item in official_snapshots).encode("ascii")
    ).hexdigest()
    evidence = {
        "schema_version": "1.0-rec001-b3-incremental",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "result": result,
        "baseline_last_reconciled_date": BASELINE_END,
        "comparison_scope": "registos COTAHIST tipo 01 completos de 245 bytes; multiconjunto de hashes por data; multiplicidade preservada; apenas datas posteriores à linha de base até à última data do RAW local",
        "raw_policy": "immutable; nenhum RAW ou manifesto histórico foi substituído",
        "bloomberg_mail": {"path": BLOOM, "zip_sha256": bloom_hash, "manifest_sha256": expected_bloom,
                           "record01_count": bloom["record01_count"], "date_min": bloom["date_min"],
                           "date_max": bloom["date_max"], "generation_date": bloom["generation_date"]},
        "official_b3": {"source": "B3 COTAHIST monthly official endpoint", "snapshot_sha256_aggregate": aggregate_hash,
                        "official_snapshots": official_snapshots,
                        "unavailable_official_dates": unavailable_official_dates,
                        "record01_count": sum(item["record01_count"] for item in official_snapshots),
                        "date_min": min((item["date_min"] for item in monthly_snapshots), default=None),
                        "date_max": max((item["date_max"] for item in monthly_snapshots), default=None)},
        "comparison": {"dates_tested_after_baseline": tested, "target_period_end": bloom["date_max"],
                       "convergent_dates": matched, "divergent_dates_count": len(divergences),
                       "divergent_dates": divergences[:200], "incremental_dates_present": has_new_data,
                       "official_dates_after_local_period": sum(1 for date in official_days if date > bloom["date_max"])},
        "interpretation": "Foi usado snapshot mensal para o mês fechado e ficheiros diários oficiais para o mês em curso. Dias úteis sem ficheiro oficial disponível bloqueiam a aprovação; o hash histórico do manifesto não é substituído.",
        "promotion_impact": "REVIEW_FOR_PROMOTION" if result.startswith("PASS_") else "BLOCKED"
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as stream:
        json.dump(evidence, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(json.dumps({"result": result, "dates_tested_after_baseline": tested,
                      "convergent_dates": matched, "divergent_dates_count": len(divergences),
                      "official_snapshots": len(official_snapshots), "output": OUT}, ensure_ascii=False))

if __name__ == "__main__":
    main()
