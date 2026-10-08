---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-LAYOUT-CVM-OFERTAS-V1-0-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — LAYOUT CVM OFERTAS — v1.0"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/LAYOUT_CVM_OFERTAS_V1_0_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — LAYOUT CVM OFERTAS — v1.0

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

# BLOOMBERG_MAIL — LAYOUT CVM OFERTAS — v1.0

> Histórico: 2026-10-07 | Projeto: BLOOMBERG_MAIL | Etapa: INGESTÃO 005 / NORMALIZAÇÃO

## Estado
**READY_FOR_IMPLEMENTATION_FROM_INSPECTED_SCHEMA**

## Evidência
- Inspeção: `INSPECAO_FORMATOS_005.json`
- RAW: `RAW/oferta_distribuicao.zip`
- SHA-256 RAW: `72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306`
- ZIP integrity: PASS
- Encoding observado: `latin-1`
- Delimitador observado: `;`

## Membros
### oferta_distribuicao.csv
Schema observado no header do arquivo. Os nomes devem ser preservados exatamente como fonte; nenhum campo deve ser renomeado ou descartado sem mapeamento explícito.

### oferta_resolucao_160.csv
Schema observado no header do arquivo. Os nomes devem ser preservados exatamente como fonte; nenhum campo deve ser renomeado ou descartado sem mapeamento explícito.

## Regras de transformação
- Datas somente para representação canônica, preservando o valor RAW.
- Valores numéricos somente após definição explícita de separador decimal e sem alteração econômica.
- Campos vazios permanecem vazios.
- Duplicidades são reportadas, nunca removidas silenciosamente.
- Todos os registros mantêm vínculo com o SHA do ZIP RAW e o membro de origem.

## Próximo gate
Implementação determinística → validação estrutural → validação de tipos/datas/missingness → reconciliação contra RAW.
