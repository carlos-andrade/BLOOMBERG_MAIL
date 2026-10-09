---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-LAYOUT-NORMALIZACAO-V1-0-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — LAYOUT DE NORMALIZAÇÃO V1.0"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/LAYOUT_NORMALIZACAO_V1_0_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — LAYOUT DE NORMALIZAÇÃO V1.0

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-LAYOUT-NORMALIZACAO-V1-0-2026-10-07-MD
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

# BLOOMBERG_MAIL — LAYOUT DE NORMALIZAÇÃO V1.0

**Data histórica:** 2026-10-07  
**Carta-fonte:** CARTA_NORMALIZACAO_V1_0_2026-10-07.md

## Registro canônico comum

| Campo | Obrigatório | Regra |
|---|---|---|
| dataset_id | sim | Identificador estável do dataset |
| source | sim | Fonte oficial declarada na aquisição |
| source_url | sim | Endpoint/arquivo oficial |
| raw_path | sim | Caminho do RAW imutável |
| raw_sha256 | sim | SHA-256 exato do RAW |
| retrieval_timestamp_utc | sim | Timestamp da aquisição |
| reference_period | sim | Período efetivamente coberto |
| processed_at_utc | sim | Momento da normalização |
| schema_version | sim | Versão deste layout |
| parser_version | sim | Versão do transformador |
| quality_status | sim | Estado da validação |
| record_count | sim | Quantidade de registros produzidos |
| duplicate_count | sim | Duplicidades detectadas |
| missing_count | sim | Ausências detectadas segundo o schema |

## Registros de domínio
Cada dataset terá seus campos específicos definidos em manifesto próprio. A normalização não poderá apagar campos da fonte sem declaração explícita de mapeamento.

## Estados
NORMALIZED_DERIVED → processamento concluído.  
NORMALIZED_VALIDATED → processamento + validação + reconciliação concluídos.  
BLOCKED → qualquer falha de contrato.

## Integridade
O manifesto deve registrar SHA-256 de cada saída normalizada e a relação inequívoca com o SHA-256 do RAW.
