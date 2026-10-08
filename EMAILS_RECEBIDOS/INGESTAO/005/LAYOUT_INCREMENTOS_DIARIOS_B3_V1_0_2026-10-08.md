# BLOOMBERG_MAIL — LAYOUT DE INCREMENTOS DIÁRIOS B3/COTAHIST — V1.0

> Cabeçalho histórico — 2026-10-08.
> Finalidade: definir a estrutura física e a identidade dos incrementos diários B3.
> Regra: este layout deriva da CARTA DE ALINHAMENTO INCREMENTAL COM B3 V1.0.

## Estrutura

```
EMAILS_RECEBIDOS/
└── INGESTAO/
    └── 005/
        └── RAW/
            └── B3/
                └── COTAHIST/
                    └── 2026/
                        ├── DIARIO/
                        │   ├── COTAHIST_A2026_<DATA>.ZIP
                        │   └── ...
                        └── SNAPSHOTS/
                            └── COTAHIST_A2026.ZIP
```

## Manifesto por incremento

Cada incremento terá manifesto associado contendo:

- dataset_id;
- source;
- source_url;
- retrieval_timestamp_utc;
- reference_period;
- trading_date_start;
- trading_date_end;
- original_filename;
- sha256;
- size_bytes;
- raw_path;
- validation_status;
- reconciliation_status;
- corresponding_b3_path;
- corresponding_b3_sha256, quando disponível.

## Regra de imutabilidade

Um arquivo diário já persistido não pode ser substituído silenciosamente.

Se a mesma data produzir novamente um arquivo com SHA diferente:

1. preservar ambos;
2. registrar os dois SHAs;
3. marcar a ocorrência para reconciliação;
4. não escolher automaticamente uma versão.

## Relação com snapshot anual

O snapshot anual permanece armazenado separadamente.

Os incrementos posteriores não serão incorporados destrutivamente ao snapshot.

A consolidação será uma camada derivada, nunca substituto do RAW.

## Chave operacional

Para COTAHIST, a reconciliação deverá utilizar:

- data do pregão;
- CODBDI;
- CODNEG;
- TPMERC;

e comparar os campos COTAHIST preservados no formato de origem.

Quando necessário, a comparação física poderá ser byte a byte para arquivos equivalentes.

## Estado

Este layout está pronto para implementação do armazenamento incremental. A implementação deverá criar os diretórios e manifestos somente quando houver aquisições reais.
