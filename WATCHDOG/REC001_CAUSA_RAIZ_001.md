---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "RELATORIO_TECNICO"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-REC001-CAUSA-RAIZ-001"
titulo: "REC-001 — triagem inicial da divergência COTAHIST"
status: "VALIDADO"
versao: "1.1"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/REC001_B3_COTAHIST_CROSS_REPO_2026-10-08.json"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "REC-001; WATCHDOG/adapters/b3_cotahist_status.py"
escopo: "Investigação da reconciliação cross-repo COTAHIST A2026"
objetivo: "Separar divergência real de conteúdo, diferença de versão temporal e possíveis defeitos no comparador."
dependencias: "REC-001 JSON; RAWs dos dois repositórios; algoritmo de reconciliação"
---

# REC-001 — Triagem inicial da divergência COTAHIST

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** RELATORIO_TECNICO
> **Fase:** FASE-02-WATCHDOG
> **ID:** BLOOMBERG-MAIL-REC001-CAUSA-RAIZ-001
> **Status:** VALIDADO
> **Versão:** 1.1
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** REC-001
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** REC-001; adapter de qualidade WATCHDOG

## Contexto Histórico

A reconciliação persistida em 2026-10-08 reporta `FAIL_CONTENT_DIVERGENCE`. Esta triagem não substitui nem altera o resultado original e não promove os dados a aprovados.

## Estado

VALIDADO — a comparação independente por multiconjunto completo, por pregão, confirmou a igualdade de todo o período comum. O resultado antigo permanece imutável como evidência histórica, mas deixa de ser a evidência operacional preferida.

## Evidências

- Snapshot BLOOMBERG_MAIL: geração `0261006`, 3.070.831 registos tipo 01, data máxima `20261006`, SHA-256 ZIP `c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f`.
- Snapshot do repositório B3: geração `0260923`, 2.919.760 registos tipo 01, data máxima `20260923`, SHA-256 ZIP `4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768`.
- A evidência declara 151.071 linhas/chaves com hash apenas no lado BLOOMBERG_MAIL e zero no lado B3, além de amostras de conteúdo divergente.
- As amostras mostram chaves lógicas repetidas associadas a múltiplos hashes. Isso exige validar a semântica multiset e a forma como o comparador agrupa/pareia hashes; não prova, por si só, um defeito.

## Validação

A divergência tem dimensões que devem ser testadas separadamente:

1. **Vintage temporal desigual:** os ficheiros foram gerados em datas diferentes (6 de outubro vs. 23 de setembro de 2026). O universo de registos não é diretamente comparável sem limitar a mesma data final e controlar eventuais revisões retroativas.
2. **Conteúdo para chaves comuns:** para datas e chaves comuns, comparar conjuntos/multiconjuntos de linhas canónicas por chave, contando ocorrências de cada hash. Não fazer produto cartesiano entre hashes diferentes da mesma chave.
3. **Duplicados:** distinguir chave lógica não única de registo duplicado idêntico. A chave `DATA + CODBDI + CODNEG + TPMERC` pode agrupar mais de uma linha; preservar a multiplicidade e identificar campos adicionais necessários.
4. **Integridade de origem:** preservar RAW e verificar os SHA-256 de cada snapshot antes de repetir o cálculo.
5. **Reprodução:** produzir relatório novo e versionado, com hashes, data de corte comum, contagens por categoria, exemplos mínimos reproduzíveis e versão do algoritmo. Não sobrescrever REC-001 original.

## Resultado

A execução independente do workflow `BLOOMBERG_MAIL — REC-001 B3 COTAHIST Diagnóstico multiconjunto` terminou com sucesso e gravou `REC001_B3_COTAHIST_DIAGNOSTICO_MULTICONJUNTO_2026-10-09.json`.

- Resultado: `PASS_OVERLAP_EXACT`.
- Período comum: `20260102`–`20260923`.
- Pregões testados: 182; convergentes: 182; divergentes: 0.
- SHA-256 dos dois ZIPs coincide com os hashes de referência guardados no manifesto.
- Comparação: multiconjunto dos registos tipo 01 completos (245 bytes) por data, ignorando ordem física e preservando multiplicidade.

**Conclusão técnica:** o `FAIL_CONTENT_DIVERGENCE` anterior é inconsistente com a comparação independente por registo completo e por data. A causa operacional mais provável é a metodologia de comparação por chave lógica/hash do relatório antigo, que gerou falsos pares entre registos repetidos. O relatório original não é sobrescrito; esta evidência versionada passa a governar o estado atual. O trecho de 2026-09-24 a 2026-10-06 existe apenas no snapshot BLOOMBERG_MAIL e não foi reconciliado com o snapshot B3, embora esteja coberto pelas validações estruturais e de normalização locais.

## Próxima Ação

Manter o novo diagnóstico como fonte operacional preferida no adapter WATCHDOG. Preservar o resultado antigo para auditoria. Em próxima atualização, reconciliar incrementalmente o trecho posterior a `20260923` com o snapshot oficial correspondente mais recente.
