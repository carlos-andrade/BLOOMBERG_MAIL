# BLOOMBERG_MAIL — REC-001 CVM — INVESTIGAÇÃO DE REPRESENTAÇÃO HISTÓRICA

> Cabeçalho histórico — 2026-10-08. Investigação controlada para resolver o bloqueio REC-001 CVM sem substituir o RAW da INGESTÃO 005.

## RAW de referência
- Dataset: CVM_OFERTAS
- RAW: EMAILS_RECEBIDOS/INGESTAO/005/RAW/oferta_distribuicao.zip
- SHA-256: 72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306
- Registros normalizados: 48.944 em oferta_distribuicao.csv e 14.772 em oferta_resolucao_160.csv.

## Fonte oficial atual
A CVM informa que o conjunto Ofertas Públicas de Distribuição é atualizado diariamente e que o ZIP contém os membros oferta_distribuicao.csv e oferta_resolucao_160.csv.

## Evidência histórica
A mesma identificação de recurso CVM c70a97f3-8e3d-4ada-9d3b-b0005e9d1fcb aparece em páginas indexadas com diferentes datas de atualização, incluindo setembro e outubro de 2026. Isso demonstra atualização histórica do recurso, mas não disponibiliza por si só os bytes históricos do ZIP.

## Segunda representação oficial
A CVM também mantém uma página institucional de séries históricas “Distribuições Públicas”, com planilhas históricas por classe de ativo. Essa representação é oficial e histórica, porém possui granularidade/estrutura diferente do ZIP diário. Não será tratada como substituta nem como PASS automático.

## Conclusão
Nesta etapa não foi localizada uma cópia oficial dos bytes cujo SHA-256 seja exatamente 72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306.

STATUS: BLOCKED / HISTORICAL_REPRESENTATION_NOT_MATERIALIZED

Não substituir RAW, não inferir igualdade, não declarar PASS pela existência de página histórica e não misturar representações com estruturas diferentes como se fossem equivalentes.

## Próximo procedimento
1. Procurar snapshot oficial/versionado correspondente à captura do RAW.
2. Procurar recurso histórico do mesmo conjunto.
3. Se não existir, avaliar reconciliação por chave entre o RAW normalizado e a representação histórica institucional, medindo cobertura e diferenças explicitamente.

O RAW permanece imutável e o REC-001 CVM permanece bloqueado.
