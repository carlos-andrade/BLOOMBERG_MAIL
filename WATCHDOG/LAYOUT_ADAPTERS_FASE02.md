---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "LAYOUT"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-LAYOUT-ADAPTERS-FASE02"
titulo: "Layout único dos adapters do WATCHDOG"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "WATCHDOG/CARTA_ADAPTERS_FASE02.md"
autoridade_documental: "CARTA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "BLOOMBERG-MAIL-WATCHDOG-CARTA-ADAPTERS-FASE02"
escopo: "WATCHDOG/adapters/replay.py; WATCHDOG/tests/"
objetivo: "Definir a única estrutura técnica aprovada para replay de eventos Watchdog em JSONL."
dependencias: "WATCHDOG/CARTA_ADAPTERS_FASE02.md; WATCHDOG/schema/event.schema.json"
---

# Layout único — Adapters do WATCHDOG — FASE 02

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** LAYOUT
> **Fase:** FASE-02-WATCHDOG
> **ID:** BLOOMBERG-MAIL-WATCHDOG-LAYOUT-ADAPTERS-FASE02
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** WATCHDOG/CARTA_ADAPTERS_FASE02.md
> **Autoridade:** CARTA
> **Rastreabilidade:** BLOOMBERG-MAIL-WATCHDOG-CARTA-ADAPTERS-FASE02

## Contexto Histórico

Este layout materializa a carta da FASE 02. É limitado a replay e validação do contrato; não é um conector de cotações em tempo real.

## Estado

IMPLEMENTADO — layout para primeira versão determinística.

## Evidências

Carta autorizadora: `WATCHDOG/CARTA_ADAPTERS_FASE02.md`.

## Validação

- CLI: `python WATCHDOG/adapters/replay.py --input <ficheiro.jsonl> [--output <eventos.jsonl>]`
- O modo de validação não escreve no destino.
- O modo de ingestão acrescenta eventos, nunca trunca o destino.
- Eventos duplicados por `event_id` são ignorados.
- Entrada malformada ou contrato inválido causa código de saída diferente de zero.
- Eventos sintéticos de teste permanecem identificados como sintéticos.

## Resultado

Layout técnico definido para implementação de replay auditável.

## Próxima Ação

Implementar o código e os testes sem introduzir dependências externas.
