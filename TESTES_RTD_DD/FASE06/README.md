FASE 06 — Gravador RTD completo

Artefactos preparados localmente:
- Gravador_RTD_Fase06.bas: módulo VBA com baseline, comparação, validação e rotina de escrita em bloco.
- CODIGO_FOLHA1_FASE06.txt: evento Worksheet_Calculate para chamar o módulo.
- Livro XLSM de teste com HISTORICO_RTD e 42 cabeçalhos.

O interruptor RTD_PERSISTENCE_ENABLED permanece False. Enquanto falso, as alterações geram CHANGED_DIAGNOSTIC_ONLY e nenhuma linha é escrita. Uma observação com erro de célula é rejeitada. O código não foi compilado nem executado no Excel real.

Instalação: fazer backup; importar o módulo BAS; substituir o evento existente de Folha1 pelo código TXT sem duplicar o evento; executar PrepararEValidarHistoricoRTD; compilar no VBA; testar baseline, alterações simples e simultâneas, erros RTD e recuperação. Não ativar persistência sem testes integrados aprovados e autorização explícita.

O livro operacional e dados RTD permanecem locais, fora do Git.