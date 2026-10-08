# BLOOMBERG_MAIL — INGESTÃO 005 — REC-001 CVM

> Cabeçalho histórico — 2026-10-07.

- Endpoint oficial: https://dados.cvm.gov.br/dados/OFERTA/DISTRIB/DADOS/oferta_distribuicao.zip
- Observado UTC: 2026-10-08T12:57:26.211202+00:00
- RAW preservado: True
- SHA RAW: 72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306
- SHA endpoint independente: 4b0ab625aa94267968e841c8c1fc2acbcc40b3fe111213b3f9852a832095212f
- Resultado: **SOURCE_UPDATED_SINCE_RAW**

## Regra

A reconciliação baixa o arquivo atual para área temporária, calcula SHA-256 independentemente e nunca substitui o RAW. Igualdade é PASS; divergência é classificada como atualização da fonte e mantém a promoção bloqueada.
