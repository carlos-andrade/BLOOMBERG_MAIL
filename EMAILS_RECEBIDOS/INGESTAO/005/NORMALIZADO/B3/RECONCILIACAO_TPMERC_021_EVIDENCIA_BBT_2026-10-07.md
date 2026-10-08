---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-B3-RECONCILIACAO-TPMERC-021-EVIDENCIA-BBT-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — Reconciliação TPMERC 021 — Evidência B3 BBT"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/RECONCILIACAO_TPMERC_021_EVIDENCIA_BBT_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — Reconciliação TPMERC 021 — Evidência B3 BBT

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

# BLOOMBERG_MAIL — Reconciliação TPMERC 021 — Evidência B3 BBT

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Repositório: carlos-andrade/BLOOMBERG_MAIL
- Etapa: INGESTÃO 005N — Reconciliação determinística do COTAHIST A2026
- Data: 2026-10-07
- Natureza: evidência documental externa oficial B3
- RAW: imutável

## Objetivo

Reconciliar o valor observado TPMERC=021 no COTAHIST A2026 sem atribuir significado por inferência.

## Evidência primária B3 — Book of Block Trade (BBT)

A página oficial atual da B3 para o Book of Block Trade (BBT) informa explicitamente:
- produtos: ações, BDRs, FIIs e Units;
- código de negociação: sufixo Q;
- pós-negociação: divulgação completa e imediata do negócio em Market Data;
- Código de mercado: 21 — BLOCK LOT.

Fonte oficial B3:
https://www.b3.com.br/pt_br/solucoes/negociacao-de-grandes-lotes/book-of-block-trade-bbt/

## Evidência primária B3 — Manual de Procedimentos Operacionais

O Manual de Procedimentos Operacionais de Negociação da B3, versão de 01/07/2026, seção 8.3 — Book of Block Trade BBT, confirma que:
- o BBT constitui livro separado do livro central;
- possui código próprio de instrumento;
- os ativos BBT utilizam o ativo subjacente acrescido da letra Q no código de negociação.

Fonte oficial B3:
https://www.b3.com.br/data/files/6F/83/85/5C/C7D1F910ADC36BE9AC094EA8/B3%20Trading%20Procedures%20Manual.pdf

## Relação com o achado do COTAHIST A2026

O validador do projeto observou:
- TPMERC=021: 1.696 ocorrências;
- todos os valores desconhecidos observados foram 021;
- CODBDI em branco: 0;
- INDOPC inválido: 0;
- datas inválidas: 0;
- campos numéricos inválidos: 0.

A evidência B3 estabelece, de forma oficial e contemporânea, que o código de mercado 21 corresponde a BLOCK LOT e que os instrumentos BBT utilizam sufixo Q.

## Limite de inferência

Esta evidência é forte e diretamente relevante, porém não é, isoladamente, uma declaração da B3 de que o campo COTAHIST TPMERC=021 é a representação de três dígitos do código de mercado 21 — BLOCK LOT.

Portanto, neste estágio:
- significado oficial de código de mercado 21: CONFIRMADO = BLOCK LOT;
- sufixo Q para BBT: CONFIRMADO;
- associação direta COTAHIST.TPMERC=021 → BBT/BLOCK LOT: AINDA NÃO DECLARADA COMO AUTORITATIVA;
- inferência automática no parser: PROIBIDA.

## Decisão

O projeto não deve ainda alterar o conjunto autoritativo de TPMERC do COTAHIST nem liberar o normalizador B3 apenas com esta evidência.

O próximo gate é localizar uma fonte B3 que faça a ligação explícita entre o domínio do campo COTAHIST/MarketName e o código 21, ou uma especificação B3 do próprio COTAHIST/Market Data que documente 021 como BLOCK LOT.

Até essa ligação explícita:
- validator B3: FAIL/BLOCKED;
- normalizador B3: BLOCKED;
- integração: BLOCKED;
- RAW: imutável.

## Governança

Nenhum valor foi inventado, convertido, interpolado ou economicamente ajustado.

## Fontes oficiais

1. B3 — Book of Block Trade (BBT):
https://www.b3.com.br/pt_br/solucoes/negociacao-de-grandes-lotes/book-of-block-trade-bbt/

2. B3 — Trading Procedures Manual, versão 01/07/2026:
https://www.b3.com.br/data/files/6F/83/85/5C/C7D1F910ADC36BE9AC094EA8/B3%20Trading%20Procedures%20Manual.pdf
