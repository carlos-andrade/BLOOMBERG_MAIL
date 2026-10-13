# Governança Documental — BLOOMBERG_MAIL

| Campo | Valor |
|---|---|
| **ID** | BLOOMBERG-MAIL-GOVERNANCA-README |
| **Projeto** | BLOOMBERG_MAIL |
| **Repositório** | [carlos-andrade/BLOOMBERG_MAIL](https://github.com/carlos-andrade/BLOOMBERG_MAIL) |
| **Tipo documental** | POLITICA_LOCAL_DE_ADOCAO |
| **Fase** | GOVERNANCA — adoção central |
| **Estado** | EM_REVISAO |
| **Versão** | 2.0.0 |
| **SHA-256 (conteúdo canónico)** | CALCULAR_APOS_PUBLICACAO |
| **Commit de referência (versão anterior)** | [3184dc41488055faf9550faaf78561b7b216d4e8](https://github.com/carlos-andrade/BLOOMBERG_MAIL/commit/3184dc41488055faf9550faaf78561b7b216d4e8) |
| **Data de criação** | 2026-10-08 |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Responsável pelo repositório BLOOMBERG_MAIL |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Regras centrais da GOVERNANCA |
| **Autoridade superior** | [CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |
| **Rastreabilidade** | [Auditoria de governação](./AUDITORIA_GOVERNANCA_2026-10-13.md); [registo de adoção](./REGISTO_ADOCAO_GOVERNANCA_CENTRAL.md) |
| **Escopo** | Governança documental e operacional do BLOOMBERG_MAIL |
| **Objetivo** | Definir a precedência das regras centrais e documentar o estado real de adoção |
| **Dependências** | Ratificação da norma central; validação automatizada; migração documental revisada |

## Contexto Histórico

O BLOOMBERG_MAIL utilizava uma convenção documental local herdada de outro repositório. A GOVERNANCA central passa a ser a fonte superior de princípios e padrões; os artefactos locais mantêm a execução e as evidências específicas do projeto.

## Estado

A adoção central está **parcialmente implementada**. A norma de cabeçalho central consultada ainda está em estado de proposta para validação; por isso, os seus critérios são usados como alvo técnico de auditoria, sem alegar ratificação formal. Documentos históricos não foram migrados em massa.

## Evidências

- [Repositório central GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA).
- [Constituição central](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md).
- [Norma de cabeçalho](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md).
- [Checklist central](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/CHECKLIST-VALIDACAO.md).
- [Auditoria local](./AUDITORIA_GOVERNANCA_2026-10-13.md).
- [Validador de cabeçalhos](../scripts/validar_cabecalho_documental.py).
- [Workflow de validação](../.github/workflows/bloomberg-mail-governanca-cabecalho.yml).

## Validação

O validador verifica a presença da tabela Markdown canónica, metadados, integridade SHA-256 segundo a regra central, cadeia de autoridade, estrutura de secções, IDs duplicados e ligações relativas. O inventário legado ainda gera achados; estes são apresentados como dívida documental e não equivalem a aprovação. A CI executa cinco testes unitários, atualmente aprovados no run [38477537938](https://github.com/carlos-andrade/BLOOMBERG_MAIL/actions/runs/38477537938).

## Resultado

O workflow de migração em massa foi restringido a acionamento manual; o gatilho automático por `push` foi removido para impedir reescritas não revistas em `main`. A migração total está pendente de aprovação formal da norma e de execução por lotes auditáveis.

## Próxima Ação

Rever os relatórios novos afetados pelo migrador legado, corrigir em branch/PR e executar a migração documental por lotes após ratificação da norma. Antes de produção, concluir a auditoria de permissões, branch protection, segredos, runtime WATCHDOG, heartbeat independente e recuperação.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-08 | Governança documental inicial | Histórico Git |
| 2.0.0 | 2026-10-13 | Adoção da GOVERNANCA central como autoridade; registo de achados e suspensão do migrador automático por push | Auditoria local e workflows |
