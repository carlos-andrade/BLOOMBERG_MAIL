---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO_TECNICO"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-ADAPTERS-README-MD"
titulo: "Adapters"
status: "IMPLEMENTADO"
versao: "1.2"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-09"
origem: "WATCHDOG/CARTA_ADAPTERS_FASE02.md"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "WATCHDOG/CARTA_B3_COTAHIST_FASE02.md"
escopo: "WATCHDOG/adapters/"
objetivo: "Documentar adapters, contrato, estado de integração e limites de evidência."
dependencias: "WATCHDOG/schema/event.schema.json"
---

# Adapters

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO_TECNICO
> **Fase:** FASE-02-WATCHDOG
> **ID:** BLOOMBERG-MAIL-WATCHDOG-ADAPTERS-README-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.2
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-09
> **Origem:** WATCHDOG/CARTA_ADAPTERS_FASE02.md
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** WATCHDOG/CARTA_B3_COTAHIST_FASE02.md

## Contexto Histórico

Os adapters isolam fontes e preservam o contrato interno. A implementação atual inclui replay genérico JSONL e leitura das evidências de qualidade do dataset histórico B3 COTAHIST.

## Estado

IMPLEMENTADO — integração de qualidade histórica. Nenhum feed intradiário está ativo.

## Evidências

- `replay.py`: valida JSONL, campos obrigatórios, severidade e estado.
- `b3_cotahist_status.py`: verifica manifesto, hashes e resultados de validação/reconciliação.
- `../tests/`: testes de validação, append, deduplicação, classificação de divergência e rejeição de hashes incompatíveis.
- Workflow supervisor executa os testes em alterações ao WATCHDOG.

## Validação

Executar `python -m unittest discover -s WATCHDOG/tests -v`. O adapter COTAHIST classifica a reconciliação atual como `DEGRADED/HIGH` quando o resultado REC-001 indica divergência ou bloqueio.

## Resultado

Ordem planeada: B3 histórico/qualidade → feed intradiário validado → IBOV/WIN/WDO → VIX/Tesouro → cripto → macro/Bloomberg Mail. A ordem não significa que as fontes estejam conectadas.

## Próxima Ação

Executar reconciliação REC-001 com análise de causa raiz e documentar um feed intradiário adequado antes de declarar fontes de mercado ativas.
