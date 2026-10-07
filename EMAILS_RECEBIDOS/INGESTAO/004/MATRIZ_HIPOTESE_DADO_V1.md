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
