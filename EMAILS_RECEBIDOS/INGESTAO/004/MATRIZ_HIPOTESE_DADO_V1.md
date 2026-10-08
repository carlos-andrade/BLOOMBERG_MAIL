---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-004-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-004-MATRIZ-HIPOTESE-DADO-V1-MD"
titulo: "BLOOMBERG_MAIL — INGESTÃO 004 — MATRIZ HIPÓTESE × DADO"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/004/MATRIZ_HIPOTESE_DADO_V1.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — INGESTÃO 004 — MATRIZ HIPÓTESE × DADO

## Contexto Histórico

Documento histórico do projeto BLOOMBERG_MAIL integrado à governança documental central de carlos-andrade.

## Estado

IMPLEMENTADO — cabeçalho migrado para o padrão canônico.

## Evidências

Modelo canônico: Curioso-da-Internet-IA/CABEÇALHO/MODELO-PADRAO-CABECALHO.md.

## Validação

Cabeçalho, identificação documental e rastreabilidade foram normalizados.

## Resultado

O conteúdo original abaixo foi preservado.

## Próxima Ação

Atualizar versão, data e rastreabilidade em alterações relevantes.

---

# BLOOMBERG_MAIL — INGESTÃO 004 — MATRIZ HIPÓTESE × DADO

> Cabeçalho histórico — 2026-10-07.

| Hipótese | Pergunta | Dados | Método inicial |
|---|---|---|---|
| H1 | Concentração dos líderes coincide com menor breadth? | pesos, retornos, altas/baixas, HHI | correlação + regressão + estabilidade temporal |
| H2 | Oferta de ações precede compressão de retorno/valuation? | ofertas CVM, tamanho, datas, retornos | estudo de eventos |
| H3 | Lock-up produz choque de oferta? | evento, quantidade potencial, free float, volume, retorno, volatilidade | estudo de eventos |
| H4 | Fiscal + política + duração alteram regime de juros/FX/equities? | DI, títulos, duration/DV01, BRL/USD, IBOV, VIX, eventos | análise de regimes + eventos |

## Variáveis derivadas prioritárias

### Breadth
`advance_count`, `decline_count`, `unchanged_count`, `advance_decline_ratio`, `pct_above_ma20`, `pct_above_ma50`, `pct_above_ma200`.

### Concentração
`top5_weight`, `top10_weight`, `hhi_weight`, `effective_number_of_constituents`.

### Liquidez
`trading_value_brl`, `trade_count`, `quantity`, `avg_trade_value_brl`, `volume_zscore`.

### Regime
`ibov_return_1d`, `ibov_return_5d`, `vix_level`, `vix_change_1d`, `brlusd_return_1d`, `di_curve_slope`, `duration_proxy`.

## Regra de promoção

Nenhuma variável vira compra/venda/long/short diretamente. A cadeia obrigatória é:

`raw_source -> transformation -> derived_field -> test -> result`

Depois: in-sample/out-of-sample, controle de múltiplos testes, estabilidade por regime e falsificadores.
