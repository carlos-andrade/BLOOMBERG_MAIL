---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-AUDITORIA-CODIGO-FOLHA1-CLS-FASE04-2026-10-13-MD"
titulo: "Auditoria do código VBA `Folha1.cls` — FASE04"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/AUDITORIA_CODIGO_FOLHA1_CLS_FASE04_2026-10-13.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-AUDITORIA-CODIGO-FOLHA1-CLS-FASE04-2026-10-13-MD"
titulo: "Auditoria do código VBA `Folha1.cls` — FASE04"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/AUDITORIA_CODIGO_FOLHA1_CLS_FASE04_2026-10-13.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# Auditoria do código VBA `Folha1.cls` — FASE04

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** N/A
> **ID:** BLOOMBERG-MAIL-TESTES-RTD-DD-AUDITORIA-CODIGO-FOLHA1-CLS-FASE04-2026-10-13-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


# Auditoria do código VBA `Folha1.cls` — FASE04

- **Data:** 2026-10-13
- **Objeto:** ficheiro `Folha1.cls` fornecido para revisão
- **Âmbito:** inspeção estática; não execução no Excel
- **Persistência:** continua desativada

## Resultado

A estrutura geral é compatível com o diagnóstico sem gravação: o evento `Worksheet_Calculate` lê `A2:AL2`, estabelece um baseline em memória, compara observações subsequentes e emite `BASELINE`, `UNCHANGED`, `CHANGED` ou `INVALID`. A atualização do baseline ocorre apenas depois de uma observação válida e quando existe alteração. O ficheiro não contém comandos para inserir linhas, escrever ficheiros ou ativar persistência.

## Pontos corretos

1. O procedimento `Worksheet_Calculate` está declarado com o nome esperado para o módulo da folha.
2. O baseline inicial não gera registo persistente.
3. Alterações em vários campos são agrupadas numa única mensagem `CHANGED`.
4. Uma célula com erro invalida a observação inteira e preserva o baseline anterior.
5. `mBusy` evita reentrada simultânea no procedimento.

## Riscos e limitações encontrados

### 1. Erros de execução ficam silenciosos — prioridade alta

`On Error GoTo SafeExit` encaminha qualquer erro de execução para uma saída que apenas repõe `mBusy = False`. Se ocorrer um erro noutra operação que não seja o teste explícito de erro de célula, o diagnóstico pode terminar sem explicar a causa. Isto pode produzir uma janela Immediate sem `CHANGED` e sem mensagem de erro.

**Correção recomendada, após confirmação do teste atual:** adicionar um bloco `ErrorHandler` separado que imprima número e descrição do erro antes de sair, mantendo a recuperação segura de `mBusy`.

### 2. `UNCHANGED` é impresso em todas as recalculações

Quando o snapshot não muda, o evento escreve uma linha `UNCHANGED` em cada execução. Se a folha recalcular frequentemente, a janela Immediate pode ficar inundada e dificultar a identificação do primeiro `CHANGED`.

**Correção recomendada:** limitar a saída de diagnóstico de snapshots inalterados, por exemplo, não imprimir `UNCHANGED` em cada cálculo, ou adotar um mecanismo de amostragem explícito. Não introduzir timers nem persistência nesta fase.

### 3. O evento depende de recálculo da folha

A presença do evento no módulo correto não prova que o Excel esteja a dispará-lo para cada atualização do servidor RTD. É necessário observar o comportamento real durante uma sessão com dados RTD em mudança.

### 4. Inspeção estática não equivale a compilação

O ficheiro exportado não foi compilado pelo editor VBA nem executado nesta auditoria. A sintaxe e o comportamento no Excel real continuam por confirmar.

## Próximos passos controlados

1. No Excel, confirmar que o Immediate apresenta os resultados das expressões de diagnóstico e que `Application.EnableEvents` está ativo.
2. Compilar o projeto VBA no editor, sem ativar qualquer gravador.
3. Durante a sessão de mercado, observar uma alteração RTD real e recolher a saída exata.
4. Se não aparecer `CHANGED`, recolher a saída de erro após introduzir tratamento explícito de erros; não alterar o código por tentativa e erro.
5. Só considerar qualquer mecanismo de gravação depois de testes integrados aprovados e autorização expressa.

## Estado

**Aprovado apenas para revisão estática preliminar. FASE04 ainda não validada funcionalmente. Gravação persistente desativada.**
