# BLOOMBERG_MAIL — INGESTÃO 004 — MAPA DE DADOS B3

> Cabeçalho histórico — 2026-10-07.

## Objetivo

Definir o painel mínimo para testar H1–H4: concentração/breadth; oferta de ações; lock-up; e regime fiscal-político-duração sobre juros, FX e equities.

## Camadas

- Equity: IBOV/IBrX, componentes, preços, retornos, pesos e contribuições.
- Breadth: altas, baixas, estáveis, máximos/mínimos e percentuais acima de médias.
- Concentração: Top-5, Top-10, HHI e número efetivo de componentes.
- Liquidez: negócios, quantidade, volume financeiro e preço médio.
- Futuros: IND/WIN, DOL/WDO, ajustes, volume e contratos em aberto quando disponíveis.
- Juros: DI, títulos públicos, yields/preços e duration/DV01 quando calculável.
- FX: BRL/USD.
- Volatilidade: VIX.
- Oferta de capital: IPO, follow-on e demais ofertas CVM.
- Eventos: macro, fiscal, política, corporate actions e vencimentos.

## Proveniência obrigatória

`source`, `source_url`, `retrieved_at_utc`, `reference_date`, `timezone`, `frequency`, `unit`, `instrument`, `field`, `raw_value`, `normalized_value`, `transformation`, `quality_status`.

O bruto nunca é substituído pelo normalizado.

## Regras

1. Missing = null, nunca zero.
2. Não interpolar gaps sem declarar o método.
3. Não misturar preços nominais, ajustados e retorno total sem identificação.
4. Não usar composição atual para reconstruir composição histórica.
5. Eventos devem ser alinhados por timestamp e fuso.
6. Intraday conserva timestamp e janela de agregação.
7. Toda derivação deve ser reproduzível.
8. Divergências de fontes ficam registradas.
9. Bloomberg gera hipóteses; não é validação independente.
10. Nenhuma variável vira sinal antes de teste estatístico e out-of-sample.

## Disponibilidade verificada

B3: histórico de cotações desde 1986, com preços, negócios, quantidade e volume; histórico de boletins e dados de derivativos/câmbio.

BCB: SGS com séries temporais e formatos estruturados.

Tesouro Direto: histórico de preços e taxas por ano.

CVM: dados abertos e consultas de ofertas públicas.

Cboe: histórico diário do VIX desde 1990.

## Limites

Cumulative Delta, VWAP/TWAP intraday e microestrutura exigem dados intraday/trades compatíveis; não devem ser inferidos do COTAHIST diário. Posição por investidor/alocação pode depender de datasets B3 específicos. Duration/DV01 só quando os dados do instrumento permitirem cálculo reproduzível.

## Painel mínimo

IBOV; componentes/pesos históricos; preço/retorno/volume/negócios; breadth; Top-5/Top-10/HHI; IND/WIN; DOL/WDO; DI; títulos públicos; BRL/USD; VIX; calendário macro; ofertas CVM.

## Passagem para INGESTÃO 005

Mapa versionado + fonte por variável + campos/unidades + cobertura das hipóteses + gaps documentados + aquisição histórica controlada pronta para iniciar.
