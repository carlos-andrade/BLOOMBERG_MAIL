---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-PLANO-VALIDACAO-005-MD"
titulo: "INGESTÃO 005 — PLANO DE VALIDAÇÃO"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/plano_validacao_005.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# INGESTÃO 005 — PLANO DE VALIDAÇÃO

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-PLANO-VALIDACAO-005-MD
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

# INGESTÃO 005 — PLANO DE VALIDAÇÃO

> Histórico: 2026-10-07 | BLOOMBERG_MAIL | INGESTÃO 005

## Estado após 005-C
B3, CVM, BCB, Tesouro e VIX possuem material RAW no repositório. A execução 005-C foi concluída com sucesso para Tesouro e VIX.

## Próxima validação
1. B3 COTAHIST: ZIP, TXT, layout, datas, registros e campos numéricos.
2. CVM ofertas: ZIP, arquivos internos, cabeçalhos, datas, duplicidades e tipos.
3. BCB SGS 1178: JSON, datas, valores e consistência da amostra.
4. Tesouro: CSV, encoding, cabeçalho, datas, títulos, preços/taxas e missingness.
5. VIX: CSV, DATE/OHLC, ordenação temporal, duplicidades e valores numéricos.
6. Consolidar checksums e resultados em relatório auditável.
7. Atualizar manifesto somente com estados efetivamente comprovados.

## Proibição
A validação não autoriza, por si só, sinal operacional. Após o gate, a promoção será RAW -> NORMALIZADO -> TESTE.
