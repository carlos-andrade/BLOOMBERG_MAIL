# BLOOMBERG_MAIL — FONTES

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Regra: todas as fontes externas utilizadas pelo projeto devem ser registradas nesta pasta.
- Data de instituição: 2026-10-07

## Regra obrigatória

Nenhuma fonte utilizada em pesquisa, aquisição, validação, normalização ou teste pode permanecer apenas no chat ou apenas em um workflow.

Cada fonte deve possuir registro persistente em `FONTES/`, contendo, quando aplicável:

- nome da instituição/fonte;
- finalidade;
- URL da página oficial;
- URL direta do recurso;
- tipo/formato do recurso;
- período/frequência;
- data de consulta;
- timestamp UTC;
- checksum SHA-256 do arquivo adquirido;
- nome original do arquivo;
- status de validação;
- observações sobre alterações da fonte;
- relação com ingestão/hipótese/dataset.

## Regra de proveniência

`FONTE OFICIAL → REGISTRO EM FONTES/ → AQUISIÇÃO → RAW → CHECKSUM → VALIDAÇÃO → NORMALIZAÇÃO → TESTE`

A pasta `FONTES/` é o catálogo persistente de proveniência do projeto.

## Proibição

É proibido considerar uma fonte como parte oficial do pipeline apenas porque sua URL apareceu em uma conversa, log temporário ou mensagem de workflow. A fonte precisa estar registrada em `FONTES/`.

## Fontes iniciais

- B3
- CVM
- Banco Central do Brasil / SGS
- Tesouro Nacional / Tesouro Transparente
- Cboe / VIX

Novas fontes devem ser adicionadas antes de serem promovidas ao pipeline.
