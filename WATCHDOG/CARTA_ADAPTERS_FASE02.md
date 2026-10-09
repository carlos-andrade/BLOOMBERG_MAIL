---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "CARTA"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-CARTA-ADAPTERS-FASE02"
titulo: "Carta de implementação dos adapters do WATCHDOG"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "WATCHDOG/ROADMAP.md; contrato WATCHDOG/schema/event.schema.json"
escopo: "WATCHDOG/adapters/"
objetivo: "Definir contrato verificável para replay e integração futura de feeds sem confundir teste com dados de mercado reais."
dependencias: "WATCHDOG/schema/event.schema.json; WATCHDOG/LAYOUT_ADAPTERS_FASE02.md"
---

# Carta — Adapters do WATCHDOG — FASE 02

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** CARTA
> **Fase:** FASE-02-WATCHDOG
> **ID:** BLOOMBERG-MAIL-WATCHDOG-CARTA-ADAPTERS-FASE02
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** WATCHDOG/ROADMAP.md; contrato WATCHDOG/schema/event.schema.json

## Contexto Histórico

A FASE 01 estabeleceu heartbeat, configuração, contrato de eventos e supervisor auxiliar. A FASE 02 inicia a separação entre ingestão de fontes e o contrato interno, sem afirmar que já existe feed intradiário B3 conectado.

## Estado

IMPLEMENTADO — especificação aprovada para a primeira entrega determinística de replay.

## Evidências

- Contrato canónico: `WATCHDOG/schema/event.schema.json`.
- Estado anterior: `WATCHDOG/ROADMAP.md`.
- A execução do replay deve preservar a origem e o timestamp do evento e nunca converter ausência em zero.

## Validação

1. Rejeitar JSONL malformado ou evento sem campos obrigatórios.
2. Validar severidade e estado contra o contrato.
3. Deduplicar pelo `event_id` sem sobrescrever eventos existentes.
4. Manter o processamento determinístico e sem rede.
5. Testes usam eventos explicitamente sintéticos; não podem ser apresentados como cotações reais.

## Resultado

A carta estabelece os critérios de aceitação antes do código. Ordem obrigatória: PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO.

## Próxima Ação

Implementar o layout e o replay determinístico, executar testes e ligar o resultado ao workflow de supervisão.
