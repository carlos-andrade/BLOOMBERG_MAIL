# BLOOMBERG_MAIL — FONTES — INGESTÃO 005

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Ingestão: 005
- Data: 2026-10-07
- Status: fontes oficiais registradas antes da aquisição.

## B3
- Instituição: B3
- Finalidade: cotações históricas COTAHIST.
- Página: https://www.b3.com.br/
- Recurso utilizado: COTAHIST anual.
- Status: fonte registrada; aquisição RAW validada em INGESTÃO 005-B.

## CVM
- Instituição: Comissão de Valores Mobiliários.
- Finalidade: ofertas/distribuições.
- Página: https://www.gov.br/cvm/
- Recurso: oferta_distribuicao.zip.
- Status: fonte registrada; aquisição RAW validada.

## Banco Central do Brasil / SGS
- Instituição: Banco Central do Brasil.
- Finalidade: séries macroeconômicas.
- Página: https://www.bcb.gov.br/
- Recurso: SGS, série 1178 na amostra técnica.
- Status: fonte registrada; amostra técnica adquirida.

## Tesouro Nacional / Tesouro Transparente
- Instituição: Tesouro Nacional / Tesouro Transparente.
- Finalidade: preços e taxas dos títulos ofertados pelo Tesouro Direto.
- Página de dados: https://www.tesourotransparente.gov.br/
- Recurso direto resolvido:
  https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/precotaxatesourodireto.csv
- Arquivo: precotaxatesourodireto.csv
- Status: fonte resolvida; aquisição pendente de execução 005-C.

## Cboe / VIX
- Instituição: Cboe Global Markets.
- Finalidade: série histórica diária do VIX.
- Página oficial:
  https://www.cboe.com/tradable_products/vix/vix_historical_data/
- Recurso direto:
  https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv
- Arquivo: VIX_History.csv
- Status: fonte resolvida; aquisição pendente de execução 005-C.

## Regra
Todas as fontes acima devem permanecer registradas em `FONTES/`, independentemente de ingestão, workflow ou conversa.
