---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "LAYOUT"
fase: "FASE-03-FEED-INTRADAY"
id_documento: "BLOOMBERG-MAIL-LAYOUT-FEED-INTRADAY-FASE03"
titulo: "Layout único da matriz de avaliação do feed intradiário"
status: "EM_ANALISE"
versao: "1.3"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "WATCHDOG/CARTA_FEED_INTRADAY_FASE03.md"
autoridade_documental: "CARTA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "BLOOMBERG-MAIL-CARTA-FEED-INTRADAY-FASE03"
escopo: "Matriz de avaliação; sem código de ingestão"
objetivo: "Definir os campos obrigatórios para comparar fornecedores e bloquear qualquer integração sem evidência."
dependencias: "WATCHDOG/CARTA_FEED_INTRADAY_FASE03.md"
---

# Layout único — Matriz de avaliação do feed intradiário

> **Projeto:** BLOOMBERG_MAIL  
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL  
> **Tipo:** LAYOUT  
> **Fase:** FASE-03-FEED-INTRADAY  
> **ID:** BLOOMBERG-MAIL-LAYOUT-FEED-INTRADAY-FASE03  
> **Status:** EM_ANALISE  
> **Versão:** 1.3  
> **Criação:** 2026-10-09  
> **Atualização:** 2026-10-09  
> **Origem:** WATCHDOG/CARTA_FEED_INTRADAY_FASE03.md  
> **Autoridade:** CARTA  
> **Rastreabilidade:** BLOOMBERG-MAIL-CARTA-FEED-INTRADAY-FASE03

## Contexto Histórico

A FASE 02 validou o COTAHIST histórico até 2026-10-06, mas esse conjunto não é um feed intradiário. A Carta da FASE 03 exige que fonte, latência, licença, cobertura e integridade sejam demonstradas antes de qualquer código.

## Estado

EM_ANALISE — o layout define a matriz e os gates; não aprova fornecedores nem autoriza ingestão.

## Evidências

- Matriz inicial de fontes: `WATCHDOG/MATRIZ_FONTES_FEED_INTRADAY_2026-10-09.json` — todos os candidatos permanecem `PENDING_EVIDENCE`.
- Carta vinculante: `WATCHDOG/CARTA_FEED_INTRADAY_FASE03.md`.
- Evidência histórica: `EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_INCREMENTAL_2026-10-09.json`.
- Fontes oficiais e de plataforma enumeradas na Carta.

## Validação

### Esquema obrigatório por fonte

| Campo | Regra de validação |
|---|---|
| `provider_id` | Identificador estável e único |
| `provider_name` | Nome legal/comercial e URL oficial |
| `market` | Mercado e classe de ativos cobertos |
| `instruments` | Lista explícita, incluindo WIN/WDO se disponíveis |
| `timeliness` | `REAL_TIME`, `DELAYED_15M`, `DELAYED_OTHER` ou `HISTORICAL` |
| `source_timestamp` | Timestamp da origem com timezone ou regra documentada |
| `observed_at_utc` | Timestamp de receção do coletor |
| `freshness_sla_seconds` | Limite mensurável de frescura |
| `transport` | API/socket/exportação/ficheiro autorizado |
| `schema_documentation` | URL ou documento versionado |
| `access_requirements` | Conta, subscrição, chave e conectividade necessárias; nunca guardar segredos no repositório |
| `license_scope` | Armazenamento, transformação, uso interno e redistribuição, separadamente |
| `cost_model` | Gratuito/pago, taxas de bolsa, taxas da plataforma e condições |
| `failure_semantics` | Timeout, indisponibilidade, gaps, duplicados e reconexão |
| `evidence_path` | Ficheiro versionado com evidência de validação |
| `decision` | `APPROVED`, `REJECTED` ou `PENDING_EVIDENCE` |

### Gates de validação

1. **Gate legal:** termos/licença autorizam o uso pretendido.
2. **Gate de cobertura:** símbolos e sessões de negociação são demonstrados.
3. **Gate temporal:** freshness é medida com timestamps; atraso conhecido não é confundido com falha.
4. **Gate de integridade:** sequência, duplicados, gaps e relógio são testados.
5. **Gate de recuperação:** reconexão e replay não alteram o RAW histórico.
6. **Gate operacional:** heartbeat e estado `STALE`/`DOWN` funcionam sem criar dados artificiais.
7. **Gate independente:** evidência de origem e testes são revistos antes de integrar ao WATCHDOG.

### Regras de implementação

- Este Layout não autoriza código de ingestão enquanto a matriz não tiver pelo menos uma fonte com decisão fundamentada.
- RAW é imutável; correções são novas evidências versionadas.
- Não inferir preços ausentes, não interpolar silenciosamente e não misturar feeds com relógios incompatíveis.
- Não declarar `UP` se a freshness exceder o SLA.
- Não usar COTAHIST para heartbeat intradiário.
- Nenhum sinal ou ordem pode ser gerado por esta fase.

## Resultado

A matriz inicial de triagem foi gravada em `WATCHDOG/MATRIZ_FONTES_FEED_INTRADAY_2026-10-09.json`. Ela identifica quatro caminhos: Profit RTD/DDE, ProfitDLL, distribuidores licenciados B3 e acesso direto B3. O utilizador confirmou a presença do menu de exportação do Profit, mas o ensaio funcional permanece por executar. O procedimento `WATCHDOG/TESTE_RTD_DDE_PROFIT_001.md` e o registo `WATCHDOG/EVIDENCIAS/RTD_DDE_PROFIT_001.json` definem a captura controlada de evidências. Não existe fornecedor aprovado, pois cobertura, campos, timestamps, freshness, recuperação, licença e custo ainda exigem prova específica da conta e do contrato.

O código só é autorizado por atualização posterior da Carta e deste Layout.

## Próxima Ação

Executar `WATCHDOG/TESTE_RTD_DDE_PROFIT_001.md` no Profit instalado e preencher `WATCHDOG/EVIDENCIAS/RTD_DDE_PROFIT_001.json` apenas com resultados observados. Guardar evidência redigida de campos, timestamps, latência calculável e comportamento em desconexão; verificar separadamente direitos de captura e armazenamento. Não colocar credenciais no repositório. Só depois preencher a decisão e propor eventual `APPROVED`.
