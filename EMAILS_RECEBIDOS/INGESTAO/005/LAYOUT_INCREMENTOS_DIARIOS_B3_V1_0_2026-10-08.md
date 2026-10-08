---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-LAYOUT-INCREMENTOS-DIARIOS-B3-V1-0-2026-10-08-MD"
titulo: "BLOOMBERG_MAIL — LAYOUT DE INCREMENTOS DIÁRIOS B3/COTAHIST — V1.0"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/LAYOUT_INCREMENTOS_DIARIOS_B3_V1_0_2026-10-08.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — LAYOUT DE INCREMENTOS DIÁRIOS B3/COTAHIST — V1.0

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
