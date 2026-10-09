---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO_TECNICO"
fase: "FONTES"
id_documento: "BLOOMBERG-MAIL-FONTES-005-INGESTAO-FONTES-OFICIAIS-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — FONTES — INGESTÃO 005"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "FONTES/005_ingestao_fontes_oficiais_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — FONTES — INGESTÃO 005

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO_TECNICO
> **Fase:** FONTES
> **ID:** BLOOMBERG-MAIL-FONTES-005-INGESTAO-FONTES-OFICIAIS-2026-10-07-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-08
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


## Contexto Histórico

Este documento pertence ao projeto BLOOMBERG_MAIL e passa a obedecer ao padrão de cabeçalho canônico adotado na governança de carlos-andrade.

## Estado

IMPLEMENTADO — cabeçalho normalizado em 2026-10-08.

## Evidências

Modelo canônico: carlos-andrade/Curioso-da-Internet-IA/CABEÇALHO/MODELO-PADRAO-CABECALHO.md.

## Validação

Estrutura revisada para Front Matter YAML, identificação documental, contexto histórico, estado, evidências, validação, resultado e próxima ação.

## Resultado

Documento integrado à governança documental central.

## Próxima Ação

Manter o cabeçalho atualizado em toda alteração relevante.

---

# BLOOMBERG_MAIL — FONTES — INGESTÃO 005

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Ingestão: 005
- Data: 2026-10-07
- Status: fontes oficiais registradas antes da aquisição.

## B3
- Instituição: B3
- Finalidade: cotações históricas COTAHIST.
- Página: https://www.b3.com.br/
- Recurso utilizado: COTAHIST anual.
- Status: fonte registrada; aquisição RAW validada em INGESTÃO 005-B.

## CVM
- Instituição: Comissão de Valores Mobiliários.
- Finalidade: ofertas/distribuições.
- Página: https://www.gov.br/cvm/
- Recurso: oferta_distribuicao.zip.
- Status: fonte registrada; aquisição RAW validada.

## Banco Central do Brasil / SGS
- Instituição: Banco Central do Brasil.
- Finalidade: séries macroeconômicas.
- Página: https://www.bcb.gov.br/
- Recurso: SGS, série 1178 na amostra técnica.
- Status: fonte registrada; amostra técnica adquirida.

## Tesouro Nacional / Tesouro Transparente
- Instituição: Tesouro Nacional / Tesouro Transparente.
- Finalidade: preços e taxas dos títulos ofertados pelo Tesouro Direto.
- Página de dados: https://www.tesourotransparente.gov.br/
- Recurso direto resolvido:
  https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/precotaxatesourodireto.csv
- Arquivo: precotaxatesourodireto.csv
- Status: fonte resolvida; aquisição pendente de execução 005-C.

## Cboe / VIX
- Instituição: Cboe Global Markets.
- Finalidade: série histórica diária do VIX.
- Página oficial:
  https://www.cboe.com/tradable_products/vix/vix_historical_data/
- Recurso direto:
  https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv
- Arquivo: VIX_History.csv
- Status: fonte resolvida; aquisição pendente de execução 005-C.

## Regra
Todas as fontes acima devem permanecer registradas em `FONTES/`, independentemente de ingestão, workflow ou conversa.
