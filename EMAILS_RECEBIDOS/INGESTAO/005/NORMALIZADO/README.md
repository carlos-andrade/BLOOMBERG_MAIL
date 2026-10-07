# NORMALIZADO — INGESTÃO 005

**Data histórica:** 2026-10-07

Esta pasta contém somente dados derivados do RAW/CAMADA_A.

## Regra central
RAW é imutável. CAMADA_A é a referência validada. NORMALIZADO é derivado e reproduzível.

O arquivo BCB existente anteriormente nesta pasta é legado técnico e não representa o dataset atualmente validado. Ele permanece preservado para auditoria histórica, mas está bloqueado para integração.

Nenhum arquivo normalizado pode entrar em integração sem:
- proveniência completa;
- SHA-256 do RAW e da saída;
- parser/schema versionados;
- validação estrutural e semântica;
- reconciliação;
- status NORMALIZED_VALIDATED.

Fonte normativa: CARTA_NORMALIZACAO_V1_0_2026-10-07.md. Layout: LAYOUT_NORMALIZACAO_V1_0_2026-10-07.md.
