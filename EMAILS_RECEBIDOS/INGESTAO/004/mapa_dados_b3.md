---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-004-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-004-MAPA-DADOS-B3-MD"
titulo: "BLOOMBERG_MAIL — INGESTÃO 004 — MAPA DE DADOS B3"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/004/mapa_dados_b3.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — INGESTÃO 004 — MAPA DE DADOS B3

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-004-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-004-MAPA-DADOS-B3-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-08
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


## Contexto Histórico

Documento histórico do projeto BLOOMBERG_MAIL integrado à governança documental central de carlos-andrade.

## Estado

IMPLEMENTADO — cabeçalho migrado para o padrão canônico.

## Evidências

Modelo canônico: Curioso-da-Internet-IA/CABEÇALHO/MODELO-PADRAO-CABECALHO.md.

## Validação

Cabeçalho, identificação documental e rastreabilidade foram normalizados.

## Resultado

O conteúdo original abaixo foi preservado.

## Próxima Ação

Atualizar versão, data e rastreabilidade em alterações relevantes.

---

# BLOOMBERG_MAIL — INGESTÃO 004 — MAPA DE DADOS B3

**Cabeçalho histórico**  
- Projeto: BLOOMBERG_MAIL
- Etapa: INGESTÃO 004
- Data: 2026-10-07
- Objetivo: transformar as hipóteses extraídas do e-mail em especificação de dados testável no mercado brasileiro.
- Regra: o mapa define dados necessários; não constitui sinal operacional nem recomendação.

## 1. Arquitetura mínima

| Camada | Variáveis | Frequência mínima | Fonte prioritária |
|---|---|---|---|
| Equity/index | IBOV, IBrX, preços, retorno, máximas/mínimas, breadth | diário; intraday quando disponível | B3 |
| Concentração | peso por ativo, HHI, top-5/top-10, contribuição | rebalanceamento + diário | B3 |
| Liquidez/volume | volume financeiro, quantidade, negócios, participação por ativo | diário; intraday para testes | B3 |
| Rates | DI, curva, NTN-B/NTN-F, preço/taxa, duration/DV01 quando calculável | diário | B3 + Tesouro |
| FX | BRL/USD, DOL/WDO, retorno e volatilidade | diário; intraday para testes | B3 + BCB |
| Volatilidade global | VIX | diário | Cboe |
| Oferta de equity | IPO, follow-on, primária/secundária, valor, data | evento + diário | CVM |
| Eventos | Copom, fiscal, macro, corporativos, mudanças de índice | evento | fontes oficiais |
| Proveniência | fonte, URL, timestamp, arquivo bruto, hash, transformação | por observação/lote | pipeline |

## 2. Variáveis derivadas obrigatórias

1. Breadth: avanço/queda e proporção de ativos acima de médias; não usar como sinal antes de teste.
2. Concentração: HHI, Top-5 e Top-10 por peso e por contribuição de retorno.
3. Divergência de liderança: retorno/contribuição de grandes pesos versus universo amplo.
4. Equity supply: valor de ofertas e intensidade relativa ao turnover do mercado.
5. Regime de juros: inclinação da curva, mudança de taxa, duration/DV01 e mark-to-market.
6. Regime cambial: retorno e volatilidade BRL/USD.
7. Regime de risco global: nível e variação do VIX.
8. Intermarket: estado conjunto EQUITY ↔ JUROS ↔ FX ↔ VOLATILIDADE ↔ LIQUIDEZ.

## 3. Granularidade

- Diário: base histórica inicial.
- Intraday: segunda camada, somente depois de fechar a especificação diária.
- Eventos: timestamp e janela de evento separados dos preços.
- Nunca misturar fechamento, intraday e evento sem declarar o alinhamento temporal.

## 4. Integridade

Cada lote deve registrar: source, retrieved_at, market_date, timezone, frequency, instrument_id, field, value, unit, raw_reference, transformation_version.

Regras mínimas:
- não preencher lacunas com valores inventados;
- não retroagir informação conhecida somente depois do pregão;
- separar dado observado de dado calculado;
- preservar versão da metodologia do índice;
- controlar corporate actions;
- controlar survivorship bias nos constituintes;
- manter timezone e calendário de pregão;
- registrar revisões de fonte.

## 5. Critério de passagem

A INGESTÃO 004 somente passa para a coleta histórica quando cada hipótese tiver variáveis, fontes, frequência, janela temporal e regra de alinhamento definidos.
