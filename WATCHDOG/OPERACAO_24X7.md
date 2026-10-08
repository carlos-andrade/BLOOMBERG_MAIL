# WATCHDOG — Operação 24x7

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Módulo: WATCHDOG
- Data: 2026-10-08

## Pré-abertura
Validar relógio, calendário, fontes, última sessão, gaps e baseline.

## Pregão
Monitorar heartbeat, latência, gaps, divergência entre fontes, volume/atividade, volatilidade e eventos macro/notícias.

## Pós-fechamento
Validar completude, consolidar estatísticas, registrar incidentes e preparar replay.

## Madrugada/fim de semana
Continuar infraestrutura, cripto 24/7, notícias/macro, backups, integridade e recuperação.

## SLAs iniciais
Feed intraday crítico: heartbeat 15s / stale 60s.
Feed secundário: 30s / 120s.
Macro/notícias/Bloomberg Mail: 5min / 30min.
Infraestrutura: 30s / 120s.

Esses SLAs são parâmetros iniciais e serão calibrados por evidência real.

## Escalonamento
Evento → persistência além do SLA → aumento de severidade → cooldown/deduplicação → recuperação registrada.

## Regra de segurança
Alerta isolado nunca autoriza operação financeira.
