# BLOOMBERG_MAIL — LAYOUT CVM OFERTAS — v1.0

> Histórico: 2026-10-07 | Projeto: BLOOMBERG_MAIL | Etapa: INGESTÃO 005 / NORMALIZAÇÃO

## Estado
**READY_FOR_IMPLEMENTATION_FROM_INSPECTED_SCHEMA**

## Evidência
- Inspeção: `INSPECAO_FORMATOS_005.json`
- RAW: `RAW/oferta_distribuicao.zip`
- SHA-256 RAW: `72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306`
- ZIP integrity: PASS
- Encoding observado: `latin-1`
- Delimitador observado: `;`

## Membros
### oferta_distribuicao.csv
Schema observado no header do arquivo. Os nomes devem ser preservados exatamente como fonte; nenhum campo deve ser renomeado ou descartado sem mapeamento explícito.

### oferta_resolucao_160.csv
Schema observado no header do arquivo. Os nomes devem ser preservados exatamente como fonte; nenhum campo deve ser renomeado ou descartado sem mapeamento explícito.

## Regras de transformação
- Datas somente para representação canônica, preservando o valor RAW.
- Valores numéricos somente após definição explícita de separador decimal e sem alteração econômica.
- Campos vazios permanecem vazios.
- Duplicidades são reportadas, nunca removidas silenciosamente.
- Todos os registros mantêm vínculo com o SHA do ZIP RAW e o membro de origem.

## Próximo gate
Implementação determinística → validação estrutural → validação de tipos/datas/missingness → reconciliação contra RAW.
