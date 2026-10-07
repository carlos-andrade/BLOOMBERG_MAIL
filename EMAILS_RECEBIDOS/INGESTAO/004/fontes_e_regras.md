# INGESTÃO 004 — FONTES E REGRAS DE COLETA

**Cabeçalho histórico**  
Projeto: BLOOMBERG_MAIL | Data: 2026-10-07 | Etapa: INGESTÃO 004

## Fontes prioritárias verificadas

### B3
A página oficial do Ibovespa descreve o índice, sua carteira teórica e os critérios de seleção/ponderação. A composição é reavaliada a cada quatro meses. Isso exige versionamento da carteira histórica para evitar survivorship bias.

### Tesouro Direto
O portal oficial mantém histórico anual de preços e taxas de títulos, incluindo NTN-B e NTN-F, com séries históricas desde 2002 na página consultada.

### CVM
A base oficial de Ofertas Públicas de Distribuição contém ofertas primárias/secundárias e registros associados; a base é atualizada diariamente e a página consultada registra atualização em 06/10/2026.

### Cboe
A Cboe disponibiliza histórico diário do VIX de 1990 até o presente, atualizado diariamente.

## Fontes ainda a fechar
- B3 intraday e detalhes de negócios: especificar endpoint/arquivo oficial antes da coleta.
- BCB PTAX/SGS: confirmar dataset/API oficial e convenção de timestamp.
- Eventos de lock-up: definir fonte primária e regra de interpretação.
- Calendário macro: selecionar exclusivamente fonte oficial por evento.

## Regra de evidência
Fonte descoberta não significa dado coletado. Antes de qualquer backtest, o pipeline deve registrar arquivo/endpoint, data de extração, hash, esquema e cobertura temporal.

## Próximo checkpoint
INGESTÃO 005: fechar a especificação de fontes/endpoints e executar uma coleta piloto pequena, com validação de esquema e cobertura, sem ainda produzir sinal de trading.
