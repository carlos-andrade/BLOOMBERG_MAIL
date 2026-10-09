---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-FONTES-ACESSIBILIDADE-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — INGESTÃO 005-A — MATRIZ DE ACESSIBILIDADE DAS FONTES"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/fontes_acessibilidade_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — INGESTÃO 005-A — MATRIZ DE ACESSIBILIDADE DAS FONTES

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-FONTES-ACESSIBILIDADE-2026-10-07-MD
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

# BLOOMBERG_MAIL — INGESTÃO 005-A — MATRIZ DE ACESSIBILIDADE DAS FONTES

> Cabeçalho histórico — 2026-10-07.

| Fonte | Acesso verificado | Conteúdo | Estado |
|---|---|---|---|
| BCB SGS 1178 | endpoint JSON oficial | amostra real | ACESSÍVEL |
| B3 Cotações | página oficial + link ZIP | histórico desde 1986 | BINÁRIO PENDENTE |
| CVM Ofertas | página oficial + ZIP listado | ofertas públicas | BINÁRIO PENDENTE |
| Tesouro Direto | página oficial | históricos anuais 2002–2026 | ARQUIVO PENDENTE |
| VIX | não concluído | histórico diário | PENDENTE |

## Regra

“Fonte confirmada” não significa “arquivo adquirido”. A etapa só pode ser marcada como adquirida quando o artefato original, checksum e metadados estiverem registrados.

## Bloqueio observado

O ambiente de execução utilizado nesta etapa não conseguiu materializar diretamente os ZIPs B3/CVM. Portanto, não foram fabricados checksums, tamanhos locais ou supostos conteúdos.

## Próximo passo

Executar um **agente de aquisição reprodutível dentro do próprio repositório**, com download no GitHub Actions/runner, checksum SHA-256, armazenamento RAW e geração automática de NORMALIZADO/VALIDAÇÃO.
