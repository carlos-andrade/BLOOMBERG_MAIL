---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-RELATORIO-CAMADA-A-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — INGESTÃO 005-A — RELATÓRIO DA CAMADA A"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/relatorio_camada_A_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — INGESTÃO 005-A — RELATÓRIO DA CAMADA A

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

# BLOOMBERG_MAIL — INGESTÃO 005-A — RELATÓRIO DA CAMADA A

> Cabeçalho histórico — 2026-10-07.  
> Status: **PARCIALMENTE_EXECUTADA_COM_BLOQUEIO_DE_BINÁRIOS**.  
> Regra: nenhum dado ausente foi inventado.

## Resultado executivo

A aquisição controlada foi iniciada com verificação de fontes oficiais e uma amostra real consultável do SGS/BCB.

### Aprovado tecnicamente
- **BCB SGS série 1178**: amostra JSON obtida por endpoint oficial e preservada como evidência normalizada.
- A série 1178 é diária, unidade percentual ao ano, início em 04/06/1986 e corresponde à Selic anualizada base 252. citeturn0search13turn4view0

### Fonte confirmada, mas binário não incorporado nesta execução
- **B3 Cotações Históricas**: fonte oficial confirma histórico desde 1986, formato ZIP/TXT e campos de preços, negócios e volume. O download binário não foi incorporado porque o mecanismo de acesso disponível nesta execução não aceitou o conteúdo ZIP. citeturn2view0turn3view1
- **CVM Ofertas Públicas de Distribuição**: dataset oficial atualizado diariamente; o arquivo `oferta_distribuicao.zip` estava disponível no diretório oficial em 06/10/2026. O binário não foi incorporado nesta execução porque o ambiente de execução não conseguiu baixar o ZIP diretamente. citeturn0search0turn0search1
- **Tesouro Direto**: página oficial consultada com históricos anuais e atualização em 05/10/2026. O arquivo anual ainda não foi incorporado nesta execução. citeturn0search8
- **VIX**: aquisição fica pendente de fonte histórica oficial acessível e verificável nesta etapa.

## Evidência BCB

Endpoint consultado:
`https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados/ultimos/10?formato=json`

A resposta recuperada contém dez observações, de 20/07/2026 a 31/07/2026, todas com valor 14,15. A amostra foi gravada em `NORMALIZADO/bcb_sgs_1178_ultimos_10.json`. citeturn4view0

## Qualidade

| Teste | Resultado |
|---|---|
| Fonte identificada | PASS |
| URL identificada | PASS |
| Formato | PASS — JSON |
| Unidade | PASS — % a.a. |
| Periodicidade | PASS — diária |
| Datas parseáveis | PASS |
| Valores numéricos | PASS |
| Missing na amostra | PASS — nenhum |
| Duplicidade por data | PASS — nenhuma |
| RAW binário | PENDENTE para fontes ZIP |
| Reconciliação independente | PENDENTE |
| Promoção para série histórica | NÃO |

## Decisão

A Camada A **não está integralmente aprovada**. O BCB está aprovado apenas como amostra técnica; B3/CVM/Tesouro/VIX continuam em aquisição controlada.

Nenhuma hipótese H1–H4 será testada com esta amostra isolada.
