# BLOOMBERG_MAIL — INGESTÃO 005 — FONTES RESOLVIDAS DIRETAMENTE

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Ingestão: 005
- Data: 2026-10-07
- Finalidade: registrar que a aquisição deve partir diretamente das fontes oficiais, sem URL inventada.

## VIX — Cboe
A página oficial da Cboe identifica explicitamente o arquivo de dados diários do VIX de 1990 até o presente e informa que é atualizado diariamente.

Arquivo oficial resolvido:
https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv

Fonte-página oficial:
https://www.cboe.com/tradable-products/vix/vix-historical-data

## Tesouro Direto
A aquisição deve começar pela página oficial de Histórico de Preços e Taxas e resolver o link do arquivo diretamente nela. Não será usado URL construído por padrão de nomenclatura.

Página oficial:
https://www.tesourodireto.com.br/produtos/dados-sobre-titulos/historico-de-precos-e-taxas

## Regra definitiva
1. consultar a fonte oficial;
2. resolver o arquivo/link efetivamente publicado pela fonte;
3. adquirir diretamente;
4. preservar RAW;
5. calcular SHA-256;
6. registrar timestamp UTC e período;
7. validar estrutura, datas, unidades, missingness e duplicidade;
8. somente então permitir promoção.

## Gate
A Layer A permanece bloqueada até a validação completa e reconciliação independente.
