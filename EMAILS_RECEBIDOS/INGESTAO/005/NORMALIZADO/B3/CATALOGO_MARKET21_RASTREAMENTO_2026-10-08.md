# BLOOMBERG_MAIL — B3 — CATALOGO MARKET 21 — RASTREAMENTO DE FONTE — 2026-10-08

> Cabeçalho histórico: investigação técnica de 2026-10-08 para resolver o bloqueio causado por 1.696 registros COTAHIST A2026 com TPMERC=021.

## Objetivo

Identificar a fonte técnica oficial que permita provar, sem inferência, a relação entre COTAHIST Registro 01 / TPMERC e o domínio B3 Market=21 — BLOCK LOT.

## Evidência oficial localizada

A página oficial B3 “Soluções de Blocos B3” informa:
- alteração de catálogo: BVBG.028;
- CE 016-2023-VNC, de 28/02/2023;
- ExternalCodeListiMercadoModuloArquivos - v1 17022023, formato sheet, 183 KB;
- ExternalCodeLists_iMERCADO - v1 17022023, formato sheet, 560 KB.

Fonte oficial:
https://clientes.b3.com.br/w/solucoes-de-blocos-b3

O CE 016/2023-VNC declara que o catálogo BVBG.028.02 — Cadastro de Instrumentos contém o novo domínio 21 — BLOCK LOT no campo Market.

Fonte oficial:
https://www.b3.com.br/data/files/14/50/F6/0B/93996810DE2C7168AC094EA8/CE%20016-2023-VNC%20Inclus%C3%A3o%20de%20novo%20dominio%20opcional%20no%20arquivo%20BVBG.028.pdf

## Resultado da tentativa de recuperação

A listagem pública B3 expõe nome, data, formato e tamanho dos materiais, mas a pesquisa pública não forneceu o URL direto do arquivo ExternalCodeListiMercadoModuloArquivos - v1 17022023.

Também não foi encontrada, em busca pública oficial B3, uma ocorrência textual que combine explicitamente TPMERC=021 com BLOCK LOT.

## Evidência do COTAHIST

O layout oficial COTAHIST v2.0/revisão 02 define TPMERC como o “CÓD. DO MERCADO EM QUE O PAPEL ESTÁ CADASTRADO”.

Fonte oficial:
https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf

O RAW A2026 contém 1.696 registros com TPMERC=021; essa contagem foi obtida pelo validador determinístico do projeto.

## Classificação da evidência

| Item | Estado |
|---|---|
| TPMERC é código de mercado no COTAHIST | CONFIRMADO |
| Market=21 significa BLOCK LOT na documentação B3 | CONFIRMADO |
| BVBG.028.02 contém o domínio Market=21 | CONFIRMADO |
| Material técnico do domínio foi identificado pelo nome oficial | CONFIRMADO |
| Conteúdo do material técnico recuperado | NÃO DISPONÍVEL NA PESQUISA PÚBLICA |
| COTAHIST TPMERC=021 = Market 21 BLOCK LOT em frase explícita B3 | NÃO LOCALIZADO |
| Alteração do validador para aceitar 021 | BLOQUEADA |

## Regra de governança

Não transformar uma correspondência numérica plausível em mapeamento autoritativo sem evidência documental direta. O FAIL atual do validador permanece válido até que a ponte documental seja obtida.

## Próximo alvo técnico

1. Recuperar o arquivo oficial ExternalCodeListiMercadoModuloArquivos - v1 17022023 por URL direta exposta pelo portal B3 ou por ferramenta autenticada, se necessária.
2. Inspecionar o domínio Market e procurar o código 21.
3. Procurar no catálogo qualquer referência a COTAHIST, Market Data, arquivos históricos ou TPMERC.
4. Reconciliar com exemplos reais de COTAHIST contendo 021.
5. Somente então atualizar o mapeamento, o validador e executar nova validação.

**Estado: BLOQUEIO MANTIDO DE FORMA DETERMINÍSTICA.**
