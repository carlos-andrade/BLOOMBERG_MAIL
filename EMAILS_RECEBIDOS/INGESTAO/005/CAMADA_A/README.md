# BLOOMBERG_MAIL — CAMADA A — REFERÊNCIA VALIDADA

> Histórico: 2026-10-07 | promoção controlada após INGESTÃO 005D #5.
> Status: PROMOVIDA COMO CAMADA DE REFERÊNCIA VALIDADA.
> Fonte primária: RAW imutável em `../RAW/`.

## Objetivo

A Camada A é a primeira camada derivada após a validação formal. Nesta fase ela funciona como **referência validada e auditável**, sem duplicar os binários RAW e sem executar normalização econômica.

A promoção foi autorizada após:

- 005D #5 = PASS;
- GAT-001 = PASS;
- REC-001 = PASS para os cinco datasets;
- PRO-001 = PASS para os cinco datasets;
- proveniência obrigatória completa no manifesto;
- aprovação explícita para prosseguir.

## Regra de origem

Cada dataset desta camada aponta para um RAW específico e para seu SHA-256. O RAW permanece imutável.

Nenhuma informação é:

- inventada;
- interpolada;
- preenchida silenciosamente;
- ajustada por inflação/proventos;
- corrigida economicamente;
- transformada em sinal operacional.

## Datasets promovidos

| Dataset | Estado | RAW |
|---|---|---|
| B3_COTACOES | PROMOTED_REFERENCE | COTAHIST_A2026.ZIP |
| CVM_OFERTAS | PROMOTED_REFERENCE | oferta_distribuicao.zip |
| BCB_SGS | PROMOTED_REFERENCE | bcb_sgs_1178_ultimos_10.json |
| TESOURO_HISTORICO | PROMOTED_REFERENCE | precotaxatesourodireto.csv |
| VIX | PROMOTED_REFERENCE | VIX_History.csv |

## Próxima etapa

A normalização física, caso necessária, será produzida separadamente a partir desta referência e do RAW, com parser/versionamento próprios e validação pós-transformação.

**Não há sinal operacional nesta camada.**
