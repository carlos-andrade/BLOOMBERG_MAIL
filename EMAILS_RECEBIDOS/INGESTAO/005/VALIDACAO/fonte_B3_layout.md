# BLOOMBERG_MAIL — INGESTÃO 005-B — ESPECIFICAÇÃO B3

> Cabeçalho histórico — 2026-10-07.  
> Estado: fonte e layout oficial verificados.

## Fonte

A B3 informa que as cotações históricas abrangem títulos negociados desde 1986, sem ajuste automático por inflação ou proventos. O produto inclui preços, número de negócios e volume, e é distribuído em ZIP contendo TXT de largura fixa. citeturn1view1

O layout oficial identifica o arquivo anual como `COTAHIST.AAAA.TXT`, com registros 00 (header), 01 (cotações diárias) e 99 (trailer), em registros de 245 bytes. citeturn0search16

## Decisão de engenharia

A aquisição B3 será executada pelo runner do GitHub Actions quando o artefato estiver acessível ao endpoint de download. O parser deverá:

1. preservar ZIP original em RAW;
2. calcular SHA-256 antes de qualquer transformação;
3. validar ZIP e arquivo TXT;
4. validar registros 00/01/99;
5. validar tamanho de registro;
6. preservar encoding de origem;
7. gerar NORMALIZADO somente depois dos testes estruturais;
8. registrar divergências no diretório VALIDACAO.

Não será feito ajuste de preços nesta fase.

## Evidência atual

A fonte oficial está confirmada, mas a URL dinâmica do download não foi materializada pelo mecanismo de pesquisa. Portanto, o workflow 005-B não deve inventar uma URL B3.

## Próxima execução

Prioridade operacional:
**CVM → BCB → B3 → Tesouro → VIX**, sempre com RAW + checksum + validação antes da promoção.


## Verificação operacional — 2026-10-07

A página oficial da B3 foi reaberta e confirma que o acesso à série histórica ocorre pelo link dinâmico “Acesse agora a série histórica de cotações”. O conteúdo informa histórico desde 1986, ZIP com TXT e necessidade de layout para interpretação. O mecanismo de acesso não materializou o destino do link: a tentativa controlada de seguir o link expirou por timeout. Portanto, nenhuma URL B3 foi inventada e nenhum arquivo foi tratado como adquirido.

### Estado
- Fonte oficial: CONFIRMADA
- Endpoint binário: NÃO MATERIALIZADO
- Aquisição RAW: PENDENTE
- Normalização: BLOQUEADA
- Regra: somente adquirir quando o destino oficial puder ser obtido de forma reproduzível.

### Evidência externa
A página oficial da B3 confirma a série desde 1986, ausência de ajuste automático por inflação/proventos, distribuição em ZIP e conteúdo de preços, negócios e volume. citeturn1view0


## Reconciliação com o repositório B3 — 2026-10-07

A pendência do endpoint foi resolvida no nível de descoberta/reprodutibilidade por evidência versionada no repositório `carlos-andrade/B3`. O manifesto `dados/cotahist/manifests/COTAHIST_A2026.json` registra o endpoint `https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A2026.ZIP`, o arquivo `COTAHIST_A2026.ZIP`, status `VALIDADO` e SHA-256 `4f2cf2aac1073446ccd827f5ba868fe5cf15d5cdc87d636178fe00ac06741768`. O B3 também mantém o arquivo RAW anual e seu checksum correspondente.

Assim, o estado deixa de ser **ENDPOINT NÃO MATERIALIZADO** e passa a ser **ENDPOINT RECONCILIADO**. O arquivo ainda não foi baixado novamente pelo BLOOMBERG_MAIL; portanto, a aquisição RAW e a normalização continuam pendentes.
