---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-FONTES-RESOLVIDAS-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — INGESTÃO 005 — FONTES RESOLVIDAS DIRETAMENTE"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/fontes_resolvidas_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — INGESTÃO 005 — FONTES RESOLVIDAS DIRETAMENTE

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-FONTES-RESOLVIDAS-2026-10-07-MD
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

# BLOOMBERG_MAIL — INGESTÃO 005 — FONTES RESOLVIDAS DIRETAMENTE

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Ingestão: 005
- Data: 2026-10-07
- Finalidade: registrar que a aquisição deve partir diretamente das fontes oficiais, sem URL inventada.

## VIX — Cboe
A página oficial da Cboe identifica explicitamente o arquivo de dados diários do VIX de 1990 até o presente e informa que é atualizado diariamente.

Arquivo oficial resolvido:
https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv

Fonte-página oficial:
https://www.cboe.com/tradable-products/vix/vix-historical-data

## Tesouro Direto
A aquisição deve começar pela página oficial de Histórico de Preços e Taxas e resolver o link do arquivo diretamente nela. Não será usado URL construído por padrão de nomenclatura.

Página oficial:
https://www.tesourodireto.com.br/produtos/dados-sobre-titulos/historico-de-precos-e-taxas

## Regra definitiva
1. consultar a fonte oficial;
2. resolver o arquivo/link efetivamente publicado pela fonte;
3. adquirir diretamente;
4. preservar RAW;
5. calcular SHA-256;
6. registrar timestamp UTC e período;
7. validar estrutura, datas, unidades, missingness e duplicidade;
8. somente então permitir promoção.

## Gate
A Layer A permanece bloqueada até a validação completa e reconciliação independente.
