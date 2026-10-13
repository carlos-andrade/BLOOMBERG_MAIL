# Módulo VBA — Fase 05: preparar cabeçalhos RTD

Este código-fonte é fornecido como módulo .bas separado. Não foi injetado no projeto VBA do livro.

## Objetivo
Criar/validar HISTORICO_RTD com 4 metadados e os 38 cabeçalhos de Folha1!A1:AL1. Não grava snapshots. A persistência permanece desativada.

## Importação
1. Fazer cópia de segurança do ficheiro XLSM.
2. Abrir a cópia de teste no Excel e pressionar Alt+F11.
3. Usar File > Import File e selecionar Gravador_RTD_Fase05.bas.
4. Executar manualmente PrepararEValidarHistoricoRTD.
5. Confirmar 42 colunas e zero linhas históricas.

## Segurança
- Não executar sobre o livro original sem cópia.
- Não ativar persistência nesta fase.
- Não colocar dados operacionais RTD no Git.
- A auditoria foi estática; a execução em Excel ainda precisa de ser confirmada.
