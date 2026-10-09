---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-DIAGNOSTICO-EXCEL-RTD-SEM-GRAVACAO-FASE04-MD"
titulo: "BLOOMBERG_MAIL — Diagnóstico Excel/RTD sem gravação"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/DIAGNOSTICO_EXCEL_RTD_SEM_GRAVACAO_FASE04.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-DIAGNOSTICO-EXCEL-RTD-SEM-GRAVACAO-FASE04-MD"
titulo: "BLOOMBERG_MAIL — Diagnóstico Excel/RTD sem gravação"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/DIAGNOSTICO_EXCEL_RTD_SEM_GRAVACAO_FASE04.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — Diagnóstico Excel/RTD sem gravação

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** N/A
> **ID:** BLOOMBERG-MAIL-TESTES-RTD-DD-DIAGNOSTICO-EXCEL-RTD-SEM-GRAVACAO-FASE04-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


# BLOOMBERG_MAIL — Diagnóstico Excel/RTD sem gravação

**Data:** 2026-10-09  
**Fase:** FASE04 — diagnóstico integrado  
**Workbook esperado:** RDT_PROFIT.xlsx  
**Folha:** Folha1  
**Intervalo monitorizado:** A2:AL2  
**Estado:** especificação preparada; teste no Excel real pendente.

## 1. Objetivo

Confirmar se as alterações das fórmulas RTD são observáveis pelo evento `Worksheet_Calculate`, sem inserir linhas, alterar células, escrever ficheiros ou ativar captura persistente.

O código é exclusivamente diagnóstico. Imprime no painel Immediate do Editor VBA os endereços e valores alterados. A primeira leitura válida estabelece baseline e não é registada como alteração.

## 2. Preparação segura

1. Fechar o workbook original sem o modificar.
2. Criar uma cópia de diagnóstico local, fora do repositório versionado.
3. Abrir a cópia no Excel e confirmar que a folha se chama `Folha1` e os dados RTD estão em `A2:AL2`.
4. Guardar uma cópia de segurança antes de abrir o Editor VBA.
5. No Editor VBA (Alt+F11), abrir o módulo de código da folha `Folha1` e colar o código abaixo.
6. Abrir o painel Immediate com Ctrl+G.
7. Compilar o projeto VBA (Debug > Compile VBAProject) antes de executar.
8. Não adicionar código de escrita, inserção de linhas ou gravação de ficheiros nesta fase.

## 3. Código de diagnóstico — módulo da folha Folha1

O evento tem de ficar no módulo de código da própria folha, não num módulo normal.

```vb
Option Explicit

Private mBaseline As Variant
Private mHasBaseline As Boolean
Private mBusy As Boolean

Private Sub Worksheet_Calculate()
    Dim current As Variant
    Dim c As Long
    Dim changedCount As Long
    Dim details As String
    Dim cellValue As Variant
    Dim oldValue As Variant

    If mBusy Then Exit Sub
    mBusy = True
    On Error GoTo SafeExit

    current = Me.Range("A2:AL2").Value2

    ' Um erro RTD/Excel invalida a observação inteira.
    ' A referência anterior é preservada.
    For c = 1 To UBound(current, 2)
        If IsError(current(1, c)) Then
            Debug.Print Format$(Now, "yyyy-mm-dd hh:nn:ss"); _
                " | INVALID | erro de célula em "; _
                Me.Cells(2, c).Address(False, False)
            GoTo SafeExit
        End If
    Next c

    If Not mHasBaseline Then
        mBaseline = current
        mHasBaseline = True
        Debug.Print Format$(Now, "yyyy-mm-dd hh:nn:ss"); _
            " | BASELINE | A2:AL2 | sem registo"
        GoTo SafeExit
    End If

    For c = 1 To UBound(current, 2)
        cellValue = current(1, c)
        oldValue = mBaseline(1, c)

        If IsDifferent(cellValue, oldValue) Then
            changedCount = changedCount + 1
            details = details & Me.Cells(2, c).Address(False, False) _
                & ": [" & SafeText(oldValue) & "] -> [" _
                & SafeText(cellValue) & "]; "
        End If
    Next c

    If changedCount = 0 Then
        Debug.Print Format$(Now, "yyyy-mm-dd hh:nn:ss"); _
            " | UNCHANGED | A2:AL2"
    Else
        Debug.Print Format$(Now, "yyyy-mm-dd hh:nn:ss"); _
            " | CHANGED | campos="; changedCount; " | "; details

        ' Atualização apenas da referência em memória.
        ' Nenhuma linha é inserida e nenhum ficheiro é escrito.
        mBaseline = current
    End If

SafeExit:
    mBusy = False
End Sub

Private Function IsDifferent(ByVal a As Variant, ByVal b As Variant) As Boolean
    If IsEmpty(a) And IsEmpty(b) Then
        IsDifferent = False
    ElseIf IsNull(a) Or IsNull(b) Then
        IsDifferent = (IsNull(a) Xor IsNull(b))
    ElseIf VarType(a) <> VarType(b) Then
        IsDifferent = True
    Else
        IsDifferent = (a <> b)
    End If
End Function

Private Function SafeText(ByVal v As Variant) As String
    If IsEmpty(v) Then
        SafeText = "<EMPTY>"
    ElseIf IsNull(v) Then
        SafeText = "<NULL>"
    ElseIf IsError(v) Then
        SafeText = "<CELL_ERROR>"
    Else
        SafeText = CStr(v)
    End If
End Function
```

## 4. Critérios de aceitação

- Compilação VBA sem erros.
- A primeira observação válida mostra `BASELINE`.
- Recalcular sem alteração mostra `UNCHANGED`.
- Alteração em uma ou mais células mostra um único evento `CHANGED` com a lista dos campos alterados.
- Erro em qualquer célula mostra `INVALID` e não avança a referência.
- O número de linhas da folha permanece inalterado.
- Nenhum ficheiro de histórico é criado.
- O código não altera valores ou fórmulas do intervalo monitorizado.

## 5. Limitações conhecidas

- O evento `Worksheet_Calculate` depende de o Excel recalcular a folha. Se o servidor RTD atualizar sem provocar esse evento, será necessário estudar polling controlado numa fase separada.
- O painel Immediate é volátil e não constitui histórico persistente.
- Esta observação compara snapshots no instante em que o evento é executado; não garante a captura de todos os ticks/negócios entre duas observações.
- A comparação é de valores expostos em A2:AL2. Não deteta alterações internas do fornecedor que não se reflitam nesses valores.
- A variável de baseline é perdida ao fechar/reiniciar o workbook, intencionalmente nesta fase.

## 6. Plano de execução

1. Executar primeiro numa cópia local, com mercado fechado, e confirmar baseline/unchanged.
2. Na próxima sessão de mercado, observar se aparecem eventos `CHANGED` ao variar os valores RTD.
3. Registar manualmente o resultado observado, incluindo hora e comportamento, sem incluir dados pessoais ou credenciais.
4. Se o evento não disparar, não ativar persistência; investigar polling/RTD em separado.
5. Só após validação diagnóstica se desenha o gravador de linhas, que continuará desativado até aprovação explícita.

## 7. Roadmap

| Etapa | Estado |
|---|---|
| Testes sintéticos do comparador | 10/10 aprovados |
| Workflow de CI publicado | Publicado; execução remota por confirmar |
| Código de diagnóstico sem gravação | Preparado neste documento |
| Compilação e teste na cópia do Excel | Pendente |
| Teste RTD ao vivo | Pendente |
| Teste de persistência e recuperação | Pendente |
| Gravação automática de linhas | Desativada; não autorizada |
