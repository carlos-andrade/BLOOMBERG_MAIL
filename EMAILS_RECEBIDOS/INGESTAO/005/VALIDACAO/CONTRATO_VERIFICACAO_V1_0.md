---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-CONTRATO-VERIFICACAO-V1-0-MD"
titulo: "BLOOMBERG_MAIL — CONTRATO DE VERIFICAÇÃO V1.0"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/CONTRATO_VERIFICACAO_V1_0.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — CONTRATO DE VERIFICAÇÃO V1.0

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

# BLOOMBERG_MAIL — CONTRATO DE VERIFICAÇÃO V1.0

> Histórico: 2026-10-07 | Projeto BLOOMBERG_MAIL | INGESTÃO 005 | Fechamento formal do mecanismo de verificação

## 1. Objetivo
Mecanismo determinístico, auditável e reproduzível para decidir se cada fonte pode ser promovida de RAW para NORMALIZADO e Layer A.

**Aquisição bem-sucedida não é validação. Validação PASS não é sinal operacional.**

## 2. Estados
- PASS — requisito comprovado por evidência.
- FAIL — requisito violado.
- BLOCKED — não foi possível testar; ausência de evidência nunca vira PASS.
- NOT_APPLICABLE — não se aplica, com justificativa.

Estado do dataset:
- VALIDATED — todos os obrigatórios PASS e todas as reconciliações obrigatórias PASS.
- REJECTED — pelo menos um obrigatório FAIL.
- BLOCKED — nenhum FAIL, mas existe obrigatório BLOCKED.
- NOT_READY — aquisição/proveniência incompleta.

## 3. Cadeia determinística
RAW → SHA-256 → integridade → estrutura → schema → datas/período → tipos/unidades → missingness → duplicidades → ordenação temporal → regras específicas → reconciliação independente → relatório → manifest → gate de promoção.

Nenhuma etapa pode ser pulada.

## 4. Evidência mínima
Cada teste registra: test_id, dataset, source_id, source_url, direct_resource_url quando existir, retrieval_timestamp_utc, reference_period, original_filename, SHA-256, versão do validador/parser, commit, expected, observed, result e evidence/rationale.

## 5. Matriz por dataset
| Dataset | Integridade | Estrutura/schema | Datas | Tipos/unidades | Missing/duplicados | Ordem temporal | Regras específicas | Reconciliação |
|---|---|---|---|---|---|---|---|---|
| B3 COTAHIST | OBR | OBR | OBR | OBR | OBR | OBR | OBR | OBR |
| CVM ofertas | OBR | OBR | OBR | OBR | OBR | OBR | OBR | OBR |
| BCB SGS | OBR | OBR | OBR | OBR | OBR | OBR | OBR | OBR |
| Tesouro Direto | OBR | OBR | OBR | OBR | OBR | OBR | OBR | OBR |
| Cboe VIX | OBR | OBR | OBR | OBR | OBR | OBR | OBR | OBR |

## 6. Regras específicas
B3: ZIP/TXT/layout/registros/datas/mercado coerentes; mudança de SHA do endpoint é atualização de fonte, não corrupção automática.
CVM: ZIP/arquivos internos/headers/tipos/datas/chaves/duplicidades/período.
BCB SGS: JSON/série/datas/valores/duplicidades.
Tesouro: CSV/encoding/cabeçalho/título/data/taxa/preço/tipos/datas/duplicidades/missingness.
VIX: CSV/DATE/OPEN/HIGH/LOW/CLOSE/datas/valores/duplicidades/ordem temporal.

## 7. Reconciliação independente
Comparar amostra ou contagem determinística contra segunda representação oficial ou independente documentada. Registrar chave/data, valor RAW, referência, tolerância e resultado. Se a segunda representação não estiver acessível, o teste é BLOCKED; nunca PASS.

## 8. Missingness e duplicidade
Missing não é zero. Nenhuma interpolação ou preenchimento silencioso. Duplicidade é avaliada pela chave lógica; duplicatas legítimas precisam de justificativa.

## 9. Promoção
Só promover RAW → NORMALIZADO quando todos os obrigatórios PASS, reconciliações PASS, proveniência completa, checksum confirmado, relatório gravado, manifest atualizado pelo resultado e commit identificável. Layer A exige ainda rastreabilidade reversível para RAW.

## 10. Proibições
Inventar valores, substituir missing por zero, interpolar silenciosamente, ajustar preços automaticamente, apagar/sobrescrever RAW, declarar PASS sem evidência, tratar Bloomberg como verdade ou emitir sinal operacional a partir do gate.

## 11. Reprodutibilidade
RAW + checksum + código/versão + configuração + fonte registrada devem permitir repetição. Alteração de parser/schema/regra gera nova versão do contrato e novo relatório.

## 12. Critério de fechamento
A especificação é **100% fechada** quando contrato, matriz, IDs dos testes e gate estiverem versionados no repositório. O dataset só é **100% validado** após execução real de todos os testes aplicáveis com PASS.
