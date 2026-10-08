# WATCHDOG — Deploy 24x7

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Módulo: WATCHDOG
- Data: 2026-10-08

## Produção
O runtime recomendado é VPS/cloud com Docker e política restart unless-stopped. GitHub Actions permanece como supervisor auxiliar e CI.

## Requisitos
Linux 64-bit, Docker/Compose, NTP, armazenamento persistente, acesso autorizado aos feeds e canal de alerta.

## Procedimento
1. Copiar a configuração de exemplo para configuração operacional protegida.
2. Definir endpoints por variáveis de ambiente.
3. Executar docker compose up -d.
4. Verificar docker compose ps.
5. Verificar WATCHDOG/runtime/events.jsonl.
6. Configurar rotação e backup.

## Segurança
Credenciais nunca entram no Git. Usar secrets do ambiente ou secret manager.
