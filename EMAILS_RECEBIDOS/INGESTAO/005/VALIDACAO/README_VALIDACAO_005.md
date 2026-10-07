# INGESTÃO 005 — VALIDAÇÃO CONTROLADA

> Histórico: 2026-10-07 | BLOOMBERG_MAIL | INGESTÃO 005

## Objetivo
Validar independentemente os RAW adquiridos antes de qualquer promoção para NORMALIZADO ou aprovação da Layer A.

## Gate obrigatório
- integridade SHA-256;
- estrutura de arquivo/arquivo compactado;
- schema/cabeçalho;
- datas e período;
- unidades e tipos;
- duplicidades;
- missingness;
- reconciliação independente quando aplicável;
- evidência gravada no repositório.

## Regra
RAW é imutável. Nenhum valor pode ser inventado, interpolado silenciosamente ou ajustado automaticamente.

## Fontes
O catálogo canônico das fontes fica em FONTES/. Evidências específicas da aquisição/validação ficam em EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/.
