# BLOOMBERG_MAIL — LAYOUT — GATE CONJUNTO 005N — 5/5

> Cabeçalho histórico: layout técnico criado em 2026-10-08 para a validação determinística conjunta dos cinco normalizadores da INGESTÃO 005.

## Entrada

- manifesto de aquisição: `EMAILS_RECEBIDOS/INGESTAO/005/manifesto_aquisicao.json`
- plano de normalização: `EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/manifesto_normalizacao.json`
- validação conjunta existente: `VALIDACAO_NORMALIZADORES_005N.json`
- validação independente B3: `B3/VALIDACAO_NORMALIZACAO_B3_A2026.json`

## Datasets e manifests

| Dataset | Manifesto |
|---|---|
| BCB_SGS_1178 | `bcb_sgs_1178_normalizado.json` |
| VIX | `vix_normalizado.json` |
| CVM_OFERTAS | `cvm_ofertas_normalizado.json` |
| TESOURO_HISTORICO | `tesouro_normalizado.json` |
| B3_COTAHIST_A2026 | `B3/b3_cotahist_normalizado.json` |

## Checks determinísticos

1. exatamente cinco datasets esperados;
2. IDs únicos;
3. SHA RAW igual ao manifesto de aquisição;
4. `quality_status = NORMALIZED_DERIVED`;
5. parser version presente;
6. source/source_url ou equivalente presente;
7. raw_path presente;
8. saída derivada presente;
9. gzip íntegro para cada `.jsonl.gz`;
10. validação individual PASS;
11. B3 independente PASS;
12. contagens de duplicidade/missingness explícitas;
13. políticas de imutabilidade e ausência de transformação econômica preservadas;
14. nenhuma remoção silenciosa de duplicidades.

## Resultado

O resultado deve ser um JSON determinístico com `status = PASS` somente se todos os checks forem verdadeiros. Qualquer falha produz `status = FAIL` e bloqueia integração.
