---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DECISAO_TECNICA"
fase: "FASE-04-PREPARACAO-GRAVADOR"
id_documento: "BLOOMBERG-MAIL-RTD-DEC-004"
titulo: "Decisões confirmadas para o gravador de snapshots RTD"
status: "DECISOES_CONFIRMADAS; PERSISTENCIA_DESATIVADA"
versao: "1.0"
data_criacao: "2026-10-13"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
---



# Decisões confirmadas — gravador RTD FASE04

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DECISAO_TECNICA
> **Fase:** FASE-04-PREPARACAO-GRAVADOR
> **ID:** BLOOMBERG-MAIL-RTD-DEC-004
> **Status:** DECISOES_CONFIRMADAS; PERSISTENCIA_DESATIVADA
> **Versão:** 1.0
> **Criação:** 2026-10-13
> **Atualização:** N/A
> **Origem:** N/A
> **Autoridade:** LAYOUT
> **Rastreabilidade:** N/A


## Decisões do utilizador

1. **Formato do livro Excel:** `.xlsm`, para preservar suporte a VBA.
2. **Destino do histórico:** nova folha denominada `HISTORICO_RTD`, no mesmo livro.
3. **Regra de captura:** criar uma linha completa por cada snapshot válido que difira do último snapshot válido aceite; alterações simultâneas em vários campos formam uma única linha.
4. **Salvaguarda obrigatória:** manter a persistência desativada até os testes integrados serem aprovados e existir autorização expressa para ativar a gravação.

## Contrato funcional proposto

- A origem monitorizada permanece `Folha1!A2:AL2`; confirmar os cabeçalhos e o mapeamento no livro de trabalho atual antes de implementar.
- A primeira observação válida estabelece o baseline e não cria linha de histórico.
- Um snapshot válido sem diferenças não cria linha.
- Um snapshot válido com uma ou mais diferenças cria exatamente uma linha com o snapshot completo, não apenas as células alteradas.
- O timestamp de receção deve ser separado da hora fornecida pelo feed. Se for registado um fuso/offset, deve ser explícito e coerente.
- Erros de célula, valores em falta, desconexão e recuperação devem ter estados de qualidade explícitos; não devem ser convertidos silenciosamente em valores normais.
- A referência de comparação só deve avançar depois de a gravação ser confirmada. Durante a fase atual, como a persistência está desativada, o protótipo não escreve no histórico.
- O código não pode alterar as células de origem, bloquear desnecessariamente o recálculo, enviar ordens ou automatizar trading.
- O livro e os dados operacionais são locais. O ficheiro de dados não deve ser versionado no Git; só código, especificações e evidências não sensíveis podem ser publicados.

## Segurança e estado de ativação

**PERSISTÊNCIA DESATIVADA.** Esta decisão não é autorização para escrever linhas automaticamente. Qualquer ativação exige:
1. confirmação do mapeamento no `.xlsm` de teste;
2. aprovação dos testes integrados de deteção, integridade, erros, reinício e falha de escrita;
3. validação de que o livro operacional está excluído do Git;
4. autorização expressa do utilizador depois de apresentados os resultados.

## Próximas ações

1. Confirmar o livro `.xlsm` de teste e os cabeçalhos atuais de `Folha1!A1:AL2`.
2. Especificar as colunas de `HISTORICO_RTD`: número sequencial, timestamp de receção, instrumento, estado/qualidade, versão do esquema e todos os campos do snapshot.
3. Implementar primeiro um modo de diagnóstico sem persistência, com contagem/validação de eventos e tratamento explícito de erros.
4. Executar os testes integrados antes de qualquer escrita persistente.
5. Só após aprovação, solicitar autorização explícita para ativar a gravação.

## Relação com a especificação anterior

Este documento regista as escolhas de destino e formato para a especificação `BLOOMBERG-MAIL-RTD-CAP-003`. Não substitui os critérios de teste já definidos nessa especificação; complementa-os.

## Estado

**Decisões de desenho confirmadas. Implementação de gravação pendente. Persistência desativada.**
