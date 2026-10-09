---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "PLANO_DE_TESTES"
fase: "FASE-03-DETECAO-DE-ALTERACOES-RTD"
id_documento: "BLOOMBERG-MAIL-RTD-TEST-003"
titulo: "Plano de testes do gravador RTD — modo diagnóstico"
status: "PREPARADO; EXECUCAO LOCAL PENDENTE"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "TESTES_RTD_DD/ESPECIFICACAO_GRAVADOR_RTD_AVANCO_POR_ALTERACAO_FASE03.md"
---



# Plano de testes — gravador RTD em modo diagnóstico

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** PLANO_DE_TESTES
> **Fase:** FASE-03-DETECAO-DE-ALTERACOES-RTD
> **ID:** BLOOMBERG-MAIL-RTD-TEST-003
> **Status:** PREPARADO; EXECUCAO LOCAL PENDENTE
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** N/A
> **Autoridade:** LAYOUT
> **Rastreabilidade:** TESTES_RTD_DD/ESPECIFICACAO_GRAVADOR_RTD_AVANCO_POR_ALTERACAO_FASE03.md


## 1. Objetivo
Demonstrar que o mecanismo deteta diferenças entre snapshots RTD sem acrescentar linhas ao histórico, sem alterar a folha de origem e sem publicar dados de mercado no Git.

## 2. Bloqueio atual
O mercado foi reportado como fechado. Portanto, testes dependentes de atualização RTD real ficam pendentes até à próxima sessão de negociação. Não declarar atualização ao vivo como aprovada com base em testes offline ou em valores em cache.

## 3. Regras de segurança do ensaio
- Não ativar gravação persistente.
- Não alterar nem guardar por cima do workbook original.
- Usar cópia de teste, modo diagnóstico e snapshots sintéticos que não contenham valores reais de mercado.
- O diagnóstico deve emitir apenas contagens, campos alterados e timestamps de teste; não despejar dados reais de mercado para consola, ficheiros versionados ou logs públicos.
- Manter destino de teste fora do Git.
- Não executar ordens nem ligar qualquer função de negociação.

## 4. Testes offline com snapshots sintéticos

| ID | Entrada | Resultado esperado |
|---|---|---|
| OFF-01 | Snapshot inicial válido | Guardar apenas como referência em memória; zero linhas persistidas |
| OFF-02 | Repetir snapshot idêntico | Zero alterações detetadas |
| OFF-03 | Alterar apenas o campo Último | Uma alteração detetada; snapshot completo preparado apenas em memória |
| OFF-04 | Alterar Oferta Compra e Quantidade na mesma leitura | Uma alteração detetada, não duas |
| OFF-05 | Alterar Quantidade sem alterar Último | Alteração detetada |
| OFF-06 | Campo muda de valor para vazio | Diferença detetada; estado classificado explicitamente |
| OFF-07 | Campo contém erro de célula | Snapshot classificado como inválido/degradado conforme regra; não aceitar silenciosamente |
| OFF-08 | Simular falha de escrita | Referência anterior permanece intacta |
| OFF-09 | Repetir após recuperação simulada | Nenhuma duplicação do mesmo snapshot aceite |
| OFF-10 | Parar e reiniciar o diagnóstico | Paragem limpa; referência inicial reinicializada conforme política documentada |

OFF-01 a OFF-10 validam apenas a lógica de comparação, não a ligação RTD nem a captura em tempo real.

## 5. Testes locais na próxima sessão de mercado

1. Confirmar que o Profit está ligado e que as células RTD mudam.
2. Iniciar apenas o diagnóstico, sem escrita em histórico.
3. Registar timestamps locais de observação e contagem de recálculos, sem publicar valores.
4. Confirmar pelo menos duas mudanças independentes em campos monitorizados.
5. Confirmar que snapshots inalterados não produzem eventos de alteração.
6. Verificar se `Worksheet_Calculate` sinaliza as mudanças; se não, avaliar polling controlado.
7. Observar o comportamento em pausa/reconexão, se ocorrer naturalmente; não simular desligamentos que afetem operação real sem autorização.
8. Parar o diagnóstico e rever o log local.
9. Comparar o diagnóstico com as células atuais, sem presumir que todos os eventos intermédios foram observados.

## 6. Critérios de aprovação
- A comparação sintética passa OFF-01 a OFF-10.
- O mecanismo local deteta alterações RTD reais durante uma sessão ativa.
- Nenhuma linha histórica foi escrita durante o diagnóstico.
- O workbook original não foi alterado.
- A taxa de eventos observados, pausas e limitações está documentada.
- Dados operacionais permanecem locais e fora do Git.

## 7. Critérios de reprovação
Reprovar se ocorrer qualquer escrita não autorizada, perda silenciosa da referência após falha, duplicação de snapshots idênticos, bloqueio relevante do Excel, uso de valores em cache como se fossem atuais, ou incapacidade de distinguir hora local de receção e hora de origem.

## 8. Estado e próximo passo
Estado: PREPARADO; EXECUÇÃO LOCAL PENDENTE. O próximo passo seguro é validar a lógica com snapshots sintéticos num teste isolado. A validação de RTD ao vivo aguarda a próxima sessão de mercado. A gravação persistente continua desativada e exige autorização expressa posterior.
