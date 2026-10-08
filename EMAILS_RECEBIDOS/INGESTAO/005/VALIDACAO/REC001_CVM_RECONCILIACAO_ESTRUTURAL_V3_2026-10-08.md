# BLOOMBERG_MAIL — REC-001 CVM — RECONCILIAÇÃO ESTRUTURAL HISTÓRICA V3

> Cabeçalho histórico — 2026-10-08. Execução controlada da alternativa histórica prevista após a busca de snapshot.

## Representações comparadas

**RAW 005:** `oferta_distribuicao.zip`

SHA-256: `72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306`

**Representação histórica oficial CVM:** página Séries Históricas — Distribuições Públicas, com planilhas individualizadas por classe de ativo.

Fonte oficial: https://www.gov.br/cvm/pt-br/centrais-de-conteudo/publicacoes/series-historicas/distribuicoes-publicas

## Testes determinísticos

| Critério REC-001 | Resultado | Evidência |
|---|---|---|
| Mesma fonte institucional | PASS | CVM |
| Representação acessível | PASS | planilhas oficiais |
| Mesmo conceito geral | PASS | distribuições públicas |
| Mesmo esquema | FAIL | ZIP possui esquema próprio; séries históricas são planilhas por classe |
| Mesmo período de referência | FAIL | séries históricas disponibilizadas na página têm atualização registrada em 19/03/2025; RAW foi capturado em 2026 |
| Mesma granularidade | FAIL | ZIP é registro operacional de ofertas; planilhas históricas são representação histórica por classe |
| Chave lógica 1:1 demonstrável | BLOCKED | estruturas não equivalentes |
| Igualdade de bytes | NOT APPLICABLE | representações distintas |

## Resultado

A representação histórica oficial é válida como **evidência contextual independente**, mas não é uma segunda representação comparável do mesmo snapshot do RAW 005.

Portanto, conforme o CONTRATO_VERIFICACAO_V1_0 e o PLANO_REC-001:

`REC-001 CVM = BLOCKED`

Código do bloqueio:
`BLOCKED_NON_EQUIVALENT_HISTORICAL_REPRESENTATION`

## Não realizado

- nenhum valor do RAW foi alterado;
- nenhuma oferta foi ajustada ou interpolada;
- nenhuma correspondência aproximada foi promovida a igualdade;
- nenhuma fonte de terceiros foi usada para declarar PASS;
- GAT-001 não foi desbloqueado.

## Conclusão operacional

A tentativa de reconciliação estrutural encerra a rota histórica disponível neste momento. Para obter PASS é necessária uma segunda representação oficial/independente do **mesmo período e da mesma granularidade** ou um snapshot histórico materializável do próprio ZIP.

RAW permanece imutável.
