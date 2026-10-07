# BLOOMBERG_MAIL — MAPEAMENTO B3 COTAHIST — v1.0

> Histórico: 2026-10-07 | Projeto: BLOOMBERG_MAIL | Etapa: INGESTÃO 005 / NORMALIZAÇÃO

## Estado
**BLOCKED_PENDING_AUTHORITATIVE_FIELD_MAPPING**

## Evidência disponível
- RAW: `EMAILS_RECEBIDOS/INGESTAO/005/RAW/COTAHIST_A2026.ZIP`
- SHA-256: `c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f`
- Membro: `COTAHIST_A2026.TXT`
- Estrutura: largura fixa, sem delimitador
- Inspeção: `INSPECAO_FORMATOS_005.json`

## Regra de bloqueio
A amostra confirma a natureza fixed-width, mas não autoriza inferir offsets econômicos. O normalizador B3 não poderá converter posições em campos sem uma fonte autoritativa ou tabela de layout versionada.

## Campos que NÃO serão inventados
Não serão assumidos offsets, tamanhos, escalas, casas decimais, códigos econômicos, chaves ou semântica para preço, quantidade, volume, tipo de mercado ou identificadores.

## Próxima evidência necessária
1. Layout oficial do COTAHIST correspondente ao formato do arquivo.
2. Tabela de posições/offsets versionada.
3. Regra explícita de escala por campo.
4. Casos de reconciliação com linhas RAW reais.

## Gate
**FIELD_MAPPING_REQUIRED** → **NORMALIZER_B3_IMPLEMENTATION** → **VALIDATION** → **RECONCILIATION**.
