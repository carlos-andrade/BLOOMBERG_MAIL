# WATCHDOG — Arquitetura Técnica

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Módulo: WATCHDOG
- Versão: 1.0
- Data: 2026-10-08

## Camadas
1. Supervisão: liveness, readiness, restart e clock.
2. Collectors: B3, FX, cripto, macro, notícias e Bloomberg Mail.
3. Normalização: contrato único preservando fonte e qualidade.
4. Detectores: stale data, gaps, spikes, divergências, regime e eventos.
5. Event store: JSONL incremental e posteriormente banco temporal.
6. Alert engine: severidade, deduplicação, cooldown e escalonamento.
7. Auditoria: timestamp, fonte, versão, payload e hash.

## Estados
UP, DEGRADED, DOWN, STALE, UNKNOWN.

## Severidade
INFO, LOW, MEDIUM, HIGH, CRITICAL.

## Contrato mínimo
Cada observação terá event_id, observed_at_utc, source, asset_class, symbol, session, event_type, severity, state, latency_ms, quality, payload e schema_version.

## Separação de responsabilidades
WATCHDOG observa. ESTRATÉGIA interpreta. EXECUTOR eventualmente executa. Nenhuma dessas camadas deve ser confundida.
