---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-CONTROLE-FALHA-VALIDACAO-CONJUNTA-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — INGESTÃO 005N — CONTROLE DE FALHAS DA NORMALIZAÇÃO E VALIDAÇÃO CONJUNTA"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/CONTROLE_FALHA_VALIDACAO_CONJUNTA_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — INGESTÃO 005N — CONTROLE DE FALHAS DA NORMALIZAÇÃO E VALIDAÇÃO CONJUNTA

## Contexto Histórico

Documento histórico do projeto BLOOMBERG_MAIL integrado à governança documental central de carlos-andrade.

## Estado

IMPLEMENTADO — cabeçalho migrado para o padrão canônico.

## Evidências

Modelo canônico: Curioso-da-Internet-IA/CABEÇALHO/MODELO-PADRAO-CABECALHO.md.

## Validação

Cabeçalho, identificação documental e rastreabilidade foram normalizados.

## Resultado

O conteúdo original abaixo foi preservado.

## Próxima Ação

Atualizar versão, data e rastreabilidade em alterações relevantes.

---

# BLOOMBERG_MAIL — INGESTÃO 005N — CONTROLE DE FALHAS DA NORMALIZAÇÃO E VALIDAÇÃO CONJUNTA

**Cabeçalho histórico — 2026-10-07**

## Evento 1 — Validação conjunta #1

Workflow: **BLOOMBERG_MAIL — INGESTÃO 005N — Validação Conjunta dos Normalizadores**  
Run: **#1**  
Conclusão: **FAILURE**

Erro:

`AssertionError: missing normalized CVM_OFERTAS`

Causa: o workflow de normalização ainda executava somente BCB e VIX, embora CVM e Tesouro já tivessem scripts implementados.

## Evento 2 — Validação conjunta #2 e #3

As execuções #2 e #3 foram realizadas no commit:

`55a54f5ed24b71dc3a7c36294703db1382f96126`

Ambas reproduziram deterministicamente:

`AssertionError: missing normalized CVM_OFERTAS`

O problema permaneceu porque as saídas de CVM e Tesouro ainda não haviam sido publicadas no repositório.

## Evento 3 — Normalização determinística #2

Workflow: **BLOOMBERG_MAIL — INGESTÃO 005N — Normalização Determinística**  
Run: **#2**  
Run ID: **37689661444**  
Commit de execução: `55a54f5ed24b71dc3a7c36294703db1382f96126`  
Conclusão: **FAILURE**

### O que passou

Os quatro normalizadores foram executados com sucesso:

1. BCB + VIX — PASS
2. CVM — PASS
3. Tesouro — PASS
4. validação estrutural 4/5 — PASS

### Causa-raiz real da falha

A etapa de publicação tentou enviar para o GitHub:

- `cvm_ofertas_normalizado.json` — **223,91 MB**
- `tesouro_normalizado.json` — **65,57 MB**

O GitHub recusou o push:

- CVM excedeu o limite máximo de 100 MB.
- Tesouro excedeu o limite recomendado de 50 MB.

Erro remoto:

`GH001: Large files detected`

Portanto, **os normalizadores não falharam**. A falha ocorreu exclusivamente na estratégia de armazenamento/publicação dos derivados.

O commit local `156b3b7` foi criado no runner, mas **não foi publicado** porque o push foi rejeitado. Não considerar esse commit como estado oficial do repositório.

## Correção aplicada

Foi adotado armazenamento derivado comprimido, sem alterar o RAW:

### CVM

`cvm_ofertas_normalizado.json` passa a ser um **manifesto**, com os registros armazenados em:

- JSONL
- UTF-8
- gzip
- um arquivo por membro do ZIP original

Parser atualizado:

`normalizacao-005-cvm-v1.1`

### Tesouro

`tesouro_normalizado.json` passa a ser um **manifesto**, com registros em JSONL gzip.

Parser atualizado:

`normalizacao-005-tesouro-v1.1`

### Validação

O validador foi atualizado para validar:

- existência dos manifests;
- SHA-256 do RAW;
- vínculo do derivado ao SHA esperado;
- `NORMALIZED_DERIVED`;
- existência dos arquivos comprimidos;
- leitura mínima de integridade gzip.

### Commits das correções

- CVM: `a6ed4a2ad8ca69a5326e7ab3b8a2ba5869a4624b`
- Tesouro: `8720514a33ce5bc01f9225c2cd7c72327e15d6b3`
- Validador: `df544e2c18e69aef3e38659a44008f793650955b`
- Workflow: `8b1d78bae56e747b29f4646781e99a0b9f5b9466`

## Evento 4 — Validação conjunta #4

A validação conjunta #4 foi executada no mesmo commit antigo `55a54f5...`.

Como a normalização #2 não conseguiu publicar os derivados, a validação #4 novamente encontrou:

`missing normalized CVM_OFERTAS`

Esse resultado é **esperado e determinístico**.

## Estado oficial

| Componente | Estado |
|---|---|
| RAW | **PRESERVADO / IMUTÁVEL** |
| BCB | implementado |
| VIX | implementado |
| CVM | corrigido para armazenamento comprimido |
| Tesouro | corrigido para armazenamento comprimido |
| Validador conjunto | corrigido |
| Workflow normalização | corrigido |
| CVM publicado | **PENDENTE DE NOVA EXECUÇÃO** |
| Tesouro publicado | **PENDENTE DE NOVA EXECUÇÃO** |
| Validação conjunta 5 | **PENDENTE** |
| B3 | BLOQUEADO por mapeamento autoritativo |
| Integração | BLOQUEADA |

## Sequência obrigatória

```
NOVO COMMIT
    ↓
005N NORMALIZAÇÃO
    ↓
publicar manifests + JSONL gzip
    ↓
verificar push bem-sucedido
    ↓
VALIDAÇÃO CONJUNTA
    ↓
PASS 4/5
    ↓
B3 authoritative mapping
    ↓
B3 normalização
    ↓
validação 5/5
    ↓
reconciliação
    ↓
integração
```

**Não executar novamente a validação conjunta até que uma nova execução da normalização termine com publicação bem-sucedida.**

RAW não é alterado, comprimido, reescrito ou substituído por esta correção.
