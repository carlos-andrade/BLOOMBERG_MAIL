---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-REC001-CVM-RECONCILIACAO-ESTRUTURAL-V3-2026-10-08-MD"
titulo: "BLOOMBERG_MAIL — REC-001 CVM — RECONCILIAÇÃO ESTRUTURAL HISTÓRICA V3"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_CVM_RECONCILIACAO_ESTRUTURAL_V3_2026-10-08.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — REC-001 CVM — RECONCILIAÇÃO ESTRUTURAL HISTÓRICA V3

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-REC001-CVM-RECONCILIACAO-ESTRUTURAL-V3-2026-10-08-MD
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

# BLOOMBERG_MAIL — REC-001 CVM — RECONCILIAÇÃO ESTRUTURAL HISTÓRICA V3

> Cabeçalho histórico — 2026-10-08. Execução controlada da alternativa histórica prevista após a busca de snapshot.

## Representações comparadas

**RAW 005:** `oferta_distribuicao.zip`

SHA-256: `72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306`

**Representação histórica oficial CVM:** página Séries Históricas — Distribuições Públicas, com planilhas individualizadas por classe de ativo.

Fonte oficial: https://www.gov.br/cvm/pt-br/centrais-de-conteudo/publicacoes/series-historicas/distribuicoes-publicas

## Testes determinísticos

| Critério REC-001 | Resultado | Evidência |
|---|---|---|
| Mesma fonte institucional | PASS | CVM |
| Representação acessível | PASS | planilhas oficiais |
| Mesmo conceito geral | PASS | distribuições públicas |
| Mesmo esquema | FAIL | ZIP possui esquema próprio; séries históricas são planilhas por classe |
| Mesmo período de referência | FAIL | séries históricas disponibilizadas na página têm atualização registrada em 19/03/2025; RAW foi capturado em 2026 |
| Mesma granularidade | FAIL | ZIP é registro operacional de ofertas; planilhas históricas são representação histórica por classe |
| Chave lógica 1:1 demonstrável | BLOCKED | estruturas não equivalentes |
| Igualdade de bytes | NOT APPLICABLE | representações distintas |

## Resultado

A representação histórica oficial é válida como **evidência contextual independente**, mas não é uma segunda representação comparável do mesmo snapshot do RAW 005.

Portanto, conforme o CONTRATO_VERIFICACAO_V1_0 e o PLANO_REC-001:

`REC-001 CVM = BLOCKED`

Código do bloqueio:
`BLOCKED_NON_EQUIVALENT_HISTORICAL_REPRESENTATION`

## Não realizado

- nenhum valor do RAW foi alterado;
- nenhuma oferta foi ajustada ou interpolada;
- nenhuma correspondência aproximada foi promovida a igualdade;
- nenhuma fonte de terceiros foi usada para declarar PASS;
- GAT-001 não foi desbloqueado.

## Conclusão operacional

A tentativa de reconciliação estrutural encerra a rota histórica disponível neste momento. Para obter PASS é necessária uma segunda representação oficial/independente do **mesmo período e da mesma granularidade** ou um snapshot histórico materializável do próprio ZIP.

RAW permanece imutável.
