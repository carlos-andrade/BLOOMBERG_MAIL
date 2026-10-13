# Fase 07 — Reconstrução limpa VBA RTD

Reconstrução para corrigir erros de importação e chamada da rotina. Origem: Folha1!A2:AL2 (38 campos). Destino: HISTORICO_RTD (4 metadados + 38 campos = 42 colunas). Persistência continua desativada por RTD_PERSISTENCE_ENABLED = False.

## Instalação
1. Fazer cópia de segurança do livro de teste.
2. Remover ou renomear módulo antigo modGravadorRTD para evitar duplicidade.
3. Importar modGravadorRTD_FASE07.bas através de Alt+F11 > File > Import File. Não colar a linha Attribute VB_Name na janela de código.
4. Em Folha1, manter apenas um evento Worksheet_Calculate e usar o código separado fornecido.
5. Executar Debug > Compile VBAProject.
6. Executar PrepararEValidarHistoricoRTD e verificar mensagens no Immediate.
7. A Fase 07 só é aprovada após compilação e testes no Excel real.

O código não foi compilado nem executado nesta ferramenta. Não guardar dados operacionais de mercado no Git.