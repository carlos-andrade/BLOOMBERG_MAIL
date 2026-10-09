---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "ARQUITETURA_OPERACIONAL_LOCAL"
fase: "FASE-01-PREPARACAO-LOCAL"
id_documento: "BLOOMBERG-MAIL-ARQ-LOCAL-RTD-001"
titulo: "Arquitetura local — RTD/Profit e sincronização Git manual"
status: "PREPARACAO_LOCAL_EXECUTADA; REVISAO_GIT_E_CAPTURA_PENDENTES"
versao: "1.2"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "Aprovação do utilizador e saída PowerShell fornecida pelo utilizador"
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
> **Status:** PREPARACAO_LOCAL_EXECUTADA; REVISAO_GIT_E_CAPTURA_PENDENTES  
> **Versão:** 1.2  
> **Criação:** 2026-10-09  
> **Atualização:** 2026-10-09  
> **Origem:** Aprovação do utilizador e saída PowerShell fornecida pelo utilizador  
> **Autoridade:** LAYOUT  
> **Rastreabilidade:** TESTES_RTD_DD/VERIFICACAO_FASE01_AMBIENTE_LOCAL_2026-10-09.md; scripts/windows/preparar_ambiente_local.ps1

## Contexto Histórico

Em 2026-10-09, foi aprovada a arquitetura local do projeto BLOOMBERG_MAIL. A raiz Windows definida pelo utilizador é `D:\BLOOMBERG_MAIL`; o repositório central é público e a sincronização Git permanece manual. O workbook RTD original deve ser preservado nesta fase.

A preparação foi executada pelo utilizador em 2026-10-09. A saída do PowerShell confirmou a criação do clone e das pastas. Esta evidência foi fornecida pelo utilizador e não resulta de acesso remoto ao computador Windows.

## Estado

- Preparação de diretórios: EXECUTADA.
- Clone Git: criado em `D:\BLOOMBERG_MAIL\repo\BLOOMBERG_MAIL`.
- Branch/commit reportados: `main`, `56ee032`.
- Estado reportado: `## main...origin/main`, sem alterações locais.
- Remoto: `https://github.com/carlos-andrade/BLOOMBERG_MAIL.git`.
- Captura RTD: NÃO IMPLEMENTADA nem ativa.
- Direitos/licença para armazenamento persistente: PENDENTES.
- PR #1: draft; não incorporada em `main`.

## Evidências

O utilizador reportou estas pastas locais: `dados_locais/RAW`, `HISTORICO`, `NORMALIZADOS`, `QUARENTENA`, `MANIFESTOS`, bem como `logs`, `backups` e `configuracao_local`. Também reportou os ficheiros `RDT_PROFIT.xlsx` e `~$RDT_PROFIT.xlsx` na raiz local.

O script reportou que não abriu nem modificou o workbook, não executou commit/push e não ativou captura. Não foi feita uma nova inspeção binária do workbook após a execução.

Estrutura local pretendida:

```text
D:\BLOOMBERG_MAIL\
├── repo\BLOOMBERG_MAIL\
├── dados_locais\
│   ├── RAW\
│   ├── HISTORICO\
│   ├── NORMALIZADOS\
│   ├── QUARENTENA\
│   └── MANIFESTOS\
├── logs\
│   ├── CAPTURA\
│   ├── VALIDACAO\
│   └── GIT\
├── backups\
└── configuracao_local\
```

## Validação

O script `scripts/windows/preparar_ambiente_local.ps1` verifica Git e remoto, cria apenas diretórios em falta e clona apenas quando o destino não existe. Não faz pull, commit, push, não inicia a captura e não abre nem altera o Excel.

A branch local `main` foi clonada antes da incorporação desta PR. Portanto, o `.gitignore` adicionado na branch de trabalho não está garantidamente presente no clone local até que a PR seja incorporada e o clone seja sincronizado. O `.gitignore` também não remove ficheiros já rastreados.

Comandos para nova verificação local:

```powershell
git -C "D:\BLOOMBERG_MAIL\repo\BLOOMBERG_MAIL" status --short --branch
git -C "D:\BLOOMBERG_MAIL\repo\BLOOMBERG_MAIL" remote -v
git -C "D:\BLOOMBERG_MAIL\repo\BLOOMBERG_MAIL" check-ignore -v dados_locais logs backups configuracao_local
```

## Resultado

A preparação local e a validação do clone estão confirmadas com base na saída do utilizador. A revisão documental encontrou caminhos antigos em `C:\BLOOMBERG_MAIL`; esta versão corrige os comandos para a raiz efetiva em D:. A validação CI do repositório falhou porque o validador atual identificou numerosos documentos pré-existentes com cabeçalhos incompletos; esta falha não deve ser ocultada nem considerada aprovada.

A publicação desta PR continua em draft até a revisão de CI e a governação documental estarem resolvidas. Nenhum ficheiro de mercado bruto deve ser publicado sem revisão dos direitos de armazenamento e aprovação explícita.

## Próxima Ação

1. Rever o resultado do validador documental e definir uma migração controlada para os documentos preexistentes, sem alterar 99 documentos em lote sem plano aprovado.
2. Confirmar os controlos de integração no GitHub.
3. Após a revisão, incorporar as proteções Git e sincronizar o clone local.
4. Mapear as células RTD e desenhar o gravador por alteração observável.
5. Testar deduplicação, timestamps, interrupção e reconexão.
6. Rever os direitos de utilização antes de qualquer armazenamento persistente ou publicação.

---
Documento operacional. A preparação de ambiente não equivale a validar o funcionamento do RTD em tempo real.
