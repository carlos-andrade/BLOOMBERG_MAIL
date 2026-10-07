# BLOOMBERG_MAIL — NORMALIZAÇÃO 005 — CONTROLE DE ESTADO

> Cabeçalho histórico: documento de governança criado em 2026-10-07 para registrar o estado verificável da etapa 005N após a promoção da CAMADA_A e atualizado após a validação conjunta 005N #5.

## Estado atual

**STATUS:** NORMALIZAÇÃO VALIDADA — INTEGRAÇÃO BLOQUEADA POR B3

A CAMADA_A permanece promovida como referência validada. A NORMALIZAÇÃO é uma camada derivada e não substitui o RAW.

## Validação conjunta 005N #5

Workflow: **BLOOMBERG_MAIL — INGESTÃO 005N — Validação Conjunta dos Normalizadores**

- Execução: **#5**
- Acionamento: manual
- Commit informado: `f241710`
- Resultado: **SUCESSO**
- Duração informada: **14 s**
- Evidência persistida: `VALIDACAO_NORMALIZADORES_005N.json`
- SHA do arquivo de evidência: `3b51a645bc0b0e6d66aee9262a310625ac602756`

A evidência persistida registra `status: PASS`, `raw_sha_match: true`, `normalized_raw_link_match: true`, `quality_status: NORMALIZED_DERIVED` e existência dos derivados publicados para BCB, VIX, CVM e Tesouro.

### Derivados confirmados

**CVM Ofertas**
- `oferta_distribuicao.jsonl.gz`
- `oferta_resolucao_160.jsonl.gz`

**Tesouro Histórico**
- `tesouro_normalizado.jsonl.gz`

BCB SGS 1178 e VIX possuem as respectivas saídas normalizadas persistidas e validadas.

## Estado dos datasets

| Dataset | Estado |
|---|---|
| BCB SGS 1178 | VALIDADO |
| VIX | VALIDADO |
| CVM Ofertas | VALIDADO |
| Tesouro Direto | VALIDADO |
| B3 COTAHIST | **BLOQUEADO — falta mapeamento autoritativo** |

A validação 005N cobre os quatro normalizadores atualmente implementados. O quinto dataset, B3 COTAHIST, permanece fora da promoção porque seu layout semântico, offsets, escalas e regras de reconciliação ainda exigem fonte autoritativa. Nenhum campo deve ser inferido.

## Gate de integração

**INTEGRAÇÃO: BLOCKED_UNTIL_B3_NORMALIZER_AND_ALL_FIVE_VALIDATED**

A NORMALIZAÇÃO dos quatro datasets implementados está validada. A integração somente poderá avançar depois de:

1. obter o mapeamento autoritativo versionado do COTAHIST;
2. implementar o normalizador B3 exclusivamente a partir desse mapeamento;
3. validar a saída B3 contra o RAW e SHA-256;
4. executar duplicidades, missingness, datas, unidades e proveniência;
5. obter reconciliação final **5/5 PASS**;
6. somente então liberar a INTEGRAÇÃO.

## Restrições permanentes

- RAW imutável.
- Sem valores inventados.
- Sem interpolação ou preenchimento silencioso.
- Sem ajuste econômico ou de preços.
- Sem sinais operacionais durante ingestão, validação ou normalização.
- Sem promoção parcial para INTEGRAÇÃO.
- VALIDAÇÃO não executa normalizadores e não modifica RAW.

## Próxima ação operacional

**Pesquisar e registrar a fonte autoritativa do layout do B3 COTAHIST antes de qualquer implementação de normalização B3.**

Não inferir offsets, posições, escalas, tipos de registro ou semântica de campos a partir de memória ou de bibliotecas de terceiros sem validação documental autoritativa.
