---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "ARQUITETURA_OPERACIONAL_LOCAL"
fase: "FASE-01-PREPARACAO-LOCAL"
id_documento: "BLOOMBERG-MAIL-ARQ-LOCAL-RTD-001"
titulo: "Arquitetura local — RTD/Profit e sincronização Git manual"
status: "PREPARACAO_LOCAL_EXECUTADA; REVISAO_GIT_E_CAPTURA_PENDENTES"
versao: "1.1"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "Aprovação do utilizador para arquitetura local"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
escopo: "Ambiente Windows local e preparação segura do clone Git"
---

# Arquitetura local — RTD/Profit e sincronização Git manual

## 1. Contexto histórico

Em 2026-10-09, foi aprovada a arquitetura local do projeto BLOOMBERG_MAIL com os seguintes parâmetros:
- Raiz Windows confirmada pelo utilizador: `D:\BLOOMBERG_MAIL`
- Repositório GitHub: público, `carlos-andrade/BLOOMBERG_MAIL`
- Captura futura: por alteração observada
- Sincronização Git: manual
- Preservação obrigatória: não modificar nem substituir os ficheiros RTD existentes nesta fase.

A preparação local foi executada pelo utilizador em 2026-10-09. A saída do PowerShell confirmou a criação do clone e das pastas. A verificação local é evidência fornecida pelo utilizador, não execução remota deste assistente.

## 2. Inspeção inicial

Na inspeção de `main` foram encontrados, entre outros:
- `TESTES_RTD_DD/RDT_PROFIT.xlsx`
- auditoria estática do workbook e evidências CSV/Markdown;
- `WATCHDOG/ARQUITETURA.md`, documentação de deploy e cartas/layouts de feeds;
- `scripts/`, `GOVERNANCA/`, `FONTES/`, `INTELIGENCIA/`, `EMAILS_RECEBIDOS/` e workflows em `.github/workflows/`.

Não foi encontrado um `.gitignore` na raiz. Já existe `WATCHDOG/.gitignore`, que não substitui uma política geral da raiz.

A auditoria disponível indica 36 fórmulas RTD, 38 colunas e o identificador `WINFUT_F_0`; a atualização ao vivo e a reconexão continuam por validar no computador com Profit.

## 3. Estrutura local

O script `scripts/windows/preparar_ambiente_local.ps1` prepara esta estrutura sem eliminar conteúdos existentes:

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

Os dados operacionais ficam fora do clone Git. Esta separação reduz o risco de adicionar acidentalmente dados de mercado, logs e backups ao repositório público.

## 4. Comportamento do script de preparação

O script:
1. verifica se o comando `git` está disponível;
2. verifica, antes de usar um clone existente, se o destino é um repositório Git e se o remoto `origin` corresponde ao projeto esperado;
3. cria apenas diretórios em falta;
4. clona o repositório apenas quando o destino ainda não existe;
5. não faz pull, commit, push nem inicia a captura;
6. não abre nem altera o Excel;
7. falha de forma explícita se encontrar um destino ambíguo ou um remoto inesperado.

Execução prevista em PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
& "D:\CAMINHO\PARA\preparar_ambiente_local.ps1"
```

O utilizador deve substituir o caminho pelo local onde guardou o script obtido do repositório. A política de execução é alterada apenas para o processo atual; não se recomenda alterar a política global do Windows.

## 5. Política Git e publicação

A sincronização é manual. Antes de qualquer commit:
1. executar `git status --short --branch`;
2. rever a lista de ficheiros alterados;
3. confirmar que não há dados brutos, credenciais, logs operacionais ou configurações privadas;
4. adicionar apenas caminhos aprovados;
5. rever o diff e os ficheiros staged;
6. criar commit com mensagem específica;
7. executar `git push` apenas depois da revisão;
8. confirmar o SHA do commit publicado.

Comandos de inspeção:

```powershell
git -C "D:\BLOOMBERG_MAIL\repo\BLOOMBERG_MAIL" status --short --branch
git -C "C:\BLOOMBERG_MAIL\repo\BLOOMBERG_MAIL" remote -v
git -C "C:\BLOOMBERG_MAIL\repo\BLOOMBERG_MAIL" check-ignore -v dados_locais logs backups configuracao_local
```

O último comando é uma verificação útil apenas para caminhos dentro do clone. A arquitetura recomendada mantém os dados operacionais fora do clone desde o início.

## 6. Política de exclusão

O `.gitignore` da raiz exclui pastas locais comuns, segredos, caches e livros `.xlsm` por defeito. O workbook original `RDT_PROFIT.xlsx` permanece rastreável porque é um ficheiro existente do projeto e não se aplica uma exclusão geral a `.xlsx`.

Importante: `.gitignore` não remove do Git ficheiros que já estejam rastreados. Antes de publicar, deve-se verificar o estado real com `git status` e rever o conteúdo a adicionar. Não executar `git add .` como procedimento de publicação.

O repositório é público. Nenhum dado bruto de mercado ou conteúdo de email deve ser publicado sem avaliação dos direitos de armazenamento/redistribuição e aprovação explícita.

## 7. Captura por alteração — fora do âmbito da Fase 1

A captura por alteração não está implementada nem ativa nesta fase. O futuro gravador deverá:
- preservar as fórmulas RTD atuais;
- detetar mudanças observáveis em campos selecionados, evitando duplicados causados por recálculo;
- gravar os valores como dados estáticos num arquivo local;
- registar falhas e reconexões sem inventar ticks perdidos;
- manter separados timestamp da fonte e timestamp local de observação;
- gerar manifestos com contagens e hashes;
- permanecer independente do acesso à Internet/GitHub.

O Excel/RTD pode expor apenas uma parte das mudanças que ocorreram no mercado. A captura por alteração não equivale a uma garantia de captura integral de todos os negócios/ticks.

## 8. Critérios de aceitação da Fase 1

- [x] Script descarregado e executado no computador Windows (a cópia do script está em Downloads; o clone local contém main).
- [x] Estrutura criada no Windows; diretórios esperados confirmados pela saída PowerShell.
- [x] Clone validado e remoto confirmado pela saída PowerShell.
- [x] Diretórios de dados/logs/backups/configuração criados ao lado do clone, fora dele.
- [ ] `.gitignore` da raiz verificado no clone.
- [x] O script informou que não abriu nem modificou o workbook; a integridade binária posterior não foi revalidada.
- [x] Nenhum commit/push local executado pelo script.
- [x] Evidência da execução registada em VERIFICACAO_FASE01_AMBIENTE_LOCAL_2026-10-09.md.

## 9. Roadmap

| Fase | Objetivo | Estado |
|---|---|---|
| 0 | Inspeção e arquitetura | CONCLUÍDA |
| 1 | Preparação local | EXECUTADA; alinhar documentação e incorporar proteções Git após revisão |
| 2 | Desenho e implementação do gravador RTD | BLOQUEADA até confirmar a estrutura e mapear as células |
| 3 | Arquivo, deduplicação, reconexão e validação | PENDENTE |
| 4 | Publicação Git manual por lista autorizada | PENDENTE |

## 10. Resultado

Foram preparados o `.gitignore` da raiz e um script idempotente. O utilizador executou o script e confirmou o clone em `main`, o remoto `origin` e as pastas locais. A preparação de diretórios está concluída. A revisão da branch do PR, a incorporação do `.gitignore` no clone local e os testes RTD continuam pendentes.

Na validação inicial do utilizador, `D:\BLOOMBERG_MAIL` contém `RDT_PROFIT.xlsx` e o ficheiro temporário do Excel, mas não foi encontrado um clone Git nas subpastas imediatas. O script foi ajustado para usar D: por omissão. A próxima ação é executar a preparação ajustada e validar o clone sem tocar no workbook original. Só depois deve começar o desenho do gravador de alterações RTD.
