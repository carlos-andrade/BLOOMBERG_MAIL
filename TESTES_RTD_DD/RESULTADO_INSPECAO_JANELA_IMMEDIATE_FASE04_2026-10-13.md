# Resultado de inspeção visual — FASE04 Excel/RTD

- **Data:** 2026-10-13
- **Evidência:** captura de ecrã fornecida pelo utilizador
- **Âmbito:** inspeção visual; não execução independente
- **Persistência:** desativada

## Observação

A captura mostra o Editor VBA com o menu `Depurar` aberto e a janela Immediate contendo várias linhas `CHANGED`, com timestamp e diferenças entre valores. A opção de compilação não é visível/disponível no menu apresentado.

## Conclusão provisória

Existe evidência visual de que o código está a emitir mensagens `CHANGED`. Isto é progresso face ao registo anterior em que a janela Immediate permanecia vazia. A imagem não basta para demonstrar que cada mensagem representa uma alteração RTD real distinta; o volume de linhas sugere verificar se a comparação está a registar mudanças legítimas ou variações/recálculos excessivos.

A ausência da opção de compilação no menu mostrado não prova erro de sintaxe. Não alterar o código apenas por esse motivo.

## Próximos passos

1. Interromper qualquer tentativa de ativar persistência; não inserir linhas nem gravar ficheiros.
2. Na janela Immediate, executar separadamente `? Application.EnableEvents` e `? Application.Calculation` e registar os valores devolvidos.
3. Confirmar se os timestamps e as mudanças de valores coincidem com a atividade real do mercado/RTD.
4. Avaliar uma redução de mensagens `UNCHANGED` e um tratamento explícito de erros, mas só após preservar o código atual e recolher os resultados do teste.
5. Manter dados operacionais locais e fora do Git.

## Estado

**Deteção de mensagens `CHANGED`: observada visualmente. Validação de correção e granularidade: pendente. Persistência: desativada.**
