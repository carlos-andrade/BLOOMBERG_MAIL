# BLOOMBERG_MAIL — Reconciliação TPMERC 021 — Evidência B3 BVBG.028

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Repositório: carlos-andrade/BLOOMBERG_MAIL
- Etapa: INGESTÃO 005N — Reconciliação determinística do COTAHIST A2026
- Data: 2026-10-07
- Natureza: evidência documental oficial B3
- RAW: imutável

## Novo achado

A B3 publicou o Comunicado Externo 016/2023-VNC em 28/02/2023 informando a criação do mercado para soluções de blocos.

O documento oficial declara que foi criado um novo domínio:
- 21 — BLOCK LOT
- campo: Market
- arquivo: BVBG.028.02 — Cadastro de Instrumentos

O mesmo comunicado informa que as especificações técnicas do BVBG.028.02 estão disponíveis na área de Market Data da B3.

Fonte oficial B3:
https://www.b3.com.br/data/files/14/50/F6/0B/93996810DE2C7168AC094EA8/CE%20016-2023-VNC%20Inclus%C3%A3o%20de%20novo%20dominio%20opcional%20no%20arquivo%20BVBG.028.pdf

## Evidência complementar

O FAQ oficial da B3 para Negociação de Grandes Lotes confirma que o código 21 — BLOCK LOT é um novo domínio em campo existente denominado Market ou ExternalMarketCode, destinado a identificar operações de grandes lotes em mercado separado dos mercados de lote padrão e fracionário.

Fonte oficial B3:
https://www.b3.com.br/data/files/7D/16/7C/CC/8938C8103152D4C8AC094EA8/FAQ%20-%20Negociacao%20Grandes%20Lotes.pdf

## Relação com COTAHIST A2026

O RAW COTAHIST A2026 contém 1.696 registros com TPMERC=021.

A nova documentação B3 confirma oficialmente que o domínio de mercado 21 existe e significa BLOCK LOT, mas o comunicado citado não declara que o campo posicional TPMERC do arquivo COTAHIST.AAAA.TXT é o mesmo campo de domínio Market do BVBG.028.02 nem que sua representação seja 021.

Portanto:
- Market=21 = BLOCK LOT: CONFIRMADO;
- existência do domínio desde 2023: CONFIRMADA;
- relação direta COTAHIST.TPMERC=021 = Market=21: AINDA NÃO DOCUMENTADA DE FORMA LITERAL;
- inferência no parser: PROIBIDA.

## Decisão

Não alterar ainda o conjunto autoritativo de TPMERC do COTAHIST.

O próximo gate é localizar a especificação técnica do COTAHIST ou catálogo de domínio que demonstre a correspondência entre TPMERC e o domínio 21 — BLOCK LOT, ou uma fonte oficial B3 que mostre o COTAHIST utilizando 021.

Até essa confirmação:
- validator B3: FAIL/BLOCKED;
- normalizador B3: BLOCKED;
- integração: BLOCKED;
- RAW: imutável.

## Governança

Nenhum valor foi inventado, convertido, interpolado ou economicamente ajustado.