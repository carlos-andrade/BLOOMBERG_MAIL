---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-CAMADA-A-README-MD"
titulo: "BLOOMBERG_MAIL — CAMADA A — REFERÊNCIA VALIDADA"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/CAMADA_A/README.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — CAMADA A — REFERÊNCIA VALIDADA

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

# BLOOMBERG_MAIL — CAMADA A — REFERÊNCIA VALIDADA

> Histórico: 2026-10-07 | promoção controlada após INGESTÃO 005D #5.
> Status: PROMOVIDA COMO CAMADA DE REFERÊNCIA VALIDADA.
> Fonte primária: RAW imutável em `../RAW/`.

## Objetivo

A Camada A é a primeira camada derivada após a validação formal. Nesta fase ela funciona como **referência validada e auditável**, sem duplicar os binários RAW e sem executar normalização econômica.

A promoção foi autorizada após:

- 005D #5 = PASS;
- GAT-001 = PASS;
- REC-001 = PASS para os cinco datasets;
- PRO-001 = PASS para os cinco datasets;
- proveniência obrigatória completa no manifesto;
- aprovação explícita para prosseguir.

## Regra de origem

Cada dataset desta camada aponta para um RAW específico e para seu SHA-256. O RAW permanece imutável.

Nenhuma informação é:

- inventada;
- interpolada;
- preenchida silenciosamente;
- ajustada por inflação/proventos;
- corrigida economicamente;
- transformada em sinal operacional.

## Datasets promovidos

| Dataset | Estado | RAW |
|---|---|---|
| B3_COTACOES | PROMOTED_REFERENCE | COTAHIST_A2026.ZIP |
| CVM_OFERTAS | PROMOTED_REFERENCE | oferta_distribuicao.zip |
| BCB_SGS | PROMOTED_REFERENCE | bcb_sgs_1178_ultimos_10.json |
| TESOURO_HISTORICO | PROMOTED_REFERENCE | precotaxatesourodireto.csv |
| VIX | PROMOTED_REFERENCE | VIX_History.csv |

## Próxima etapa

A normalização física, caso necessária, será produzida separadamente a partir desta referência e do RAW, com parser/versionamento próprios e validação pós-transformação.

**Não há sinal operacional nesta camada.**
