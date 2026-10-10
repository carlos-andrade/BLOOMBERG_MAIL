---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-RESULTADO-BASELINE-EXCEL-RTD-FASE04-2026-10-10-MD"
titulo: "BLOOMBERG_MAIL — Registo histórico de teste"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/RESULTADO_BASELINE_EXCEL_RTD_FASE04_2026-10-10.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-RESULTADO-BASELINE-EXCEL-RTD-FASE04-2026-10-10-MD"
titulo: "BLOOMBERG_MAIL — Registo histórico de teste"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/RESULTADO_BASELINE_EXCEL_RTD_FASE04_2026-10-10.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — Registo histórico de teste

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** N/A
> **ID:** BLOOMBERG-MAIL-TESTES-RTD-DD-RESULTADO-BASELINE-EXCEL-RTD-FASE04-2026-10-10-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


# BLOOMBERG_MAIL — Registo histórico de teste

- **Projeto:** BLOOMBERG_MAIL
- **Fase:** FASE04 — diagnóstico Excel/RTD sem gravação
- **Data do registo:** 2026-10-10
- **Origem:** resultado comunicado pelo utilizador na sessão de diagnóstico
- **Estado:** evidência inicial confirmada; teste de alteração real pendente

## Resultado observado

Saída comunicada da janela Immediate:

```text
2026-10-10 15:07:40 | BASELINE | A2:AL2 | sem registo
```

## Interpretação

O diagnóstico emitiu uma mensagem `BASELINE` para o intervalo monitorizado `A2:AL2`. Isto confirma que o caminho de inicialização/diagnóstico produziu saída nesta execução. Não demonstra, por si só, que alterações subsequentes dos valores RTD sejam detetadas nem que a inserção de linhas de histórico esteja correta.

## Salvaguardas

- A gravação persistente continua **desativada**.
- Não foi autorizada nem efetuada a criação automática de linhas.
- A primeira leitura válida é tratada como baseline e não deve originar uma linha de histórico por defeito.
- Alterações simultâneas em vários campos devem ser avaliadas como um único snapshot/evento.
- Os dados operacionais da folha devem permanecer locais e não ser versionados no Git.

## Próximo teste controlado

Durante uma sessão em que os dados RTD estejam efetivamente a variar, observar o intervalo `A2:AL2` e confirmar se surge `CHANGED` após uma alteração real. Não editar os valores RTD para simular um evento, não modificar o livro original e não ativar persistência. Registar a saída exata e a hora; só depois avaliar a deteção.

## Critério de conclusão da FASE04

A fase só poderá ser considerada validada quando existir evidência reproduzível de baseline, ausência de falso positivo em snapshots inalterados e deteção de uma alteração real, mantendo a persistência desligada. A validação do evento não equivale à autorização para implementar gravação automática.
