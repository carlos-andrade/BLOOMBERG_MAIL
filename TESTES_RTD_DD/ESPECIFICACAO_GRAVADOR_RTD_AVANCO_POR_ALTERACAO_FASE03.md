---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "ESPECIFICACAO_TECNICA"
fase: "FASE-03-DETECAO-DE-ALTERACOES-RTD"
id_documento: "BLOOMBERG-MAIL-RTD-CAP-003"
titulo: "Gravador RTD por alteração observada"
status: "ESPECIFICADO; GRAVACAO DESATIVADA; AGUARDA TESTES"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
---



# Especificação — gravador RTD por alteração observada

> **Projeto:** BLOOMBERG_MAIL
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL
> **Tipo:** ESPECIFICACAO_TECNICA
> **Fase:** FASE-03-DETECAO-DE-ALTERACOES-RTD
> **ID:** BLOOMBERG-MAIL-RTD-CAP-003
> **Status:** ESPECIFICADO; GRAVACAO DESATIVADA; AGUARDA TESTES
> **Versão:** 1.0
> **Criação:** 2026-10-09
> **Atualização:** 2026-10-09
> **Origem:** N/A
> **Autoridade:** LAYOUT
> **Rastreabilidade:** N/A


## Contexto histórico
A inspeção estática de `RDT_PROFIT.xlsx` identificou a folha `Folha1`, cabeçalhos na linha 1 e campos na linha 2, incluindo fórmulas RTD. A atualização em tempo real ainda não foi validada. O utilizador definiu que deve ser criada uma nova linha sempre que algum dado monitorizado mudar.

## Regra funcional
1. Obter um snapshot completo e coerente dos campos monitorizados.
2. Compará-lo com o último snapshot válido observado.
3. Se pelo menos um campo mudar, criar exatamente uma linha com o snapshot completo.
4. Se nenhum campo mudar, não criar linha.
5. A primeira leitura válida estabelece a referência inicial; não é gravada por defeito.
6. Alterações em vários campos na mesma observação geram uma única linha.
7. A referência só avança após a escrita no destino ser confirmada.

## Deteção
Não depender exclusivamente de `Worksheet_Change`: resultados de fórmulas RTD podem mudar sem edição direta. Testar `Worksheet_Calculate` e, se necessário, polling controlado. A implementação deve evitar reentrância, escrita nas células de origem e snapshots parciais.

## Campos e integridade
Confirmar no livro local atual os endereços e campos. A auditoria anterior reportou 36 fórmulas RTD entre B2:AL2, com A2 fixo (`WINFUT`) e M2 fixo (`Ibovespa Mini`). Comparar valores efetivos, não fórmulas; incluir mudanças para/de vazio ou erro como estados explícitos. Não arredondar preços/quantidades para deduplicar. Guardar timestamp local de receção separado da hora do feed; não o apresentar como hora de mercado.

Cada registo deve conter número sequencial, timestamp ISO 8601 com offset/fuso, instrumento, snapshot integral, estado/qualidade do feed e versão do esquema. Os dados operacionais devem ficar num destino local autorizado e fora do Git. Não enviar ordens nem automatizar trading.

## Testes obrigatórios
- T01 confirmar folha, células, cabeçalhos e campos monitorizados.
- T02 primeira leitura estabelece referência sem gravar por defeito.
- T03 snapshot inalterado não gera linha.
- T04 alteração de um campo gera uma linha completa.
- T05 alteração de vários campos numa observação gera uma só linha.
- T06 alteração de oferta/quantidade gera linha mesmo com último preço inalterado.
- T07 vazio/erro/recuperação são tratados explicitamente.
- T08 snapshots repetidos não duplicam linhas.
- T09 interrupção/reconexão é diagnosticada.
- T10 falha de escrita não avança silenciosamente a referência.
- T11 captura não bloqueia recálculo nem altera origem.
- T12 paragem/reinício têm comportamento documentado.
- T13 destino local está excluído do Git.

## Limitação
O gravador regista alterações efetivamente observadas. Estados que surjam e desapareçam entre duas leituras podem não ser capturados; isto não garante captura integral de ticks ou negócios.

## Critérios para ativar
Manter `GRAVACAO_DESATIVADA` até que o mapeamento e os testes estejam aprovados, o destino local e as exclusões Git sejam verificados, a autorização de armazenamento esteja confirmada e o utilizador autorize expressamente a ativação.

## Roadmap
- [x] Definir regra de avanço por alteração observada.
- [x] Preparar especificação.
- [ ] Registar especificação no repositório.
- [ ] Confirmar mapeamento no workbook atual.
- [ ] Testar deteção RTD numa sessão ativa.
- [ ] Implementar protótipo em modo diagnóstico sem gravação persistente.
- [ ] Executar e documentar T01–T13.
- [ ] Validar destino local, integridade e exclusões Git.
- [ ] Obter autorização explícita para ativar.
