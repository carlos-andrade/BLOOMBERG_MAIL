# BLOOMBERG_MAIL — INGESTÃO 005-B — ESPECIFICAÇÃO B3

> Cabeçalho histórico — 2026-10-07.  
> Estado: fonte e layout oficial verificados.

## Fonte

A B3 informa que as cotações históricas abrangem títulos negociados desde 1986, sem ajuste automático por inflação ou proventos. O produto inclui preços, número de negócios e volume, e é distribuído em ZIP contendo TXT de largura fixa. citeturn1view1

O layout oficial identifica o arquivo anual como `COTAHIST.AAAA.TXT`, com registros 00 (header), 01 (cotações diárias) e 99 (trailer), em registros de 245 bytes. citeturn0search16

## Decisão de engenharia

A aquisição B3 será executada pelo runner do GitHub Actions quando o artefato estiver acessível ao endpoint de download. O parser deverá:

1. preservar ZIP original em RAW;
2. calcular SHA-256 antes de qualquer transformação;
3. validar ZIP e arquivo TXT;
4. validar registros 00/01/99;
5. validar tamanho de registro;
6. preservar encoding de origem;
7. gerar NORMALIZADO somente depois dos testes estruturais;
8. registrar divergências no diretório VALIDACAO.

Não será feito ajuste de preços nesta fase.

## Evidência atual

A fonte oficial está confirmada, mas a URL dinâmica do download não foi materializada pelo mecanismo de pesquisa. Portanto, o workflow 005-B não deve inventar uma URL B3.

## Próxima execução

Prioridade operacional:
**CVM → BCB → B3 → Tesouro → VIX**, sempre com RAW + checksum + validação antes da promoção.
