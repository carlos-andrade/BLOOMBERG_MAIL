---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-CAMADA-A-VALIDACAO-POS-PROMOCAO-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — CAMADA A — VALIDAÇÃO PÓS-PROMOÇÃO"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/CAMADA_A/VALIDACAO_POS_PROMOCAO_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — CAMADA A — VALIDAÇÃO PÓS-PROMOÇÃO

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

# BLOOMBERG_MAIL — CAMADA A — VALIDAÇÃO PÓS-PROMOÇÃO

> Histórico: 2026-10-07 | validação após promoção controlada da INGESTÃO 005.
> Regra: a Layer A é somente referência derivada; RAW permanece imutável.

## Resultado

**POST-PROMOTION VALIDATION = PASS**

Os cinco SHA-256 declarados no manifesto da Layer A foram confrontados com os respectivos arquivos `.sha256` preservados junto aos RAWs.

| Dataset | SHA Layer A | SHA sidecar RAW | Resultado |
|---|---|---|---|
| B3_COTACOES | c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f | c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f | PASS |
| CVM_OFERTAS | 72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306 | 72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306 | PASS |
| BCB_SGS | 7343beba0c0d8fad8593bf7d4d74746f7981fd186bc1b25bece94a6d3bd71f36 | 7343beba0c0d8fad8593bf7d4d74746f7981fd186bc1b25bece94a6d3bd71f36 | PASS |
| TESOURO_HISTORICO | 8c0aa0c51b23d49843bf8c912adec1eb8fc959755f3a671e319c98a692b83d4e | 8c0aa0c51b23d49843bf8c912adec1eb8fc959755f3a671e319c98a692b83d4e | PASS |
| VIX | cfcb9dce25bbbbd83aedca9a1480468bb25db2e988b3e893a4eebabb1905e1ab | cfcb9dce25bbbbd83aedca9a1480468bb25db2e988b3e893a4eebabb1905e1ab | PASS |

## Controles

- RAW alterado: **NÃO**
- SHA divergente: **NÃO**
- Dados inventados: **NÃO**
- Interpolação: **NÃO**
- Ajuste automático: **NÃO**
- Sinal operacional: **NÃO**
- Normalização econômica: **NÃO**

## Estado

**Layer A = PROMOTED_REFERENCE_VALIDATED**

A próxima etapa é a construção da normalização derivada, com contrato e parser versionados. A Layer A não deve ser confundida com dados normalizados nem com sinais de mercado.
