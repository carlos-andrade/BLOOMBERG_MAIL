---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-CARTA-POLITICA-INCREMENTAL-BASES-V1-0-2026-10-08-MD"
titulo: "BLOOMBERG_MAIL — CARTA DE POLÍTICA INCREMENTAL DAS BASES — V1.0"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/CARTA_POLITICA_INCREMENTAL_BASES_V1_0_2026-10-08.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — CARTA DE POLÍTICA INCREMENTAL DAS BASES — V1.0

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-CARTA-POLITICA-INCREMENTAL-BASES-V1-0-2026-10-08-MD
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

# BLOOMBERG_MAIL — CARTA DE POLÍTICA INCREMENTAL DAS BASES — V1.0

> Cabeçalho histórico — 2026-10-08.
> Origem: decisão de arquitetura para impedir desatualização das bases adquiridas.
> Status: REGRA PERMANENTE DE GOVERNANÇA.
> Escopo: todas as bases de dados armazenadas em BLOOMBERG_MAIL/INGESTAO.

## 1. Regra-mestra

**Toda base de dados armazenada neste projeto deve possuir estratégia de atualização incremental.**

Nenhuma base deve depender exclusivamente de um snapshot histórico para permanecer atualizada.

A atualização incremental deve:
1. preservar o dado já adquirido;
2. adquirir o novo período/evento disponível;
3. registrar proveniência, data/hora e SHA-256;
4. validar o incremento antes de promovê-lo;
5. manter o histórico anterior imutável;
6. permitir reconstrução da base a partir dos incrementos;
7. registrar divergências quando uma nova aquisição da mesma competência tiver SHA diferente;
8. nunca substituir silenciosamente um arquivo anterior.

## 2. Aplicação por dataset

| Dataset | Estratégia incremental | Unidade mínima |
|---|---|---|
| B3_COTACOES | diária | pregão/arquivo diário disponível |
| CVM_OFERTAS | incremental por atualização/evento | novo registro/arquivo oficial atualizado |
| BCB_SGS | por período novo de cada série | observação/data |
| TESOURO_HISTORICO | por novo período/arquivo publicado | registro/data ou arquivo de atualização |
| VIX | diária | pregão/data |

A periodicidade operacional pode variar conforme a fonte, mas a obrigação de atualização incremental permanece.

## 3. Snapshots e incrementos

Snapshots são representações de referência. Incrementos são a unidade de atualização.

Quando ambos existirem:
- o snapshot não é apagado;
- o incremento não é fundido destrutivamente;
- a relação entre eles deve ser documentada;
- o período comum pode ser reconciliado;
- extensão temporal posterior deve ser identificada explicitamente.

## 4. Proveniência obrigatória

Todo incremento deve registrar, no mínimo:
- dataset_id;
- source;
- source_url;
- retrieval_timestamp_utc;
- reference_period;
- original_filename;
- sha256;
- size_bytes, quando aplicável;
- raw_path;
- parser/schema/layout;
- validation_status;
- reconciliation_status, quando aplicável.

## 5. Divergência de reaquisição

Se a mesma competência/período for baixada novamente e o SHA mudar:
- preservar as duas representações;
- registrar ambas;
- executar reconciliação;
- não escolher automaticamente uma versão;
- bloquear promoção quando a divergência não estiver explicada.

## 6. Integridade

São proibidos:
- valores inventados;
- interpolação silenciosa;
- ajuste econômico automático;
- exclusão silenciosa de duplicados;
- sobrescrita destrutiva;
- transformação que impeça rastrear o valor de origem.

## 7. Relação entre repositórios

Quando uma base tiver repositório especializado, o BLOOMBERG_MAIL permanece como arquivo de aquisição/proveniência e o repositório especializado pode receber os incrementos validados.

Para B3/COTAHIST:
**BLOOMBERG_MAIL → validação/reconciliação → B3**.

A propagação não autoriza substituir RAW histórico em nenhum dos repositórios.

## 8. Continuidade

Toda nova fonte adicionada ao projeto deve nascer com:
**RAW + manifesto + incremento + validação + reconciliação + destino de consolidação**, quando houver.

Esta carta prevalece como regra geral; cartas específicas podem detalhar o mecanismo de cada fonte sem contrariar esta regra.
