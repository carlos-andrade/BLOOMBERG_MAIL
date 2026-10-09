---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO_TECNICO"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-ROADMAP-MD"
titulo: "WATCHDOG — Roadmap"
status: "EM_DESENVOLVIMENTO"
versao: "1.3"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "WATCHDOG/CARTA_B3_COTAHIST_FASE02.md; WATCHDOG/LAYOUT_B3_COTAHIST_FASE02.md; WATCHDOG/REC001_CAUSA_RAIZ_001.md"
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
> **Versão:** 1.3
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-09
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** WATCHDOG/CARTA_B3_COTAHIST_FASE02.md; WATCHDOG/LAYOUT_B3_COTAHIST_FASE02.md; WATCHDOG/REC001_CAUSA_RAIZ_001.md

## Contexto Histórico

A FASE 01 criou contrato, configuração, heartbeat, persistência incremental, Docker restart e supervisor auxiliar. A FASE 02 adicionou replay JSONL e um adapter de qualidade que lê evidências históricas COTAHIST existentes. A divergência de REC-001 continua explicitamente sinalizada; este adapter não representa feed intradiário.

## Estado

EM_DESENVOLVIMENTO — adapter histórico implementado e integrado nos testes automatizados. Promoção condicionada à execução do workflow e manutenção do estado real da reconciliação.

## Evidências

- Replay: `WATCHDOG/adapters/replay.py`.
- Adapter histórico B3: `WATCHDOG/adapters/b3_cotahist_status.py`.
- Carta: `WATCHDOG/CARTA_B3_COTAHIST_FASE02.md`.
- Layout: `WATCHDOG/LAYOUT_B3_COTAHIST_FASE02.md`.
- Testes: `WATCHDOG/tests/`.
- Supervisor: `.github/workflows/bloomberg-mail-watchdog-supervisor.yml`.

## Validação

O workflow compila os scripts, executa testes determinísticos, verifica o contrato e valida o adapter em modo `--validate-only` contra as evidências reais persistidas. A evidência cross-repo atual declara `FAIL_CONTENT_DIVERGENCE`; o adapter deve produzir `DEGRADED/HIGH`, nunca `UP`, enquanto essa evidência não for substituída por reconciliação aprovada.

## Resultado

### FASE 01 — Fundação
- [x] contrato de evento e configuração
- [x] heartbeat e persistência incremental
- [x] política Docker restart
- [x] supervisor GitHub Actions auxiliar

### FASE 02 — Adapters e dados históricos
- [x] carta/layout/replay JSONL determinístico
- [x] testes de validação, append e deduplicação
- [x] carta/layout do adapter de qualidade COTAHIST
- [x] classificação de divergência cross-repo como `DEGRADED/HIGH`
- [x] workflow executado com testes dos adapters e validação contra evidências B3 persistidas
- [ ] reconciliação REC-001 reavaliada após diagnóstico de causa raiz
- [ ] feed intradiário real, com fonte, licença, timestamps, heartbeat e freshness verificados
- [ ] mini-índice (WIN), mini-dólar (WDO), IBOV, VIX e Tesouro
- [ ] cripto 24/7

### FASE 03 — Fluxo
- [ ] VWAP/TWAP
- [ ] cumulative delta
- [ ] volume financeiro
- [ ] estrutura ICT como detector
- [ ] divergência preço/fluxo
- [ ] regime de volatilidade

### FASE 04 — Macro/notícias
- [ ] calendário económico
- [ ] PCE/Fed/BCB
- [ ] Bloomberg Mail
- [ ] classificação de impacto

### FASE 05 — Alertas
- [ ] webhook
- [ ] n8n/Mailgun
- [ ] deduplicação e cooldown

### FASE 06 — Qualidade
- [ ] reconciliação de fontes em execução periódica
- [ ] análise de gaps e falsos positivos
- [ ] replay com histórico real
- [ ] auditoria determinística

### FASE 07 — Produção
- [ ] VPS/cloud 24x7
- [ ] persistência externa
- [ ] watchdog do watchdog
- [ ] backup e recuperação de desastre

### FASE 08 — Decisão
- [ ] sinais para o ecossistema
- [ ] paper trading
- [ ] gate independente antes de qualquer execução real

## Próxima Ação

Confirmar o workflow com validação das evidências reais. Investigar REC-001 pela triagem em `WATCHDOG/REC001_CAUSA_RAIZ_001.md`; não promover reconciliação até uma comparação reproduzível com data de corte comum. Selecionar feed intradiário somente após esta etapa.
