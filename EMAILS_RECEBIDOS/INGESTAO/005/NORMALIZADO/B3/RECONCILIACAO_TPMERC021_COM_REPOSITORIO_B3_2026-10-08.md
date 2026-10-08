# BLOOMBERG_MAIL — RECONCILIAÇÃO TPMERC 021 — EVIDÊNCIA INTERNA DO REPOSITÓRIO B3 — 2026-10-08

> Cabeçalho histórico: documento criado em 2026-10-08 para resolver o bloqueio do COTAHIST A2026 usando dados já validados e preservados no repositório carlos-andrade/B3.

## 1. Fonte interna validada

O repositório B3 possui:
- RAW COTAHIST A2026: dados/cotahist/raw/anual/COTAHIST_A2026.ZIP;
- SHA-256 registrado: 4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768;
- Dataset NORMALIZED 2026 certificado;
- cadastro oficial BVBG.028.02 capturado em ativos/catalogo/raw/IN260922.zip;
- SHA-256 do BVBG: 4e29690d9ce9e226bb61da80a167c11c50f828565431351eaf1f8fbbdcfe0a49.

O documento do B3 que certifica o Dataset Oficial 2026 registra 2.919.760 registros e status DATASET_OFICIAL_VALIDADO.

## 2. Resultado determinístico encontrado no B3

A execução controlada:

B3 — Reconciliação COTAHIST TPMERC 021 x BVBG.028

Run #1:
- Run ID: 37763162650
- conclusão: success
- commit: ee16e08ff1138adecdab1c4e0555f143c545fd8d

Gerou:
dados/cotahist/quality/COTAHIST_A2026_TPMERC021_BVBG028_RECONCILIACAO_V1.json

Resultado:
- TPMERC=021: 1.544 registros;
- 255 códigos de negociação distintos;
- presença em 179 pregões;
- amostras observadas incluem EMET11Q, GGRC11Q, MCRE11Q, SBFG3Q, AXIA3Q, CPTS11Q, BBAS3Q, VALE3Q, BTLG11Q, entre outras;
- as ocorrências observadas no COTAHIST possuem o padrão de código de negociação terminado em Q;
- os exemplos possuem CODBDI=93.

O RAW do BLOOMBERG_MAIL A2026 apresenta 1.696 ocorrências de TPMERC=021. A diferença é temporal: o RAW do repositório B3 usado nessa reconciliação vai até 23/09/2026, enquanto o RAW BLOOMBERG_MAIL vai além dessa data.

## 3. Evidência oficial B3 que fecha o contexto

A página oficial B3 do Book of Block Trade informa simultaneamente:
- produtos: ações, BDRs, FIIs e Units;
- código de negociação: Final Q;
- código de mercado: 21 — BLOCK LOT.

Fonte:
https://b3.com.br/main.jsp?doui_processActionId=setLocaleProcessAction&locale=pt_BR&lumA=1&lumII=8AE490CA8B77BA2F018B86949C992323&lumPageId=8AE490CA8B77BA2F018B867AFE875882

## 4. Reconciliação

A combinação das evidências estabelece uma correspondência operacional forte:

COTAHIST TPMERC=021
→ códigos CODNEG terminados em Q
→ padrão oficial B3 de BBT: Final Q
→ BBT: Código de mercado 21 — BLOCK LOT

Isso resolve o significado operacional do código 021 para o gate de ingestão 005N.

### Limitação mantida

O documento não afirma que a B3 publicou literalmente a frase:
COTAHIST.TPMERC=021 = Market 21

A ponte é uma reconciliação determinística entre dados oficiais B3 já validados no repositório e documentação operacional oficial B3.

## 5. Decisão

Para o BLOOMBERG_MAIL:
- TPMERC=021 passa a ser aceito pelo validador 005N;
- significado operacional: BLOCK LOT / BBT;
- RAW permanece imutável;
- nenhuma transformação econômica é aplicada;
- nenhuma interpolação é aplicada;
- nenhum preço é ajustado;
- o próximo gate continua sendo a execução determinística do validador sobre o RAW BLOOMBERG_MAIL.

## 6. Fonte interna principal

carlos-andrade/B3/dados/cotahist/quality/COTAHIST_A2026_TPMERC021_BVBG028_RECONCILIACAO_V1.json
