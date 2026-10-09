---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "CARTA"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-CARTA-B3-COTAHIST-FASE02"
titulo: "Carta do adapter de qualidade histórica B3 COTAHIST"
status: "IMPLEMENTADO"
versao: "1.2"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL/INGESTAO-005"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "REC-001 B3; WATCHDOG/REC001_CAUSA_RAIZ_001.md; WATCHDOG/CARTA_ADAPTERS_FASE02.md"
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
> **Versão:** 1.1
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
- Reconciliação histórica original (imutável): `EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_CROSS_REPO_2026-10-08.json`.
- Diagnóstico operacional atual: `EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_DIAGNOSTICO_MULTICONJUNTO_2026-10-09.json`.
- Triagem/causa raiz: `WATCHDOG/REC001_CAUSA_RAIZ_001.md`.

## Validação

1. Exigir os quatro artefactos de evidência.
2. Confirmar que os hashes RAW dos relatórios de validação coincidem com o manifesto.
3. Emitir evento `HISTORICAL_DATASET_QUALITY` com identificador determinístico.
4. Quando existir o diagnóstico multiconjunto versionado, usá-lo como evidência operacional preferida e validar hash RAW, hash de referência B3, igualdade do período comum e zero datas divergentes. O REC-001 original permanece imutável e disponível para auditoria.
5. Se o diagnóstico mais recente confirmar `PASS_OVERLAP_EXACT`, emitir `UP/INFO` com qualidade `VALIDATED_HISTORICAL_OVERLAP`; registar no payload o resultado original e o caminho da evidência que o supersede.
6. Se houver divergência, ausência de evidência ou inconsistência de hashes/contagens, bloquear a promoção e emitir `DEGRADED/HIGH` ou erro de validação.
5. Não transformar registos históricos em heartbeat de mercado, cotação em tempo real ou sinal de negociação.
6. Entrada ausente ou inconsistente bloqueia a emissão e retorna erro.

## Resultado

A carta autoriza a integração do estado de qualidade do COTAHIST histórico no contrato de eventos do WATCHDOG. Não autoriza declarar feed intradiário ativo.

## Reconciliação incremental oficial — regra obrigatória

- A evidência multiconjunto de 2026-10-09 reconcilia somente o período comum até 2026-09-23; não aprova datas posteriores.
- Executar `scripts/rec001_b3_cotahist_incremental_v16.py` contra os snapshots mensais oficiais B3 (`COTAHIST_M{MMAAAA}.ZIP`) e ficheiros diários `COTAHIST_D{DDMMAAAA}.ZIP` para o mês em curso necessários ao período incremental.
- Comparar cada registo tipo 01 completo de 245 bytes por data, como multiconjunto, preservando multiplicidade e detetando datas ausentes de qualquer lado.
- A linha de base é 2026-09-23. O hash atual do endpoint oficial deve ser registado como observação nova; a diferença em relação ao hash histórico do manifesto não pode ser tratada automaticamente como falha nem silenciosamente substituir a referência histórica.
- Guardar resultado separado em `EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_INCREMENTAL_2026-10-09.json`. RAW, manifesto e REC-001 anteriores são imutáveis.
- Apenas `PASS_INCREMENTAL_EXACT` ou `PASS_INCREMENTAL_OVERLAP_ONLY` sem divergências podem ser encaminhados para revisão humana; a evidência não altera automaticamente a promoção do dataset nem ativa sinais.

## Próxima Ação

Confirmar execução do workflow incremental, analisar a evidência publicada e resolver qualquer divergência ou ausência de datas. Só depois avaliar a promoção. Selecionar separadamente um fornecedor de dados intradiários; COTAHIST não é feed em tempo real.
