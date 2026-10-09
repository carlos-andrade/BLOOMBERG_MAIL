---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "PROCEDIMENTO_TECNICO"
fase: "FASE-03-FEED-INTRADAY"
id_documento: "BLOOMBERG-MAIL-TESTE-RTD-DDE-PROFIT-001"
titulo: "Teste assistido RTD/DDE do Profit"
status: "AGUARDA_EXECUCAO_LOCAL"
versao: "1.0"
data_criacao: "2026-10-09"
data_atualizacao: "2026-10-09"
origem: "WATCHDOG/CARTA_FEED_INTRADAY_FASE03.md; confirmação do utilizador"
autoridade_documental: "LAYOUT"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "WATCHDOG/MATRIZ_FONTES_FEED_INTRADAY_2026-10-09.json; WATCHDOG/EVIDENCIAS/RTD_DDE_PROFIT_001.json"
escopo: "Verificação manual e controlada da exportação RTD/DDE; sem ordens e sem coletor automático"
objetivo: "Determinar se a edição/conta Profit do utilizador expõe dados utilizáveis por RTD/DDE com timestamps, cobertura e comportamento operacional verificáveis."
dependencias: "Acesso local ao Profit; aplicação de folha de cálculo compatível; termos de licença aplicáveis"
---

# Procedimento de teste — Profit RTD/DDE

> **Projeto:** BLOOMBERG_MAIL  
> **Repositório:** carlos-andrade/BLOOMBERG_MAIL  
> **Tipo:** PROCEDIMENTO_TECNICO  
> **Fase:** FASE-03-FEED-INTRADAY  
> **ID:** BLOOMBERG-MAIL-TESTE-RTD-DDE-PROFIT-001  
> **Status:** AGUARDA_EXECUCAO_LOCAL  
> **Versão:** 1.0  
> **Criação/atualização:** 2026-10-09  
> **Autoridade:** LAYOUT  
> **Cadeia:** PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO

## 1. Contexto e evidência inicial

O utilizador confirmou que a opção **Arquivo → Exportar em Tempo Real** está disponível na instalação do Profit. Esta é uma confirmação de disponibilidade do menu, não uma prova de transmissão RTD/DDE funcional, cobertura de instrumentos, timestamp de origem, latência ou direitos de armazenamento.

Documentação oficial da Nelogica: [Como configurar RTD/DDE no Profit](https://ajuda.nelogica.com.br/hc/pt-br/articles/360044293432-Como-configurar-RTD-DDE-no-Profit).

## 2. Segurança e limites

- Executar apenas observação manual e exportação para uma folha de cálculo local.
- Não enviar ordens; não ativar funções de envio, automação ou trading.
- Não publicar capturas com nome, número de conta, e-mail, tokens, licenças ou outros dados privados.
- Não guardar credenciais nem dados pessoais no repositório.
- Antes de armazenar séries de mercado de forma persistente, confirmar por escrito os direitos aplicáveis a captura, armazenamento, transformação e uso interno.
- Usar apenas instrumentos que a conta esteja autorizada a consultar.
- Se a plataforma não expuser timestamp da origem, registar explicitamente como ausente; não o substituir pelo timestamp local.
- Não assumir que a atualização visível de uma célula prova que cada evento foi recebido, nem que RTD e DDE têm semântica idêntica em todas as versões.

## 3. Execução

### Etapa A — Preparação

1. Abrir o Profit e confirmar que a sessão de mercado e a conta estão operacionais.
2. Abrir **Arquivo → Exportar em Tempo Real**.
3. Consultar as opções apresentadas pela versão instalada e selecionar o método RTD ou DDE documentado pela própria aplicação.
4. Abrir uma folha de cálculo local vazia. Não utilizar ficheiros que contenham credenciais.
5. Registar versão/edição do Profit, versão da folha de cálculo, método escolhido e data/hora local com fuso horário.

**Critério A:** o assistente de exportação abre e permite identificar o destino/método sem erro. Caso contrário, parar e registar a mensagem de erro, sem inferir a causa.

### Etapa B — Primeiro instrumento e campos

1. Escolher um instrumento autorizado e líquido que apareça na conta. Se WIN e WDO estiverem disponíveis, testar ambos separadamente; caso contrário, registar indisponibilidade.
2. Selecionar apenas campos que a interface/documentação efetivamente disponibilize. Prioridade:
   - símbolo/código do instrumento;
   - último preço;
   - melhor compra e melhor venda, se disponíveis;
   - volume/quantidade negociada, com semântica identificada;
   - timestamp de origem ou timestamp da última atualização, se exposto.
3. Iniciar a exportação e observar a folha durante pelo menos 10 minutos numa sessão de mercado ativa. Para avaliar estabilidade, o ensaio recomendado é de 30 minutos.
4. Guardar localmente uma captura redigida da configuração e da folha, sem dados privados. Registar a evidência no manifesto JSON por descrição, nome de ficheiro local não sensível ou hash; anexar a captura ao repositório apenas se não houver restrições de licença.

**Critério B:** símbolo e campos são identificáveis; as alterações observadas são coerentes com o instrumento; a semântica dos campos é documentada. Se não existir timestamp de origem, o gate temporal fica pendente.

### Etapa C — Atualização e freshness

1. Registar pelo menos 10 observações espaçadas ao longo do ensaio, incluindo hora local de receção em UTC e fuso original.
2. Se houver timestamp da origem, calcular a diferença entre hora de receção UTC e timestamp de origem convertido para UTC.
3. Distinguir latência observada de frequência de atualização: são medidas diferentes.
4. Registar mercado fechado, instrumento sem negócio, célula sem alteração ou feed parado como situações distintas; não concluir falha apenas porque o último preço não mudou.
5. Não fixar SLA arbitrário. Definir o limite apenas depois de conhecer a semântica do feed, a frequência esperada e os termos do fornecedor.

**Critério C:** origem temporal identificada, amostras auditáveis e regra de freshness justificável. Sem timestamp de origem, pode-se medir apenas o comportamento de atualização local, não a latência real de mercado.

### Etapa D — Desconexão e recuperação

1. Não interromper a conectividade do computador inteiro se isso puder afetar outras atividades. Usar primeiro um procedimento suportado pela aplicação para parar/reiniciar a exportação ou simular a indisponibilidade da folha de cálculo.
2. Registar a hora de início da interrupção, valores mantidos na folha, mensagens apresentadas e comportamento de recuperação.
3. Retomar a exportação e observar se os valores voltam a atualizar.
4. Registar se houve gaps, repetição de valores, perda de ligação ou necessidade de reabrir a folha/aplicação.
5. Não tratar o último valor retido como atual: após exceder o limite de frescura validado, o estado futuro deverá ser STALE/UNKNOWN, não UP.

**Critério D:** comportamento da interrupção e recuperação descrito e repetível. O ensaio de uma folha RTD/DDE não substitui testes de sequência/gaps de um feed de eventos completo.

## 4. Resultados a registar

Atualizar WATCHDOG/EVIDENCIAS/RTD_DDE_PROFIT_001.json com:
- estado real do ensaio e data/hora;
- método RTD ou DDE e versões;
- instrumentos e campos realmente observados;
- presença/ausência de timestamp de origem;
- número de amostras e duração;
- latência, apenas se calculável a partir de timestamp de origem;
- interrupção/reconexão e gaps observados;
- evidências locais redigidas;
- situação da licença e armazenamento;
- limitações e resultado de cada critério.

Não preencher resultados por suposição. Se o ensaio não tiver sido executado, manter NOT_RUN.

## 5. Gate de decisão

A fonte permanece PENDING_EVIDENCE até haver evidência funcional, cobertura dos instrumentos prioritários, timestamp/freshness, comportamento em falha e confirmação dos direitos de utilização. A presença do menu, isoladamente, não satisfaz nenhum gate de aprovação.

**Próximo passo:** executar as Etapas A e B no computador do utilizador e registar os campos que a interface realmente disponibiliza. Não será criado coletor nem código de ingestão nesta etapa.
