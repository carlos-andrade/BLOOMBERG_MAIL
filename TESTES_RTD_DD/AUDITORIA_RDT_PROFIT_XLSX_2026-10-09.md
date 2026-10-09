---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "RELATORIO_AUDITORIA_WORKBOOK_RTD"
fase: "FASE-03-FEED-INTRADAY"
id_documento: "BLOOMBERG-MAIL-RTD-PROFIT-XLSX-AUDIT-001"
titulo: "Auditoria estática de RDT_PROFIT.xlsx"
status: "ANALISADO_COM_LIMITACOES"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "Ficheiro RDT_PROFIT.xlsx anexado pelo utilizador"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
---



# Auditoria estática — RDT_PROFIT.xlsx

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** RELATORIO_AUDITORIA_WORKBOOK_RTD
> **Fase:** FASE-03-FEED-INTRADAY
> **ID:** BLOOMBERG-MAIL-RTD-PROFIT-XLSX-AUDIT-001
> **Status:** ANALISADO_COM_LIMITACOES
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** Ficheiro RDT_PROFIT.xlsx anexado pelo utilizador
> **Autoridade:** LAYOUT
> **Rastreabilidade:** N/A


## 1. Resultado executivo

**Confirmado:** o workbook contém fórmulas Excel RTD reais e valores em cache para WINFUT.  
**Não confirmado:** atualização contínua em tempo real, frequência de atualização, timestamp de origem/fuso, reconexão, funcionamento DDE, funcionamento com WDO ou autorização para guardar redistribuir os dados.

A auditoria foi executada sobre uma cópia do ficheiro anexado. O original não foi alterado.

## 2. Integridade e estrutura

- Ficheiro: `RDT_PROFIT.xlsx`
- Tamanho: 11.302 bytes
- SHA-256: `60d45db25deb794de024b8494f2233d25b0670420edad690256e471b3125a207`
- Folhas: `Folha1`
- Dimensão: 2 linhas × 38 colunas (cabeçalho + 1 registo)
- Fórmulas: 36; todas usam a função `RTD`
- Fórmulas com valores em cache: 36
- Servidor RTD referenciado: `rtdtrading.rtdserver`
- Identificador do instrumento nas fórmulas: `WINFUT_F_0`
- Ligações externas Excel: 0
- Nomes definidos: 0
- Fórmulas DDE encontradas: 0
- Registos para WDO: 0

## 3. Campos presentes

`Asset`, `Data`, `Hora`, `Último`, `Abertura`, `Máximo`, `Mínimo`, `Fechamento Anterior`, `Strike`, `Variação`, `Variação(pts)`, `Média`, `Nome do Ativo`, `Negócios`, `QUL`, `Quantidade`, `Volume`, `Of. Compra`, `Of. Venda`, `VOC`, `VOV`, `Ajuste`, `Aj. Anterior`, `Preço Teórico`, `Qtd. Teórica`, `Volume Projetado`, `Semana`, `Mês`, `3 meses`, `6 meses`, `12 meses`, `Ano`, `Trimestre`, `Semestre`, `Vencimento`, `Validade`, `Cont. Abertos`, `Estado Atual`.

## 4. Valores em cache observados

Os valores seguintes são os que estavam guardados no ficheiro quando foi gravado; não devem ser tratados como cotações atuais.

| Campo | Valor em cache |
|---|---:|
| Ativo | WINFUT |
| Data | 09/10/2026 |
| Hora | 09:38:34 |
| Último | 208070 |
| Abertura | 209115 |
| Máximo | 209540 |
| Mínimo | 207625 |
| Fechamento anterior | 207185 |
| Variação (%) | 0,4271544755 |
| Variação (pts) | 885 |
| Estado atual | Aberto |

Validação aritmética: `208070 - 207185 = 885`, consistente com o campo `Variação(pts)`. O valor percentual também é aproximadamente consistente com essa diferença em relação ao fechamento anterior. Esta coerência não valida a origem ou a atualidade dos dados.

## 5. Diagnóstico

1. **RTD — presença de fórmula: PASS.** As 36 fórmulas são do tipo `=RTD("rtdtrading.rtdserver",,"WINFUT_F_0","TÓPICO")`.
2. **Valores em cache: PASS.** Todas as 36 fórmulas têm um valor armazenado no workbook.
3. **Atualização ao vivo: NOT VERIFIED.** Uma fotografia de um workbook não demonstra que as células continuaram a mudar após a gravação.
4. **Timestamp de origem e fuso: NOT VERIFIED.** As células `Data` e `Hora` fornecem uma data/hora apresentada pelo servidor, mas a semântica e o fuso não foram estabelecidos.
5. **Reconexão: NOT RUN.** Não foi possível interromper e restabelecer a ligação ao RTD do computador do utilizador a partir desta auditoria.
6. **DDE: NOT RUN.** Nenhuma fórmula DDE foi encontrada neste workbook.
7. **WDO: NOT RUN.** O workbook só contém o identificador `WINFUT_F_0`.
8. **Direitos de armazenamento: PENDING.** Confirmar termos/licença antes de armazenar, reutilizar ou redistribuir dados de mercado.

## 6. Correções de processo

- Separar `FORMULAS_CONFIRMED` de `LIVE_UPDATE_CONFIRMED`.
- Não alterar os quatro testes operacionais para PASS com base nesta inspeção.
- Manter RTD+WIN, RTD+WDO, DDE+WIN e DDE+WDO como testes independentes.
- Guardar cada nova observação com data, hora, fuso, duração e evidência antes/depois.
- Não calcular latência até validar timestamp de origem e relógio de referência.
- Não iniciar coletor de produção antes dos gates funcionais e de licenciamento.

## 7. Resultado final da auditoria

`WORKBOOK_STATIC_AUDIT=PASS`  
`RTD_FORMULAS_PRESENT=PASS`  
`RTD_LIVE_UPDATE=NOT_VERIFIED`  
`DDE_FUNCTIONALITY=NOT_RUN`  
`WDO_FUNCTIONALITY=NOT_RUN`  
`TIMESTAMP_SEMANTICS=NOT_VERIFIED`  
`RECONNECT=NOT_RUN`  
`STORAGE_RIGHTS=PENDING`  
`PRODUCTION_INGESTION=BLOCKED`

## 8. Próximos passos

1. Abrir a folha no computador com Profit/Excel e registar valores em dois ou mais instantes separados por intervalo conhecido.
2. Testar uma interrupção controlada e confirmar se os campos retomam atualização.
3. Duplicar o teste para WIN e WDO, primeiro RTD e depois DDE.
4. Confirmar documentação e direitos de armazenamento aplicáveis.
5. Só após aprovação de todos os gates, desenhar a ingestão automática.

---
Relatório gerado a partir da inspeção do workbook anexado em 2026-10-09. Não contém credenciais.
