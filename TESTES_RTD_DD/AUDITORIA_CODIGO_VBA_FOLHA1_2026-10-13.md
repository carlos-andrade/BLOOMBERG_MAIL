---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-AUDITORIA-CODIGO-VBA-FOLHA1-2026-10-13-MD"
titulo: "Auditoria do código VBA de diagnóstico RTD — 2026-10-13"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/AUDITORIA_CODIGO_VBA_FOLHA1_2026-10-13.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-AUDITORIA-CODIGO-VBA-FOLHA1-2026-10-13-MD"
titulo: "Auditoria do código VBA de diagnóstico RTD — 2026-10-13"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/AUDITORIA_CODIGO_VBA_FOLHA1_2026-10-13.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# Auditoria do código VBA de diagnóstico RTD — 2026-10-13

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** N/A
> **ID:** BLOOMBERG-MAIL-TESTES-RTD-DD-AUDITORIA-CODIGO-VBA-FOLHA1-2026-10-13-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


# Auditoria do código VBA de diagnóstico RTD — 2026-10-13

## Escopo

Auditoria estática do código `Worksheet_Calculate` fornecido para a folha `Folha1`. O código observa `A2:AL2`, mantém uma baseline em memória e escreve mensagens na janela Immediate. Não foi executado no Excel.

## Conclusão

**Aprovado para continuar testes de diagnóstico, com ressalvas. Não aprovado como gravador histórico.** O código não insere linhas, não cria a folha `HISTORICO_RTD` e não persiste snapshots.

## Comportamentos corretos observados

- `Option Explicit` exige declaração de variáveis.
- `mBusy` impede reentrada no evento.
- A leitura de `A2:AL2` é feita em bloco por `.Value2`.
- O primeiro conjunto sem erros é guardado como baseline e não é registado como alteração.
- Alterações simultâneas são agregadas numa única mensagem `CHANGED`.
- Se qualquer célula tiver erro, a observação é rejeitada e a baseline anterior é preservada.
- `SafeText` trata valores vazios, nulos e erros antes de os converter em texto.
- Não existem comandos de persistência no código fornecido.

## Riscos e melhorias necessárias

1. **Tratamento silencioso de erros VBA.** `On Error GoTo SafeExit` encaminha qualquer erro inesperado para uma saída sem diagnóstico. Isto pode esconder falhas na comparação ou no evento. Recomenda-se um bloco `ErrorHandler` que escreva número e descrição do erro em `Debug.Print`, garantindo sempre `mBusy = False` na saída.
2. **Ruído no log.** `UNCHANGED` é impresso em todos os recálculos sem alterações. Em RTD frequente, isto pode inundar a janela Immediate. Para a fase de diagnóstico, considerar registar `UNCHANGED` apenas quando necessário ou contar ocorrências.
3. **Erros RTD repetidos.** Uma célula com erro provoca uma mensagem `INVALID` em cada recálculo. Pode ser útil suprimir mensagens repetidas enquanto o erro persistir, sem alterar a regra de invalidar a observação.
4. **Baseline exclusivamente em memória.** A baseline desaparece quando o módulo da folha é reinicializado ou o livro é fechado/reaberto. O primeiro conjunto válido após reinício passa a ser uma nova baseline; isso é esperado no código atual.
5. **Conversão textual de valores.** `SafeText` usa `CStr`; é suficiente para diagnóstico simples, mas a representação de datas e números pode depender das definições regionais. O texto atual serve para observar alterações, não como formato canónico de histórico.
6. **Comparação tipada.** `IsDifferent` considera alteração quando `VarType` muda. Isto é conservador, mas um mesmo valor apresentado como texto numa execução e número noutra será classificado como alteração. Antes da persistência, é necessário definir a normalização dos campos.

## Plano de teste recomendado

1. Abrir apenas a cópia `RDT_PROFIT_TESTADO.xlsm`.
2. Confirmar `BASELINE` após o primeiro conjunto válido.
3. Confirmar `UNCHANGED` quando nenhum valor muda.
4. Alterar um campo e confirmar uma mensagem `CHANGED` com um campo.
5. Alterar vários campos no mesmo recálculo e confirmar uma única mensagem com todos os campos detetados.
6. Introduzir ou observar um erro RTD e confirmar `INVALID`, sem atualização da baseline.
7. Restaurar valores válidos e observar a comparação com a baseline anterior.
8. Reiniciar o livro e confirmar que é estabelecida uma nova baseline.
9. Confirmar que não há linhas gravadas em `HISTORICO_RTD` nem qualquer persistência automática.

## Decisão operacional

- Manter a persistência desativada.
- Não alterar o livro original.
- Não executar macros sem autorização e sem cópia de teste.
- Não guardar dados operacionais RTD no Git; este documento regista apenas a auditoria técnica.
- Só evoluir para gravador histórico depois dos testes de diagnóstico e de autorização explícita.
