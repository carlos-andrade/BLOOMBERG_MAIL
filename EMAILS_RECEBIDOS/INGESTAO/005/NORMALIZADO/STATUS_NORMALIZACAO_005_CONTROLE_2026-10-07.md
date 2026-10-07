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

## Validação B3 preparada

Foram publicados, sem executar ainda o workflow:

- `scripts/validacao_layout_b3_cotahist_005.py`
- `.github/workflows/bloomberg-mail-ingestao-005n-validacao-b3-layout.yml`

A validação é **somente leitura do RAW** e verifica deterministically:
1. SHA-256 do ZIP contra o manifesto;
2. integridade do ZIP e quantidade de membros;
3. registros de 245 bytes;
4. tipos 00/01/99;
5. unicidade estrutural de header/trailer;
6. posições e formatos dos campos do registro 01;
7. datas;
8. campos numéricos;
9. INDOPC;
10. contagem informada no trailer versus registros de cotação.

O workflow é `workflow_dispatch` e publica a evidência somente se a validação terminar em **PASS**. Não houve execução automática nesta etapa.

## Próxima ação operacional

A fonte autoritativa do layout B3 COTAHIST foi identificada e registrada em:

EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/MAPEAMENTO_AUTORITATIVO_COTAHIST_V2_0_2026-10-07.md

Fonte oficial B3: https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf

O mapeamento documenta os registros 00, 01 e 99, os offsets oficiais, tipos, escalas e tabelas relevantes. O bloqueio documental inicial está resolvido.

Antes da implementação do normalizador B3, executar validação determinística do layout contra o RAW COTAHIST_A2026.ZIP: comprimento de 245 bytes, header/trailer, offsets, tipos, escalas, datas, quantidade, volume e contagem do trailer.

A INTEGRAÇÃO continua bloqueada até a validação completa dos cinco datasets.
