---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-EXECUCAO-AUTOMATICA-AQUISICAO-TESOURO-DIRETO-005-MD"
titulo: "BLOOMBERG_MAIL — INGESTÃO 005 — Aquisição Tesouro Direto"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/EXECUCAO_AUTOMATICA/aquisicao_tesouro_direto_005.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — INGESTÃO 005 — Aquisição Tesouro Direto

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

# BLOOMBERG_MAIL — INGESTÃO 005 — Aquisição Tesouro Direto

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Ingestão: 005
- Fonte: Tesouro Direto / Tesouro Transparente

Resultado: PASS

{
  "dataset": "TESOURO_HISTORICO",
  "source": "Tesouro Direto/Tesouro Transparente",
  "endpoint": "https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/precotaxatesourodireto.csv",
  "observed_at_utc": "2026-10-07T14:39:34.553923+00:00",
  "raw_preserved": true,
  "result": "PASS",
  "endpoint_sha256": "8c0aa0c51b23d49843bf8c912adec1eb8fc959755f3a671e319c98a692b83d4e",
  "raw_sha256": "8c0aa0c51b23d49843bf8c912adec1eb8fc959755f3a671e319c98a692b83d4e",
  "validation": {
    "bytes": 14571074,
    "rows": 177086,
    "columns": 8,
    "header": [
      "Tipo Titulo",
      "Data Vencimento",
      "Data Base",
      "Taxa Compra Manha",
      "Taxa Venda Manha",
      "PU Compra Manha",
      "PU Venda Manha",
      "PU Base Manha"
    ],
    "first_data_base": "01/02/2005",
    "last_data_base": "31/12/2015",
    "missing_rows": 0,
    "duplicate_rows": 0
  },
  "promotion_impact": "TESOURO_ACQUIRED_RAW_VALIDATED"
}
