# BLOOMBERG_MAIL — Correção de instalação do evento Excel/RTD — FASE04

- Projeto: BLOOMBERG_MAIL
- Data: 2026-10-10
- Fase: 04 — diagnóstico Excel/RTD sem gravação
- Estado: instruções corretivas; execução no Excel do utilizador ainda não confirmada
- Segurança: sem escrita persistente, sem inserção de linhas e sem alteração dos valores/fórmulas RTD

## Ocorrência reportada

Foi criado um `Módulo1`, mas a janela Verificação imediata (`Ctrl+G)) não apresentou mensagens.

## Causa provável

O procedimento `Worksheet_Calculate` é um evento de folha e deve ficar no módulo de código da folha `Folha1), dentro do projeto VBA do livro de diagnóstico. Um módulo padrão chamado `Módulo1` não recebe automaticamente esse evento de folha. Isto é uma hipótese provável, não uma causa confirmada.

## Procedimento corretivo

1. Confirmar que está aberto o livro de diagnóstico, e não o original.
2. Premir `Alt+F11) para abrir o Editor do Visual Basic.
3. Mostrar o Explorador de Projetos com `Ctrl+R), se necessário.
4. No projeto VBA do livro de diagnóstico, expandir **Microsoft Excel Objects**.
5. Fazer duplo clique na folha correspondente a `Folha1` (o nome pode aparecer como `Folha1 (Folha1)`).
6. Colocar o código do diagnóstico FASE04 na janela de código dessa folha. O procedimento de evento deve começar com `Private Sub Worksheet_Calculate()` e terminar com `End Sub`.
7. Se o código tiver sido colocado em `Módulo1`, removê-lo dali depois de confirmar que foi copiado integralmente para a folha. Não deixar duas cópias do mesmo procedimento.
8. No Editor VBA, selecionar **Depurar > Compilar VBAProject**. Se surgir erro de compilação, parar e registar a mensagem exata.
9. Abrir a janela Verificação imediata com `Ctrl+G).
10. Voltar ao Excel e, apenas no livro de diagnóstico, forçar um recálculo completo com `Ctrl+Alt+F9). Observar se surge `BASELINE`, `UNCHANGED`, `CHANGED` ou `INVALID`.
11. Com o mercado fechado, o recálculo pode servir para verificar se o evento está ligado, mas não valida a atualização real dos valores RTD durante a sessão.

## Interpretação

- Se surgir `BASELINE`: o evento executou e inicializou a referência em memória.
- Se surgir `UNCHANGED`: o evento executou e não detetou diferença em relação à referência atual.
- Se surgir `CHANGED`: o evento executou e detetou alteração no snapshot.
- Se surgir `INVALID`: registar a mensagem e não avançar para qualquer gravação.
- Se continuar vazio: confirmar o nome do livro/projeto selecionado, se o código está realmente no módulo da folha, se as macros/eventos estão habilitados e se a compilação terminou sem erros. Não ativar persistência.

## Critérios para avançar

Só considerar esta verificação aprovada quando:
- o código estiver no módulo correto da folha;
- a compilação não apresentar erros;
- a janela imediata apresentar evidência reproduzível da execução;
- a alteração real de RTD for verificada durante uma sessão de mercado.

A gravação persistente continua desativada até aos testes integrados serem aprovados e existir autorização expressa do utilizador.
