---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO_TECNICO"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-ROADMAP-MD"
titulo: "WATCHDOG — Roadmap"
status: "EM_DESENVOLVIMENTO"
versao: "1.1"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "WATCHDOG/CARTA_ADAPTERS_FASE02.md; WATCHDOG/LAYOUT_ADAPTERS_FASE02.md"
escopo: "WATCHDOG/ROADMAP.md"
objetivo: "Controlar a sequência de implementação e a evidência de cada fase do WATCHDOG."
dependencias: "WATCHDOG/schema/event.schema.json; governança documental"
---

# WATCHDOG — Roadmap

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO_TECNICO
> **Fase:** FASE-02-WATCHDOG
> **ID:** BLOOMBERG-MAIL-WATCHDOG-ROADMAP-MD
> **Status:** EM_DESENVOLVIMENTO
> **Versão:** 1.1
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-09
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** WATCHDOG/CARTA_ADAPTERS_FASE02.md; WATCHDOG/LAYOUT_ADAPTERS_FASE02.md

## Contexto Histórico

A FASE 01 criou contrato de eventos, configuração, heartbeat, persistência incremental, reinício Docker e supervisor auxiliar. Em 2026-10-09 iniciou-se a FASE 02 com carta, layout e replay determinístico. O replay é infraestrutura de validação; não equivale a feed intradiário real.

## Estado

EM_DESENVOLVIMENTO — infraestrutura de replay implementada; testes automatizados incorporados ao supervisor. Integrações de dados de mercado permanecem pendentes.

## Evidências

- Carta: `WATCHDOG/CARTA_ADAPTERS_FASE02.md`.
- Layout único: `WATCHDOG/LAYOUT_ADAPTERS_FASE02.md`.
- Implementação: `WATCHDOG/adapters/replay.py`.
- Testes: `WATCHDOG/tests/test_replay.py`.
- Workflow: `.github/workflows/bloomberg-mail-watchdog-supervisor.yml`.

## Validação

O workflow deve compilar os scripts Python, executar os testes de replay e verificar os enums do contrato. O sucesso do workflow será a evidência de execução; não declarar a FASE 02 concluída apenas por existir código.

## Resultado

### FASE 01 — Fundação
- [x] pasta WATCHDOG
- [x] contrato de evento
- [x] configuração base
- [x] heartbeat
- [x] persistência incremental
- [x] Docker restart policy
- [x] supervisor GitHub Actions

### FASE 02 — Mercado e adapters
- [x] carta e layout do adapter de replay
- [x] replay JSONL append-only com deduplicação por `event_id`
- [x] validação do contrato e rejeição de entradas inválidas
- [x] testes determinísticos no workflow
- [ ] B3 intraday — feed real validado
- [ ] mini-índice (WIN)
- [ ] mini-dólar (WDO)
- [ ] IBOV
- [ ] VIX
- [ ] Tesouro
- [ ] cripto 24/7

### FASE 03 — Fluxo
- [ ] VWAP/TWAP
- [ ] cumulative delta
- [ ] volume financeiro
- [ ] FVG/estrutura ICT como detector
- [ ] divergência preço/fluxo
- [ ] regime de volatilidade

### FASE 04 — Macro/notícias
- [ ] calendário econômico
- [ ] PCE/Fed/BCB
- [ ] Bloomberg Mail
- [ ] classificação de impacto

### FASE 05 — Alertas
- [ ] webhook
- [ ] n8n
- [ ] Mailgun
- [ ] deduplicação/cooldown

### FASE 06 — Qualidade
- [ ] replay com dados reais históricos
- [ ] gaps
- [ ] reconciliação entre fontes
- [ ] falso positivo
- [ ] auditoria determinística

### FASE 07 — Produção
- [ ] VPS/cloud 24x7
- [ ] persistência externa
- [ ] watchdog do watchdog
- [ ] backup/DR

### FASE 08 — Decisão
- [ ] sinais para ecossistema
- [ ] paper trading
- [ ] gate independente antes de qualquer execução real

## Próxima Ação

Executar e inspecionar o workflow. Se aprovado, escolher o primeiro feed real com fonte, limites, licença, timestamp e reconciliação documentados; não promover dados de teste a dados de mercado.
