---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "ESPECIFICACAO_TECNICA"
fase: "FASE-02-MAPEAMENTO-RTD"
id_documento: "BLOOMBERG-MAIL-RTD-MAP-002"
titulo: "Especificação de mapeamento e captura observável RTD"
status: "ESPECIFICADO; AGUARDA_VALIDACAO_LOCAL"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "Auditoria estática do workbook RDT_PROFIT.xlsx e sincronização local confirmada"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "TESTES_RTD_DD/AUDITORIA_RDT_PROFIT_XLSX_2026-10-09.md; WATCHDOG/TESTE_RTD_DDE_PROFIT_001.md"
escopo: "Definição prévia do mapeamento e dos requisitos de um gravador local; sem executar captura"
objetivo: "Definir um caminho verificável para resolver a ausência de avanço de linha sem perder a distinção entre alterações observadas e ticks completos"
dependencias: "Workbook local; Excel/Profit operacionais; mapeamento de células confirmado; direitos de armazenamento"
---



# Especificação — mapeamento e captura observável RTD

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** ESPECIFICACAO_TECNICA
> **Fase:** FASE-02-MAPEAMENTO-RTD
> **ID:** BLOOMBERG-MAIL-RTD-MAP-002
> **Status:** ESPECIFICADO; AGUARDA_VALIDACAO_LOCAL
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** Auditoria estática do workbook RDT_PROFIT.xlsx e sincronização local confirmada
> **Autoridade:** LAYOUT
> **Rastreabilidade:** TESTES_RTD_DD/AUDITORIA_RDT_PROFIT_XLSX_2026-10-09.md; WATCHDOG/TESTE_RTD_DDE_PROFIT_001.md


## Contexto Histórico

A auditoria estática de 2026-10-09 encontrou a folha `Folha1`, 2 linhas por 38 colunas, 36 fórmulas RTD, o servidor `rtdtrading.rtdserver` e o tópico de instrumento `WINFUT_F_0`. A linha 1 contém os cabeçalhos e a linha 2 contém o registo observado. Estes dados descrevem a cópia auditada e devem ser confirmados no workbook local atual.

O utilizador informou que o Excel continua a receber informações, mas não avança para a linha seguinte. A causa ainda não foi confirmada por teste local.

## Estado

- Auditoria estrutural do ficheiro: PASS, estática.
- Atualização RTD ao vivo: NOT VERIFIED.
- Mapeamento de endereço de cada campo: PENDING.
- Captura persistente: NÃO IMPLEMENTADA.
- Direitos de armazenamento: PENDING.
- Ativação em produção: BLOQUEADA.

## Hipótese técnica a testar

Uma fórmula RTD pode recalcular o seu resultado sem disparar o evento VBA `Worksheet_Change`, que normalmente está associado a alterações feitas nas células. Por isso, não se deve assumir que `Worksheet_Change` sozinho detetará atualizações RTD. A abordagem deverá ser testada com `Worksheet_Calculate` ou polling controlado, evitando escrita recursiva na folha de origem.

## Mapeamento obrigatório

Antes de escrever código, confirmar e registar:

| Item | Estado conhecido | Ação de validação |
|---|---|---|
| Livro e folha | `RDT_PROFIT.xlsx`, `Folha1` na auditoria | Confirmar nome atual |
| Cabeçalhos | 38 colunas reportadas, linha 1 | Exportar nomes e endereços das colunas |
| Linha de dados RTD | Linha 2 reportada | Confirmar quais células contêm fórmulas RTD |
| Chave do instrumento | `WINFUT_F_0` nas fórmulas auditadas | Confirmar símbolo/tópico atual |
| Data e hora | Cabeçalhos `Data` e `Hora` | Confirmar se são tempo de origem ou apenas campos apresentados |
| Estado da ligação | Campo `Estado Atual` reportado | Confirmar valores possíveis e semântica |
| Frequência de cálculo | Desconhecida | Observar mudanças com hora local registada |
| Autorização de armazenamento | Pendente | Confirmar termos antes de persistir dados |

## Requisitos do futuro gravador

1. **Não alterar o workbook de origem:** a captura deve escrever para uma folha de destino separada, um CSV local ou uma base local aprovada.
2. **Não usar a linha de origem como histórico:** os resultados RTD podem atualizar repetidamente a mesma linha.
3. **Deteção:** comparar um snapshot dos campos selecionados após cálculo ou por polling; não depender exclusivamente de `Worksheet_Change`.
4. **Deduplicação:** não gravar repetidamente snapshots idênticos. Definir a assinatura de comparação com os campos selecionados e documentar se a mudança de bid/ask, quantidade, hora ou estado cria novo registo.
5. **Timestamp de receção:** guardar a hora local de receção em formato ISO 8601 com offset/fuso explícito. Não apresentar esse valor como timestamp da bolsa ou do fornecedor.
6. **Timestamp de origem:** guardar separadamente apenas quando a fonte o disponibilizar e a semântica estiver confirmada.
7. **Integridade:** registar número sequencial local, versão do esquema, instrumento, estado do feed e erros.
8. **Falhas:** marcar o estado como `STALE` ou `UNKNOWN` segundo um limite definido após caracterização; nunca reutilizar silenciosamente valores antigos como atuais.
9. **Reconexão:** registar começo/fim da interrupção, recuperação e eventuais gaps observáveis.
10. **Privacidade e licenciamento:** manter dados operacionais fora do clone Git e não publicar amostras de mercado sem autorização explícita.
11. **Sem ordens:** não incluir funções de negociação, envio de ordens ou automatização de trading.
12. **Limite declarado:** o registo de snapshots deteta alterações observadas; não garante capturar todos os ticks, negócios ou estados intermédios que ocorram entre duas leituras.

## Testes de aceitação

- T01 — Mapeamento: cada coluna selecionada tem cabeçalho, endereço, tipo e origem documentados.
- T02 — Atualização: duas ou mais alterações observáveis são refletidas no destino com timestamp local.
- T03 — Deduplicação: snapshot idêntico não cria registo duplicado, salvo regra explícita.
- T04 — Não bloqueio: a captura não impede o recálculo RTD nem escreve nas células de origem.
- T05 — Paragem/retoma: erros e reconexão são registados sem declarar frescura indevida.
- T06 — Persistência: o destino permanece local e excluído do Git.
- T07 — Licença: aprovação dos direitos de armazenamento registada antes da persistência contínua.
- T08 — Regressão: workbook original abre e atualiza depois do teste sem alteração estrutural.

Nenhum teste é considerado PASS sem evidência local. A execução de um teste não deve enviar ordens.

## Próxima Ação

No computador local, confirmar a folha e os endereços das células com as fórmulas RTD e os cabeçalhos. A etapa seguinte será preparar um relatório de mapeamento sem modificar o workbook. Só depois será proposta a implementação do gravador e a execução de testes controlados.
