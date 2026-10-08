---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-STATUS-REC001-CVM-2026-10-08-MD"
titulo: "BLOOMBERG_MAIL — REC-001 CVM — STATUS"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/STATUS_REC001_CVM_2026-10-08.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — REC-001 CVM — STATUS

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

# BLOOMBERG_MAIL — REC-001 CVM — STATUS

> Cabeçalho histórico — 2026-10-08. Registro determinístico da reconciliação do conjunto INGESTÃO 005 / REC-001.

## Resultado

**STATUS: BLOCKED — SOURCE_UPDATED_SINCE_RAW**

A execução controlada #5 do workflow `BLOOMBERG_MAIL — INGESTÃO 005E — REC-001 CVM` confirmou que o arquivo oficial atualmente publicado pela CVM não possui o mesmo SHA-256 do RAW capturado na INGESTÃO 005.

- Workflow run: **#5**
- Run ID: **37780280976**
- Commit executor: `46a574bf1ecacd5b690c7f545c0261e9e0cdcf4c`
- Execução UTC: `2026-10-08T12:54:49.187165+00:00`
- Endpoint oficial: `https://dados.cvm.gov.br/dados/OFERTA/DISTRIB/DADOS/oferta_distribuicao.zip`
- SHA-256 RAW: `72574a340f39da1d9f541647d5f9e740754a607344b6f979eb4c32c64a91c306`
- SHA-256 endpoint atual: `4b0ab625aa94267968e841c8c1fc2acbcc40b3fe111213b3f9852a832095212f`
- RAW preservado: **SIM**
- Impacto: **BLOCKED_NEWER_ENDPOINT**

## Interpretação

A divergência não autoriza substituir o RAW nem concluir que os dados históricos estejam errados. Ela demonstra somente que a representação oficial atualmente disponível foi atualizada em relação à representação capturada na INGESTÃO 005.

A evidência anterior de igualdade em 2026-10-07 permanece histórica e não deve ser sobrescrita como se fosse a observação atual.

## Regra aplicada

- divergência de SHA-256: não é PASS;
- RAW permanece imutável;
- nenhuma correção ou substituição automática;
- nenhuma interpolação;
- nenhuma transformação econômica;
- REC-001 CVM permanece bloqueado até ser encontrada uma representação oficial correspondente ao mesmo período/versão do RAW, ou até existir uma reconciliação histórica reproduzível que satisfaça a carta REC-001.

## Workflow

O gatilho temporário `push` utilizado para a execução controlada foi removido. O workflow voltou a operar somente por `workflow_dispatch`.

## Próximo passo

**Não avançar o CVM para PASS e não executar o GAT-001 final.** O próximo trabalho é localizar/materializar uma segunda representação histórica oficial correspondente ao RAW CVM da INGESTÃO 005 e reconciliá-la sem modificar o RAW.
