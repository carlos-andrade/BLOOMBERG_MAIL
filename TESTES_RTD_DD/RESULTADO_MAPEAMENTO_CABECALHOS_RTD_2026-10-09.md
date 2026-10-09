---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-RESULTADO-MAPEAMENTO-CABECALHOS-RTD-2026-10-09-MD"
titulo: "BLOOMBERG_MAIL — Resultado do mapeamento dos cabeçalhos RTD"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/RESULTADO_MAPEAMENTO_CABECALHOS_RTD_2026-10-09.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "N/A"
id_documento: "BLOOMBERG-MAIL-TESTES-RTD-DD-RESULTADO-MAPEAMENTO-CABECALHOS-RTD-2026-10-09-MD"
titulo: "BLOOMBERG_MAIL — Resultado do mapeamento dos cabeçalhos RTD"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "TESTES_RTD_DD/RESULTADO_MAPEAMENTO_CABECALHOS_RTD_2026-10-09.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# BLOOMBERG_MAIL — Resultado do mapeamento dos cabeçalhos RTD

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** DOCUMENTO
> **Fase:** N/A
> **ID:** BLOOMBERG-MAIL-TESTES-RTD-DD-RESULTADO-MAPEAMENTO-CABECALHOS-RTD-2026-10-09-MD
> **Status:** IMPLEMENTADO
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** BLOOMBERG_MAIL
> **Autoridade:** GOVERNANÇA
> **Rastreabilidade:** MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA


# BLOOMBERG_MAIL — Resultado do mapeamento dos cabeçalhos RTD

> **Projeto:** BLOOMBERG_MAIL  
> **Área:** TESTES_RTD_DD  
> **Data da verificação:** 2026-10-09  
> **Origem:** inspeção XML somente de leitura da cópia diagnóstica `RDT_PROFIT_DIAGNOSTICO.xlsx`  
> **Estado:** MAPEAMENTO ESTÁTICO CONFIRMADO; CAPTURA AO VIVO AINDA NÃO VALIDADA

## Objetivo

Relacionar os cabeçalhos da linha 1 da folha `Folha1` com as fórmulas RTD encontradas na linha 2, sem alterar a pasta de trabalho original e sem publicar valores de mercado em cache.

## Mapeamento

| Coluna | Cabeçalho na linha 1 | Tópico RTD na linha 2 |
|---|---|---|
| A | Asset | Sem fórmula RTD identificada |
| B | Data | DAT |
| C | Hora | HOR |
| D | Último | ULT |
| E | Abertura | ABE |
| F | Máximo | MAX |
| G | Mínimo | MIN |
| H | Fechamento Anterior | FEC |
| I | Strike | PEX |
| J | Variação | VAR |
| K | Variação(pts) | VARPTS |
| L | Média | MED |
| M | Nome do Ativo | Sem fórmula RTD identificada |
| N | Negócios | NEG |
| O | QUL | QUL |
| P | Quantidade | QTT |
| Q | Volume | VOL |
| R | Of. Compra | OCP |
| S | Of. Venda | OVD |
| T | VOC | VOC |
| U | VOV | VOV |
| V | Ajuste | AJU |
| W | Aj. Anterior | AJA |
| X | Preço Teórico | PRT |
| Y | Qtd. Teórica | QTE |
| Z | Volume Projetado | VPJ |
| AA | Semana | SEM |
| AB | Mês | MES |
| AC | 3 meses | 3M |
| AD | 6 meses | 6M |
| AE | 12 meses | 12M |
| AF | Ano | ANO |
| AG | Trimestre | TRIM |
| AH | Semestre | SEMES |
| AI | Vencimento | VEN |
| AJ | Validade | VAL |
| AK | Cont. Abertos | CAB |
| AL | Estado Atual | EST |

## Observações e limites

1. A inspeção confirma a estrutura estática da cópia examinada: cabeçalhos na linha 1 e fórmulas RTD em B2:AL2, com M2 sem fórmula.
2. A coluna A (`Asset`) e a coluna M (`Nome do Ativo`) não têm fórmula RTD identificada na linha 2. A forma como esses campos são preenchidos ainda precisa ser determinada.
3. A leitura do XML não comprova que o RTD esteja atualizando ao vivo, que a hora represente a hora de cada negócio, nem que seja possível recuperar todos os ticks.
4. Não foi implementada nem ativada qualquer gravação automática. A planilha original não foi alterada por esta inspeção.
5. Valores de mercado em cache foram deliberadamente omitidos deste relatório.

## Próximas etapas

1. Determinar a origem de `Asset` e `Nome do Ativo`, incluindo a eventual existência de fórmulas, valores fixos ou preenchimento manual.
2. Validar ao vivo, com teste controlado, quais células mudam e com que comportamento.
3. Definir a regra de captura: instante de observação, deduplicação, tratamento de desconexões e registo de lacunas.
4. Implementar o gravador separado somente após aprovação da especificação e dos testes de aceitação.
5. Manter dados operacionais brutos e históricos locais, fora do Git, salvo autorização e direitos de armazenamento confirmados.

## Critério de conclusão desta etapa

**Concluída:** cabeçalhos e tópicos RTD mapeados estaticamente.  
**Pendente:** origem das colunas A e M, teste RTD ao vivo e validação da estratégia de captura.
