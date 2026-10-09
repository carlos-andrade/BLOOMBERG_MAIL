---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-STATUS-POLITICA-INCREMENTAL-BASES-2026-10-08-MD"
titulo: "BLOOMBERG_MAIL — STATUS DA POLÍTICA INCREMENTAL — 2026-10-08"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/STATUS_POLITICA_INCREMENTAL_BASES_2026-10-08.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — STATUS DA POLÍTICA INCREMENTAL — 2026-10-08

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-STATUS-POLITICA-INCREMENTAL-BASES-2026-10-08-MD
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

# BLOOMBERG_MAIL — STATUS DA POLÍTICA INCREMENTAL — 2026-10-08

> Cabeçalho histórico — 2026-10-08.

## Estado

**APROVADO COMO REGRA PERMANENTE.**

## Cobertura

A regra foi aplicada conceitualmente a todas as cinco bases da INGESTÃO 005:

- B3_COTACOES;
- CVM_OFERTAS;
- BCB_SGS;
- TESOURO_HISTORICO;
- VIX.

## Implementação já existente

- B3 possui carta/layout específicos para incrementos diários.
- O manifesto 005 passa a declarar política incremental para todas as fontes.
- RAW permanece imutável.
- A normalização continua derivada do RAW.
- A reconciliação continua obrigatória quando houver segunda representação.
- O B3 continua sendo atualizado por incrementos COTAHIST validados.

## Próxima execução

Após a formalização da regra geral, o trabalho retorna ao ponto anterior:
**REC-001**, priorizando a materialização determinística da reconciliação B3/COTAHIST e, em seguida, os demais bloqueios.

## Regra de não-regressão

Nenhum novo pipeline poderá introduzir uma base somente como snapshot sem declarar:
- frequência de atualização;
- unidade do incremento;
- caminho de armazenamento;
- manifesto;
- validação;
- estratégia de reconciliação.
