---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO_TECNICO"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-ROADMAP-MD"
titulo: "WATCHDOG — Roadmap"
status: "EM_DESENVOLVIMENTO"
versao: "1.7"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "WATCHDOG/CARTA_B3_COTAHIST_FASE02.md; WATCHDOG/LAYOUT_B3_COTAHIST_FASE02.md; WATCHDOG/CARTA_FEED_INTRADAY_FASE03.md; WATCHDOG/LAYOUT_FEED_INTRADAY_FASE03.md; REC001_B3_COTAHIST_INCREMENTAL_2026-10-09.json"
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
> **Versão:** 1.4
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-09
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** WATCHDOG/CARTA_B3_COTAHIST_FASE02.md; WATCHDOG/LAYOUT_B3_COTAHIST_FASE02.md; WATCHDOG/REC001_CAUSA_RAIZ_001.md

## Contexto Histórico

A FASE 01 criou contrato, configuração, heartbeat, persistência incremental, Docker restart e supervisor auxiliar. A FASE 02 adicionou replay JSONL e um adapter de qualidade que lê evidências históricas COTAHIST existentes. A divergência de REC-001 continua explicitamente sinalizada; este adapter não representa feed intradiário.

## Estado

EM_DESENVOLVIMENTO — diagnóstico independente aprovado para o período comum; adapter atualizado para usar evidência multiconjunto verificada e preservar o resultado histórico original.

## Evidências

- Replay: `WATCHDOG/adapters/replay.py`.
- Adapter histórico B3: `WATCHDOG/adapters/b3_cotahist_status.py`.
- Carta: `WATCHDOG/CARTA_B3_COTAHIST_FASE02.md`.
- Layout: `WATCHDOG/LAYOUT_B3_COTAHIST_FASE02.md`.
- Testes: `WATCHDOG/tests/`.
- Supervisor: `.github/workflows/bloomberg-mail-watchdog-supervisor.yml`.

## Validação

O workflow compila os scripts, executa testes determinísticos, verifica o contrato e valida o adapter em modo `--validate-only` contra as evidências reais persistidas. A evidência histórica original declara `FAIL_CONTENT_DIVERGENCE`, mas a reconciliação independente atual confirmou `PASS_OVERLAP_EXACT`: 182/182 pregões convergentes, zero divergentes, hashes dos snapshots conferidos. O adapter só promove para `UP/INFO` quando valida esses invariantes e mantém rastreado o resultado histórico anterior.

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
- [x] diagnóstico REC-001 por multiconjunto completo e por pregão: 182/182 convergentes\n- [x] adapter WATCHDOG atualizado para usar diagnóstico verificado sem sobrescrever a evidência original\n- [x] reconciliar pregões de 20260924 a 20261006 contra snapshots oficiais B3 mensais/diários: 9/9 convergentes, zero divergências; evidência versionada e RAW/manifesto históricos preservados
- [ ] feed intradiário real, com fonte, licença, timestamps, heartbeat e freshness verificados
- [ ] mini-índice (WIN), mini-dólar (WDO), IBOV, VIX e Tesouro
- [ ] cripto 24/7

### FASE 03 — Fonte intradiária e fluxo
- [x] carta de seleção de feed intradiário com gates legais, temporais, de cobertura e integridade
- [x] layout único da matriz comparativa; código de ingestão continua bloqueado até fonte aprovada
- [ ] preencher matriz de fornecedores e validar plataforma existente, fonte autorizada, custo, licença e freshness
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

Submeter `PASS_INCREMENTAL_EXACT` a revisão de promoção independente, mantendo a Layer A bloqueada até ao gate de aprovação definido no manifesto. Preservar a evidência original REC-001, o diagnóstico de sobreposição e a evidência incremental como artefactos distintos. A Carta e o Layout da FASE 03 já estão versionados; próximo passo é preencher a matriz de fontes e validar acesso, licença, cobertura, custos e freshness antes de autorizar código. COTAHIST permanece dado histórico, não tempo real.
