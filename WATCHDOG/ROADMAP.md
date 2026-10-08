# WATCHDOG — Roadmap

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Módulo: WATCHDOG
- Data: 2026-10-08

### FASE 01 — Fundação
- [x] pasta WATCHDOG
- [x] contrato de evento
- [x] configuração base
- [x] heartbeat
- [x] persistência incremental
- [x] Docker restart policy
- [x] supervisor GitHub Actions

### FASE 02 — Mercado
- [ ] B3 intraday
- [ ] mini-índice
- [ ] mini-dólar
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
- [ ] replay
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
