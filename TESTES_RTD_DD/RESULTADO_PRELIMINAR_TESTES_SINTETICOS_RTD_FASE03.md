---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "RESULTADO_DE_TESTES"
fase: "FASE-03-DETECAO-DE-ALTERACOES-RTD"
id_documento: "BLOOMBERG-MAIL-RTD-RESULT-003A"
titulo: "Resultado preliminar dos testes sintéticos do comparador RTD"
status: "LOGICA PRELIMINAR APROVADA; SCRIPT DO REPOSITORIO AINDA SEM EXECUCAO DIRETA"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "TESTES_RTD_DD/prototipo_comparacao_snapshots_sinteticos.py; TESTES_RTD_DD/PLANO_TESTES_GRAVADOR_RTD_MODO_DIAGNOSTICO_FASE03.md"
---



# Resultado preliminar — testes sintéticos do comparador RTD

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** RESULTADO_DE_TESTES
> **Fase:** FASE-03-DETECAO-DE-ALTERACOES-RTD
> **ID:** BLOOMBERG-MAIL-RTD-RESULT-003A
> **Status:** LOGICA PRELIMINAR APROVADA; SCRIPT DO REPOSITORIO AINDA SEM EXECUCAO DIRETA
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** N/A
> **Autoridade:** LAYOUT
> **Rastreabilidade:** TESTES_RTD_DD/prototipo_comparacao_snapshots_sinteticos.py; TESTES_RTD_DD/PLANO_TESTES_GRAVADOR_RTD_MODO_DIAGNOSTICO_FASE03.md


## Âmbito e limite da evidência

Foi executada localmente uma cópia de teste da lógica do comparador com snapshots exclusivamente sintéticos. Os dez testes passaram. **Esta execução não foi feita a partir do ficheiro descarregado diretamente do repositório; por isso, não constitui ainda prova de execução do artefacto versionado exato.** O próximo passo é executar diretamente `prototipo_comparacao_snapshots_sinteticos.py` no ambiente local ou num workflow de CI e guardar o resultado correspondente.

Não houve ligação ao Excel ou Profit, leitura de valores reais de mercado, escrita de histórico, nem ativação de captura persistente.

## Resultados da execução local da lógica

| Teste | Resultado |
|---|---|
| Snapshot inicial estabelece referência | PASS |
| Snapshot idêntico não gera alteração | PASS |
| Alteração de um campo detetada | PASS |
| Alterações em vários campos formam um evento de comparação | PASS |
| Quantidade muda com último preço constante | PASS |
| Transição para vazio detetada | PASS |
| Snapshot com erro rejeitado e referência preservada | PASS |
| Snapshot vazio rejeitado | PASS |
| Alteração do esquema rejeitada sem avançar referência | PASS |
| Novo snapshot válido torna-se referência seguinte | PASS |

**Resumo da execução local da lógica:** 10 passaram; 0 falharam.

## Interpretação

Os resultados indicam que a lógica de comparação, isoladamente, responde às regras sintéticas definidas. Não demonstram que o Excel/Profit sinalize todas as atualizações RTD, que o mecanismo de observação seja não bloqueante, nem que todos os estados intermédios de mercado sejam capturados.

## Próximas ações

1. Executar diretamente o script versionado e guardar o output integral dos testes.
2. Se aprovado, preparar diagnóstico integrado com Excel/RTD sem persistência.
3. Aguardar sessão ativa de mercado para verificar atualizações reais.
4. Manter a gravação persistente desativada até todos os testes e autorização expressa.
