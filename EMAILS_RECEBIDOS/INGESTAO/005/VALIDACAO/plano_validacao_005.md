# INGESTÃO 005 — PLANO DE VALIDAÇÃO

> Histórico: 2026-10-07 | BLOOMBERG_MAIL | INGESTÃO 005

## Estado após 005-C
B3, CVM, BCB, Tesouro e VIX possuem material RAW no repositório. A execução 005-C foi concluída com sucesso para Tesouro e VIX.

## Próxima validação
1. B3 COTAHIST: ZIP, TXT, layout, datas, registros e campos numéricos.
2. CVM ofertas: ZIP, arquivos internos, cabeçalhos, datas, duplicidades e tipos.
3. BCB SGS 1178: JSON, datas, valores e consistência da amostra.
4. Tesouro: CSV, encoding, cabeçalho, datas, títulos, preços/taxas e missingness.
5. VIX: CSV, DATE/OHLC, ordenação temporal, duplicidades e valores numéricos.
6. Consolidar checksums e resultados em relatório auditável.
7. Atualizar manifesto somente com estados efetivamente comprovados.

## Proibição
A validação não autoriza, por si só, sinal operacional. Após o gate, a promoção será RAW -> NORMALIZADO -> TESTE.
