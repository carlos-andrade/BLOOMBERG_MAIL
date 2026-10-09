---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "EVIDENCIA_DE_TESTE"
fase: "FASE04"
id_documento: "BLOOMBERG-MAIL-RTD-FASE04-SEM-SAIDA-2026-10-10"
titulo: "Resultado do teste Excel/RTD FASE04 — janela imediata sem saída"
status: "BLOQUEADO_POR_DIAGNOSTICO"
versao: "1.0"
data_criacao: "2026-10-10"
data_atualizacao: "2026-10-10"
origem: "Relato do utilizador"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
---

# Resultado do teste Excel/RTD FASE04 — janela imediata sem saída

## Resultado observado

O utilizador confirmou:
- o código está no módulo de código da folha `Folha1`;
- a janela Verificação imediata (`Ctrl+G`) continuou vazia;
- a gravação persistente continua desativada.

Não foi fornecida confirmação de que a compilação VBA terminou sem erros nem de que a janela imediata foi testada com uma expressão direta. Portanto, ainda não é possível concluir que o evento não dispara: pode haver um problema de configuração, compilação, eventos desativados ou ausência de saída no caminho executado.

## Próximo diagnóstico — não persistente

Executar no livro de diagnóstico, não no workbook original:
1. Abrir o Editor VBA com `Alt+F11`.
2. Abrir a Verificação imediata com `Ctrl+G`.
3. Na linha de entrada da janela, escrever `? Application.EnableEvents` e premir Enter. O resultado esperado é `True` ou `False`.
4. Se o resultado for `False`, escrever `Application.EnableEvents = True` e premir Enter. Isto reativa os eventos da aplicação Excel nessa sessão; não grava dados de mercado.
5. Escrever `? Application.Calculation` e premir Enter para verificar o modo de cálculo.
6. Voltar a `Folha1` e selecionar **Depurar > Compilar VBAProject**. Se existir erro, parar e registar a mensagem exata.
7. Se a janela imediata aceitar comandos, mas continuar sem mensagens do evento, inspecionar o procedimento `Worksheet_Calculate` e confirmar se existe um `Debug.Print` alcançável no início do procedimento. Não substituir nem duplicar o código às cegas.
8. Só depois de a compilação passar, provocar um recálculo no livro de diagnóstico e verificar se a linha de diagnóstico aparece.

## Critério de interpretação

- Se `? Application.EnableEvents` não produzir resultado, primeiro diagnosticar a utilização da janela imediata/projeto VBA ativo.
- Se devolver `False`, reativar eventos e repetir o teste.
- Se devolver `True`, compilar e verificar o código do evento.
- Se o código compilar, os eventos estiverem ativos e ainda não houver saída, solicitar captura de ecrã da janela de código de `Folha1` e da janela imediata para inspeção antes de qualquer modificação adicional.

## Segurança e estado

- Nenhuma linha de mercado foi gravada.
- Nenhum snapshot foi persistido.
- Não inserir linhas nem alterar fórmulas RTD nesta fase.
- A primeira leitura válida continua a ser apenas baseline em memória.
- A gravação persistente continua desativada até aprovação dos testes integrados e autorização expressa do utilizador.
- Este registo documenta o resultado reportado; não afirma execução independente no computador do utilizador.
