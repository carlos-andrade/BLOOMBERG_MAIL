# BLOOMBERG_MAIL — REC-001 B3 — Execução Cross-Repo — 2026-10-08

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Repositório central: carlos-andrade/BLOOMBERG_MAIL
- Processo: REC-001 — Reconciliação B3 COTAHIST
- Data: 2026-10-08
- Regra: nenhuma conclusão PASS pode ser inferida de uma execução GitHub que não materialize evidência persistida.

## Objetivo
Comparar determinísticamente o RAW COTAHIST_A2026 do BLOOMBERG_MAIL com a segunda representação disponível no repositório carlos-andrade/B3.

## Representações
- BLOOMBERG_MAIL RAW SHA-256: c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f
- B3 snapshot SHA-256: 4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768
- B3 caminho: dados/cotahist/raw/anual/COTAHIST_A2026.ZIP
- Evidência prévia B3 TPMERC=021: dados/cotahist/quality/COTAHIST_A2026_TPMERC021_BVBG028_RECONCILIACAO_V1.json

## Procedimento implantado
Foi criado o executor:
`scripts/rec001_b3_cotahist_cross_repo.py`

Foi criado o workflow:
`.github/workflows/bloomberg-mail-rec001-b3-cotahist-cross-repo.yml`

O executor:
1. preserva o RAW BLOOMBERG_MAIL;
2. baixa a segunda representação oficial armazenada no repositório B3;
3. calcula SHA-256 dos dois ZIPs;
4. valida o membro COTAHIST_A2026.TXT;
5. valida registros de 245 bytes;
6. compara os registros em streaming, evitando carregar o arquivo inteiro em memória;
7. distingue igualdade exata, igualdade por sobreposição temporal e divergência de conteúdo;
8. grava evidência JSON no repositório central.

## Atualização da implementação — política incremental

A regra permanente de atualização incremental foi formalizada em:
- `EMAILS_RECEBIDOS/INGESTAO/005/CARTA_POLITICA_INCREMENTAL_BASES_V1_0_2026-10-08.md`
- `EMAILS_RECEBIDOS/INGESTAO/005/LAYOUT_POLITICA_INCREMENTAL_BASES_V1_0_2026-10-08.md`

Para este REC-001, o executor foi reforçado para:
- comparar somente registros COTAHIST tipo 01;
- excluir cabeçalho/trailer da igualdade de conteúdo, pois são metadados do arquivo;
- registrar data de geração dos dois arquivos;
- registrar o timestamp de aquisição do BLOOMBERG_MAIL;
- calcular a diferença entre datas de geração quando disponíveis;
- classificar somente em `PASS_EXACT`, `PASS_OVERLAP_EXACT` ou `FAIL_CONTENT_DIVERGENCE`, mantendo bloqueio quando não houver evidência.

## Resultado desta tentativa
A execução controlada foi preparada e disparada por alteração do executor, mas a evidência de saída não foi materializada no repositório dentro da janela de verificação. Portanto:

**REC-001 B3 = BLOCKED — EXECUÇÃO COMPARATIVA NÃO MATERIALIZADA**

Não é permitido converter essa ausência de evidência em PASS.

## Estado
- Segunda representação encontrada: PASS
- Executor determinístico criado: PASS
- Comparação byte-a-byte em streaming: IMPLEMENTADA
- Evidência final da comparação: NÃO MATERIALIZADA
- REC-001 B3: BLOCKED
- RAW BLOOMBERG_MAIL: preservado
- Nenhuma correção ou alteração econômica aplicada

## Próximo passo obrigatório
Executar manualmente o workflow `BLOOMBERG_MAIL — REC-001 B3 COTAHIST Cross-Repo` e somente promover o REC-001 quando o JSON de evidência for persistido com resultado explícito:
- `PASS_EXACT`, ou
- `PASS_OVERLAP_EXACT`, ou
- `FAIL_CONTENT_DIVERGENCE`.

O workflow foi restaurado para `workflow_dispatch`; não permanece trigger automático de push.
