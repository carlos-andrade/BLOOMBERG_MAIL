---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-NORMALIZADO-CARTA-GATE-CONJUNTO-005N-V1-0-2026-10-08-MD"
titulo: "BLOOMBERG_MAIL — CARTA — GATE CONJUNTO 005N — 5/5"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/CARTA_GATE_CONJUNTO_005N_V1_0_2026-10-08.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — CARTA — GATE CONJUNTO 005N — 5/5

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

# BLOOMBERG_MAIL — CARTA — GATE CONJUNTO 005N — 5/5

> Cabeçalho histórico: documento de governança criado em 2026-10-08 para consolidar, em um único gate determinístico, a validação dos cinco datasets da INGESTÃO 005N após a conclusão do normalizador B3.

## 1. Objetivo

O Gate Conjunto 005N verifica se os cinco datasets normalizados da INGESTÃO 005 estão simultaneamente aptos para a etapa de integração, sem executar transformações entre datasets.

Datasets obrigatórios:

1. B3 COTAHIST A2026
2. CVM Ofertas
3. BCB SGS 1178
4. Tesouro Histórico
5. VIX

## 2. Regra de PASS

O gate somente pode resultar em **PASS** quando todos os cinco datasets estiverem com:

- manifesto normalizado existente;
- `quality_status = NORMALIZED_DERIVED`;
- SHA-256 RAW consistente com o manifesto de aquisição;
- parser/layout identificável;
- saída derivada existente;
- integridade dos arquivos derivados comprimidos, quando aplicável;
- validação individual PASS;
- proveniência suficiente;
- política RAW imutável;
- ausência de interpolação, invenção e ajuste econômico;
- duplicidades e missingness explicitamente reportados, sem remoção silenciosa.

O B3 exige adicionalmente a validação independente `VALIDACAO_NORMALIZACAO_B3_A2026.json = PASS`.

## 3. O que este gate NÃO faz

Este gate não:

- cruza séries entre fontes;
- cria chaves de integração;
- escolhe uma fonte como verdade econômica;
- ajusta preços;
- preenche dados;
- remove duplicidades;
- gera ranking, previsão ou sinal operacional.

Essas operações pertencem às etapas posteriores e devem possuir suas próprias cartas, layouts e gates.

## 4. Duplicidades

Duplicidade declarada não é automaticamente falha. O gate exige que a contagem esteja registrada e que nenhum registro tenha sido removido silenciosamente.

A caracterização econômica/estrutural das duplicidades do B3 será tratada na reconciliação seguinte.

## 5. Evidência

O executor é:

`scripts/validacao_gate_conjunto_005n.py`

A evidência persistida é:

`EMAILS_RECEBIDOS/INGESTAO/005/NORMALIZADO/VALIDACAO_GATE_CONJUNTO_005N_5X5.json`

O workflow é manual por padrão. Qualquer execução controlada por `push` é temporária e deve ser restaurada para manual-only após o teste.

## 6. Gate seguinte

Somente após **5/5 PASS** fica elegível a execução de **REC-001 de integração cruzada**. PASS neste gate não constitui autorização para gerar inteligência de mercado.
