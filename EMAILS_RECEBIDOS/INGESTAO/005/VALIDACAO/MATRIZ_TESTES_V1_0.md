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
