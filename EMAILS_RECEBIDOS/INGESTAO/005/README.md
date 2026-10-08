# BLOOMBERG_MAIL — INGESTÃO 005 — AMOSTRA HISTÓRICA CONTROLADA

> Cabeçalho histórico — 2026-10-07.  
> Status: ESPECIFICAÇÃO DE AQUISIÇÃO — nenhum dado de mercado foi fabricado.

## Política incremental permanente

Todas as bases adquiridas pela INGESTÃO 005 devem receber **incrementos** para permanecerem atualizadas. Snapshots são referências e não substituem a sequência incremental.

- [Carta — Política Incremental das Bases](./CARTA_POLITICA_INCREMENTAL_BASES_V1_0_2026-10-08.md)
- [Layout — Política Incremental das Bases](./LAYOUT_POLITICA_INCREMENTAL_BASES_V1_0_2026-10-08.md)
- [Status — Política Incremental](./STATUS_POLITICA_INCREMENTAL_BASES_2026-10-08.md)
- [Carta — Alinhamento Incremental B3](./CARTA_ALINHAMENTO_INCREMENTAL_B3_V1_0_2026-10-08.md)

A regra abrange B3, CVM, BCB/SGS, Tesouro Direto e VIX. Cada incremento deve manter RAW, proveniência, SHA-256, validação e reconciliação quando aplicável.

## Objetivo

Iniciar a aquisição histórica controlada para testar H1–H4, preservando separação entre fonte, RAW e NORMALIZADO.

## Fontes confirmadas

| Dataset | Fonte | Papel |
|---|---|---|
| Cotações B3 | B3 — histórico de cotações | preço, negócios, quantidade, volume; histórico desde 1986 |
| SGS | Banco Central | séries macro/financeiras estruturadas |
| Tesouro | Tesouro Direto | preços/taxas de títulos públicos por ano |
| Ofertas | CVM — Ofertas Públicas de Distribuição | eventos de IPO/follow-on/ofertas |
| VIX | Cboe | regime de volatilidade global |

A página da B3 confirma que o histórico começa em 1986, que os valores são fornecidos na moeda/forma de cotação da época e sem ajuste para inflação ou proventos, e que o arquivo contém, entre outros campos, preço, quantidade de negócios e volume. citeturn0search13

O SGS possui interfaces JSON/CSV e metadados por série; a infraestrutura do BCB deve ser utilizada preservando código da série e unidade. citeturn0search12turn0search19

O Tesouro Direto disponibiliza históricos anuais de preços e taxas, atualmente cobrindo pelo menos 2002–2026 na interface consultada. citeturn0search0

A CVM mantém conjunto específico de Ofertas Públicas de Distribuição; os registros incluem ofertas primárias/secundárias e o conjunto é atualizado diariamente. citeturn0search4turn0search6

## Janela inicial

A aquisição inicial será dividida em duas camadas:

### Camada A — teste técnico
Período curto e recente, suficiente para verificar download, parsing, esquema, datas, unidades, duplicidades e reconciliação.

### Camada B — série histórica
Após a aprovação técnica da Camada A, ampliar progressivamente o período, sem assumir que todos os datasets têm a mesma data inicial.

## Estrutura obrigatória

`EMAILS_RECEBIDOS/INGESTAO/005/`

- `manifesto_aquisicao.json`
- `README.md`
- `RAW/`
- `NORMALIZADO/`
- `VALIDACAO/`

## Identidade de cada arquivo

Cada artefato deve registrar:

- source
- source_url
- retrieval_timestamp_utc
- reference_period
- original_filename
- checksum_sha256
- format
- encoding
- schema_version
- parser_version
- quality_status

## Regras de ingestão

1. RAW é imutável.
2. NORMALIZADO é derivado de RAW.
3. Nunca editar RAW para corrigir parsing.
4. Correções de interpretação devem alterar parser/schema, não o original.
5. Não preencher missing com zero.
6. Não ajustar preços B3 automaticamente.
7. Não misturar pregão, data de liquidação e data de referência.
8. Datas e horários devem preservar o timezone de origem.
9. Todo download deve produzir checksum.
10. Toda transformação deve ser reproduzível.
11. Nenhum resultado estatístico será calculado antes da validação estrutural.
12. Nenhum sinal operacional será criado nesta ingestão.

## Primeiros datasets

1. B3 Cotações Históricas — amostra recente + posteriormente série histórica.
2. CVM Ofertas Públicas — amostra e catálogo de campos.
3. BCB SGS — séries escolhidas para BRL/USD e juros/macro.
4. Tesouro Direto — amostra de séries de títulos públicos.
5. VIX — histórico diário.

## Dependências para H1–H4

- H1 depende principalmente de B3 + composição histórica.
- H2 depende de CVM + retornos/volume B3.
- H3 depende de CVM + dados corporativos e de mercado; lock-up exige identificação documental específica.
- H4 depende de BCB/Tesouro + B3 + VIX + calendário/eventos.

## Critério de aprovação

A Camada A só passa se:

- arquivos originais puderem ser identificados;
- checksum for calculado;
- encoding/formato forem registrados;
- datas forem parseadas sem ambiguidade;
- campos críticos tiverem unidade definida;
- duplicidades e missing forem mensurados;
- pelo menos uma reconciliação independente for executada;
- o manifesto apontar exatamente de onde cada tabela veio.

## Estado atual

**READY_FOR_ACQUISITION**

Não afirmar que a base histórica já foi baixada. A etapa seguinte é executar a aquisição real e armazenar os arquivos no repositório conforme o manifesto.
