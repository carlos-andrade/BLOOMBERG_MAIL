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
