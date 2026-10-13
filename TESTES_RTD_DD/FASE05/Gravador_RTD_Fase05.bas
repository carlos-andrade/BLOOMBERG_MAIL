Attribute VB_Name = "modGravadorRTD"
Option Explicit

' FASE 05 — estrutura e validação dos cabeçalhos.
' Persistência intencionalmente DESATIVADA.
Private Const RTD_PERSISTENCE_ENABLED As Boolean = False
Private Const SOURCE_SHEET As String = "Folha1"
Private Const HISTORY_SHEET As String = "HISTORICO_RTD"

Public Sub PrepararEValidarHistoricoRTD()
    Dim wb As Workbook
    Dim wsSource As Worksheet
    Dim wsHistory As Worksheet
    Dim sourceHeaders As Variant
    Dim expected As Variant
    Dim i As Long

    On Error GoTo ErrorHandler
    Set wb = ThisWorkbook
    Set wsSource = wb.Worksheets(SOURCE_SHEET)
    sourceHeaders = wsSource.Range("A1:AL1").Value2

    If UBound(sourceHeaders, 2) <> 38 Then
        Err.Raise vbObjectError + 501, "PrepararEValidarHistoricoRTD", _
                  "O intervalo de origem não contém 38 colunas."
    End If

    Set wsHistory = GetOrCreateHistorySheet(wb, HISTORY_SHEET)
    expected = Array("Timestamp_Observacao", "Sequencia_Snapshot", _
                     "Campos_Alterados", "Estado_Validacao")

    For i = 0 To 3
        wsHistory.Cells(1, i + 1).Value = expected(i)
    Next i

    For i = 1 To 38
        If Len(Trim$(CStr(sourceHeaders(1, i)))) = 0 Then
            Err.Raise vbObjectError + 502, "PrepararEValidarHistoricoRTD", _
                      "Cabeçalho vazio na origem: " & wsSource.Cells(1, i).Address(False, False)
        End If
        wsHistory.Cells(1, i + 4).Value = sourceHeaders(1, i)
    Next i

    With wsHistory.Range("A1:AP1")
        .Font.Bold = True
        .WrapText = True
        .AutoFilter
    End With
    wsHistory.Rows(1).RowHeight = 32
    wsHistory.Range("A1:AP1").EntireColumn.AutoFit
    wsHistory.Columns("A").NumberFormat = "yyyy-mm-dd hh:mm:ss"
    wsHistory.Columns("B").NumberFormat = "0"

    Debug.Print Format$(Now, "yyyy-mm-dd hh:nn:ss") & _
                " | HEADER_CHECK | campos=38 | colunas_totais=42 | persistencia=DESATIVADA"
    MsgBox "Cabeçalhos HISTORICO_RTD preparados e validados." & vbCrLf & _
           "38 campos de origem + 4 metadados = 42 colunas." & vbCrLf & _
           "Persistência automática permanece DESATIVADA.", vbInformation
    Exit Sub

ErrorHandler:
    Debug.Print Format$(Now, "yyyy-mm-dd hh:nn:ss") & _
                " | ERROR | " & Err.Number & " | " & Err.Description
    MsgBox "Falha ao preparar HISTORICO_RTD: " & Err.Number & vbCrLf & _
           Err.Description, vbExclamation
End Sub

Private Function GetOrCreateHistorySheet(ByVal wb As Workbook, _
                                         ByVal sheetName As String) As Worksheet
    On Error Resume Next
    Set GetOrCreateHistorySheet = wb.Worksheets(sheetName)
    On Error GoTo 0

    If GetOrCreateHistorySheet Is Nothing Then
        Set GetOrCreateHistorySheet = wb.Worksheets.Add(After:=wb.Worksheets(wb.Worksheets.Count))
        GetOrCreateHistorySheet.Name = sheetName
    End If
End Function

Public Function PersistenciaRTDAutorizada() As Boolean
    PersistenciaRTDAutorizada = RTD_PERSISTENCE_ENABLED
End Function
