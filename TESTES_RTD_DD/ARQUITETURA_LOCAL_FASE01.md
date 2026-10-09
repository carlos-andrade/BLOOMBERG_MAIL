---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "ARQUITETURA_OPERACIONAL_LOCAL"
fase: "FASE-01-PREPARACAO-LOCAL"
id_documento: "BLOOMBERG-MAIL-ARQ-LOCAL-RTD-001"
titulo: "Arquitetura local — RTD/Profit e sincronização Git manual"
status: "PREPARACAO_LOCAL_EXECUTADA; CI_DOCUMENTAL_OK; CLONE_LOCAL_SINCRONIZADO"
versao: "1.4"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "Saída PowerShell fornecida pelo utilizador em 2026-10-09"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "TESTES_RTD_DD/VERIFICACAO_FASE01_AMBIENTE_LOCAL_2026-10-09.md; scripts/windows/preparar_ambiente_local.ps1"
escopo: "Preparação segura do ambiente Windows local e clone Git; não inclui implementação do gravador RTD"
objetivo: "Registar arquitetura, validação local, proteções e gates para a futura captura RTD/Profit"
dependencias: "Windows; Git for Windows; Excel e Profit instalados para os testes operacionais; confirmação dos direitos de armazenamento"
---

# Arquitetura local — RTD/Profit e sincronização Git manual

> **Projeto:** BLOOMBERG_MAIL  
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL  
> **Tipo:** ARQUITETURA_OPERACIONAL_LOCAL  
> **Fase:** FASE-01-PREPARACAO-LOCAL  
> **ID:** BLOOMBERG-MAIL-ARQ-LOCAL-RTD-001  
> **Status:** PREPARACAO_LOCAL_EXECUTADA; CI_DOCUMENTAL_OK; CLONE_LOCAL_SINCRONIZADO  
> **Versão:** 1.4  
> **Criação:** 2026-10-09  
> **Atualização:** 2026-10-09  
> **Origem:** Saída PowerShell fornecida pelo utilizador em 2026-10-09  
> **Autoridade:** LAYOUT  
> **Rastreabilidade:** TESTES_RTD_DD/VERIFICACAO_FASE01_AMBIENTE_LOCAL_2026-10-09.md; scripts/windows/preparar_ambiente_local.ps1

## Contexto Histórico

Em 2026-10-09, foi aprovada a arquitetura local do projeto BLOOMBERG_MAIL. A raiz Windows definida é `D:\\BLOOMBERG_MAIL`; o repositório central é público e a sincronização Git é manual. O workbook RTD original deve ser preservado.

A preparação inicial foi executada pelo utilizador. Em seguida, a sincronização local foi confirmada por saída PowerShell fornecida pelo utilizador: `git pull --ff-only` avançou por fast-forward de `56ee032` para `1ed8948`, sem conflitos.

## Estado

- Preparação de diretórios: EXECUTADA, conforme saída anterior do utilizador.
- Clone Git: `D:\\BLOOMBERG_MAIL\\repo\\BLOOMBERG_MAIL`.
- Branch: `main`.
- Commit após sincronização: `1ed8948 | 2026-10-09 | FECHO FASE 01: atualizar estado final da verificação`.
- Estado Git após atualização: `## main...origin/main`, sem alterações locais reportadas.
- Exclusões verificadas por `git check-ignore -v`: `dados_locais/`, `logs/`, `backups/` e `configuracao_local/`.
- Captura RTD: NÃO IMPLEMENTADA nem ativa.
- Direitos/licença para armazenamento persistente: PENDENTES.
- PR #1 e PR #2: incorporadas em `main`, conforme histórico do projeto.

## Evidências

O utilizador reportou as pastas locais `dados_locais/RAW`, `HISTORICO`, `NORMALIZADOS`, `QUARENTENA`, `MANIFESTOS`, além de `logs`, `backups` e `configuracao_local`. O workbook `RDT_PROFIT.xlsx` permanece fora do clone, na raiz local, segundo o estado anteriormente reportado.

A atualização Git apresentada em 2026-10-09 enumerou oito ficheiros atualizados/criados e concluiu sem erros. A validação `git check-ignore -v` identificou as regras de exclusão esperadas. Estas são evidências fornecidas pelo utilizador; não representam acesso direto ao computador Windows.

## Validação

Comandos executados pelo utilizador:

```powershell
git -C "D:\\BLOOMBERG_MAIL\\repo\\BLOOMBERG_MAIL" status --short --branch
git -C "D:\\BLOOMBERG_MAIL\\repo\\BLOOMBERG_MAIL" pull --ff-only
git -C "D:\\BLOOMBERG_MAIL\\repo\\BLOOMBERG_MAIL" log -1 --format="%h | %cs | %s"
git -C "D:\\BLOOMBERG_MAIL\\repo\\BLOOMBERG_MAIL" check-ignore -v dados_locais/ logs/ backups/ configuracao_local/
```

Resultado reportado:
- `git status`: `## main...origin/main`.
- `git pull --ff-only`: atualização fast-forward concluída.
- Commit final: `1ed8948`.
- As quatro pastas operacionais foram abrangidas por regras em `.gitignore`.

O `.gitignore` impede a inclusão de novos ficheiros ignorados, mas não retira automaticamente ficheiros já rastreados. A revisão de ficheiros rastreados e dos direitos de utilização continua necessária antes de qualquer publicação de dados.

## Resultado

`FASE01_LOCAL_PREPARATION=PASS`  
`LOCAL_CLONE_SYNC=PASS`  
`LOCAL_IGNORE_RULES=PASS`  
`RTD_FORMULAS_PRESENT=PASS`  
`RTD_LIVE_UPDATE=NOT_VERIFIED`  
`RECONNECT=NOT_RUN`  
`STORAGE_RIGHTS=PENDING`  
`PRODUCTION_INGESTION=BLOCKED`

A sincronização do clone local está confirmada pela saída do utilizador. A captura RTD não foi implementada nem ativada. A presença de fórmulas RTD no workbook não prova que cada atualização possa ser registada sem perdas.

## Próxima Ação

1. Mapear as células e os campos efetivamente usados no workbook sem alterar o original.
2. Especificar a captura de resultados recalculados: uma fórmula RTD pode atualizar o seu resultado sem disparar o evento VBA `Worksheet_Change`; avaliar `Worksheet_Calculate` ou polling controlado com deduplicação.
3. Fazer teste local assistido de atualização, estabilidade e reconexão antes de ativar qualquer gravador.
4. Confirmar direitos/licença antes de armazenamento persistente ou publicação.

---
Documento operacional. Preparação e sincronização Git não equivalem a validar RTD ao vivo.
