# BLOOMBERG_MAIL — INGESTÃO 005N — CONTROLE DE FALHA DA VALIDAÇÃO CONJUNTA

**Cabeçalho histórico — 2026-10-07**

## Evento

Workflow: **BLOOMBERG_MAIL — INGESTÃO 005N — Validação Conjunta dos Normalizadores**  
Run: **#1**  
Run ID: **37685223362**  
Commit executado: **a219b1dfb7639f1a654ad4d1a8f814e9c036c318**  
Conclusão: **FAILURE**

## Diagnóstico determinístico

A falha ocorreu no passo `Run joint deterministic validation`.

Erro objetivo:

`AssertionError: missing normalized CVM_OFERTAS`

O validador encontrou os RAW necessários, mas o arquivo derivado `cvm_ofertas_normalizado.json` ainda não estava publicado no checkout usado pela execução.

A falha não foi causada por SHA divergente, corrupção do RAW ou erro de reconciliação. O pipeline parou antes dessas verificações.

## Causa-raiz

Os normalizadores de CVM e Tesouro haviam sido implementados como scripts, mas o workflow de normalização ainda executava somente:

- BCB
- VIX

Portanto, havia uma inconsistência entre:

**estado do código:** 4 normalizadores implementados  
**execução do workflow:** somente 2 normalizadores executados  
**validação conjunta:** exigia 4 saídas persistidas

## Correção aplicada

O workflow:

`.github/workflows/bloomberg-mail-ingestao-005n-normalizacao.yml`

foi corrigido para executar, em sequência:

1. BCB + VIX
2. CVM
3. Tesouro
4. validação estrutural das quatro saídas implementadas
5. publicação dos derivados

Commit da correção:

`2799626e8b68b5b498b8e116d2827233b2407d16`

## Estado após a correção

**NÃO EXECUTADO AINDA:** nova execução do workflow de normalização após a correção.

Consequentemente:

- BCB normalizado: implementado e anteriormente executado
- VIX normalizado: implementado e anteriormente executado
- CVM normalizado: implementado, aguardando execução
- Tesouro normalizado: implementado, aguardando execução
- B3 normalizado: BLOQUEADO por falta de mapeamento autoritativo
- validação conjunta 005N: **BLOCKED** até existirem as quatro saídas implementadas
- integração: **BLOCKED**

## Regra

A falha deve permanecer registrada. Não será transformada artificialmente em PASS.

A próxima sequência correta é:

**executar 005N Normalização → verificar 4/5 → executar 005N Validação Conjunta → corrigir eventuais falhas → somente depois avançar para B3 e reconciliação 5/5.**

RAW permanece imutável.
