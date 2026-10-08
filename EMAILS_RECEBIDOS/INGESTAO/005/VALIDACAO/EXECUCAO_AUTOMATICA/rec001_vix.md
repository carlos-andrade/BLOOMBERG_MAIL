---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-EXECUCAO-AUTOMATICA-REC001-VIX-MD"
titulo: "REC-001 VIX — Reconciliação independente"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/EXECUCAO_AUTOMATICA/rec001_vix.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# REC-001 VIX — Reconciliação independente

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

# REC-001 VIX — Reconciliação independente

{
  "dataset": "VIX",
  "result": "PASS",
  "endpoint": "https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv",
  "raw_sha256": "cfcb9dce25bbbbd83aedca9a1480468bb25db2e988b3e893a4eebabb1905e1ab",
  "endpoint_sha256": "cfcb9dce25bbbbd83aedca9a1480468bb25db2e988b3e893a4eebabb1905e1ab",
  "raw_records": 9288,
  "endpoint_records": 9288,
  "headers_equal": true,
  "semantic_records_equal": true,
  "raw_preserved": true,
  "promotion_impact": "VIX_REC_RECONCILED"
}
