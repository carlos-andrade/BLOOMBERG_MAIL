---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-B3-MAPEAMENTO-AUTORITATIVO-COTAHIST-V2-0-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — B3 COTAHIST — MAPEAMENTO AUTORITATIVO V2.0"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/MAPEAMENTO_AUTORITATIVO_COTAHIST_V2_0_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — B3 COTAHIST — MAPEAMENTO AUTORITATIVO V2.0

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

# BLOOMBERG_MAIL — B3 COTAHIST — MAPEAMENTO AUTORITATIVO V2.0

> Cabeçalho histórico: registro criado em 2026-10-07 para substituir o bloqueio anterior de mapeamento do COTAHIST por evidência documental oficial da B3. Fonte primária identificada e preservada como referência de governança; nenhum campo foi inferido.

## Fonte autoritativa

**B3 — Layout do Arquivo de Cotações Históricas — COTAHIST.AAAA.TXT**

Documento oficial B3:
https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf

Versão indicada no próprio documento:
- atualização: 05/10/2020
- versão: 2.0
- revisão: 02
- 245 bytes por registro

A página oficial de Cotações Históricas da B3 também informa que os arquivos históricos são disponibilizados em ZIP e que a interpretação do TXT deve utilizar o layout de arquivo fornecido pela B3.

## Estrutura oficial

Tipos de registro:
- "00" — Header
- "01" — Cotações históricas por papel-mercado
- "99" — Trailer

Tamanho de cada registro: **245 bytes**.

## Registro 00 — Header

| Campo | Tipo | Inicial | Final |
|---|---:|---:|---:|
| TIPO DE REGISTRO | N(02) | 01 | 02 |
| NOME DO ARQUIVO | X(13) | 03 | 15 |
| CÓDIGO DA ORIGEM | X(08) | 16 | 23 |
| DATA DA GERAÇÃO DO ARQUIVO | N(08) | 24 | 31 |
| RESERVA | X(214) | 32 | 245 |

## Registro 01 — Cotações históricas

| Campo | Tipo | Inicial | Final |
|---|---:|---:|---:|
| TIPREG | N(02) | 01 | 02 |
| DATA DO PREGÃO | N(08) | 03 | 10 |
| CODBDI | X(02) | 11 | 12 |
| CODNEG | X(12) | 13 | 24 |
| TPMERC | N(03) | 25 | 27 |
| NOMRES | X(12) | 28 | 39 |
| ESPECI | X(10) | 40 | 49 |
| PRAZOT | X(03) | 50 | 52 |
| MODREF | X(04) | 53 | 56 |
| PREABE | (11)V99 | 57 | 69 |
| PREMAX | (11)V99 | 70 | 82 |
| PREMIN | (11)V99 | 83 | 95 |
| PREMED | (11)V99 | 96 | 108 |
| PREULT | (11)V99 | 109 | 121 |
| PREOFC | (11)V99 | 122 | 134 |
| PREOFV | (11)V99 | 135 | 147 |
| TOTNEG | N(05) | 148 | 152 |
| QUATOT | N(18) | 153 | 170 |
| VOLTOT | (16)V99 | 171 | 188 |
| PREEXE | (11)V99 | 189 | 201 |
| INDOPC | N(01) | 202 | 202 |
| DATVEN | N(08) | 203 | 210 |
| FATCOT | N(07) | 211 | 217 |
| PTOEXE | (07)V06 | 218 | 230 |
| CODISI | X(12) | 231 | 242 |
| DISMES | 9(03) | 243 | 245 |

## Registro 99 — Trailer

| Campo | Tipo | Inicial | Final |
|---|---:|---:|---:|
| TIPO DE REGISTRO | N(02) | 01 | 02 |
| NOME DO ARQUIVO | X(13) | 03 | 15 |
| CÓDIGO DA ORIGEM | X(08) | 16 | 23 |
| DATA DA GERAÇÃO DO ARQUIVO | N(08) | 24 | 31 |
| TOTAL DE REGISTROS | N(11) | 32 | 42 |
| RESERVA | X(203) | 43 | 245 |

## Tabelas oficiais relevantes

### CODBDI

A documentação oficial fornece a tabela de códigos BDI. Exemplos documentados incluem:
- "02" LOTE PADRAO
- "12" FUNDOS IMOBILIARIOS
- "62" MERCADO A TERMO
- "71" MERCADO DE FUTURO
- "78" OPCOES DE VENDA
- "96" MERCADO FRACIONARIO
- "99" TOTAL GERAL

A tabela completa permanece conforme o documento oficial da B3.

### TPMERC

- "010" — VISTA
- "012" — EXERCÍCIO DE OPÇÕES DE COMPRA
- "013" — EXERCÍCIO DE OPÇÕES DE VENDA
- "017" — LEILÃO
- "020" — FRACIONÁRIO
- "030" — TERMO
- "050" — FUTURO COM RETENÇÃO DE GANHO
- "060" — FUTURO COM MOVIMENTAÇÃO CONTÍNUA
- "070" — OPÇÕES DE COMPRA
- "080" — OPÇÕES DE VENDA

### INDOPC

- "1" — US$ / correção pela taxa do dólar
- "2" — TJLP / correção pela TJLP
- "8" — IGP-M / opções protegidas
- "9" — URV / correção pela URV

## Regra de interpretação numérica

A documentação B3 define:
- N = numérico;
- X = alfanumérico;
- V = número com casas decimais;
- N(11)V99 = 11 posições antes da parte decimal e 2 casas decimais.

A própria B3 orienta considerar as duas últimas casas dos campos de preço como decimais.

**Não aplicar ajuste econômico, inflação, proventos ou qualquer transformação de preço.** A página oficial da B3 declara que as cotações históricas são fornecidas na moeda e forma de cotação da época, sem ajuste para inflação ou proventos.

## Decisão de governança

O bloqueio anterior PENDING_AUTHORITATIVE_FIELD_MAPPING pode ser removido para os campos acima porque existe documentação oficial B3 com posições, tipos e semântica.

Entretanto, antes de liberar o normalizador para produção, deve ser feita uma reconciliação determinística contra o RAW 2026:
1. validar comprimento de registros;
2. identificar exclusivamente registros 00/01/99;
3. validar header e trailer;
4. validar offsets contra amostras reais do RAW;
5. validar tipos e escalas;
6. validar datas;
7. validar campos de quantidade/volume;
8. validar TPMERC/CODBDI/INDOPC;
9. validar contagem do trailer;
10. somente então implementar o normalizador B3.

## Restrições

- RAW permanece imutável.
- Nenhum offset pode ser alterado por inferência.
- Nenhuma escala pode ser inferida quando contradita pela documentação.
- Nenhum campo ausente pode ser preenchido.
- Nenhum ajuste de preços será aplicado.
- O normalizador B3 será derivado exclusivamente do layout oficial e do RAW.


## Achado de reconciliação — COTAHIST A2026

A validação determinística do RAW A2026 (SHA-256 `c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f`) encontrou 1.696 registros com `TPMERC=021`. Esse código **não consta** na tabela TPMERC do documento B3 v2.0/revisão 02 usado como referência. O projeto não atribui significado ao código 021 por inferência. Até identificação de fonte oficial B3 que o reconcilie, o gate de validação permanece FAIL/BLOCKED e o normalizador B3 não pode ser promovido.


## Reconciliação controlada de TPMERC=021 — 2026-10-08

O código 021 não consta da tabela TPMERC do layout B3 v2.0/revisão 02 de 2020. A investigação foi ampliada para dados já validados no repositório carlos-andrade/B3.

No COTAHIST A2026 preservado e validado no repositório B3 foram encontrados 1.544 registros com TPMERC=021, em 255 CODNEG distintos e 179 pregões até 23/09/2026. As ocorrências observadas usam o padrão de código de negociação terminado em Q, com exemplos como EMET11Q, GGRC11Q, MCRE11Q, SBFG3Q, AXIA3Q, CPTS11Q, BBAS3Q e VALE3Q.

A documentação oficial atual da B3 para o Book of Block Trade (BBT) define simultaneamente:
- código de negociação: Final Q;
- código de mercado: 21 — BLOCK LOT.

A reconciliação entre o COTAHIST validado do repositório B3 e a especificação operacional oficial B3 estabelece uma correspondência operacional determinística forte entre TPMERC=021 e o mercado BLOCK LOT/BBT.

### Classificação

- significado operacional aceito: BLOCK LOT / BBT;
- base: dados COTAHIST validados no repositório B3 + documentação oficial B3 BBT;
- natureza: reconciliação controlada, não simples inclusão arbitrária de código;
- RAW BLOOMBERG_MAIL: imutável;
- ajuste econômico: proibido;
- interpolação: proibida.

### Limitação documental

Não foi localizada uma especificação B3 que contenha literalmente a frase COTAHIST.TPMERC=021 = Market 21. Portanto, o projeto registra esta ponte como reconciliação operacional validada, mantendo a proveniência e a distinção em relação à tabela textual do layout 2020.

Evidência detalhada: RECONCILIACAO_TPMERC021_COM_REPOSITORIO_B3_2026-10-08.md.
