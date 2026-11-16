# Atividade – Diagrama de Sequências

**Disciplina:** SSC0124 — Análise e Projeto Orientados a Objetos (APOO)
**Docente:** Profa. Dra. Lina Garcés
**Aluno:** Rafael Feltrim — **N° USP:** 15942812
**Contexto:** Plataforma de Venda de Passagens Rodoviárias Integrada (estilo ClickBus)
**Entrega:** individual · e-Disciplinas · prazo **16/11/2026, 12:00**

> Enunciado original: [Atividade – Elaboração de diagrama de sequências.docx.pdf](<./Atividade – Elaboração de diagrama de sequências.docx.pdf>)
> Todos os diagramas devem ser montados no [diagrams.net](https://app.diagrams.net/): **Organizar → Inserir → Avançado → PlantUML**, colando o conteúdo dos arquivos `.puml` desta pasta.

---

## 1. Caso de Uso Selecionado: **Comprar Passagem**

Reaproveitado das atividades anteriores (Tópico 4), onde já foram entregues o diagrama de casos de uso, a descrição textual estendida e o diagrama de atividades:
- [RESPOSTAS_ATIVIDADE_2.md](<../../../Tópico 4 - Especificacao de Requisitos e Casos de Uso/Entregas/Atividade - Descricao Textual e Diagrama de Atividades/RESPOSTAS_ATIVIDADE_2.md>) — descrição textual, diagrama de casos de uso (zoom) e diagrama de atividades em PlantUML.
- [Comprar Passagem.pdf](<../../../Tópico 4 - Especificacao de Requisitos e Casos de Uso/Entregas/Atividade - Descricao Textual e Diagrama de Atividades/Comprar Passagem.pdf>) e [Diagrama de Atividades.pdf](<../../../Tópico 4 - Especificacao de Requisitos e Casos de Uso/Entregas/Atividade - Descricao Textual e Diagrama de Atividades/Diagrama de Atividades.pdf>) — versões já exportadas do diagrams.net.

### 1.1 Descrição textual estendida (resumo dos fluxos usados no diagrama)

- **Ator principal:** Passageiro · **Atores secundários:** Sistema de Pagamento, Sistema de Notificações
- **Pré-condição:** o Passageiro pesquisou e selecionou uma viagem.
- **Pós-condição:** pagamento aprovado, passagens emitidas, assentos bloqueados definitivamente e notificação enviada.

| Fluxo | Passos | Onde aparece no diagrama de sequência |
|---|---|---|
| **Básico** | 1. Iniciar compra → 2. Exibir layout do ônibus → 3. Selecionar assentos → 4. Verificar disponibilidade e reservar temporariamente → 5. Informar dados dos passageiros → 6. Exibir resumo financeiro → 7. Informar pagamento → 8–9. Cobrança autorizada pelo Sistema de Pagamento → 10. Efetivar compra, emitir passagens e notificar → 11. Exibir confirmação | Sequência principal, `loop` de reserva, `alt [aprovado = true]` |
| **FA01** Aplicar Cupom (`<<extend>>`) | No passo 6, validar cupom e recalcular valor | `opt [Passageiro informou cupom]` |
| **FA02** Voltar para alterar assentos | No passo 6, descartar reservas e voltar ao passo 2 | `opt [Passageiro decide alterar assentos]` |
| **FE01** Assento indisponível | No passo 4, avisar e voltar ao passo 2 | `alt [disponivel = false]` dentro do `loop` |
| **FE02** Pagamento recusado | No passo 9, alertar e voltar ao passo 6 | `alt [aprovado = false]` |
| **FE03** Tempo de reserva esgotado | Entre os passos 4 e 9, expirar reserva e cancelar | `alt [reservasValidas = false]` |
| `<<include>>` Notificar Usuário | Passo 10 | `ref` → `sd Notificar Usuario` |

---

## 2. Elementos que Interagem (2a) e Classes no Padrão MVC (2b)

Coerente com o diagrama de componentes MVC da atividade anterior (`ViewPassageiro` → `ControllerVendas` → `ComponenteVendas` → `ComponenteAcessoDados_Vendas`), e seguindo o exemplo da Aula 10, em que a classe de persistência (`UsuárioDatabase`) é parte do **Modelo**:

| Camada MVC | Elemento | Papel no caso de uso |
|---|---|---|
| Ator | `Passageiro` | Inicia o caso de uso e interage com a tela |
| **View** | `CompraPassagemView` *(componente ViewPassageiro)* | Recebe as ações do usuário e exibe layout, resumo, alertas e confirmação |
| **Controller** | `CompraPassagemController` *(componente ControllerVendas)* | Orquestra o fluxo, aplica as decisões (`alt`/`opt`/`loop`) e aciona o modelo |
| **Model** | `VendasDatabase` | Recupera e persiste viagens, passageiros, reservas e compras |
| **Model** | `Viagem` | Informa poltronas disponíveis, disponibilidade de uma poltrona e tarifa |
| **Model** | `ReservaPoltrona` | Bloqueio temporário com timeout, ocupante, confirmação e cancelamento |
| **Model** | `CompraPassagem` | Agrupa as reservas, calcula valor, aplica cupom, confirma e emite bilhetes |
| **Model** | `Pagamento` | Processa a cobrança no gateway externo |
| **Model** | `BilhetePassagem` | Bilhete nominal com QR Code de embarque |
| **Model** | `Passageiro`, `NotificacaoEmbarque` | Canais de contato e envio de notificações (`sd Notificar Usuario`) |
| Externo | `GatewayPagamento` | Ator secundário **Sistema de Pagamento** |
| Externo | `ServicoNotificacao` | Ator secundário **Sistema de Notificações** (e-mail/WhatsApp) |

---

## 3. Diagramas de Sequência

| Arquivo | Conteúdo | Notação UML exigida coberta |
|---|---|---|
| [diagrama-sequencia-comprar-passagem.puml](./diagrama-sequencia-comprar-passagem.puml) | `sd Comprar Passagem`: fluxo básico + FA01, FA02, FE01, FE02, FE03 | lifelines, ativação, setas síncronas e de retorno, `<<create>>`, **`loop`**, **`alt`**, **`opt`**, **`ref`**, restrições `[ ]` |
| [diagrama-sequencia-notificar-usuario.puml](./diagrama-sequencia-notificar-usuario.puml) | `sd Notificar Usuario`, a interação referenciada pelo `ref` | **gate** (mensagem de entrada e retorno pela borda do quadro), `loop`, `opt`, mensagem **assíncrona** |

> [!NOTE]
> O **gate** fica no diagrama referenciado porque é lá que uma mensagem chega de fora do quadro (do controlador do `sd Comprar Passagem`), exatamente a semântica da Aula 10 ("mensagem recebida pelo objeto e que precisa ser processada").

---

## 4. Métodos Requeridos nas Classes de Modelo

Derivados das mensagens recebidas pelas lifelines de modelo:

| Classe | Métodos |
|---|---|
| `VendasDatabase` | `buscarViagem(idViagem: Integer): Viagem` · `buscarPassageiro(idPassageiro: Integer): Passageiro` · `salvarReserva(reserva: ReservaPoltrona): void` · `salvarCompra(compra: CompraPassagem): void` |
| `Viagem` | `listarPoltronasDisponiveis(): List<Poltrona>` · `verificarDisponibilidade(idPoltrona: Integer): Boolean` · `obterTarifa(): Decimal` |
| `ReservaPoltrona` | `ReservaPoltrona(passageiro, viagem, idPoltrona, minutosTimeout)` *(construtor)* · `definirOcupante(nome: String, documento: String): void` · `estaExpirada(): Boolean` · `confirmar(): void` · `cancelar(): void` |
| `CompraPassagem` | `CompraPassagem(passageiro, reservas)` *(construtor)* · `calcularValorTotal(): Decimal` · `aplicarCupom(codigoCupom: String): Boolean` · `verificarReservasValidas(): Boolean` · `confirmar(pagamento: Pagamento): List<BilhetePassagem>` · `cancelar(): void` · `obterPassageiro(): Passageiro` |
| `Pagamento` | `Pagamento(metodo, valor)` *(construtor)* · `processar(dadosPagamento: DadosPagamento): Boolean` |
| `BilhetePassagem` | `BilhetePassagem(reserva)` *(construtor)* · `gerarQrCode(): String` |
| `Passageiro` | `obterCanaisContato(): List<String>` |
| `NotificacaoEmbarque` | `NotificacaoEmbarque(canal, destinatario)` *(construtor)* · `enviar(bilhetes: List<BilhetePassagem>): Boolean` · `registrarFalha(): void` |

---

## 5. Diagrama de Classes Atualizado

Arquivo: [diagrama-classes-com-metodos.puml](./diagrama-classes-com-metodos.puml)

Mudanças em relação ao modelo conceitual entregue no Tópico 5:
1. **Operações** adicionadas às classes de modelo (tabela da seção 4).
2. Classes **View** (`CompraPassagemView`) e **Controller** (`CompraPassagemController`) com seus métodos, além de dependências `<<use>>`/`<<create>>`.
3. `VendasDatabase` (persistência do modelo) e interfaces externas `GatewayPagamento` e `ServicoNotificacao`.
4. Tipos de dados `DadosPagamento` e `DadosOcupante` (parâmetros das operações).
5. Atributos `nomeOcupante` e `documentoOcupante` em `ReservaPoltrona` (o passo 5 coleta os dados de cada passageiro da reserva antes da emissão).
6. Nova associação `CompraPassagem "0..1" — "1..*" ReservaPoltrona : agrupa`, necessária porque a compra confirma e cancela as suas reservas.

---

## 6. Verificação de Coerência entre os Diagramas

Conforme a observação do enunciado, cada mensagem que chama uma operação de um objeto precisa existir na classe receptora com nome, parâmetros e retorno compatíveis. A checagem foi automatizada com um script que lê os `.puml`:

- **44 mensagens** verificadas nos dois diagramas de sequência (View, Controller, Model e externos).
- **0 divergências** de nome ou número de parâmetros em relação ao diagrama de classes.

> [!WARNING]
> **Divergência corrigida em relação ao Tópico 4:** o **diagrama de atividades** entregue no Tópico 4 encerrava o fluxo quando o pagamento era recusado ("Exibir Erro de Pagamento e Cancelar Reserva" → fim), enquanto a **descrição textual** (FE02) retorna ao passo 6 para outra forma de pagamento. O diagrama de sequência segue a descrição textual, e uma versão ajustada do diagrama de atividades foi adicionada em [diagrama-atividades-comprar-passagem.puml](./diagrama-atividades-comprar-passagem.puml) para manter 100% de coerência no documento final.

---

## 7. Documento Final e Checklist de Envio (item 6 do enunciado)

Documento consolidado pronto para envio (8 páginas, em vetor): [Atividade - Diagrama de Sequencias - Rafael Feltrim.pdf](<./Atividade - Diagrama de Sequencias - Rafael Feltrim.pdf>)

- [x] Diagrama de casos de uso geral (PDF do `diagrams.net` do Tópico 4) e recorte/zoom de `Comprar Passagem`
- [x] Diagrama de atividades ajustado do caso **Comprar Passagem** ([diagrama-atividades-comprar-passagem.puml](./diagrama-atividades-comprar-passagem.puml))
- [x] Descrição textual estendida completa de **Comprar Passagem** (cenário principal + FA01–FA02 + FE01–FE03)
- [x] Entidades MVC, lista de métodos de modelo e diagrama de classes atualizado ([diagrama-classes-com-metodos.puml](./diagrama-classes-com-metodos.puml))
- [x] Diagramas de sequência `sd Comprar Passagem` e `sd Notificar Usuario` (com **gate**)
- [ ] Enviar [Atividade - Diagrama de Sequencias - Rafael Feltrim.pdf](<./Atividade - Diagrama de Sequencias - Rafael Feltrim.pdf>) no e-Disciplinas até **16/11, 12:00** *(nota: os diagramas em `.puml` foram renderizados via PlantUML em SVG vetorial; caso deseje editar ou reexportar pelo `app.diagrams.net`, use **Organizar → Inserir → Avançado → PlantUML** com os arquivos desta pasta)*

