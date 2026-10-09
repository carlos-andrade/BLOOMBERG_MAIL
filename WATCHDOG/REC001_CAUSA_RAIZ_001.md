---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "RELATORIO_TECNICO"
fase: "FASE-02-WATCHDOG"
id_documento: "BLOOMBERG-MAIL-REC001-CAUSA-RAIZ-001"
titulo: "REC-001 — triagem inicial da divergência COTAHIST"
status: "EM_DESENVOLVIMENTO"
versao: "1.0"
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
> **Status:** EM_DESENVOLVIMENTO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** REC-001
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** REC-001; adapter de qualidade WATCHDOG

## Contexto Histórico

A reconciliação persistida em 2026-10-08 reporta `FAIL_CONTENT_DIVERGENCE`. Esta triagem não substitui nem altera o resultado original e não promove os dados a aprovados.

## Estado

EM_DESENVOLVIMENTO — causas ainda não confirmadas; o estado operacional permanece `DEGRADED/HIGH`.

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

Não é possível atribuir a causa raiz apenas com o relatório resumido. A diferença de datas explica uma parte provável das diferenças de cobertura, mas não explica automaticamente divergências de conteúdo em chaves comuns. A hipótese de problema de agrupamento/pareamento precisa de teste independente.

## Próxima Ação

Executar reconciliação de diagnóstico com data de corte comum (até `20260923`), canonicalização idêntica e comparação multiset por chave; testar os exemplos `AXIA3T`, `BBAS3T` e `BEEF3T`. Guardar o resultado como diagnóstico versionado, sem alterar REC-001 original nem o estado `DEGRADED/HIGH`.
