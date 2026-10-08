# BLOOMBERG_MAIL — STATUS FINAL — TPMERC=021 — 2026-10-08

> Cabeçalho histórico: fechamento do incidente determinístico TPMERC=021 da INGESTÃO 005N, após reconciliação com dados validados do repositório carlos-andrade/B3.

## Resultado

**TPMERC=021: RESOLVIDO PARA O GATE 005N.**

A resolução foi baseada em:
1. dados COTAHIST A2026 validados no repositório B3;
2. execução controlada no próprio repositório B3;
3. evidência oficial B3 do BBT: Final Q e Market 21 — BLOCK LOT;
4. confirmação no RAW BLOOMBERG_MAIL de 1.696 ocorrências de TPMERC=021;
5. reexecução do validador BLOOMBERG_MAIL.

## Evidência B3

Run:
- workflow: B3 — Reconciliação COTAHIST TPMERC 021 x BVBG.028
- run: 37763162650
- resultado: success
- COTAHIST B3: 1.544 registros TPMERC=021
- 255 CODNEG distintos
- 179 pregões
- padrão observado: CODNEG terminado em Q

Arquivo:
dados/cotahist/quality/COTAHIST_A2026_TPMERC021_BVBG028_RECONCILIACAO_V1.json

## Evidência BLOOMBERG_MAIL

Run:
- workflow: BLOOMBERG_MAIL — INGESTÃO 005N — Validação Layout B3 COTAHIST
- run: 37763718725
- run number: 8
- resultado: success

Resultado:
- registros físicos: 3.070.833
- registros tipo 01: 3.070.831
- registros tipo 00: 1
- registros tipo 99: 1
- comprimento 245 bytes: 3.070.833
- registros tipo 01 inválidos: 0
- datas inválidas: 0
- numéricos inválidos: 0
- TPMERC inválido: 0
- CODBDI em branco: 0
- INDOPC inválido: 0
- trailer = registros tipo 01: true
- RAW SHA: c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f

## Decisão

O conjunto aceito de TPMERC do validador 005N agora inclui:

010, 012, 013, 017, 020, 021, 030, 050, 060, 070, 080.

O código 021 é classificado operacionalmente como **BLOCK LOT / BBT**, com base na reconciliação documentada.

## Governança

- RAW: IMUTÁVEL.
- Ajuste econômico: NÃO.
- Interpolação: NÃO.
- Invenção: NÃO.
- Normalização B3: ainda não executada neste gate.
- Workflow de validação: restaurado para execução manual.
- Integração: permanece condicionada aos próximos gates.

## Próximo passo

Implementar o normalizador B3 COTAHIST usando o layout oficial já mapeado e a exceção/reconciliação TPMERC=021 formalizada, seguido de validação independente do NORMALIZED.
