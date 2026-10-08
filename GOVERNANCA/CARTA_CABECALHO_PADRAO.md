---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "CARTA_GOVERNANCA"
fase: "GOVERNANCA"
id_documento: "BLOOMBERG-MAIL-CARTA-CABECALHO-PADRAO-V1"
titulo: "CARTA — Cabeçalho Padrão dos Documentos"
status: "PUBLICADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "Curioso-da-Internet-IA — MODELO-PADRAO-CABECALHO.md"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO"
escopo: "Todos os documentos Markdown do BLOOMBERG_MAIL"
objetivo: "Tornar todos os documentos identificáveis, rastreáveis, contextualizados e validáveis."
dependencias: "Curioso-da-Internet-IA/CABEÇALHO/MODELO-PADRAO-CABECALHO.md"
---

# CARTA — Cabeçalho Padrão dos Documentos

## Contexto Histórico

A governança documental do BLOOMBERG_MAIL passa a adotar como padrão canônico o modelo de cabeçalho existente no repositório Curioso-da-Internet-IA.

## Estado

PUBLICADO.

## Evidências

O modelo canônico define Front Matter YAML obrigatório, título, contexto histórico, estado, evidências, validação, resultado e próxima ação.

## Validação

A estrutura foi conferida contra o modelo canônico de referência.

## Resultado

Todo novo documento Markdown do BLOOMBERG_MAIL deverá nascer com o cabeçalho completo. Documentos históricos deverão ser migrados para o padrão sem perda do conteúdo original.

## Regras permanentes

1. O Front Matter YAML é a primeira informação do Markdown.
2. Os campos do modelo permanecem estáveis.
3. Campos não aplicáveis recebem `N/A`.
4. `id_documento` é único.
5. Alteração relevante atualiza versão, data e rastreabilidade.
6. Documentos derivados apontam para sua origem.
7. Evidência e validação permanecem separadas.
8. A cadeia de autoridade é `PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO`.
9. O cabeçalho é parte da governança e não texto opcional.
10. A regra vale para documentos futuros e para a migração do acervo histórico.

## Próxima Ação

Executar e validar a migração integral do acervo Markdown existente e manter verificação automática no CI.
