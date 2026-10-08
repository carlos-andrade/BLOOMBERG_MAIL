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
