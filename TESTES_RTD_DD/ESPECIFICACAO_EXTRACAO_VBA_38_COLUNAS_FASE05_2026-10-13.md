---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-ESPECIFICACAO-EXTRACAO-VBA-38-COLUNAS-FASE05-2026-10-13-MD"
titulo: "Especificação — Extração VBA das 38 colunas RTD — Fase 05"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/ESPECIFICACAO_EXTRACAO_VBA_38_COLUNAS_FASE05_2026-10-13.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-ESPECIFICACAO-EXTRACAO-VBA-38-COLUNAS-FASE05-2026-10-13-MD"
titulo: "Especificação — Extração VBA das 38 colunas RTD — Fase 05"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/ESPECIFICACAO_EXTRACAO_VBA_38_COLUNAS_FASE05_2026-10-13.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# Especificação — Extração VBA das 38 colunas RTD — Fase 05

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** N/A
> **ID:** BLOOMBERG-MAIL-TESTES-RTD-DD-ESPECIFICACAO-EXTRACAO-VBA-38-COLUNAS-FASE05-2026-10-13-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


# Especificação — Extração VBA das 38 colunas RTD — Fase 05

## Ficheiro oficial indicado

`RDT_PROFIT_TESTADO_E_APROVADO.xlsm` (ficheiro operacional local; não guardar o livro nem dados RTD no Git).

## Estrutura observada em leitura

- Folha de origem: `Folha1`.
- Cabeçalhos: `A1:AL1`, 38 colunas.
- Valores/fórmulas RTD: `A2:AL2`.
- Fórmulas RTD identificadas usam o servidor `rtdtrading.rtdserver` e o tópico `WINFUT_F_0`.
- A2 contém `WINFUT` e M2 contém `Ibovespa Mini` como valores fixos na amostra.
- A auditoria foi estática; nenhuma macro foi executada.

## Cabeçalhos na ordem original

1. Asset
2. Data
3. Hora
4. Último
5. Abertura
6. Máximo
7. Mínimo
8. Fechamento Anterior
9. Strike
10. Variação
11. Variação(pts)
12. Média
13. Nome do Ativo
14. Negócios
15. QUL
16. Quantidade
17. Volume
18. Of. Compra
19. Of. Venda
20. VOC
21. VOV
22. Ajuste
23. Aj. Anterior
24. Preço Teórico
25. Qtd. Teórica
26. Volume Projetado
27. Semana
28. Mês
29. 3 meses
30. 6 meses
31. 12 meses
32. Ano
33. Trimestre
34. Semestre
35. Vencimento
36. Validade
37. Cont. Abertos
38. Estado Atual

## Arquitetura proposta

1. O evento `Worksheet_Calculate` observa `A2:AL2`.
2. A leitura é feita em bloco com `.Value2`.
3. Uma observação com qualquer célula em erro é inválida e não deve produzir snapshot.
4. A primeira observação válida estabelece a baseline e não é gravada como snapshot de mercado.
5. Quando houver alteração, todos os valores de `A2:AL2` são copiados para uma única linha de histórico, agrupando alterações detetadas na mesma observação.
6. A folha `HISTORICO_RTD` deve conter metadados à esquerda e os 38 campos originais na ordem acima. Metadados propostos: `Timestamp_Observacao`, `Sequencia_Snapshot`, `Campos_Alterados` e `Estado_Validacao`.
7. A escrita deve ocorrer como uma operação única de matriz, não célula a célula, para reduzir custo e risco de linhas parcialmente escritas.
8. O código deve tratar e registar erros de execução; não pode falhar silenciosamente.
9. A escrita histórica deve ter um interruptor de ativação explícito, inicialmente desligado.

## Regras de segurança e validação

- Não modificar o livro original.
- Não executar macros durante a auditoria estática.
- Não ativar persistência até à conclusão dos testes integrados e autorização explícita do utilizador.
- Testar baseline, ausência de alterações, alteração de um campo, alterações simultâneas, erro RTD, recuperação e falha de escrita.
- Verificar que o número e a ordem dos 38 campos correspondem exatamente a `A1:AL1`.
- Dados operacionais e snapshots de mercado ficam locais e não devem ser commitados no Git.

## Estado

Especificação registada. Ainda não é uma implementação do gravador, não comprova a execução de macros e não autoriza persistência automática.
