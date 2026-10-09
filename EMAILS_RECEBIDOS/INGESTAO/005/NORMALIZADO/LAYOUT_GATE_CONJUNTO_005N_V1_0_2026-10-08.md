---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-LAYOUT-GATE-CONJUNTO-005N-V1-0-2026-10-08-MD"
titulo: "BLOOMBERG_MAIL — LAYOUT — GATE CONJUNTO 005N — 5/5"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/LAYOUT_GATE_CONJUNTO_005N_V1_0_2026-10-08.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — LAYOUT — GATE CONJUNTO 005N — 5/5

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-LAYOUT-GATE-CONJUNTO-005N-V1-0-2026-10-08-MD
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

# BLOOMBERG_MAIL — LAYOUT — GATE CONJUNTO 005N — 5/5

> Cabeçalho histórico: layout técnico criado em 2026-10-08 para a validação determinística conjunta dos cinco normalizadores da INGESTÃO 005.

## Entrada

- manifesto de aquisição: `EMAILS_RECEBIDOS/INGESTAO/005/manifesto_aquisicao.json`
- plano de normalização: `EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/manifesto_normalizacao.json`
- validação conjunta existente: `VALIDACAO_NORMALIZADORES_005N.json`
- validação independente B3: `B3/VALIDACAO_NORMALIZACAO_B3_A2026.json`

## Datasets e manifests

| Dataset | Manifesto |
|---|---|
| BCB_SGS_1178 | `bcb_sgs_1178_normalizado.json` |
| VIX | `vix_normalizado.json` |
| CVM_OFERTAS | `cvm_ofertas_normalizado.json` |
| TESOURO_HISTORICO | `tesouro_normalizado.json` |
| B3_COTAHIST_A2026 | `B3/b3_cotahist_normalizado.json` |

## Checks determinísticos

1. exatamente cinco datasets esperados;
2. IDs únicos;
3. SHA RAW igual ao manifesto de aquisição;
4. `quality_status = NORMALIZED_DERIVED`;
5. parser version presente;
6. source/source_url ou equivalente presente;
7. raw_path presente;
8. saída derivada presente;
9. gzip íntegro para cada `.jsonl.gz`;
10. validação individual PASS;
11. B3 independente PASS;
12. contagens de duplicidade/missingness explícitas;
13. políticas de imutabilidade e ausência de transformação econômica preservadas;
14. nenhuma remoção silenciosa de duplicidades.

## Resultado

O resultado deve ser um JSON determinístico com `status = PASS` somente se todos os checks forem verdadeiros. Qualquer falha produz `status = FAIL` e bloqueia integração.
