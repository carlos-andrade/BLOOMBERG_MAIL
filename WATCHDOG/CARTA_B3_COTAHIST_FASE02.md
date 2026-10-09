---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "CARTA"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-CARTA-B3-COTAHIST-FASE02"
titulo: "Carta do adapter de qualidade histórica B3 COTAHIST"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL/INGESTAO-005"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "REC-001 B3; WATCHDOG/CARTA_ADAPTERS_FASE02.md"
escopo: "WATCHDOG/adapters/b3_cotahist_status.py"
objetivo: "Expor ao WATCHDOG o estado auditável da qualidade do dataset histórico B3 já adquirido, sem o apresentar como feed intradiário."
dependencias: "manifesto B3; validação de layout; validação da normalização; evidência REC-001"
---

# Carta — Adapter de qualidade histórica B3 COTAHIST

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** CARTA
> **Fase:** FASE-02-WATCHDOG
> **ID:** BLOOMBERG-MAIL-WATCHDOG-CARTA-B3-COTAHIST-FASE02
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** BLOOMBERG_MAIL/INGESTAO-005
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** REC-001 B3; WATCHDOG/CARTA_ADAPTERS_FASE02.md

## Contexto Histórico

O BLOOMBERG_MAIL já mantém COTAHIST RAW, manifesto, artefactos normalizados e relatórios de validação. A validação estrutural do RAW não elimina a divergência já registada na reconciliação entre snapshots dos repositórios.

## Estado

IMPLEMENTADO — autorização limitada a um adapter de observabilidade da qualidade histórica.

## Evidências

- Manifesto: `EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/b3_cotahist_normalizado.json`.
- Validação de layout: `EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/VALIDACAO_LAYOUT_COTAHIST_A2026.json`.
- Validação da normalização: `EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/VALIDACAO_NORMALIZACAO_B3_A2026.json`.
- Reconciliação cross-repo: `EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_CROSS_REPO_2026-10-08.json`.

## Validação

1. Exigir os quatro artefactos de evidência.
2. Confirmar que os hashes RAW dos relatórios de validação coincidem com o manifesto.
3. Emitir evento `HISTORICAL_DATASET_QUALITY` com identificador determinístico.
4. Se a reconciliação for `FAIL_CONTENT_DIVERGENCE`, emitir estado `DEGRADED` e severidade `HIGH`; nunca declarar a reconciliação aprovada.
5. Não transformar registos históricos em heartbeat de mercado, cotação em tempo real ou sinal de negociação.
6. Entrada ausente ou inconsistente bloqueia a emissão e retorna erro.

## Resultado

A carta autoriza a integração do estado de qualidade do COTAHIST histórico no contrato de eventos do WATCHDOG. Não autoriza declarar feed intradiário ativo.

## Próxima Ação

Implementar o layout, executar testes automatizados e confirmar o workflow. Só depois selecionar um fornecedor adequado a dados intradiários.
