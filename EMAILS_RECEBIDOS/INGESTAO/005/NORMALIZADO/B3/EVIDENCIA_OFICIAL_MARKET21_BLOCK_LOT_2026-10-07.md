---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-B3-EVIDENCIA-OFICIAL-MARKET21-BLOCK-LOT-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — B3 COTAHIST — EVIDÊNCIA OFICIAL SOBRE MARKET 21 / BLOCK LOT"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/EVIDENCIA_OFICIAL_MARKET21_BLOCK_LOT_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — B3 COTAHIST — EVIDÊNCIA OFICIAL SOBRE MARKET 21 / BLOCK LOT

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-B3-EVIDENCIA-OFICIAL-MARKET21-BLOCK-LOT-2026-10-07-MD
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

# BLOOMBERG_MAIL — B3 COTAHIST — EVIDÊNCIA OFICIAL SOBRE MARKET 21 / BLOCK LOT

> Cabeçalho histórico: investigação complementar registrada em 2026-10-07 após a validação determinística do COTAHIST A2026 identificar 1.696 registros com TPMERC=021. Objetivo: procurar documentação oficial B3 que permita reconciliar o valor observado com o novo domínio de mercado 21. Nenhum significado é atribuído por inferência.

## 1. Evidência oficial B3 — BBT

A página oficial da B3 para o Book of Block Trade (BBT) informa explicitamente:

- Código de mercado: 21 — BLOCK LOT.
- O BBT é uma solução para negociação contínua de grandes lotes.
- Os produtos incluem ações, BDRs, FIIs e Units.
- O código de negociação dos instrumentos BBT possui final Q.

Fonte oficial B3:
https://b3.com.br/main.jsp?doui_processActionId=setLocaleProcessAction&locale=pt_BR&lumA=1&lumII=8AE490CA8B77BA2F018B86949C992323&lumPageId=8AE490CA8B77BA2F018B867AFE875882

## 2. Evidência oficial B3 — FAQ de Negociação de Grandes Lotes

A FAQ oficial da B3 afirma que o código de mercado 21 — BLOCK LOT é um novo domínio no campo existente Market ou ExternalMarketCode, destinado a identificar negócios de grandes lotes em mercado separado dos mercados padrão e fracionário.

A mesma documentação informa que os negócios de grandes lotes possuem estatísticas separadas do livro central e são identificados como pertencentes ao block trade market.

Fonte oficial B3:
https://b3.com.br/data/files/7D/F6/78/F3/DD9FC8103152D4C8AC094EA8/Block%20Trading%20Solutions.pdf

## 3. Evidência oficial B3 — material técnico das soluções de grandes lotes

Material técnico oficial da B3 apresenta, no contexto de BVBG.028, o campo Mercado com valor 21 (BLOCK LOT) para as soluções de grandes lotes.

Fonte oficial B3/Clientes B3:
https://clientes.b3.com.br/c/document_library/get_file?groupId=20119&uuid=88b5af46-5e95-a026-9d92-bb5e598086c0

## 4. O que foi confirmado

Foi confirmada documentalmente pela B3 a existência e a semântica do domínio:

21 → BLOCK LOT

Também foi confirmado que o domínio é utilizado no campo Market/ExternalMarketCode em documentação de mercado da B3.

## 5. O que ainda NÃO foi confirmado

A documentação oficial localizada nesta investigação não declara literalmente que:

COTAHIST.AAAA.TXT / Registro 01 / TPMERC = 021

seja a representação direta do domínio:

Market = 21 / BLOCK LOT.

O layout oficial COTAHIST v2.0/revisão 02, de 05/10/2020, continua apresentando a tabela TPMERC sem o código 021. A documentação posterior sobre grandes lotes confirma o domínio 21, mas não foi localizada, até este registro, uma especificação oficial B3 que faça a ponte textual direta entre TPMERC=021 e Market=21 no arquivo COTAHIST.

## 6. Consequência de governança

O projeto mantém a regra:

Evidência de Market 21 = BLOCK LOT não autoriza, isoladamente, alterar a tabela TPMERC do COTAHIST nem liberar o normalizador.

Portanto:

- RAW permanece imutável;
- TPMERC=021 permanece observado no RAW;
- o significado econômico não é inventado;
- o validador não deve ser alterado para aceitar 021 apenas com base nesta evidência indireta;
- o normalizador B3 continua bloqueado;
- a integração dos cinco datasets continua bloqueada.

## 7. Próximo alvo de pesquisa

A investigação deve continuar nos documentos técnicos oficiais B3 que possam fornecer a ponte direta, especialmente:

1. especificação técnica/catálogo de BVBG.028.02;
2. documentação atualizada do COTAHIST posterior à implantação das soluções de grandes lotes;
3. catálogos oficiais de domínios do Market Data B3;
4. Daily Market Bulletin ou documentação técnica que mostre explicitamente a correspondência entre o mercado 21 e o campo TPMERC do COTAHIST.

## 8. Estado

RECONCILIAÇÃO PARCIAL — EVIDÊNCIA OFICIAL DE MARKET 21 CONFIRMADA; MAPEAMENTO DIRETO COTAHIST/TPMERC AINDA PENDENTE.
