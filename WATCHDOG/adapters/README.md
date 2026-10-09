---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO_TECNICO"
fase: "FASE-01-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-ADAPTERS-README-MD"
titulo: "Adapters"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "WATCHDOG/adapters/README.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# Adapters

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO_TECNICO
> **Fase:** FASE-01-WATCHDOG
> **ID:** BLOOMBERG-MAIL-WATCHDOG-ADAPTERS-README-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-08
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


## Contexto Histórico

Documento do WATCHDOG integrado à governança documental central.

## Estado

IMPLEMENTADO.

## Evidências

Modelo canônico de cabeçalho do projeto Curioso-da-Internet-IA.

## Validação

Cabeçalho e rastreabilidade aplicados.

## Resultado

Documento normalizado.

## Próxima Ação

Atualizar versão, data e rastreabilidade quando houver alteração relevante.

---

# Adapters

Adapters isolam cada fornecedor. Nenhum adapter pode alterar o contrato central. Cada adapter deve expor health, last_event, latency e quality.

Ordem planejada: B3 → IBOV → WIN/WDO → VIX → Tesouro → cripto → macro → Bloomberg Mail.