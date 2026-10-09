---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-LAYOUT-B3-COTAHIST-V1-0-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — LAYOUT B3 COTAHIST — v1.0"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/LAYOUT_B3_COTAHIST_V1_0_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — LAYOUT B3 COTAHIST — v1.0

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-LAYOUT-B3-COTAHIST-V1-0-2026-10-07-MD
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

# BLOOMBERG_MAIL — LAYOUT B3 COTAHIST — v1.0

> Histórico: 2026-10-07 | Projeto: BLOOMBERG_MAIL | Etapa: INGESTÃO 005 / NORMALIZAÇÃO

## Estado
**PENDING_AUTHORITATIVE_FIELD_MAPPING**

## Evidência utilizada
- Inspeção: `INSPECAO_FORMATOS_005.json`
- RAW: `RAW/COTAHIST_A2026.ZIP`
- SHA-256 RAW: `c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f`
- ZIP integrity: PASS
- Membro: `COTAHIST_A2026.TXT`
- Formato observado: registro de largura fixa; sem delimitador CSV/TSV/pipe
- Encoding observado: `utf-8-sig`

## Regra de não-inferência
A inspeção confirma que o arquivo é de largura fixa, mas a amostra disponível não é suficiente para autorizar a definição de posições/campos econômicos. Portanto, este layout **não inventa offsets nem nomes de campos**.

## Contrato mínimo autorizado
1. Preservar a linha RAW integral antes de qualquer parsing.
2. Preservar o tipo de registro observado.
3. Preservar o texto original e seu vínculo ao RAW SHA-256.
4. Só publicar campos econômicos depois de uma tabela de posições validada por documentação oficial ou evidência adicional determinística.
5. Falha de mapeamento bloqueia a promoção para NORMALIZED_VALIDATED.

## Próximo gate
**FIELD_MAPPING_REQUIRED** → depois normalizador B3 → validação estrutural/semântica → reconciliação.
