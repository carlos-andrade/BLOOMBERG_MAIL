---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-STATUS-NORMALIZACAO-005-CONTROLE-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — NORMALIZAÇÃO 005 — CONTROLE DE ESTADO"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/STATUS_NORMALIZACAO_005_CONTROLE_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — NORMALIZAÇÃO 005 — CONTROLE DE ESTADO

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-STATUS-NORMALIZACAO-005-CONTROLE-2026-10-07-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-08
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


## Contexto Histórico

Documento histórico do projeto BLOOMBERG_MAIL integrado à governança documental central de carlos-andrade.

## Estado

IMPLEMENTADO — cabeçalho migrado para o padrão canônico.

## Evidências

Modelo canônico: Curioso-da-Internet-IA/CABEÇALHO/MODELO-PADRAO-CABECALHO.md.

## Validação

Cabeçalho, identificação documental e rastreabilidade foram normalizados.

## Resultado

O conteúdo original abaixo foi preservado.

## Próxima Ação

Atualizar versão, data e rastreabilidade em alterações relevantes.

---

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

## Execução controlada da validação B3 — run #6

- Commit de disparo: `ceb870f7bbcd2289a23d8452bf7547970e5e6ab2`
- Workflow run: `37693597585`
- Acionamento: `push` controlado sobre a revisão 1.1 do validador
- Estado verificado: `in_progress`
- Etapa em execução: `Validar COTAHIST contra layout oficial B3`
- Evidência final: ainda não publicada; o workflow publica o JSON somente após PASS.
- RAW permanece imutável.


## 2026-10-07 — Correção e execução controlada B3 — TPMERC 021

- Run #7: 37694046706
- Commit executor: 0ba7f00cbab1c82535c96da8c5c44de953809cf0
- Resultado: FAIL determinístico.
- Evidência: 1.696 registros com TPMERC = 021.
- O layout B3 v2.0/rev.02 atualmente mapeado documenta 010, 012, 013, 017, 020, 030, 050, 060, 070 e 080; 021 não foi atribuído por inferência.
- RAW SHA confirmado e RAW permaneceu imutável.
- Diagnóstico publicado em `NORMALIZADO/B3/DIAGNOSTICO_TPMERC_021_2026-10-07.md`.
- Workflow temporariamente usado com gatilho push foi restaurado para `workflow_dispatch` בלבד/manual-only no commit `f2b0934e7ad128ce49c19b4b6cd8ed802b2be536`.
- B3 normalizer: BLOQUEADO.
- Integração: BLOQUEADA.
- Próximo gate: reconciliação oficial do TPMERC 021 antes de qualquer PASS.


## 2026-10-08 — B3 COTAHIST normalizado e validado

- Normalizador: `scripts/normalizacao_b3_005.py`
- Parser: `normalizacao-005-b3-v1.0`
- Workflow controlado de normalização: run **37765338810** (#4)
- Resultado: **SUCCESS**
- Registros físicos: **3.070.833**
- Registros 00/01/99: **1 / 3.070.831 / 1**
- Saída: **31 partições JSONL gzip**, 100.000 registros por partição
- SHA RAW confirmado: `c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f`
- TPMERC=021: **1.696 registros**, sem erro semântico após reconciliação controlada.
- Duplicidades pela chave operacional `data_pregao+codbdi+codneg+tpmerc`: **9.675**; reportadas, não removidas silenciosamente.
- Missing fields: **0**.

### Validação independente

Workflow: **BLOOMBERG_MAIL — INGESTÃO 005N — Validação Independente Normalização B3**

- Check run: **113275405446**
- Resultado: **SUCCESS**
- Duração: aproximadamente **2m26s**
- Partições verificadas: **31**
- Registros verificados: **3.070.831**
- JSON inválido: **0**
- Datas inválidas: **0**
- Decimais inválidos: **0**
- Erros na semântica reconciliada de TPMERC=021: **0**
- Evidência: `B3/VALIDACAO_NORMALIZACAO_B3_A2026.json`
- SHA da evidência: `016566c0fc5f6857c4ac4a3f14c7c4d4f43952aa`

O gatilho `push` utilizado para execução controlada foi removido imediatamente após a validação. O workflow de validação independente voltou a `workflow_dispatch`/manual-only.

## Estado atualizado dos datasets

| Dataset | Estado |
|---|---|
| BCB SGS 1178 | VALIDADO |
| VIX | VALIDADO |
| CVM Ofertas | VALIDADO |
| Tesouro Direto | VALIDADO |
| B3 COTAHIST | **NORMALIZADO + VALIDAÇÃO INDEPENDENTE PASS** |

**Integração:** permanece **BLOCKED** até revisão/promulgação do gate conjunto 5/5. A conclusão da normalização B3 não autoriza automaticamente a integração.


## 2026-10-08 — Gate Conjunto 005N 5/5 — verificação, correção e execução controlada

Foi criado o contrato do Gate Conjunto 5/5:

- `CARTA_GATE_CONJUNTO_005N_V1_0_2026-10-08.md`
- `LAYOUT_GATE_CONJUNTO_005N_V1_0_2026-10-08.md`
- `scripts/validacao_gate_conjunto_005n.py`
- `.github/workflows/bloomberg-mail-ingestao-005n-gate-conjunto.yml`

### Primeira execução verificável

A execução acionada pelo workflow produziu evidência persistida:

`VALIDACAO_GATE_CONJUNTO_005N_5X5.json`

Resultado: **FAIL**.

O FAIL não foi atribuído aos cinco datasets. Foram identificados dois defeitos no executor:

1. os arquivos particionados do B3 são relativos à subpasta `NORMALIZADO/B3/`;
2. o manifesto de aquisição identifica o BCB como `BCB_SGS`, enquanto o manifesto normalizado usa `BCB_SGS_1178`.

### Correção

O executor foi corrigido e publicado no commit `e3a97b78410d8c2ae91a55dae163bc8c7fd45eed`.

A tentativa seguinte de disparo por `push` não produziu nova execução verificável; portanto, **nenhum PASS é declarado**.

O workflow foi restaurado para **manual-only** no commit `8fa83affe269be1e746d8377b4897f7f6f85a6c2`.

### Estado do gate

**005N CONJUNTO 5/5: BLOQUEADO — execução manual pós-correção ainda necessária.**

A evidência FAIL existente é preservada como histórico e não deve ser sobrescrita como se fosse uma execução posterior.

**REC-001 de integração permanece bloqueado.**


## 2026-10-08 — Gate Conjunto 005N 5/5 — PASS

Run #7 (`37776431192`) concluído com SUCCESS. O gate 5/5 confirmou os cinco datasets normalizados, SHA RAW compatível, derivados presentes, integridade gzip e validações individuais PASS. Foram corrigidos o mapeamento B3/BCB, o escape literal que invalidava o executor e a lógica permissiva de validação individual. RAW permanece imutável. A evidência está em `VALIDACAO_GATE_CONJUNTO_005N_5X5.json`. O workflow foi restaurado para execução manual. Próxima etapa: REC-001 integração cross-source controlada.
