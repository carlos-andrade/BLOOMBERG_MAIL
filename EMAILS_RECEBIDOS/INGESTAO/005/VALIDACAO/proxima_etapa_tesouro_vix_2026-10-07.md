# BLOOMBERG_MAIL — INGESTÃO 005 — PRÓXIMA ETAPA DE AQUISIÇÃO

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Ingestão: 005
- Etapa: aquisição controlada — Tesouro Histórico + VIX
- Data: 2026-10-07
- Regra: nenhuma fonte pendente pode ser promovida por inferência ou substituição silenciosa.

## 1. Tesouro Direto — fonte oficial
A página oficial de Histórico de Preços e Taxas disponibiliza históricos anuais de 2002 a 2026 e dados consolidados de preços/taxas. A fonte deve ser capturada preservando o arquivo original, nome, período, checksum e timestamp UTC.

Fonte oficial: https://www.tesourodireto.com.br/produtos/dados-sobre-titulos/historico-de-precos-e-taxas

Escopo inicial:
- históricos anuais disponíveis;
- preços e taxas de compra/venda quando presentes;
- identificação do título e vencimento;
- data de referência;
- preservação do arquivo original;
- checksum SHA-256;
- validação de estrutura, datas, unidades, duplicidades e missingness.

Observação: a página oficial informa que os históricos anuais estão disponíveis desde 2002. A aquisição deve capturar o arquivo efetivamente disponibilizado pelo portal, sem fabricar uma URL de download.

## 2. VIX — fonte oficial Cboe
A Cboe disponibiliza dados históricos diários de fechamento do VIX de 1990 até o presente, com atualização diária.

Fonte oficial: https://www.cboe.com/tradable_products/vix/vix_historical_data/

Escopo inicial:
- VIX diário;
- data de pregão;
- fechamento;
- preservação do arquivo original quando houver download;
- checksum SHA-256;
- validação de datas, duplicidades e missingness.

A página também distingue o histórico VIX 1990–2003. Não misturar séries/metodologias sem registrar explicitamente a natureza da série.

## 3. Gate de promoção
Nenhum dos dois datasets deve alterar layer_A_approved para true sozinho.

Promoção somente após:
1. RAW preservado;
2. checksum calculado;
3. validação estrutural PASS;
4. validação de datas PASS;
5. unidades/documentação PASS;
6. missingness report;
7. duplicidade report;
8. reconciliação independente quando aplicável;
9. manifesto atualizado;
10. evidência publicada no repositório.

## 4. Regra de segurança
- Não substituir RAW existente.
- Não aceitar SHA inesperado silenciosamente.
- Não transformar ausência em zero.
- Não interpolar dados sem método explícito.
- Não gerar sinal operacional nesta etapa.

## 5. Estado após INGESTÃO 005-B #11
- B3 COTAHIST: ACQUIRED / VALIDATED / RECONCILED
- CVM OFERTAS: ACQUIRED / VALIDATED
- BCB SGS: TECHNICAL SAMPLE
- Tesouro Histórico: PENDING_FILE_ACQUISITION
- VIX: PENDING_SOURCE_ACCESS
- Layer A: BLOCKED

## Referências externas verificadas em 2026-10-07
- Tesouro Direto: histórico oficial e séries anuais.
- Cboe: histórico diário oficial do VIX.
