---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-PLANO-REC-001-RECONCILIACAO-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — INGESTÃO 005 — PLANO REC-001"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/PLANO_REC-001_RECONCILIACAO_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — INGESTÃO 005 — PLANO REC-001

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

# BLOOMBERG_MAIL — INGESTÃO 005 — PLANO REC-001

> Cabeçalho histórico — 2026-10-07.
> Finalidade: executar a reconciliação independente exigida pelo CONTRATO_VERIFICACAO_V1_0 antes de qualquer promoção.

## Regra

REC-001 somente pode ser PASS quando existir uma segunda representação documentada, acessível e comparável ao RAW da INGESTÃO 005. Diferenças devem ser registradas; não podem ser corrigidas silenciosamente.

## Matriz operacional

| Dataset | RAW 005 | Segunda representação | Chave | Estado inicial |
|---|---|---|---|---|
| B3_COTACOES | COTAHIST_A2026.ZIP | evidência versionada COTAHIST no repositório B3 + endpoint oficial | arquivo/período + estrutura COTAHIST | BLOCKED até comparação executada |
| CVM_OFERTAS | oferta_distribuicao.zip | segunda representação oficial/independente a definir e materializar | identificador da oferta + data + emissor | BLOCKED |
| BCB_SGS | bcb_sgs_1178_ultimos_10.json | endpoint oficial consultado novamente, período sobreposto | data | BLOCKED |
| TESOURO_HISTORICO | precotaxatesourodireto.csv | arquivo/representação oficial independente do mesmo período | título + vencimento + data base | BLOCKED |
| VIX | VIX_History.csv | segunda representação independente/oficial acessível do mesmo período | DATE | BLOCKED |

## Critérios

1. Mesmo período de referência.
2. Mesma unidade e definição econômica.
3. Chave lógica explicitamente definida.
4. Comparação sem conversão destrutiva.
5. Tolerância somente se documentada pela natureza do dado.
6. Ausência de segunda representação = BLOCKED.
7. Divergência não explicada = BLOCKED/FAIL conforme o contrato.
8. Evidência salva no repositório.
9. Resultado reproduzível por código.
10. GAT-001 continua bloqueado enquanto qualquer REC-001 obrigatório estiver BLOCKED.

## Sequência

B3 → CVM → BCB → TESOURO → VIX → GAT-001

Nenhum dataset será promovido antecipadamente para Layer A.

## Resultado desta etapa

Este documento define o trabalho executável. Não declara nenhuma reconciliação como PASS por planejamento.