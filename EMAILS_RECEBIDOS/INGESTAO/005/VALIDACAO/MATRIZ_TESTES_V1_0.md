---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "DOCUMENTO"
fase: "FASE-005-INGESTAO"
id_documento: "BLOOMBERG-MAIL-EMAILS-RECEBIDOS-INGESTAO-005-VALIDACAO-MATRIZ-TESTES-V1-0-MD"
titulo: "MATRIZ DE TESTES — INGESTÃO 005 V1.0"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "EMAILS_RECEBIDOS/INGESTAO/005/VALIDACAO/MATRIZ_TESTES_V1_0.md"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# MATRIZ DE TESTES — INGESTÃO 005 V1.0

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

# MATRIZ DE TESTES — INGESTÃO 005 V1.0

> Histórico: 2026-10-07 | BLOOMBERG_MAIL | INGESTÃO 005

| ID | Teste | Aplicação | PASS |
|---|---|---|---|
| INT-001 | SHA-256 | todos | SHA observado = checksum registrado |
| STR-001 | estrutura | todos | arquivo/ZIP abre e contém estrutura esperada |
| SCH-001 | schema/header | todos | campos obrigatórios presentes e compatíveis |
| DAT-001 | datas | todos | datas parseáveis e dentro do período |
| TYP-001 | tipos | todos | tipos respeitam schema |
| UNT-001 | unidades | todos | unidade/escala documentadas e coerentes |
| MIS-001 | missingness | todos | ausências identificadas sem conversão silenciosa |
| DUP-001 | duplicidade | todos | chave lógica sem duplicidade inexplicada |
| ORD-001 | ordem temporal | séries | ordem/coerência temporal confirmada |
| SRC-001 | regra da fonte | todos | regra própria satisfeita |
| REC-001 | reconciliação independente | todos | coincide dentro da tolerância documentada |
| PRO-001 | proveniência | todos | fonte, URL, timestamp, período, filename, SHA e versão completos |
| EVD-001 | evidência | todos | resultado e evidência gravados |
| GAT-001 | gate | todos | todos obrigatórios PASS; nenhum FAIL/BLOCKED |

B3: STR,SCH,DAT,TYP,UNT,MIS,DUP,SRC,REC,PRO,EVD.
CVM: STR,SCH,DAT,TYP,UNT,MIS,DUP,SRC,REC,PRO,EVD.
BCB: STR,SCH,DAT,TYP,UNT,MIS,DUP,ORD,SRC,REC,PRO,EVD.
Tesouro: STR,SCH,DAT,TYP,UNT,MIS,DUP,ORD,SRC,REC,PRO,EVD.
VIX: STR,SCH,DAT,TYP,UNT,MIS,DUP,ORD,SRC,REC,PRO,EVD.

INT-001 e GAT-001 são globais.

Nenhuma tolerância é presumida. Para dados exatos, tolerância = 0; arredondamento só conforme precisão documentada.

Resultado global: VALIDATED = todos PASS; REJECTED = qualquer FAIL; BLOCKED = nenhum FAIL e algum BLOCKED; NOT_READY = aquisição/proveniência incompleta.
