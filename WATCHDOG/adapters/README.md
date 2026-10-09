---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO_TECNICO"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-WATCHDOG-ADAPTERS-README-MD"
titulo: "Adapters"
status: "IMPLEMENTADO"
versao: "1.1"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-09"
origem: "WATCHDOG/CARTA_ADAPTERS_FASE02.md"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "BLOOMBERG-MAIL-WATCHDOG-CARTA-ADAPTERS-FASE02"
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
> **Versão:** 1.1
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-09
> **Origem:** WATCHDOG/CARTA_ADAPTERS_FASE02.md
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** BLOOMBERG-MAIL-WATCHDOG-CARTA-ADAPTERS-FASE02

## Contexto Histórico

Os adapters isolam fontes e preservam o contrato interno. A implementação atual de replay verifica a ingestão de eventos canónicos, mas não consulta um fornecedor de cotações.

## Estado

IMPLEMENTADO — replay JSONL determinístico; feeds reais ainda não conectados.

## Evidências

- `replay.py`: valida JSONL, campos obrigatórios, severidade e estado.
- `../tests/test_replay.py`: casos de validação, append, deduplicação e rejeição.
- Workflow supervisor executa testes em alterações no WATCHDOG.

## Validação

Executar `python -m unittest discover -s WATCHDOG/tests -v`. O modo `--validate-only` não escreve. O modo com `--output` acrescenta eventos sem truncar o destino; IDs existentes são deduplicados.

## Resultado

Ordem planeada de fontes reais: B3 → IBOV → WIN/WDO → VIX → Tesouro → cripto → macro → Bloomberg Mail. Nenhuma fonte é considerada ativa até haver conexão testada e evidência rastreável.

## Próxima Ação

Integrar primeiro uma fonte real escolhida com carta e layout específicos, medição de latência, heartbeat, freshness e reconciliação.
