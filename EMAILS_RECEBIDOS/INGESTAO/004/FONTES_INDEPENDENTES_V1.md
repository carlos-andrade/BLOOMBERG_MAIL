# BLOOMBERG_MAIL — INGESTÃO 004 — FONTES INDEPENDENTES

> Cabeçalho histórico — 2026-10-07.

## Fontes institucionais

- B3 — Cotações históricas: https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/
- B3 — Histórico/boletins: https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/
- B3 — DataWise+: https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/datawise/
- BCB — Dados abertos/SGS: https://dadosabertos.bcb.gov.br/
- Tesouro Direto — Histórico: https://www.tesourodireto.com.br/produtos/dados-sobre-titulos/historico-de-precos-e-taxas
- CVM — Dados abertos: https://dados.cvm.gov.br/
- CVM — Ofertas públicas: https://www.gov.br/cvm/pt-br/assuntos/regulados/consultas-por-participante/ofertas-publicas
- Cboe — Histórico VIX: https://www.cboe.com/tradable_products/vix/vix_historical_data

## Evidência de disponibilidade

B3 declara histórico de cotações desde 1986 e campos de preço, número de negócios, quantidade e volume. Também mantém arquivos históricos de boletins e derivativos/câmbio.

BCB disponibiliza séries SGS estruturadas.

Tesouro Direto publica históricos anuais de preços e taxas.

CVM mantém bases abertas e consultas de ofertas públicas; o plano 2026–2028 prevê novas bases e API pública.

Cboe disponibiliza histórico diário do VIX desde 1990.

## Regra de proveniência

Na ingestão efetiva, cada arquivo/série deve registrar URL institucional, data/hora UTC de coleta, referência temporal, identificador do arquivo/série e transformação aplicada.

## Limite de acesso

Não assumir que book, trades tick-by-tick, microestrutura, posição/alocação por participante ou segmentações avançadas B3 sejam gratuitos. Se houver acesso condicionado, registrar explicitamente a restrição.
