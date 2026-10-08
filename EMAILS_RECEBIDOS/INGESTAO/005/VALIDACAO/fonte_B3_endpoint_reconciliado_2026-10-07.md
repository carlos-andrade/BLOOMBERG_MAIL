---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-FONTE-B3-ENDPOINT-RECONCILIADO-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — INGESTÃO 005 — RECONCILIAÇÃO DO ENDPOINT B3"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/fonte_B3_endpoint_reconciliado_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — INGESTÃO 005 — RECONCILIAÇÃO DO ENDPOINT B3

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

# BLOOMBERG_MAIL — INGESTÃO 005 — RECONCILIAÇÃO DO ENDPOINT B3

> Cabeçalho histórico — 2026-10-07.
> Artefato de governança: reconciliação da aquisição B3 com a infraestrutura já existente no repositório oficial interno B3.

## Resultado

O endpoint anual COTAHIST foi localizado e confirmado por evidência versionada no repositório `carlos-andrade/B3`.

Arquivo de referência:

- `dados/cotahist/manifests/COTAHIST_A2026.json`
- SHA do blob de referência: `314c860ded632dac2dc0b98f53c4fba32a4a35e7`
- fonte declarada: `B3`
- arquivo original: `COTAHIST_A2026.ZIP`
- endpoint declarado: `https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A2026.ZIP`
- status no manifesto B3: `VALIDADO`
- SHA-256 do artefato B3: `4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768`
- validação declarada: ZIP com 1 arquivo COTAHIST; registros de 245 bytes; header 00; cotações 01; trailer 99
- aquisição registrada no B3: `2026-09-24T07:52:17.798962+00:00`

## Reconciliação adicional

O B3 também mantém:

- `dados/cotahist/raw/anual/COTAHIST_A2026.ZIP`
- `dados/cotahist/checksums/COTAHIST_A2026.ZIP.sha256`

O checksum publicado pelo B3 é:

`4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768`

A infraestrutura B3 mantém arquivos anuais desde 1986 e arquivos diários COTAHIST em `dados/cotahist/raw/diario/`.

## Workflow de referência

O repositório B3 possui o workflow:

`.github/workflows/cotahist-orquestrador-anual-dryrun-v2.yml`

Ele trata como pré-condição da FASE 01 a existência de:

`dados/cotahist/raw/anual/COTAHIST_A{ano}.ZIP`

A cadeia posterior depende de RAW → parser → normalização → validação → certificação.

## Decisão BLOOMBERG_MAIL

A pendência anterior de **endpoint B3 não materializado** fica **resolvida no nível de descoberta/reprodutibilidade do endpoint**.

A aquisição binária dentro de `BLOOMBERG_MAIL` continua separada da descoberta do endpoint.

Portanto:

- endpoint B3: **RECONCILIADO**
- fonte: **CONFIRMADA**
- arquivo-alvo: **COTAHIST_A2026.ZIP**
- checksum de referência: **CONFIRMADO**
- RAW dentro de BLOOMBERG_MAIL: **AINDA NÃO ADQUIRIDO**
- normalização em BLOOMBERG_MAIL: **BLOQUEADA**
- promoção da camada A: **BLOQUEADA**

## Regra

Não copiar um arquivo do repositório B3 para BLOOMBERG_MAIL e chamá-lo de aquisição da fonte primária.

Quando a aquisição for executada no BLOOMBERG_MAIL, o runner deverá baixar o endpoint B3, calcular seu próprio SHA-256 e comparar com a evidência de referência quando o mesmo arquivo/período for utilizado.

Diferença de checksum deverá gerar bloqueio e investigação, nunca substituição silenciosa.

## Próximo passo controlado

Executar a aquisição binária B3 em `INGESTAO/005/RAW`, preservando:

1. URL;
2. timestamp UTC;
3. nome original;
4. tamanho;
5. SHA-256;
6. teste ZIP;
7. conteúdo interno;
8. comparação com a estrutura COTAHIST esperada.

Somente depois disso o dataset poderá avançar para normalização.
