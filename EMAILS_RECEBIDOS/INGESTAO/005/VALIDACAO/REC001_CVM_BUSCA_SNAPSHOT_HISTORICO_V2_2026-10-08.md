# BLOOMBERG_MAIL — REC-001 CVM — BUSCA DE SNAPSHOT HISTÓRICO V2

> Cabeçalho histórico — 2026-10-08. Segunda investigação controlada para localizar representação oficial correspondente ao RAW da INGESTÃO 005.

## Resultado da busca

Foi confirmada no índice oficial da CVM a existência do recurso atual oferta_distribuicao.zip, com atualização registrada em 07/10/2026. O recurso possui o mesmo identificador CKAN c70a97f3-8e3d-4ada-9d3b-b0005e9d1fcb e aparece em páginas históricas indexadas com datas distintas de atualização, incluindo 25/07, 28/07, 11/08, 10/09 e 12/09/2026.

Isso comprova versionamento temporal do recurso, mas as páginas históricas não expõem os bytes ou uma URL versionada do ZIP.

## Busca pelo SHA do RAW

SHA-256 procurado:
72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306

Não foi encontrada na indexação pública uma cópia do ZIP com esse SHA, nem um snapshot oficial diretamente materializável.

## Evidência adicional

A busca por cópias em repositórios públicos também não produziu uma representação confiável e oficial do mesmo arquivo. Fontes de terceiros não serão promovidas a evidência REC-001 sem uma regra específica de independência e equivalência.

## Decisão

REC-001 CVM = BLOCKED_NO_MATERIALIZED_HISTORICAL_SECOND_REPRESENTATION

A divergência atual continua registrada como SOURCE_UPDATED_SINCE_RAW. Ela não invalida o RAW histórico e não autoriza substituição.

## Próximo passo controlado

Antes de abandonar a reconciliação histórica, testar uma reconciliação estrutural contra a representação histórica institucional da CVM, sem declarar PASS automaticamente. A saída deverá separar cobertura, chaves encontradas, diferenças e registros sem correspondência.

RAW permanece imutável.
