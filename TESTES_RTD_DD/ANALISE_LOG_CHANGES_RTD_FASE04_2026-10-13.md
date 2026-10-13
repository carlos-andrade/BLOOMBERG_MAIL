# Análise do log `CHANGED` — FASE04

- **Data da análise:** 2026-10-13
- **Fonte:** `Texto colado.txt` enviado pelo utilizador
- **Âmbito:** análise dos registos apresentados no ficheiro; não validação independente do Excel
- **Persistência:** desativada

## Observações do ficheiro

O ficheiro contém 40 linhas de log com estado `CHANGED`: 39 registos no intervalo aproximado 13:50:40–13:51:59 e um registo posterior às 14:11:37. Nos registos sequenciais da primeira série, os timestamps avançam geralmente 2 segundos. Cada mensagem compara valores anteriores e atuais de várias células de `A2:AL2`; a contagem indicada de campos alterados varia, nos exemplos visíveis, de 8 a 22.

## Conclusão suportada

O log demonstra que o procedimento de diagnóstico está a emitir repetidamente mensagens `CHANGED` e a identificar diferenças entre snapshots consecutivos. Os dados apresentados são consistentes com observação periódica de valores RTD que mudam.

O log **não demonstra** que tenham sido inseridas linhas na folha de histórico nem que exista persistência em disco. Também não prova, isoladamente, que cada alteração seja uma atualização atómica e sincronizada de todos os campos RTD.

## Risco técnico a investigar

Os campos são comparados no momento de `Worksheet_Calculate`. Como vários tópicos RTD podem atualizar em momentos diferentes, um snapshot pode combinar valores de instantes próximos, mas não idênticos. Antes de gravar histórico, é necessário definir se o objetivo é capturar o estado observado a cada ciclo de aproximadamente 2 segundos ou exigir sincronização/estabilidade dos campos.

## Próximos passos

1. Preservar a versão atual do código e o log como evidência.
2. Confirmar se a necessidade é uma linha persistente na folha por cada snapshot alterado, ou apenas registo de diagnóstico na janela Immediate.
3. Validar a consistência do snapshot e o esquema de colunas antes de implementar qualquer gravação.
4. Manter a persistência desativada até testes integrados aprovados e autorização expressa.

## Estado

**Deteção repetida de alterações: demonstrada pelo log. Gravação de histórico: não demonstrada. Persistência: desativada.**
