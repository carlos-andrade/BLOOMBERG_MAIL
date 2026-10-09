---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-CARTA-ALINHAMENTO-INCREMENTAL-B3-V1-0-2026-10-08-MD"
titulo: "BLOOMBERG_MAIL — CARTA DE ALINHAMENTO INCREMENTAL COM B3 — V1.0"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/CARTA_ALINHAMENTO_INCREMENTAL_B3_V1_0_2026-10-08.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — CARTA DE ALINHAMENTO INCREMENTAL COM B3 — V1.0

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-CARTA-ALINHAMENTO-INCREMENTAL-B3-V1-0-2026-10-08-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-08
> **Atualização:** 2026-10-08
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


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

# BLOOMBERG_MAIL — CARTA DE ALINHAMENTO INCREMENTAL COM B3 — V1.0

> Cabeçalho histórico — 2026-10-08.
> Origem: decisão de arquitetura decorrente do REC-001 B3/COTAHIST.
> Status: REGRA DE GOVERNANÇA APROVADA PARA IMPLEMENTAÇÃO.
> Repositórios envolvidos:
> - BLOOMBERG_MAIL: https://github.com/carlos-andrade/BLOOMBERG_MAIL
> - B3: https://github.com/carlos-andrade/B3

## 1. Objetivo

Manter o BLOOMBERG_MAIL e o B3 alinhados por meio de **incrementos diários imutáveis**, evitando depender de snapshots anuais como única forma de sincronização.

O snapshot anual é uma fotografia de referência. O incremento diário é a unidade operacional de atualização.

## 2. Regra permanente

Para dados COTAHIST/B3:

1. O BLOOMBERG_MAIL deve armazenar o RAW recebido de cada incremento diário disponível.
2. Cada incremento deve preservar o arquivo original, SHA-256, fonte, URL, data/hora de aquisição e período coberto.
3. O incremento nunca deve ser sobrescrito por uma versão posterior.
4. O B3 deve continuar recebendo os incrementos que forem validados no BLOOMBERG_MAIL.
5. O snapshot anual não será tratado como substituto dos incrementos.
6. Quando existir snapshot anual e incrementos posteriores, a comparação deve reconhecer explicitamente a extensão temporal.
7. SHA diferente entre snapshots não é, por si só, divergência de conteúdo.
8. A reconciliação deve comparar primeiro o **período comum** e, depois, registrar a extensão temporal posterior.
9. Nenhum dado deve ser inventado, interpolado ou ajustado para produzir alinhamento.
10. A origem de cada registro deve permanecer auditável.

## 3. Modelo operacional

```
B3 oficial
   │
   ├── snapshot anual
   │
   └── incremento diário D
             │
             ▼
      BLOOMBERG_MAIL
             │
             ├── RAW imutável
             ├── SHA-256
             ├── NORMALIZADO
             └── REC-001
                    │
                    ▼
              B3 consolidado
```

O fluxo de dados não significa que um repositório possa alterar o RAW do outro. Significa que cada incremento validado possui uma representação persistida e rastreável nos dois repositórios.

## 4. Identidade do incremento

Cada incremento deve ser identificado por, no mínimo:

- dataset;
- data do pregão/período coberto;
- nome original do arquivo;
- URL de origem;
- timestamp UTC de aquisição;
- SHA-256;
- tamanho do arquivo;
- período inicial;
- período final;
- status de validação;
- referência cruzada para o artefato equivalente no outro repositório.

## 5. Relação com REC-001

Para o caso COTAHIST:

- `PASS_EXACT`: duas representações têm conteúdo completo idêntico;
- `PASS_OVERLAP_EXACT`: a representação mais antiga é exatamente igual em todo o período comum e a outra possui extensão temporal posterior;
- `FAIL_CONTENT_DIVERGENCE`: existe diferença dentro do período comum;
- `BLOCKED_EXECUTION`: comparação ainda não produziu evidência materializada.

A diferença de extensão temporal deve ser registrada como **diferença de cobertura**, não como divergência de conteúdo.

## 6. Não fazer

- não substituir RAW antigo por RAW novo;
- não juntar arquivos destruindo suas fronteiras de aquisição;
- não apagar incrementos depois de incorporá-los a um consolidado;
- não alterar registros para fazê-los coincidir;
- não declarar PASS sem evidência determinística;
- não usar o snapshot anual para apagar ou ignorar incrementos diários.

## 7. Resultado esperado

O BLOOMBERG_MAIL passa a funcionar também como **arquivo de aquisição incremental auditável**, enquanto o B3 permanece como base histórica consolidada e continua recebendo os incrementos validados.

Isso reduz a dependência de snapshots anuais e torna a reconciliação entre os dois repositórios simples, determinística e contínua.
