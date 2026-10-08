# BLOOMBERG_MAIL — LAYOUT DA POLÍTICA INCREMENTAL DAS BASES — V1.0

> Cabeçalho histórico — 2026-10-08.
> Derivado da CARTA_POLITICA_INCREMENTAL_BASES_V1_0.

## Estrutura lógica

```
BASE
├── SNAPSHOT (referência histórica)
├── INCREMENTOS/
│   ├── período_001
│   ├── período_002
│   └── ...
├── MANIFESTOS/
│   └── manifesto_por_incremento
├── VALIDACAO/
└── RECONCILIACAO/
```

## Identidade mínima do incremento

```text
dataset_id
source
source_url
retrieval_timestamp_utc
reference_period
original_filename
sha256
size_bytes
raw_path
schema_version
parser_version
validation_status
reconciliation_status
```

## Regras

1. Incrementos são imutáveis.
2. Snapshots não substituem incrementos.
3. Incrementos não substituem snapshots.
4. A soma lógica dos incrementos deve permitir rastrear a evolução temporal da base.
5. Uma nova versão do mesmo período com SHA diferente gera uma nova representação, nunca uma sobrescrita.
6. A normalização é derivada do RAW e deve preservar a referência ao incremento de origem.
7. O histórico deve continuar auditável mesmo quando a fonte publicar arquivos consolidados.

## Convenções por fonte

- B3: incremento diário por pregão/arquivo disponível.
- CVM: atualização por novos eventos/registros ou nova versão oficial do recurso.
- BCB: novas observações por série e data.
- Tesouro: novos registros/períodos e novas versões oficiais do recurso.
- VIX: novo pregão/data.

## Reconstrução

A arquitetura deve permitir identificar:
- primeiro período armazenado;
- último período armazenado;
- lacunas;
- duplicidades;
- versões concorrentes;
- SHA de cada representação;
- validação de cada incremento.

Nenhum processo de reconstrução pode alterar os RAWs históricos.
