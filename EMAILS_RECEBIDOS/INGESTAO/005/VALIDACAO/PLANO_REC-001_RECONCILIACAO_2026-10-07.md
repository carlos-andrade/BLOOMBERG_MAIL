# BLOOMBERG_MAIL — INGESTÃO 005 — PLANO REC-001

> Cabeçalho histórico — 2026-10-07.
> Finalidade: executar a reconciliação independente exigida pelo CONTRATO_VERIFICACAO_V1_0 antes de qualquer promoção.

## Regra

REC-001 somente pode ser PASS quando existir uma segunda representação documentada, acessível e comparável ao RAW da INGESTÃO 005. Diferenças devem ser registradas; não podem ser corrigidas silenciosamente.

## Matriz operacional

| Dataset | RAW 005 | Segunda representação | Chave | Estado inicial |
|---|---|---|---|---|
| B3_COTACOES | COTAHIST_A2026.ZIP | evidência versionada COTAHIST no repositório B3 + endpoint oficial | arquivo/período + estrutura COTAHIST | BLOCKED até comparação executada |
| CVM_OFERTAS | oferta_distribuicao.zip | segunda representação oficial/independente a definir e materializar | identificador da oferta + data + emissor | BLOCKED |
| BCB_SGS | bcb_sgs_1178_ultimos_10.json | endpoint oficial consultado novamente, período sobreposto | data | BLOCKED |
| TESOURO_HISTORICO | precotaxatesourodireto.csv | arquivo/representação oficial independente do mesmo período | título + vencimento + data base | BLOCKED |
| VIX | VIX_History.csv | segunda representação independente/oficial acessível do mesmo período | DATE | BLOCKED |

## Critérios

1. Mesmo período de referência.
2. Mesma unidade e definição econômica.
3. Chave lógica explicitamente definida.
4. Comparação sem conversão destrutiva.
5. Tolerância somente se documentada pela natureza do dado.
6. Ausência de segunda representação = BLOCKED.
7. Divergência não explicada = BLOCKED/FAIL conforme o contrato.
8. Evidência salva no repositório.
9. Resultado reproduzível por código.
10. GAT-001 continua bloqueado enquanto qualquer REC-001 obrigatório estiver BLOCKED.

## Sequência

B3 → CVM → BCB → TESOURO → VIX → GAT-001

Nenhum dataset será promovido antecipadamente para Layer A.

## Resultado desta etapa

Este documento define o trabalho executável. Não declara nenhuma reconciliação como PASS por planejamento.