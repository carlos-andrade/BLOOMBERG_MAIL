---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "README_GOVERNANCA_DE_EVIDENCIAS"
fase: "FASE-03-FEED-INTRADAY"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-README"
titulo: "TESTES_RTD_DD — Arquivo permanente dos resultados RTD/DDE"
status: "ATIVO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "Decisão do utilizador"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
---



# TESTES_RTD_DD

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** README_GOVERNANCA_DE_EVIDENCIAS
> **Fase:** FASE-03-FEED-INTRADAY
> **ID:** BLOOMBERG-MAIL-TESTES-RTD-DD-README
> **Status:** ATIVO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** Decisão do utilizador
> **Autoridade:** LAYOUT
> **Rastreabilidade:** N/A


## Finalidade

Esta pasta é o arquivo permanente dos resultados do teste assistido de exportação RTD/DDE do Profit para Microsoft Excel. Os ficheiros aqui guardados serão consultados posteriormente para análise, comparação e auditoria.

## Regras de armazenamento

1. Guardar aqui as folhas de cálculo originais produzidas ou utilizadas durante os testes, preferencialmente em formato `.xlsx`, preservando também `.csv` quando for necessário analisar os dados exportados.
2. Guardar cada execução como ficheiro separado; não substituir silenciosamente resultados anteriores.
3. Usar nomes previsíveis, por exemplo:
   - `RTD_WIN_YYYY-MM-DD_HHMM.xlsx`
   - `RTD_WDO_YYYY-MM-DD_HHMM.xlsx`
   - `DDE_WIN_YYYY-MM-DD_HHMM.xlsx`
   - `DDE_WDO_YYYY-MM-DD_HHMM.xlsx`
4. Incluir no registo de cada execução o método (RTD/DDE), instrumento (WIN/WDO), data e hora local, fuso horário, campos exportados, resultado observado, interrupções/reconexões e notas.
5. Preservar o ficheiro original sem alterações. Se houver tratamento dos dados, guardar a versão tratada separadamente e documentar as transformações.
6. Não declarar funcionalidade confirmada apenas porque a opção aparece no menu. Registar separadamente se a exportação foi iniciada, se as células receberam dados e se os valores se atualizaram.
7. Não calcular latência de mercado até confirmar a semântica e o fuso horário do timestamp de origem.
8. Não incluir palavras-passe, tokens, chaves de API, dados pessoais ou outras credenciais nos ficheiros.
9. Antes de partilhar folhas de cálculo, confirmar que os termos/licenças aplicáveis permitem guardar e versionar os dados no repositório.

## Estado inicial

A informação recebida até à criação desta pasta confirma apenas que, segundo o relato do utilizador, as opções RTD/DDE, Excel, WIN/WDO e campos de preço, bid/ask, volume e timestamp estão visíveis na interface. **Ainda não constitui prova de exportação funcional.**

As quatro combinações devem ser testadas separadamente: RTD + WIN, RTD + WDO, DDE + WIN e DDE + WDO.

## Documentos relacionados

- Procedimento: [`WATCHDOG/TESTE_RTD_DDE_PROFIT_001.md`](../WATCHDOG/TESTE_RTD_DDE_PROFIT_001.md)
- Evidência estruturada: [`WATCHDOG/EVIDENCIAS/RTD_DDE_PROFIT_001.json`](../WATCHDOG/EVIDENCIAS/RTD_DDE_PROFIT_001.json)
- Matriz de fontes: [`WATCHDOG/MATRIZ_FONTES_FEED_INTRADAY_2026-10-09.json`](../WATCHDOG/MATRIZ_FONTES_FEED_INTRADAY_2026-10-09.json)

## Roadmap imediato

1. Executar e registar RTD + WIN.
2. Guardar a folha de cálculo e registar o resultado observado.
3. Repetir para RTD + WDO, DDE + WIN e DDE + WDO.
4. Verificar atualização contínua, timestamps, interrupção/reconexão e direitos de armazenamento.
5. Só depois decidir se o candidato pode avançar para a fase seguinte.
