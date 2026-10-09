---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO_TECNICO"
fase: "FASE-01-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-ARQUITETURA-MD"
titulo: "WATCHDOG — Arquitetura Técnica"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "WATCHDOG/ARQUITETURA.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# WATCHDOG — Arquitetura Técnica

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO_TECNICO
> **Fase:** FASE-01-WATCHDOG
> **ID:** BLOOMBERG-MAIL-WATCHDOG-ARQUITETURA-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-08
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


## Contexto Histórico

Documento do WATCHDOG integrado à governança documental central de carlos-andrade.

## Estado

IMPLEMENTADO.

## Evidências

Modelo canônico de cabeçalho do projeto Curioso-da-Internet-IA.

## Validação

Front Matter YAML e seções de rastreabilidade aplicados.

## Resultado

Documento normalizado.

## Próxima Ação

Atualizar versão, data e rastreabilidade em alterações relevantes.

---

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
