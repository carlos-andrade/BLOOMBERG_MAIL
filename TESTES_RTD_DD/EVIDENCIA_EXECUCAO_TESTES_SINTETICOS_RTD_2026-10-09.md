---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-EVIDENCIA-EXECUCAO-TESTES-SINTETICOS-RTD-2026-10-09-MD"
titulo: "BLOOMBERG_MAIL — Evidência de execução dos testes sintéticos RTD"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/EVIDENCIA_EXECUCAO_TESTES_SINTETICOS_RTD_2026-10-09.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-EVIDENCIA-EXECUCAO-TESTES-SINTETICOS-RTD-2026-10-09-MD"
titulo: "BLOOMBERG_MAIL — Evidência de execução dos testes sintéticos RTD"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/EVIDENCIA_EXECUCAO_TESTES_SINTETICOS_RTD_2026-10-09.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — Evidência de execução dos testes sintéticos RTD

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** N/A
> **ID:** BLOOMBERG-MAIL-TESTES-RTD-DD-EVIDENCIA-EXECUCAO-TESTES-SINTETICOS-RTD-2026-10-09-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


# BLOOMBERG_MAIL — Evidência de execução dos testes sintéticos RTD

Data: 2026-10-09
Fase: FASE03
Ficheiro: TESTES_RTD_DD/prototipo_comparacao_snapshots_sinteticos.py
Blob SHA confirmado: 572ffd54a96234b092dd7fd5a809edb636ffa95d

## Resultado
O conteúdo foi obtido do repositório pela integração GitHub, colocado numa cópia temporária e executado localmente. O SHA-1 Git blob calculado para a cópia coincide com o blob publicado, confirmando a identidade do conteúdo executado.

A sintaxe Python foi validada com py_compile. O programa executou os dez testes unitários: 10 aprovados, 0 falhados.

Os testes abrangem baseline inicial, snapshot idêntico, alteração única, alterações múltiplas num snapshot, alteração de quantidade, valor vazio, erro de célula, snapshot vazio, alteração de esquema e atualização da referência em memória.

## Workflow
Foi publicado o workflow .github/workflows/rtd-synthetic-tests.yml no commit 470d10b3bc55178f208ab380310d665abeb83dd6. Executa validação de sintaxe e testes com Python 3.12, usando dados sintéticos e sem ligação ao Excel/Profit.

O workflow está publicado, mas a execução remota do GitHub Actions ainda não foi confirmada nesta verificação.

## Segurança e limites
Não houve ligação ao Excel/Profit, não foram alteradas as fórmulas RTD e não foi modificada a planilha original. A gravação persistente continua DESATIVADA. Os testes sintéticos não demonstram ainda a captura de alterações RTD ao vivo.

## Roadmap
- Especificação e plano: concluídos.
- Protótipo versionado: concluído.
- Integridade do conteúdo executado: confirmada pelo Git blob SHA.
- Testes sintéticos: 10/10 aprovados.
- Workflow CI: publicado; execução remota por confirmar.
- Diagnóstico integrado Excel/RTD sem persistência: pendente.
- Validação RTD ao vivo na próxima sessão: pendente.
- Persistência e recuperação de falhas: pendente.
- Ativação da gravação: não autorizada.
