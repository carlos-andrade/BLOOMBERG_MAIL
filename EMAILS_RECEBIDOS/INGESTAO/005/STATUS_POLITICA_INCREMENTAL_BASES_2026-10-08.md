# BLOOMBERG_MAIL — STATUS DA POLÍTICA INCREMENTAL — 2026-10-08

> Cabeçalho histórico — 2026-10-08.

## Estado

**APROVADO COMO REGRA PERMANENTE.**

## Cobertura

A regra foi aplicada conceitualmente a todas as cinco bases da INGESTÃO 005:

- B3_COTACOES;
- CVM_OFERTAS;
- BCB_SGS;
- TESOURO_HISTORICO;
- VIX.

## Implementação já existente

- B3 possui carta/layout específicos para incrementos diários.
- O manifesto 005 passa a declarar política incremental para todas as fontes.
- RAW permanece imutável.
- A normalização continua derivada do RAW.
- A reconciliação continua obrigatória quando houver segunda representação.
- O B3 continua sendo atualizado por incrementos COTAHIST validados.

## Próxima execução

Após a formalização da regra geral, o trabalho retorna ao ponto anterior:
**REC-001**, priorizando a materialização determinística da reconciliação B3/COTAHIST e, em seguida, os demais bloqueios.

## Regra de não-regressão

Nenhum novo pipeline poderá introduzir uma base somente como snapshot sem declarar:
- frequência de atualização;
- unidade do incremento;
- caminho de armazenamento;
- manifesto;
- validação;
- estratégia de reconciliação.
