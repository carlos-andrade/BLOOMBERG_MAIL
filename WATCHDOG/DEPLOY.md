---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO_TECNICO"
fase: "FASE-01-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-DEPLOY-MD"
titulo: "WATCHDOG — Deploy 24x7"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "WATCHDOG/DEPLOY.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# WATCHDOG — Deploy 24x7

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO_TECNICO
> **Fase:** FASE-01-WATCHDOG
> **ID:** BLOOMBERG-MAIL-WATCHDOG-DEPLOY-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-08
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


## Contexto Histórico

Documento do WATCHDOG integrado à governança documental central de carlos-andrade.

## Estado

IMPLEMENTADO.

## Evidências

Modelo canônico de cabeçalho do projeto Curioso-da-Internet-IA.

## Validação

Front Matter YAML e seções de rastreabilidade aplicados.

## Resultado

Documento normalizado.

## Próxima Ação

Atualizar versão, data e rastreabilidade em alterações relevantes.

---

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
