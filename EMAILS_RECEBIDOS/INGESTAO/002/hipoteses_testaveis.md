---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-002-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-002-HIPOTESES-TESTAVEIS-MD"
titulo: "INGESTÃO 002 — HIPÓTESES TESTÁVEIS"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/002/hipoteses_testaveis.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# INGESTÃO 002 — HIPÓTESES TESTÁVEIS

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

# INGESTÃO 002 — HIPÓTESES TESTÁVEIS

## Cabeçalho histórico
- Projeto: BLOOMBERG_MAIL
- Fonte primária: newsletter Bloomberg recebida em MSG
- Ingestão de origem: 001
- Camada: extração estruturada
- Regra: separar afirmação da fonte, hipótese analítica e resultado de teste.

## H1 — Concentração reduz amplitude
**Hipótese:** quando o índice sobe para máximas enquanto a participação da alta se concentra em poucas empresas, a amplitude interna tende a deteriorar.
**Teste futuro:** comparar breadth, participação das maiores ações, advance/decline, new highs/new lows e concentração de retorno no S&P 500 e, por tradução, no IBOV/IBrX.
**Variáveis brasileiras:** IBOV, IBrX 100, small caps, volume financeiro, número de ativos positivos/negativos e contribuição por ativo.

## H2 — Oferta de ações pode comprimir valuation
**Hipótese:** aumento persistente de IPOs, follow-ons e outras emissões pode reduzir o suporte marginal dos preços mesmo com earnings crescendo.
**Teste futuro:** construir série temporal de equity supply e confrontá-la com retorno futuro, valuation forward, volume e volatilidade.
**Variáveis brasileiras:** IPO, follow-on, ofertas subsequentes, free float, volume financeiro e múltiplos.

## H3 — Lock-up é choque de oferta
**Hipótese:** grandes liberações de ações devem ser tratadas como eventos de supply shock e não apenas como eventos corporativos.
**Teste futuro:** medir retornos anormais, volume, volatilidade e liquidez antes/depois do evento.

## H4 — Fiscal + política + duration
**Hipótese:** o efeito de risco fiscal/político sobre títulos depende da duration e da posição da curva, e não apenas do nível absoluto da dívida.
**Teste futuro:** cruzar mudanças em risco político/fiscal com inclinação da curva, taxas longas, duration e marcação a mercado.
**Tradução brasileira:** DI, NTN-B, NTN-F, dólar, CDS Brasil quando disponível e ativos de risco.

## H5 — Newsletter só vira informação útil depois de validação
**Hipótese metodológica:** uma narrativa recebida gratuitamente só adquire valor operacional quando seus fatos são identificados, validados contra fontes independentes, convertidos em séries temporais e testados fora da amostra.
**Critério:** nenhum sinal será promovido a regra de trading sem evidência estatística e controle de overfitting.

## Resultado desta etapa
Nenhuma hipótese acima é considerada comprovada. Esta camada define apenas o que deverá ser medido.
