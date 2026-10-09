---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "LAYOUT"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-LAYOUT-B3-COTAHIST-FASE02"
titulo: "Layout único do adapter de qualidade histórica B3 COTAHIST"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "WATCHDOG/CARTA_B3_COTAHIST_FASE02.md"
autoridade_documental: "CARTA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "BLOOMBERG-MAIL-WATCHDOG-CARTA-B3-COTAHIST-FASE02"
escopo: "WATCHDOG/adapters/b3_cotahist_status.py; WATCHDOG/tests/"
objetivo: "Especificar a conversão de evidências B3 persistidas num evento Watchdog de qualidade histórica."
dependencias: "WATCHDOG/CARTA_B3_COTAHIST_FASE02.md; contrato de eventos"
---

# Layout único — Adapter B3 COTAHIST

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** LAYOUT
> **Fase:** FASE-02-WATCHDOG
> **ID:** BLOOMBERG-MAIL-WATCHDOG-LAYOUT-B3-COTAHIST-FASE02
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** WATCHDOG/CARTA_B3_COTAHIST_FASE02.md
> **Autoridade:** CARTA
> **Rastreabilidade:** BLOOMBERG-MAIL-WATCHDOG-CARTA-B3-COTAHIST-FASE02

## Contexto Histórico

Este layout materializa a carta que permite observar a qualidade de COTAHIST já adquirido. Não recolhe dados da Internet nem altera o RAW.

## Estado

IMPLEMENTADO — layout aprovado para implementação local e automatizada.

## Evidências

Artefactos de ingestão 005 e REC-001 enumerados na carta.

## Validação

CLI: `python WATCHDOG/adapters/b3_cotahist_status.py --root . --output <ficheiro.jsonl>`.

- `--validate-only` valida evidências e imprime o evento, sem escrever.
- Sem `--validate-only`, escreve um evento JSONL append-only.
- ID determinístico baseado no dataset, SHA RAW e resultado REC-001; repetições não duplicam o evento existente.
- Estado `UP` apenas se layout, normalização e reconciliação estiverem aprovados; divergência de reconciliação resulta em `DEGRADED/HIGH`.
- Timestamp do evento representa a avaliação atual, enquanto timestamps de aquisição permanecem no payload.
- Não declara que há dados em tempo real.

## Resultado

Contrato do adapter definido e rastreável à carta.

## Próxima Ação

Implementar, testar e executar no workflow do WATCHDOG.
