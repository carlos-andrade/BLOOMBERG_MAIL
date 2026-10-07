# BLOOMBERG_MAIL — CARTA DE NORMALIZAÇÃO V1.0

**Data histórica:** 2026-10-07  
**Projeto:** BLOOMBERG_MAIL  
**Etapa:** INGESTÃO 005 → NORMALIZAÇÃO  
**Status:** CONTRATO OPERACIONAL APROVADO PARA IMPLEMENTAÇÃO

## 1. Objetivo
Transformar, de forma determinística e reproduzível, os artefatos promovidos em CAMADA_A em dados derivados canônicos, preservando integralmente a rastreabilidade até o RAW.

## 2. Hierarquia obrigatória
RAW imutável → CAMADA_A validada → NORMALIZADO derivado → validação → INTEGRAÇÃO.

NORMALIZADO nunca substitui RAW e nunca é fonte de verdade independente.

## 3. Regras
1. Cada saída deve declarar dataset, origem, SHA-256 do RAW, caminho do RAW, timestamp de processamento, período de referência, schema_version e parser_version.
2. A transformação deve ser determinística: mesma entrada + mesma versão do parser = mesma saída.
3. Não são permitidos valores inventados, interpolação, preenchimento silencioso, ajuste econômico, ajuste de preço, arredondamento não especificado ou geração de sinal operacional.
4. Datas devem ser convertidas apenas para representação canônica, sem alterar o significado temporal da fonte.
5. Unidades devem ser preservadas; conversões somente quando explicitamente declaradas no layout.
6. Registros duplicados não podem ser removidos silenciosamente. Devem ser detectados e reportados.
7. Falhas de schema, unidade, data, missingness ou proveniência bloqueiam a promoção.
8. Arquivos NORMALIZADO anteriores sem vínculo verificável com o RAW atual são LEGACY e não podem alimentar integração.

## 4. Chave de proveniência mínima
dataset_id + raw_sha256 + source_url + retrieval_timestamp_utc + reference_period + parser_version + schema_version.

## 5. Gate de promoção
A saída só pode receber NORMALIZED_VALIDATED após validação estrutural, semântica, de unicidade, datas, unidades, missingness e reconciliação contra o RAW.

## 6. Proibição operacional
Esta etapa não cria ranking, previsão, recomendação, entrada/saída, hedge ou qualquer sinal de negociação. Inteligência de mercado começa somente nas camadas posteriores governadas.

## 7. Regra de legado
O arquivo bcb_sgs_1178_ultimos_10.json existente nesta pasta é classificado como LEGACY_TECHNICAL_SAMPLE, pois seu período e valores não correspondem ao RAW atualmente promovido. Não deve ser usado pela integração.
