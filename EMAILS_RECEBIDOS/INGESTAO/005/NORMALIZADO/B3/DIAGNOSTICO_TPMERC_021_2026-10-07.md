# BLOOMBERG_MAIL — Diagnóstico COTAHIST A2026 — TPMERC 021

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Repositório: carlos-andrade/BLOOMBERG_MAIL
- Etapa: INGESTÃO 005N — Validação do layout B3
- Data: 2026-10-07
- Natureza: evidência determinística de execução
- RAW: imutável

## Execução
- Workflow: BLOOMBERG_MAIL — INGESTÃO 005N — Validação Layout B3 COTAHIST
- Run: #7
- Run ID: 37694046706
- Commit executor: 0ba7f00cbab1c82535c96da8c5c44de953809cf0
- Evento: push controlado sobre alteração do validador
- Resultado: FAIL

## Evidência
- RAW SHA-256 esperado/observado: c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f
- ZIP íntegro: SIM
- Membro: COTAHIST_A2026.TXT
- Registros físicos: 3.070.833
- Registro 00: 1
- Registro 01: 3.070.831
- Registro 99: 1
- Comprimento de registros: 245 bytes, sem inválidos
- Trailer = registros 01: SIM
- TPMERC inválidos: 1.696
- Valor observado dos TPMERC inválidos: 021 (1.696 ocorrências)
- CODBDI em branco: 0
- INDOPC inválido: 0
- Datas inválidas: 0
- Campos numéricos inválidos: 0

## Decisão
O código TPMERC 021 foi observado no RAW de 2026, mas não está contemplado na tabela TPMERC do layout B3 v2.0/revisão 02 utilizado como referência, que documenta 010, 012, 013, 017, 020, 030, 050, 060, 070 e 080.

Portanto, o sistema **não deve atribuir significado ao código 021 por inferência**. A validação permanece FAIL/BLOCKED até existir fonte oficial que reconcilie o código 021.

## Governança
- RAW alterado: NÃO
- Normalização executada: NÃO
- Interpolação: NÃO
- Invenção: NÃO
- Ajuste econômico: NÃO
- Sinais operacionais: NÃO
- Normalizador B3: BLOQUEADO
- Integração: BLOQUEADA

## Próximo gate
Identificar fonte oficial B3 que defina TPMERC 021 para COTAHIST A2026. Somente após essa reconciliação:
1. atualizar o mapeamento autoritativo;
2. corrigir o validador;
3. executar novamente;
4. exigir PASS;
5. publicar a evidência final;
6. só então liberar o normalizador B3.
