---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "RELATORIO_EVIDENCIA_INSPECAO_XML"
fase: "FASE-02-MAPEAMENTO-RTD"
id_documento: "BLOOMBERG-MAIL-RTD-XML-001"
titulo: "Resultado da inspeção XML da cópia de diagnóstico RDT_PROFIT"
status: "INSPECAO_ESTRUTURAL_CONCLUIDA; MAPEAMENTO_DE_CABECALHOS_PENDENTE"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "Saída PowerShell fornecida pelo utilizador após leitura de uma cópia local"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "TESTES_RTD_DD/ESPECIFICACAO_MAPEAMENTO_CAPTURA_RTD_FASE02.md; TESTES_RTD_DD/AUDITORIA_RDT_PROFIT_XLSX_2026-10-09.md"
escopo: "Registar estrutura de fórmulas sem publicar valores de mercado em cache"
objetivo: "Confirmar a localização das fórmulas RTD e preparar o mapeamento dos cabeçalhos"
dependencias: "Cópia local RDT_PROFIT_DIAGNOSTICO.xlsx; inspeção XML PowerShell"
---



# Resultado da inspeção XML — cópia de diagnóstico

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** RELATORIO_EVIDENCIA_INSPECAO_XML
> **Fase:** FASE-02-MAPEAMENTO-RTD
> **ID:** BLOOMBERG-MAIL-RTD-XML-001
> **Status:** INSPECAO_ESTRUTURAL_CONCLUIDA; MAPEAMENTO_DE_CABECALHOS_PENDENTE
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** Saída PowerShell fornecida pelo utilizador após leitura de uma cópia local
> **Autoridade:** LAYOUT
> **Rastreabilidade:** TESTES_RTD_DD/ESPECIFICACAO_MAPEAMENTO_CAPTURA_RTD_FASE02.md; TESTES_RTD_DD/AUDITORIA_RDT_PROFIT_XLSX_2026-10-09.md


## Contexto Histórico

Em 2026-10-09, o utilizador executou uma inspeção XML de uma cópia de diagnóstico do ficheiro `RDT_PROFIT.xlsx`. A cópia foi lida sem abrir nem modificar intencionalmente o workbook original. O relatório regista apenas a estrutura das fórmulas; os valores de mercado em cache foram omitidos para não publicar dados operacionais no repositório.

## Estado

- Cópia de diagnóstico encontrada: PASS.
- XML do workbook e relações: PASS.
- Folha identificada: `Folha1`.
- Fórmulas RTD encontradas: 36.
- Atualização RTD ao vivo: NOT VERIFIED.
- Mapeamento de cabeçalhos por endereço: PENDING.
- Gravação histórica automática: NOT IMPLEMENTED.
- Direitos/licença para armazenamento de dados: PENDING.
- Ativação em produção: BLOCKED.

## Evidências

As 36 fórmulas encontradas estão na linha 2. Todas utilizam o servidor `rtdtrading.rtdserver` e o identificador de instrumento `WINFUT_F_0`.

| Célula | Tópico RTD |
|---|---|
| B2 | DAT |
| C2 | HOR |
| D2 | ULT |
| E2 | ABE |
| F2 | MAX |
| G2 | MIN |
| H2 | FEC |
| I2 | PEX |
| J2 | VAR |
| K2 | VARPTS |
| L2 | MED |
| N2 | NEG |
| O2 | QUL |
| P2 | QTT |
| Q2 | VOL |
| R2 | OCP |
| S2 | OVD |
| T2 | VOC |
| U2 | VOV |
| V2 | AJU |
| W2 | AJA |
| X2 | PRT |
| Y2 | QTE |
| Z2 | VPJ |
| AA2 | SEM |
| AB2 | MES |
| AC2 | 3M |
| AD2 | 6M |
| AE2 | 12M |
| AF2 | ANO |
| AG2 | TRIM |
| AH2 | SEMES |
| AI2 | VEN |
| AJ2 | VAL |
| AK2 | CAB |
| AL2 | EST |

A célula `M2` não contém uma fórmula RTD na cópia inspecionada. A saída também indica que a inspeção terminou com 36 fórmulas encontradas.

## Validação

A leitura XML confirma a estrutura guardada na cópia, mas não demonstra atualização ao vivo, frequência de alteração, integridade temporal, reconexão ou captura de todos os eventos de mercado.

O erro posterior `finally is not recognized` ocorreu porque o bloco `finally` foi inserido como comando separado depois de concluído o bloco `try/catch`. Esse erro não invalida a saída de inspeção que já foi produzida. Não executar o `finally` isoladamente.

## Resultado

`DIAGNOSTIC_COPY=FOUND`  
`WORKBOOK_XML_READ=PASS`  
`RTD_FORMULA_COUNT=36`  
`RTD_LIVE_UPDATE=NOT_VERIFIED`  
`HEADER_CELL_MAPPING=PENDING`  
`AUTOMATIC_CAPTURE=NOT_IMPLEMENTED`  
`STORAGE_RIGHTS=PENDING`  
`PRODUCTION_INGESTION=BLOCKED`

## Próxima Ação

Extrair da mesma cópia os valores da linha 1 para mapear os cabeçalhos aos endereços de coluna. Não iniciar ainda a gravação automática. Depois de validar o mapa, especificar um gravador separado que não altere as células RTD de origem, registe a hora local de receção, deduplique snapshots conforme regra explícita e mantenha os dados operacionais fora do Git.
