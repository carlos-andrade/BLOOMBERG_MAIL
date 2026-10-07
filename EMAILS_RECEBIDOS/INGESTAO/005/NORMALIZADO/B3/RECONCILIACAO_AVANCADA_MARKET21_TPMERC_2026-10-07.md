# BLOOMBERG_MAIL — B3 — RECONCILIAÇÃO AVANÇADA MARKET 21 E TPMERC — 2026-10-07

> Cabeçalho histórico: nova rodada de pesquisa oficial B3 realizada em 2026-10-07. A validação do COTAHIST A2026 encontrou 1.696 registros com TPMERC=021. Esta nota registra somente evidências oficiais e mantém separada a evidência direta da hipótese de correspondência.

## Evidências oficiais

1. O layout oficial COTAHIST v2.0/revisão 02 define TPMERC como “CÓD. DO MERCADO EM QUE O PAPEL ESTÁ CADASTRADO”.
Fonte:
https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf

2. O Comunicado Externo 016/2023-VNC cria, no BVBG.028.02 — Cadastro de Instrumentos, o domínio “21 — BLOCK LOT” no campo Market.
Fonte:
https://www.b3.com.br/data/files/14/50/F6/0B/93996810DE2C7168AC094EA8/CE%20016-2023-VNC%20Inclus%C3%A3o%20de%20novo%20dominio%20opcional%20no%20arquivo%20BVBG.028.pdf

3. O Ofício Circular 176/2023-PRE apresenta para Midpoint, BBT e RFQ o “Código de mercado: 21 — BLOCK LOT”.
Fonte:
https://www.b3.com.br/data/files/2C/50/FE/15/4778B810E97E07B8DC0D8AA8/OC%20176-2023%20PRE%20%20Lan%C3%A7amento%20das%20Solu%C3%A7%C3%B5es%20para%20Negocia%C3%A7%C3%A3o%20de%20Grandes%20Lotes%20%28PT%29.pdf

4. A página oficial atual do BBT mantém “Código de mercado: 21 — BLOCK LOT”.
Fonte:
https://b3.com.br/main.jsp?doui_processActionId=setLocaleProcessAction&locale=pt_BR&lumA=1&lumII=8AE490CA8B77BA2F018B86949C992323&lumPageId=8AE490CA8B77BA2F018B867AFE875882

5. A página oficial das Soluções de Blocos identifica BVBG.028 como catálogo alterado e lista o material “ExternalCodeListiMercadoModuloArquivos - v1 17022023”, datado de 17/02/2023.
Fonte:
https://clientes.b3.com.br/w/solucoes-de-blocos-b3

## Relevância para o COTAHIST A2026

O RAW A2026 contém 1.696 ocorrências de TPMERC=021. O layout COTAHIST estabelece que TPMERC é um código de mercado. A B3, posteriormente, criou oficialmente o código de mercado 21 — BLOCK LOT.

Isso torna a correspondência TPMERC=021 ↔ Market=21 tecnicamente plausível e muito mais forte que uma hipótese baseada apenas em fontes de terceiros.

## Limite probatório

Ainda não foi localizada documentação B3 que diga literalmente:

COTAHIST Registro 01 / TPMERC=021 = Market 21 / BLOCK LOT.

Portanto, esta nota NÃO autoriza alteração do validador.

## Decisão

- RAW: IMUTÁVEL.
- Evidência Market 21: CONFIRMADA.
- TPMERC como código de mercado: CONFIRMADO.
- TPMERC=021 no RAW: CONFIRMADO.
- Correspondência direta TPMERC=021 ↔ Market=21: PENDENTE.
- Validador B3: BLOQUEADO.
- Normalizador B3: BLOQUEADO.
- Integração: BLOQUEADA.

## Próximo alvo

Prioridade máxima: recuperar o catálogo técnico “ExternalCodeListiMercadoModuloArquivos - v1 17022023” e o catálogo BVBG.028.02 efetivamente referido pelo CE 016/2023, procurando a definição do domínio Market e qualquer ponte explícita com COTAHIST.

## Estado

**RECONCILIAÇÃO AVANÇADA — EVIDÊNCIA OFICIAL SUFICIENTE PARA FORMULAR HIPÓTESE FORTE, MAS NÃO PARA PROMOVER TPMERC=021 AINDA.**
