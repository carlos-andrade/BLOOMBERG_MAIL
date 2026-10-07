# BLOOMBERG_MAIL — NORMALIZAÇÃO 005 — CONTROLE DE ESTADO

> Cabeçalho histórico: documento de governança criado em 2026-10-07 para registrar o estado verificável da etapa 005N após a promoção da CAMADA_A.

## Estado atual

**STATUS:** IMPLEMENTAÇÃO PARCIAL — INTEGRAÇÃO BLOQUEADA

A CAMADA_A permanece promovida como referência validada. A NORMALIZAÇÃO é uma camada derivada e não substitui o RAW.

## Correção aplicada

O normalizador BCB SGS 1178 foi corrigido para interpretar DD/MM/YYYY como data real antes da ordenação, publicar a data canônica em ISO-8601, preservar date_raw sem alteração, preservar o valor decimal exatamente como string RAW sem coerção numérica silenciosa e manter SHA-256, proveniência e período de referência.

Parser atual do código: normalizacao-005-v1.1.

## Estado dos cinco datasets

| Dataset | Estado |
|---|---|
| BCB SGS 1178 | normalizador implementado; revisão v1.1 aplicada |
| VIX | normalizador implementado |
| B3 COTAHIST | aguardando inspeção determinística do ZIP |
| CVM Ofertas | aguardando inspeção determinística do ZIP |
| Tesouro Direto | aguardando inspeção determinística do CSV |

## Gate

A promoção para NORMALIZED_VALIDATED continua BLOQUEADA até que: (1) a inspeção dos formatos restantes seja executada no GitHub Actions; (2) os layouts sejam confirmados a partir dos próprios RAW; (3) os cinco normalizadores sejam implementados; (4) as cinco saídas sejam validadas contra seus RAW e SHA-256; (5) duplicidades, missingness, datas, unidades e proveniência sejam aprovados; (6) a reconciliação final seja PASS para 5/5; e (7) somente então seja autorizada a INTEGRAÇÃO.

## Restrições permanentes

- RAW imutável.
- Sem valores inventados.
- Sem interpolação ou preenchimento silencioso.
- Sem ajuste econômico ou de preços.
- Sem sinais operacionais.
- Sem promoção parcial para INTEGRAÇÃO.

## Próxima ação operacional

Executar manualmente no GitHub o workflow BLOOMBERG_MAIL — INGESTÃO 005N — Inspeção de Formatos.

Não há neste registro qualquer alegação de que essa execução já ocorreu.
