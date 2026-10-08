---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-LAYOUT-TESOURO-DIRETO-V1-0-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — LAYOUT TESOURO DIRETO — v1.0"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/LAYOUT_TESOURO_DIRETO_V1_0_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — LAYOUT TESOURO DIRETO — v1.0

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

# BLOOMBERG_MAIL — LAYOUT TESOURO DIRETO — v1.0

> Histórico: 2026-10-07 | Projeto: BLOOMBERG_MAIL | Etapa: INGESTÃO 005 / NORMALIZAÇÃO

## Estado
**READY_FOR_IMPLEMENTATION_FROM_INSPECTED_SCHEMA**

## Evidência
- Inspeção: `INSPECAO_FORMATOS_005.json`
- RAW: `RAW/precotaxatesourodireto.csv`
- SHA-256 RAW: `8c0aa0c51b23d49843bf8c912adec1eb8fc959755f3a671e319c98a692b83d4e`
- Encoding observado: `utf-8-sig`
- Delimitador observado: `;`

## Campos fonte observados
1. Tipo Titulo
2. Data Vencimento
3. Data Base
4. Taxa Compra Manha
5. Taxa Venda Manha
6. PU Compra Manha
7. PU Venda Manha
8. PU Base Manha

## Regras de transformação
- Datas DD/MM/YYYY podem ser representadas em ISO-8601, mantendo o valor RAW.
- Valores com vírgula decimal devem preservar o texto RAW e só receber representação numérica derivada com regra explícita.
- Não alterar unidade, escala, precisão ou arredondamento sem autorização no layout.
- Campos vazios permanecem vazios.
- Duplicidades devem ser detectadas e reportadas.

## Próximo gate
Implementação determinística → validação estrutural/tipos/datas/missingness → reconciliação contra RAW.
