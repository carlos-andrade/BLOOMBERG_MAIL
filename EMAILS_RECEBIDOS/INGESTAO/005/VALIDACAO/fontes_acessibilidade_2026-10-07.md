# BLOOMBERG_MAIL — INGESTÃO 005-A — MATRIZ DE ACESSIBILIDADE DAS FONTES

> Cabeçalho histórico — 2026-10-07.

| Fonte | Acesso verificado | Conteúdo | Estado |
|---|---|---|---|
| BCB SGS 1178 | endpoint JSON oficial | amostra real | ACESSÍVEL |
| B3 Cotações | página oficial + link ZIP | histórico desde 1986 | BINÁRIO PENDENTE |
| CVM Ofertas | página oficial + ZIP listado | ofertas públicas | BINÁRIO PENDENTE |
| Tesouro Direto | página oficial | históricos anuais 2002–2026 | ARQUIVO PENDENTE |
| VIX | não concluído | histórico diário | PENDENTE |

## Regra

“Fonte confirmada” não significa “arquivo adquirido”. A etapa só pode ser marcada como adquirida quando o artefato original, checksum e metadados estiverem registrados.

## Bloqueio observado

O ambiente de execução utilizado nesta etapa não conseguiu materializar diretamente os ZIPs B3/CVM. Portanto, não foram fabricados checksums, tamanhos locais ou supostos conteúdos.

## Próximo passo

Executar um **agente de aquisição reprodutível dentro do próprio repositório**, com download no GitHub Actions/runner, checksum SHA-256, armazenamento RAW e geração automática de NORMALIZADO/VALIDAÇÃO.
