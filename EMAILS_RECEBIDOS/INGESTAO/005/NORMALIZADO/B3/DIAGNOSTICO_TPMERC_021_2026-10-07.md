---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-B3-DIAGNOSTICO-TPMERC-021-2026-10-07-MD"
titulo: "BLOOMBERG_MAIL — Diagnóstico COTAHIST A2026 — TPMERC 021"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/B3/DIAGNOSTICO_TPMERC_021_2026-10-07.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---



# BLOOMBERG_MAIL — Diagnóstico COTAHIST A2026 — TPMERC 021

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** FASE-005-INGESTAO
> **ID:** BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-B3-DIAGNOSTICO-TPMERC-021-2026-10-07-MD
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

# BLOOMBERG_MAIL — Diagnóstico COTAHIST A2026 — TPMERC 021

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Repositório: carlos-andrade/BLOOMBERG_MAIL
- Etapa: INGESTÃO 005N — Validação do layout B3
- Data: 2026-10-07
- Natureza: evidência determinística de execução
- RAW: imutável

## Execução
- Workflow: BLOOMBERG_MAIL — INGESTÃO 005N — Validação Layout B3 COTAHIST
- Run: #7
- Run ID: 37694046706
- Commit executor: 0ba7f00cbab1c82535c96da8c5c44de953809cf0
- Evento: push controlado sobre alteração do validador
- Resultado: FAIL

## Evidência
- RAW SHA-256 esperado/observado: c65e64f468def41439ff05e47869d934b406cb3f59ab2638f66a3a59bd4d974f
- ZIP íntegro: SIM
- Membro: COTAHIST_A2026.TXT
- Registros físicos: 3.070.833
- Registro 00: 1
- Registro 01: 3.070.831
- Registro 99: 1
- Comprimento de registros: 245 bytes, sem inválidos
- Trailer = registros 01: SIM
- TPMERC inválidos: 1.696
- Valor observado dos TPMERC inválidos: 021 (1.696 ocorrências)
- CODBDI em branco: 0
- INDOPC inválido: 0
- Datas inválidas: 0
- Campos numéricos inválidos: 0

## Decisão
O código TPMERC 021 foi observado no RAW de 2026, mas não está contemplado na tabela TPMERC do layout B3 v2.0/revisão 02 utilizado como referência, que documenta 010, 012, 013, 017, 020, 030, 050, 060, 070 e 080.

Portanto, o sistema **não deve atribuir significado ao código 021 por inferência**. A validação permanece FAIL/BLOCKED até existir fonte oficial que reconcilie o código 021.

## Governança
- RAW alterado: NÃO
- Normalização executada: NÃO
- Interpolação: NÃO
- Invenção: NÃO
- Ajuste econômico: NÃO
- Sinais operacionais: NÃO
- Normalizador B3: BLOQUEADO
- Integração: BLOQUEADA

## Próximo gate
Identificar fonte oficial B3 que defina TPMERC 021 para COTAHIST A2026. Somente após essa reconciliação:
1. atualizar o mapeamento autoritativo;
2. corrigir o validador;
3. executar novamente;
4. exigir PASS;
5. publicar a evidência final;
6. só então liberar o normalizador B3.


## Pesquisa de reconciliação — 2026-10-07

### Evidência oficial B3
A página oficial de Cotações Históricas confirma que o COTAHIST usa um layout para interpretar o TXT e que o produto contém o tipo de mercado. O PDF oficial B3 v2.0/revisão 02 mantém a tabela TPMERC com os códigos 010, 012, 013, 017, 020, 030, 050, 060, 070 e 080; **021 não aparece nessa tabela**.

Fonte oficial: https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/
PDF oficial: https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf

### Evidência histórica/externa
Foi localizada uma reprodução de catálogo de domínios que contém `TpMerc 21` entre os valores de um catálogo posterior, mas a fonte localizada não fornece, no trecho disponível, a descrição semântica do código 21. Essa evidência demonstra que o código pode existir em um domínio mais recente, mas **não autoriza atribuir significado ao TPMERC=021 do COTAHIST A2026**. Portanto, permanece apenas como pista de investigação.

### Decisão de governança
Não alterar o significado de `021`, não substituir por outro código e não liberar o validador. O próximo gate é obter uma fonte B3 autoritativa que associe explicitamente `21/021` a uma descrição de mercado aplicável ao COTAHIST A2026. Até lá: FAIL/BLOCKED.
