---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO_TECNICO"
fase: "FASE-01-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-README-MD"
titulo: "BLOOMBERG_MAIL — WATCHDOG"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "WATCHDOG/README.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — WATCHDOG

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO_TECNICO
> **Fase:** FASE-01-WATCHDOG
> **ID:** BLOOMBERG-MAIL-WATCHDOG-README-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-08
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


## Contexto Histórico

Este documento pertence ao projeto BLOOMBERG_MAIL e passa a obedecer ao padrão de cabeçalho canônico adotado na governança de carlos-andrade.

## Estado

IMPLEMENTADO — cabeçalho normalizado em 2026-10-08.

## Evidências

Modelo canônico: carlos-andrade/Curioso-da-Internet-IA/CABEÇALHO/MODELO-PADRAO-CABECALHO.md.

## Validação

Estrutura revisada para Front Matter YAML, identificação documental, contexto histórico, estado, evidências, validação, resultado e próxima ação.

## Resultado

Documento integrado à governança documental central.

## Próxima Ação

Manter o cabeçalho atualizado em toda alteração relevante.

---

# BLOOMBERG_MAIL — WATCHDOG

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Módulo: WATCHDOG
- Data de criação: 2026-10-08
- Repositório: carlos-andrade/BLOOMBERG_MAIL

## Objetivo
O WATCHDOG é o plano de controle operacional para vigiar o mercado 24x7. Ele detecta, registra e alerta sobre eventos de mercado, ausência/degradação de dados, divergências entre fontes e falhas de infraestrutura.

## Regra fundamental
24x7 significa serviço operacional continuamente. A análise de mercado respeita o calendário de cada praça; fora do pregão o watchdog continua ativo para fontes, notícias, cripto e infraestrutura.

## Arquitetura
COLLECTORS → NORMALIZER/QUALITY → DETECTORS → EVENT STORE → ALERT ENGINE → N8N/MAILGUN/FUTURO.

## Princípios
- Não executar ordens nesta primeira versão.
- Nunca mascarar ausência de dados como zero.
- Toda leitura preserva origem e timestamp.
- Toda falha gera evidência.
- Toda base recebe incrementos; não haverá sobrescrita destrutiva.
- Uma fonte indisponível não pode derrubar o watchdog inteiro.

## Limitação
GitHub Actions será supervisor auxiliar. Ele não é um servidor 24x7: schedules podem atrasar. Produção deverá rodar em VPS/cloud/container persistente com restart automático.

## Roadmap
FASE 01 Fundação; FASE 02 adapters de mercado; FASE 03 fluxo; FASE 04 macro/notícias; FASE 05 alertas; FASE 06 qualidade/replay; FASE 07 produção; FASE 08 integração com decisão.
