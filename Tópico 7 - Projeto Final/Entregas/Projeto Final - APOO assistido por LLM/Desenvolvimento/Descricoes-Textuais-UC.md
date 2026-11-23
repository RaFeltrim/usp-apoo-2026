# Descrições Textuais Estendidas de Casos de Uso — Plataforma ClickBus

> **Referência:** Capítulo 3 — Especificação gerada na Etapa 2 ([`Diretrizes - APOO apoiado por LLM.docx.pdf`](<../../../Material%20de%20Apoio/Diretrizes%20-%20APOO%20apoiado%20por%20LLM.docx.pdf>), págs. 5–6, Figura 3).  
> **Artefatos de entrada:** [`01-casos-de-uso-final.puml`](<./PUML/01-casos-de-uso-final.puml>) e [`Historias-de-Usuario.md`](<./Historias-de-Usuario.md>).

---

### UC01 — Pesquisar e Comparar Viagens
- **Rastreabilidade:** HU01, HU02
- **Ator Primário:** Passageiro
- **Atores Secundários:** —
- **Relacionamentos:** Pode ser estendido por `UC02 - Selecionar e Reservar Assentos` (`<<extend>>`).
- **Pré-condições:** A plataforma está operacional e há rotas, horários e tarifas cadastrados pelas Empresas de Viação.
- **Pós-condições:** O Passageiro visualiza a lista de viagens compatíveis com os filtros informados, ordenada/comparada por preço, horário e viação.
- **Fluxo Principal:**
  1. O Passageiro acessa a tela inicial de busca da plataforma.
  2. O Passageiro informa cidade de origem, cidade de destino e data desejada da viagem.
  3. O sistema valida os parâmetros de busca e consulta as viagens disponíveis nas viações parceiras (ex.: Cometa, 1001, Catarinense).
  4. O sistema exibe a lista de viagens encontradas com horários de partida/chegada, duração estimada, categoria do ônibus, empresa de viação e preço.
  5. O Passageiro compara as opções aplicando filtros ou ordenação (menor preço, horário de saída, empresa de viação).
  6. *(Ponto de extensão — `<<extend>>` UC02)* O Passageiro seleciona uma viagem desejada para avançar à escolha de assentos.
- **Fluxos Alternativos:**
  - **FA01 (Refinar busca):** No passo 5, o Passageiro altera data, origem ou destino e executa nova pesquisa a partir do passo 3.
- **Fluxos de Exceção:**
  - **FE01 (Nenhuma viagem encontrada):** No passo 3, caso não existam viagens para os critérios informados, o sistema exibe mensagem informativa sugerindo datas próximas ou rotas alternativas.
  - **FE02 (Parâmetros inválidos):** No passo 3, caso origem e destino sejam iguais ou a data seja anterior à data atual, o sistema solicita correção dos campos.

---

### UC02 — Selecionar e Reservar Assentos
- **Rastreabilidade:** HU03, HU04
- **Ator Primário:** Passageiro
- **Atores Secundários:** —
- **Relacionamentos:** Estende `UC01 - Pesquisar e Comparar Viagens` (`<<extend>>`).
- **Pré-condições:** O Passageiro selecionou uma viagem disponível em `UC01`; a viagem possui ônibus vinculado com mapa de poltronas configurado.
- **Pós-condições:** Os assentos selecionados ficam reservados temporariamente (com prazo de expiração) para o Passageiro enquanto os dados dos viajantes são preenchidos.
- **Fluxo Principal:**
  1. O sistema carrega e exibe o mapa interativo de poltronas do ônibus vinculado à viagem escolhida, indicando assentos livres, ocupados e reservados.
  2. O Passageiro seleciona um ou mais assentos disponíveis de sua preferência.
  3. O sistema cria uma reserva temporária bloqueando os assentos selecionados para outros compradores por tempo determinado (TTL).
  4. O sistema solicita os dados de identificação dos viajantes (nome completo e documento) para cada assento reservado.
  5. O Passageiro preenche os dados dos viajantes e confirma a reserva temporária para seguir ao pagamento (`UC03`).
- **Fluxos Alternativos:**
  - **FA01 (Alterar assentos antes de confirmar):** No passo 2 ou 4, o Passageiro desmarca um assento e escolhe outro livre; o sistema atualiza a reserva temporária.
- **Fluxos de Exceção:**
  - **FE01 (Assento ocupado concorrentemente):** No passo 3, se outro comprador reservar o mesmo assento milissegundos antes, o sistema notifica a indisponibilidade e atualiza o mapa de poltronas.
  - **FE02 (Expiração da reserva temporária):** Caso o tempo limite da reserva expire antes da confirmação dos dados/pagamento, o sistema libera os assentos automaticamente e informa o Passageiro.

---

### UC03 — Efetuar Pagamento Online
- **Rastreabilidade:** HU05
- **Ator Primário:** Passageiro
- **Ator Secundário:** Plataforma de Pagamento (`<<Sistema Externo>>`)
- **Relacionamentos:** Inclui `UC04 - Receber Bilhete e Notificações` (`<<include>>`).
- **Pré-condições:** O Passageiro possui uma reserva temporária ativa (proveniente de `UC02`) com os dados dos viajantes preenchidos.
- **Pós-condições:** Pagamento aprovado e registrado; reserva convertida em compra/bilhete confirmado; envio do bilhete acionado via `UC04`.
- **Fluxo Principal:**
  1. O sistema apresenta o resumo da compra (viagem, assentos, viajantes e valor total) e as formas de pagamento disponíveis.
  2. O Passageiro escolhe a forma de pagamento (ex.: cartão de crédito, Pix) e informa os dados necessários.
  3. O sistema envia a solicitação de transação à `Plataforma de Pagamento`.
  4. A `Plataforma de Pagamento` processa a transação e retorna a confirmação de aprovação.
  5. O sistema registra o pagamento aprovado, confirma definitivamente os assentos e gera os bilhetes da viagem.
  6. O sistema executa `<<include>> UC04 - Receber Bilhete e Notificações` para entregar os bilhetes confirmados ao Passageiro.
- **Fluxos Alternativos:**
  - **FA01 (Trocar forma de pagamento):** Antes do envio no passo 3, o Passageiro seleciona outro meio de pagamento disponível.
- **Fluxos de Exceção:**
  - **FE01 (Pagamento recusado):** No passo 4, caso a `Plataforma de Pagamento` recuse a transação, o sistema exibe o motivo informado e permite nova tentativa enquanto a reserva temporária estiver válida.
  - **FE02 (Falha ou timeout de comunicação):** Caso a `Plataforma de Pagamento` não responda dentro do tempo limite, o sistema registra a pendência/falha, mantém a integridade da reserva e orienta o Passageiro.

---

### UC04 — Receber Bilhete e Notificações
- **Rastreabilidade:** HU06
- **Ator Primário:** Passageiro
- **Ator Secundário:** Serviço de Notificações (`<<Sistema Externo>>`)
- **Relacionamentos:** Incluído por `UC03 - Efetuar Pagamento Online` (`<<include>>`) e por `UC09 - Gerenciar Cancelamentos, Reembolsos e Alterações` (`<<include>>`).
- **Pré-condições:** Existe um bilhete emitido/confirmado ou um evento de atualização de viagem (cancelamento, alteração ou reembolso) associado ao Passageiro.
- **Pós-condições:** O Passageiro recebe o bilhete eletrônico e/ou notificação de atualização por e-mail ou WhatsApp; o status de entrega é registrado.
- **Fluxo Principal:**
  1. O sistema compõe a mensagem com o bilhete eletrônico (código localizador, QR Code, dados da viagem e assento) ou atualização operacional.
  2. O sistema seleciona os canais preferenciais do Passageiro (e-mail e/ou WhatsApp).
  3. O sistema envia a requisição de disparo ao `Serviço de Notificações`.
  4. O `Serviço de Notificações` entrega a mensagem ao Passageiro e retorna o status de envio ao sistema.
  5. O Passageiro acessa o comprovante e orientações de embarque no canal escolhido (ou visualiza na plataforma).
- **Fluxos Alternativos:**
  - **FA01 (Reenvio sob demanda):** O Passageiro solicita o reenvio do bilhete pela área do usuário, reiniciando a partir do passo 1.
- **Fluxos de Exceção:**
  - **FE01 (Falha no envio externo):** No passo 4, se o `Serviço de Notificações` retornar erro ou indisponibilidade, o sistema registra o log de falha para retentativa automática e mantém o bilhete acessível na plataforma.

---

### UC05 — Solicitar Cancelamento, Alteração ou Reembolso
- **Rastreabilidade:** HU07
- **Ator Primário:** Passageiro
- **Atores Secundários:** —
- **Relacionamentos:** — (as solicitações registradas são posteriormente tratadas em `UC09`).
- **Pré-condições:** O Passageiro está autenticado e possui ao menos uma passagem/bilhete confirmado em seu histórico.
- **Pós-condições:** A solicitação de cancelamento, alteração ou reembolso é registrada com status pendente/em análise conforme as regras aplicáveis.
- **Fluxo Principal:**
  1. O Passageiro acessa suas compras/bilhetes na plataforma.
  2. O Passageiro seleciona o bilhete desejado e escolhe a ação (cancelamento, alteração de viagem/assento ou reembolso).
  3. O sistema apresenta as regras e eventuais taxas/prazos aplicáveis à solicitação.
  4. O Passageiro confirma os termos, informa o motivo (quando aplicável) e envia a solicitação.
  5. O sistema registra a solicitação vinculada ao bilhete e informa o protocolo de acompanhamento ao Passageiro.
- **Fluxos Alternativos:**
  - **FA01 (Desistência antes do envio):** No passo 3 ou 4, o Passageiro desiste da solicitação e o bilhete permanece inalterado.
- **Fluxos de Exceção:**
  - **FE01 (Prazo expirado ou bilhete não elegível):** No passo 2, caso o bilhete esteja fora do prazo regulamentar ou já utilizado/cancelado, o sistema bloqueia a solicitação e exibe a justificativa.

---

### UC06 — Cadastrar e Atualizar Rotas e Horários
- **Rastreabilidade:** HU08
- **Ator Primário:** Empresa de Viação
- **Atores Secundários:** —
- **Relacionamentos:** —
- **Pré-condições:** A Empresa de Viação está autenticada e devidamente habilitada na plataforma.
- **Pós-condições:** A rota e/ou grade de horários é criada ou atualizada no catálogo da plataforma.
- **Fluxo Principal:**
  1. A Empresa de Viação acessa o painel de gestão de rotas e horários.
  2. A Empresa de Viação opta por cadastrar nova rota/horário ou selecionar uma existente para edição.
  3. A Empresa de Viação informa ou atualiza origem, destino, paradas intermediárias, horários de partida/chegada e frequência de operação.
  4. O sistema valida a consistência dos dados (cidades válidas, duração coerente, ausência de duplicidade conflitante).
  5. O sistema persiste a rota e os horários, tornando-os aptos para precificação e alocação de ônibus (`UC07`).
- **Fluxos Alternativos:**
  - **FA01 (Inativar rota ou horário):** No passo 2, a Empresa de Viação opta por desativar uma linha sem vendas futuras ativas.
- **Fluxos de Exceção:**
  - **FE01 (Dados inválidos ou conflitantes):** No passo 4, caso haja inconsistência nos horários ou campos obrigatórios ausentes, o sistema impede a gravação e exibe os erros.
  - **FE02 (Horário com passagens já vendidas):** Ao tentar alterar/inativar horário com bilhetes emitidos, o sistema alerta sobre os passageiros impactados e restringe alterações incompatíveis.

---

### UC07 — Definir Preços e Vincular Ônibus
- **Rastreabilidade:** HU09
- **Ator Primário:** Empresa de Viação
- **Atores Secundários:** —
- **Relacionamentos:** —
- **Pré-condições:** A Empresa de Viação está autenticada e possui rotas/horários cadastrados (`UC06`) e frota de ônibus configurada (com mapa de assentos).
- **Pós-condições:** As viagens ofertadas possuem tarifa definida e ônibus (com configuração de poltronas) vinculado, ficando disponíveis para pesquisa e venda (`UC01`/`UC02`).
- **Fluxo Principal:**
  1. A Empresa de Viação seleciona uma rota/horário cadastrado no painel operacional.
  2. A Empresa de Viação define o valor da passagem (e eventuais classes/tarifas) para a viagem.
  3. A Empresa de Viação seleciona o ônibus da frota (com tipo de serviço e mapa de assentos) a ser vinculado à viagem.
  4. O sistema valida que o preço é válido e que o ônibus não está alocado em horário conflitante.
  5. O sistema salva a configuração e disponibiliza a viagem com seus assentos para comercialização na plataforma.
- **Fluxos Alternativos:**
  - **FA01 (Reajustar tarifa ou substituir ônibus):** A Empresa de Viação atualiza o preço ou troca o ônibus por outro de configuração compatível antes do embarque.
- **Fluxos de Exceção:**
  - **FE01 (Conflito de alocação de ônibus):** No passo 4, se o ônibus selecionado já estiver vinculado a outra viagem no mesmo intervalo, o sistema recusa o vínculo e solicita outro veículo.
  - **FE02 (Preço inválido):** Se o valor informado for menor ou igual a zero, o sistema solicita correção.

---

### UC08 — Acompanhar Vendas de Viagens
- **Rastreabilidade:** HU10
- **Ator Primário:** Empresa de Viação
- **Atores Secundários:** —
- **Relacionamentos:** —
- **Pré-condições:** A Empresa de Viação está autenticada e possui viagens ofertadas na plataforma.
- **Pós-condições:** A Empresa de Viação visualiza os indicadores atualizados de vendas, ocupação e receita de suas viagens.
- **Fluxo Principal:**
  1. A Empresa de Viação acessa o painel de acompanhamento de vendas.
  2. A Empresa de Viação aplica filtros por período, rota, horário ou status da viagem.
  3. O sistema consolida os bilhetes vendidos, assentos ocupados/disponíveis, reservas temporárias e receita bruta correspondente.
  4. O sistema exibe os dados em tabela e indicadores resumidos por viagem/rota.
- **Fluxos Alternativos:**
  - **FA01 (Detalhar viagem específica):** No passo 4, a Empresa de Viação seleciona uma viagem para visualizar o mapa atual de ocupação dos assentos e o histórico de vendas.
- **Fluxos de Exceção:**
  - **FE01 (Sem vendas no período):** Caso não existam vendas para os filtros aplicados, o sistema exibe mensagem informativa com contadores zerados.

---

### UC09 — Gerenciar Cancelamentos, Reembolsos e Alterações
- **Rastreabilidade:** HU11
- **Ator Primário:** Empresa de Viação
- **Ator Secundário:** Plataforma de Pagamento (`<<Sistema Externo>>`)
- **Relacionamentos:** Inclui `UC04 - Receber Bilhete e Notificações` (`<<include>>`).
- **Pré-condições:** A Empresa de Viação está autenticada e existem solicitações registradas por passageiros (`UC05`) pendentes de análise ou processamento.
- **Pós-condições:** A solicitação é aprovada ou recusada; em caso de aprovação, o assento é liberado/alterado, eventual estorno é processado na `Plataforma de Pagamento` e o Passageiro é notificado via `UC04`.
- **Fluxo Principal:**
  1. A Empresa de Viação acessa a fila de solicitações de cancelamento, reembolso e alteração referentes às suas viagens.
  2. A Empresa de Viação seleciona uma solicitação pendente e analisa os detalhes do bilhete e as políticas operacionais aplicáveis.
  3. A Empresa de Viação aprova a solicitação (confirmando cancelamento, nova viagem/assento ou valor de reembolso).
  4. Caso haja reembolso financeiro, o sistema envia a solicitação de estorno à `Plataforma de Pagamento`, que processa e confirma a operação.
  5. O sistema atualiza o status do bilhete, libera o assento original (ou vincula o novo assento na alteração) e registra a conclusão do atendimento.
  6. O sistema executa `<<include>> UC04 - Receber Bilhete e Notificações` para informar o Passageiro sobre a decisão/novo bilhete.
- **Fluxos Alternativos:**
  - **FA01 (Recusar solicitação):** No passo 3, caso a solicitação viole as políticas operacionais, a Empresa de Viação registra a recusa com justificativa e o sistema executa `<<include>> UC04` para notificar o Passageiro.
- **Fluxos de Exceção:**
  - **FE01 (Falha no estorno externo):** No passo 4, caso a `Plataforma de Pagamento` recuse ou apresente erro no estorno, o sistema mantém a solicitação em estado de erro/pendente de reprocessamento e alerta a Empresa de Viação.

---

### UC10 — Consultar Viagens Alocadas
- **Rastreabilidade:** HU12
- **Ator Primário:** Motorista
- **Atores Secundários:** —
- **Relacionamentos:** —
- **Pré-condições:** O Motorista está autenticado e possui viagens atribuídas à sua escala operacional.
- **Pós-condições:** O Motorista visualiza os detalhes das viagens alocadas (rotas, horários, paradas e veículo designado).
- **Fluxo Principal:**
  1. O Motorista acessa a área de escala operacional na plataforma.
  2. O sistema consulta as viagens em que o Motorista está alocado (filtrando por data atual ou próximas viagens).
  3. O sistema exibe a lista de viagens com rota (origem, destino e paradas), horários previstos de partida/chegada e identificação do ônibus vinculado (placa/prefixo/categoria).
  4. O Motorista seleciona uma viagem para conferir detalhes completos do trajeto ou avançar para a lista de passageiros (`UC11`).
- **Fluxos Alternativos:**
  - **FA01 (Filtrar por período):** No passo 2, o Motorista seleciona outro intervalo de datas para consultar escalas futuras ou recentes.
- **Fluxos de Exceção:**
  - **FE01 (Nenhuma viagem alocada):** Caso não haja viagens atribuídas ao Motorista no período consultado, o sistema informa que a escala está vazia.

---

### UC11 — Consultar Lista de Passageiros
- **Rastreabilidade:** HU13
- **Ator Primário:** Motorista
- **Atores Secundários:** —
- **Relacionamentos:** —
- **Pré-condições:** O Motorista está autenticado e possui ao menos uma viagem alocada (`UC10`).
- **Pós-condições:** O Motorista visualiza a lista atualizada de passageiros confirmados e seus respectivos assentos para conferência no embarque.
- **Fluxo Principal:**
  1. O Motorista seleciona uma de suas viagens alocadas.
  2. O sistema consulta todos os bilhetes confirmados vinculados à viagem selecionada.
  3. O sistema exibe a lista de passageiros ordenada por número do assento ou nome, contendo nome completo, documento de identificação, número da poltrona e código do bilhete.
  4. O Motorista utiliza a lista para conferir os viajantes no momento do embarque.
- **Fluxos Alternativos:**
  - **FA01 (Buscar passageiro na lista):** No passo 3, o Motorista filtra por nome, documento ou poltrona para agilizar a conferência.
- **Fluxos de Exceção:**
  - **FE01 (Viagem sem passageiros confirmados):** Caso não existam bilhetes confirmados para a viagem, o sistema exibe mensagem informando que não há passageiros registrados.

---

### UC12 — Gerenciar Cadastros e Configurações Globais
- **Rastreabilidade:** HU14
- **Ator Primário:** Administrador da Plataforma
- **Atores Secundários:** —
- **Relacionamentos:** —
- **Pré-condições:** O Administrador da Plataforma está autenticado com privilégios administrativos.
- **Pós-condições:** Cadastros globais (usuários, viações parceiras, perfis de acesso) ou parâmetros de integrações externas são criados, atualizados ou inativados com sucesso.
- **Fluxo Principal:**
  1. O Administrador acessa o módulo de administração geral da plataforma.
  2. O Administrador escolhe a entidade ou configuração a gerenciar: Usuários (passageiros, motoristas, operadores), Empresas de Viação Parceiras ou Configurações de Integrações Externas (pagamento e notificações).
  3. O Administrador realiza a operação desejada (cadastrar, editar, habilitar/desabilitar ou atualizar parâmetros/credenciais).
  4. O sistema valida os dados e permissões informados.
  5. O sistema persiste as alterações e registra log de auditoria administrativa.
- **Fluxos Alternativos:**
  - **FA01 (Consultar/filtrar cadastros):** No passo 2, o Administrador pesquisa cadastros existentes antes de efetuar alterações.
- **Fluxos de Exceção:**
  - **FE01 (Dados inválidos ou duplicados):** No passo 4, caso haja e-mail/CNPJ duplicado ou parâmetros de integração inválidos, o sistema rejeita a operação e exibe o erro.

---

### UC13 — Monitorar Operações em Andamento
- **Rastreabilidade:** HU15
- **Ator Primário:** Administrador da Plataforma
- **Atores Secundários:** —
- **Relacionamentos:** —
- **Pré-condições:** O Administrador da Plataforma está autenticado com privilégios de monitoramento.
- **Pós-condições:** O Administrador visualiza o estado em tempo real das operações críticas e identifica eventuais falhas ou gargalos.
- **Fluxo Principal:**
  1. O Administrador acessa o painel de monitoramento operacional.
  2. O sistema coleta e exibe indicadores em tempo real sobre reservas temporárias ativas/expiradas, transações de pagamento (aprovadas, pendentes, recusadas) e status da fila de notificações (e-mail/WhatsApp).
  3. O sistema destaca alertas de falhas, timeouts de integração externa ou gargalos operacionais.
  4. O Administrador inspeciona os logs detalhados de uma ocorrência para diagnosticar a causa.
- **Fluxos Alternativos:**
  - **FA01 (Filtrar por tipo de evento ou severidade):** No passo 2, o Administrador filtra apenas por falhas de pagamento ou erros de notificação.
- **Fluxos de Exceção:**
  - **FE01 (Indisponibilidade parcial de telemetria):** Caso algum serviço de log esteja temporariamente indisponível, o sistema exibe os dados disponíveis e sinaliza o componente sem telemetria.

---

### UC14 — Gerar Relatórios Financeiros e Operacionais
- **Rastreabilidade:** HU16
- **Ator Primário:** Administrador da Plataforma
- **Atores Secundários:** —
- **Relacionamentos:** —
- **Pré-condições:** O Administrador da Plataforma está autenticado e existem dados históricos de vendas, pagamentos, cancelamentos e viagens na base.
- **Pós-condições:** O relatório financeiro ou operacional consolidado é gerado e exibido/exportado conforme os critérios escolhidos.
- **Fluxo Principal:**
  1. O Administrador acessa o módulo de relatórios gerenciais.
  2. O Administrador seleciona o tipo de relatório (financeiro — faturamento, estornos, comissões; ou operacional — volume de passagens, taxa de ocupação, desempenho por viação/rota) e define o período e filtros.
  3. O sistema consulta e agrega os dados históricos correspondentes.
  4. O sistema apresenta o relatório consolidado em tela com totalizadores e permite exportação (ex.: CSV/PDF).
- **Fluxos Alternativos:**
  - **FA01 (Comparar períodos ou viações):** No passo 2, o Administrador seleciona múltiplas viações parceiras para análise comparativa.
- **Fluxos de Exceção:**
  - **FE01 (Nenhum dado no período):** No passo 3, caso não haja movimentação no intervalo informado, o sistema informa que não há registros para gerar o relatório.
