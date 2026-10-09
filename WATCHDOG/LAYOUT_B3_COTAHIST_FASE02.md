---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "LAYOUT"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-LAYOUT-B3-COTAHIST-FASE02"
titulo: "Layout único do adapter de qualidade histórica B3 COTAHIST"
status: "IMPLEMENTADO"
versao: "1.2"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "WATCHDOG/CARTA_B3_COTAHIST_FASE02.md"
autoridade_documental: "CARTA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "BLOOMBERG-MAIL-WATCHDOG-CARTA-B3-COTAHIST-FASE02; REC001_CAUSA_RAIZ_001"
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
> **Versão:** 1.1
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

Artefactos de ingestão 005, REC-001 histórico e diagnóstico multiconjunto versionado enumerados na carta.

## Validação

CLI: `python WATCHDOG/adapters/b3_cotahist_status.py --root . --output <ficheiro.jsonl>`.

- `--validate-only` valida evidências e imprime o evento, sem escrever.
- Sem `--validate-only`, escreve um evento JSONL append-only.
- ID determinístico baseado no dataset, SHA RAW e resultado REC-001; repetições não duplicam o evento existente.
- O diagnóstico multiconjunto atual é preferido ao resultado histórico, sem sobrescrever o original.
- `PASS_OVERLAP_EXACT` exige hashes verificados, igualdade exata do período comum, contagem positiva de datas testadas e zero datas divergentes.
- Se o diagnóstico passar essas condições, o evento pode ser `UP/INFO`, com qualidade `VALIDATED_HISTORICAL_OVERLAP`; o payload conserva o resultado histórico anterior.
- Falha, ausência ou inconsistência de evidência resulta em `DEGRADED/HIGH` ou erro de validação.
- Timestamp do evento representa a avaliação atual, enquanto timestamps de aquisição permanecem no payload.
- Não declara que há dados em tempo real.

## Resultado

Contrato do adapter definido e rastreável à carta.

## Reconciliação incremental oficial

- Script: `scripts/rec001_b3_cotahist_incremental_v16.py`.
- Testes: `scripts/tests/test_rec001_b3_incremental.py`.
- Workflow: `.github/workflows/bloomberg-mail-rec001-b3-cotahist-incremental.yml`.
- Linha de base fixa: último pregão reconciliado 2026-09-23.
- Fonte de comparação: endpoint oficial anual B3 definido no manifesto de aquisição.
- O relatório incremental tem caminho próprio e não substitui evidências REC-001 históricas.
- Comparar união de datas após a linha de base; comparar registos completos como multiconjunto; preservar multiplicidade.
- O hash atual do endpoint oficial é registado separadamente do hash histórico do manifesto.
- Uma divergência, data ausente, arquivo inválido ou ausência de datas incrementais bloqueia a aprovação.
- Uma convergência permite apenas revisão da evidência, não promove automaticamente Layer A nem declara dados intradiários.

## Próxima Ação

Executar e inspecionar o workflow incremental, confirmar a evidência versionada e atualizar o roadmap com o resultado real.
