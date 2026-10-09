---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO_TECNICO"
fase: "FONTES"
id_documento: "BLOOMBERG-MAIL-FONTES-README-MD"
titulo: "BLOOMBERG_MAIL — FONTES"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "FONTES/README.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — FONTES

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO_TECNICO
> **Fase:** FONTES
> **ID:** BLOOMBERG-MAIL-FONTES-README-MD
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

# BLOOMBERG_MAIL — FONTES

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Regra: todas as fontes externas utilizadas pelo projeto devem ser registradas nesta pasta.
- Data de instituição: 2026-10-07

## Regra obrigatória

Nenhuma fonte utilizada em pesquisa, aquisição, validação, normalização ou teste pode permanecer apenas no chat ou apenas em um workflow.

Cada fonte deve possuir registro persistente em `FONTES/`, contendo, quando aplicável:

- nome da instituição/fonte;
- finalidade;
- URL da página oficial;
- URL direta do recurso;
- tipo/formato do recurso;
- período/frequência;
- data de consulta;
- timestamp UTC;
- checksum SHA-256 do arquivo adquirido;
- nome original do arquivo;
- status de validação;
- observações sobre alterações da fonte;
- relação com ingestão/hipótese/dataset.

## Regra de proveniência

`FONTE OFICIAL → REGISTRO EM FONTES/ → AQUISIÇÃO → RAW → CHECKSUM → VALIDAÇÃO → NORMALIZAÇÃO → TESTE`

A pasta `FONTES/` é o catálogo persistente de proveniência do projeto.

## Proibição

É proibido considerar uma fonte como parte oficial do pipeline apenas porque sua URL apareceu em uma conversa, log temporário ou mensagem de workflow. A fonte precisa estar registrada em `FONTES/`.

## Fontes iniciais

- B3
- CVM
- Banco Central do Brasil / SGS
- Tesouro Nacional / Tesouro Transparente
- Cboe / VIX

Novas fontes devem ser adicionadas antes de serem promovidas ao pipeline.
