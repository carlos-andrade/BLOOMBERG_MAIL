---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "CARTA"
fase: "FASE-03-FEED-INTRADAY"
id_documento: "BLOOMBERG-MAIL-CARTA-FEED-INTRADAY-FASE03"
titulo: "Carta de seleção e validação de feed intradiário"
status: "EM_ANALISE"
versao: "1.2"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "WATCHDOG/ROADMAP.md; pesquisa de fontes oficiais"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "REC001_B3_COTAHIST_INCREMENTAL_2026-10-09.json; fontes oficiais B3 e TradingView"
escopo: "Seleção de fonte para observabilidade intradiária, sem execução de ordens"
objetivo: "Selecionar uma fonte legítima, mensurável e auditável para dados intradiários, separando dados históricos, atrasados e em tempo real."
dependencias: "Reconciliação REC-001; contrato de eventos WATCHDOG; licenças e condições de uso da fonte"
---

# Carta — Seleção e validação de feed intradiário

> **Projeto:** BLOOMBERG_MAIL  
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL  
> **Tipo:** CARTA  
> **Fase:** FASE-03-FEED-INTRADAY  
> **ID:** BLOOMBERG-MAIL-CARTA-FEED-INTRADAY-FASE03  
> **Status:** EM_ANALISE  
> **Versão:** 1.2  
> **Criação:** 2026-10-09  
> **Atualização:** 2026-10-09  
> **Origem:** WATCHDOG/ROADMAP.md; pesquisa de fontes oficiais  
> **Autoridade:** GOVERNANÇA  
> **Rastreabilidade:** REC001_B3_COTAHIST_INCREMENTAL_2026-10-09.json; fontes oficiais B3 e TradingView

## Contexto Histórico

A reconciliação oficial do COTAHIST concluiu `PASS_INCREMENTAL_EXACT`: 9/9 pregões entre 2026-09-24 e 2026-10-06 convergentes. Isto valida a extensão histórica do período comparado, mas não transforma COTAHIST em feed intradiário.

A B3 descreve o Market Data como distribuição por UMDF, com dados em tempo real ou atraso de 15 minutos, profundidade L1 ou L2. O acesso direto requer conectividade e contratos; o acesso indireto é feito por distribuidores autorizados. A disponibilidade e o custo dependem do produto, licença e utilizador.

## Estado

EM_ANALISE — fase de seleção e validação de fonte. Nenhum fornecedor intradiário foi aprovado e nenhum código de ingestão está autorizado por esta Carta.

## Evidências

- Reconciliação incremental oficial: `EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_INCREMENTAL_2026-10-09.json`.
- Workflow de reconciliação: https://github.com/carlos-andrade/BLOOMBERG_MAIL/actions/runs/37918438688
- B3 — [Perguntas frequentes sobre Market Data](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/distribuidores/perguntas-frequentes/).
- B3 — [Plataformas de difusão](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/plataformas-de-difusao/).
- B3 — [Política comercial Market Data 2026 (PDF)](https://www.b3.com.br/data/files/EF/F6/93/D7/364599100A29E189AC094EA8/Market%20Data%20Commercial%20Policy%202026.pdf).
- TradingView — [Assinaturas adicionais de dados de mercado](https://br.tradingview.com/support/solutions/43000471705/).

## Validação

Nenhum fornecedor será selecionado apenas por exibir uma cotação num gráfico. Antes da integração, devem ser demonstrados:

1. Fonte e endpoint/documentação verificáveis.
2. Instrumentos cobertos: WIN, WDO, IBOV e outros ativos prioritários.
3. Semântica temporal explícita: tempo real, atraso conhecido ou histórico.
4. Timestamp de origem e regra de freshness.
5. Transporte e formato reproduzíveis (API, socket, exportação autorizada ou ficheiro).
6. Direitos de acesso, armazenamento, transformação e uso interno; não presumir direito de redistribuição.
7. Política de falha, heartbeat, reconexão, gaps, duplicados e relógio.
8. Custo total e requisitos de conta/licença documentados.
9. Replay e reconciliação independentes antes de qualquer uso operacional.
10. Sem geração automática de ordens nesta fase.

### Ordem de avaliação

1. Verificar primeiro as capacidades de exportação ou integração da plataforma de mercado já utilizada no ecossistema do utilizador. Não presumir que exista API pública nem que os dados possam ser redistribuídos.
2. Avaliar distribuidores licenciados pela B3 e condições comerciais oficiais, caso a fonte atual não permita uma integração autorizada.
3. Considerar fontes públicas atrasadas apenas para pesquisa, observabilidade ou comparação, nunca rotulando-as como tempo real.
4. Manter COTAHIST como referência histórica e ferramenta de reconciliação, não como substituto de cotações intradiárias.

### Bloqueios de promoção

- A fonte não está aprovada até haver prova documental dos itens acima.
- Dados atrasados não podem ser promovidos a `UP` como se fossem tempo real.
- Sem timestamp/freshness verificável, estado máximo permitido: `UNKNOWN` ou `STALE`.
- Não se autoriza sinal de negociação, paper trading automatizado ou execução real nesta Carta.

## Resultado

A Carta estabelece os critérios de seleção e impede a implementação prematura. O utilizador confirmou que o menu Arquivo → Exportar em Tempo Real está presente no Profit. Esta confirmação é apenas evidência declarativa de disponibilidade do menu; o ensaio funcional ainda não foi executado. A fonte permanece `PENDING_EVIDENCE` até que a matriz comparativa seja preenchida e revista.

## Evidência nova — 2026-10-09

- Procedimento guiado: `WATCHDOG/TESTE_RTD_DDE_PROFIT_001.md`.
- Registo estruturado inicial (estado `NOT_RUN`): `WATCHDOG/EVIDENCIAS/RTD_DDE_PROFIT_001.json`.
- Proveniência: confirmação do utilizador de que o menu existe; não houve acesso remoto/local do assistente à sessão Profit.
- Não há ainda evidência de exportação ativa, instrumentos, campos, timestamps, latência, reconexão ou licença de armazenamento.

## Próxima Ação

Executar localmente `WATCHDOG/TESTE_RTD_DDE_PROFIT_001.md` e atualizar `WATCHDOG/EVIDENCIAS/RTD_DDE_PROFIT_001.json` com observações reais. Confirmar licença de captura/armazenamento, cobertura, timestamps, freshness e recuperação antes de alterar a decisão da matriz. Só depois o Layout poderá autorizar código.

**Data da consulta das fontes:** 2026-10-09. As condições comerciais devem ser revalidadas no momento da contratação.
