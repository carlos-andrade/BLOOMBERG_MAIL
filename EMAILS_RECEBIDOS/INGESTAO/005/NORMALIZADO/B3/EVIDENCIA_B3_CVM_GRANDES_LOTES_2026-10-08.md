# BLOOMBERG_MAIL — B3/CVM — GRANDES LOTES — EVIDÊNCIA REGULATÓRIA — 2026-10-08

> Cabeçalho histórico: pesquisa solicitada em 2026-10-08 a partir de fontes oficiais B3 e CVM para complementar a reconciliação de TPMERC=021 no COTAHIST A2026.

## 1. B3 — Soluções de Blocos

Fonte oficial:
https://clientes.b3.com.br/w/solucoes-de-blocos-b3

A página oficial informa que as soluções de grandes lotes são Midpoint Order Book, Book of Block Trade (BBT) e Request for Quote (RFQ). Também informa que a negociação ocorre em novos instrumentos e deve respeitar o lote mínimo estabelecido pela CVM para grandes lotes.

Nos detalhes técnicos, a página identifica alteração de catálogo BVBG.028.

Nos materiais de apoio, a B3 lista:
- CE 016-2023-VNC Inclusão de novo domínio opcional no arquivo BVBG.028 — 28/02/2023 — PDF — 108 KB;
- ExternalCodeListiMercadoModuloArquivos - v1 17022023 — 17/02/2023 — sheet — 183 KB;
- ExternalCodeLists_iMERCADO - v1 17022023 — 17/02/2023 — sheet — 560 KB;
- ExternalCodeLists_Clearing - v1 17022023 — 17/02/2023 — Excel — 3 MB.

A página também informa que as ofertas das novas soluções não são divulgadas no livro transparente/Market Data antes da execução e que os negócios são divulgados após a execução.

### Relevância

Esta fonte confirma a existência do catálogo técnico e o vínculo operacional entre as soluções de grandes lotes e a infraestrutura BVBG.028.

Ela, isoladamente, não prova que COTAHIST TPMERC=021 seja o mesmo domínio que Market=21.

## 2. CVM — metodologia de grandes lotes

Fonte oficial:
https://www.gov.br/cvm/pt-br/assuntos/noticias/2022/cvm-divulga-metodologia-para-definicao-do-tamanho-dos-grandes-lotes-minimos-art-95-ss-1o-da-resolucao-cvm-135

Publicação: 04/10/2022. Atualização: 30/01/2024.

A CVM informa que a Resolução CVM 135/2022 passou a permitir segmentos ou procedimentos específicos para operações com grandes lotes nos mercados de bolsa e balcão, condicionados a sistemas que privilegiem adequada formação de preços.

A CVM estabelece metodologia para definir os lotes mínimos, considerando:
- mediana do volume diário negociado no período-base;
- mínimo de 25% das sessões com negociação para elegibilidade.

A publicação apresenta oito faixas de liquidez e respectivos lotes mínimos, de R$ 8,5 milhões até R$ 500 mil.

A CVM informa ainda que divulgaria, inicialmente a cada quatro meses, por Ofício Circular da SMI, as ações e valores mobiliários elegíveis e os respectivos lotes mínimos.

## 3. Relação B3 ↔ CVM

As duas fontes documentam camadas diferentes:

| Camada | Fonte | Evidência |
|---|---|---|
| Regulatória | CVM | metodologia e limites mínimos para grandes lotes |
| Infraestrutura/mercado | B3 | soluções específicas de negociação de grandes lotes |
| Catálogo técnico | B3 | BVBG.028 e listas de códigos |
| COTAHIST | B3 | TPMERC é código do mercado cadastrado |
| Market=21 | B3 | BLOCK LOT, conforme documentação já registrada no projeto |
| TPMERC=021 = Market=21 | — | ainda sem prova textual direta |

## 4. Decisão para o projeto

A documentação da CVM reforça que “grandes lotes” é um conceito regulatório relacionado à infraestrutura criada pela B3, mas não deve ser usada para inferir o significado do campo TPMERC.

Portanto:
- RAW: IMUTÁVEL.
- Evidência CVM: REGISTRADA.
- Evidência B3: REGISTRADA.
- Validador TPMERC=021: NÃO ALTERAR.
- Normalizador B3: BLOQUEADO.
- Integração: BLOQUEADA.
- Próximo alvo: conteúdo efetivo do ExternalCodeListiMercadoModuloArquivos - v1 17022023 ou documento oficial equivalente que faça a ponte entre TPMERC e Market.

## 5. Fontes primárias

B3:
https://clientes.b3.com.br/w/solucoes-de-blocos-b3

CVM:
https://www.gov.br/cvm/pt-br/assuntos/noticias/2022/cvm-divulga-metodologia-para-definicao-do-tamanho-dos-grandes-lotes-minimos-art-95-ss-1o-da-resolucao-cvm-135
