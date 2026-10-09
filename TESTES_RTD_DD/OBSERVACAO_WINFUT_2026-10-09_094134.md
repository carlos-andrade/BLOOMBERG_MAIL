---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "REGISTO_DE_OBSERVACAO_DE_TESTE"
fase: "FASE-03-FEED-INTRADAY"
id_documento: "BLOOMBERG-MAIL-RTD-DDE-OBS-WINFUT-20261009-094134"
titulo: "Observação recebida — WINFUT às 09:41:34"
status: "DADOS_RECEBIDOS; METODO_E_EXPORTACAO_NAO_CONFIRMADOS"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "Tabela fornecida pelo utilizador nesta conversa"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "OBSERVACAO_WINFUT_2026-10-09_094134.csv; TESTES_RTD_DD/README.md"
escopo: "Registo documental de uma tabela WINFUT fornecida pelo utilizador"
objetivo: "Preservar a observação recebida sem inferir que RTD/DDE foi validado"
dependencias: "Tabela fornecida pelo utilizador; método de exportação e fuso horário ainda por confirmar"
---



# Observação de mercado — WINFUT

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** REGISTO_DE_OBSERVACAO_DE_TESTE
> **Fase:** FASE-03-FEED-INTRADAY
> **ID:** BLOOMBERG-MAIL-RTD-DDE-OBS-WINFUT-20261009-094134
> **Status:** DADOS_RECEBIDOS; METODO_E_EXPORTACAO_NAO_CONFIRMADOS
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** Tabela fornecida pelo utilizador nesta conversa
> **Autoridade:** LAYOUT
> **Rastreabilidade:** N/A


- Data/hora apresentada na tabela: 09/10/2026 09:41:34.
- Ativo: WINFUT (Ibovespa Mini).
- Método de exportação: não informado (RTD ou DDE por confirmar).
- Fuso horário e semântica do timestamp: não verificados.
- Formato recebido: tabela colada na conversa e arquivada em CSV.
- Ficheiro Excel original: não foi anexado nesta mensagem; este registo CSV preserva os valores fornecidos, mas não substitui o workbook original.
- Exportação iniciada, atualização contínua das células, reconexão e direitos de armazenamento: não confirmados por esta observação.
- Classificação: amostra de dados recebida; não é prova isolada de que RTD/DDE esteja funcional.

Os valores originais recebidos foram preservados em `OBSERVACAO_WINFUT_2026-10-09_094134.csv`. A pontuação decimal por vírgula foi mantida; por isso o ficheiro usa ponto e vírgula como delimitador.


## Contexto Histórico
Esta observação foi arquivada em 2026-10-09 a partir de uma tabela fornecida pelo utilizador; não constitui teste operacional autónomo.

## Estado
Dados recebidos. Método RTD/DDE, fuso horário, atualização contínua, reconexão e direitos de armazenamento não confirmados.

## Evidências
A tabela e os valores foram preservados no CSV associado, mantendo vírgula decimal e ponto e vírgula como delimitador.

## Validação
A amostra confirma apenas que os valores foram fornecidos e arquivados. Não valida a origem do feed nem que todos os eventos de mercado tenham sido observados.

## Resultado
OBSERVATION_ARCHIVED=YES; EXPORT_METHOD=UNKNOWN; LIVE_UPDATE=NOT_VERIFIED; STORAGE_RIGHTS=PENDING.

## Próxima Ação
Associar a observação a um ensaio RTD/DDE documentado, com instrumento, campos, horário local/fuso e evidência redigida.
