# Tópico 6 — Diagrama de Sequências (Interação)

Módulo correspondente à **Aula 12 (26/10/2026)** do cronograma oficial, dedicado à modelagem comportamental de interações temporais entre objetos via **Diagrama de Sequência (UML)**, derivação de **métodos das classes** e tradução direta do **diagrama de sequência para o código**.

---

## 🔗 Links e Recursos do e-Disciplinas

- **Seção Moodle:** [Diagrama de Sequências](https://edisciplinas.usp.br/course/section.php?id=6991983)
- **Arquivo da Aula:** [`Aula 10 - Diagramas de interação - sequência.pdf`](<./Material%20de%20Apoio/Aula%2010%20-%20Diagramas%20de%20intera%C3%A7%C3%A3o%20-%20sequ%C3%AAncia.pdf>) *(Disponível localmente; [link Moodle](https://edisciplinas.usp.br/mod/resource/view.php?id=6620361))*
- **Atividade Prática (Prazo: 16/11/2026, 12:00 — Individual):**
  - Enunciado: [`Atividade – Elaboração de diagrama de sequências.docx.pdf`](<./Entregas/Atividade%20-%20Diagrama%20de%20Sequencias/Atividade%20%E2%80%93%20Elabora%C3%A7%C3%A3o%20de%20diagrama%20de%20sequ%C3%AAncias.docx.pdf>)
  - Documento Consolidado (PDF pronto para envio): [`Atividade - Diagrama de Sequencias - Rafael Feltrim.pdf`](<./Entregas/Atividade%20-%20Diagrama%20de%20Sequencias/Atividade%20-%20Diagrama%20de%20Sequencias%20-%20Rafael%20Feltrim.pdf>)
  - Resolução e Rastreabilidade: [`RESPOSTAS_ATIVIDADE_SEQUENCIA.md`](<./Entregas/Atividade%20-%20Diagrama%20de%20Sequencias/RESPOSTAS_ATIVIDADE_SEQUENCIA.md>)
  - Diagramas PlantUML (para importar no [diagrams.net](https://app.diagrams.net/)):
    - [`diagrama-sequencia-comprar-passagem.puml`](<./Entregas/Atividade%20-%20Diagrama%20de%20Sequencias/diagrama-sequencia-comprar-passagem.puml>)
    - [`diagrama-sequencia-notificar-usuario.puml`](<./Entregas/Atividade%20-%20Diagrama%20de%20Sequencias/diagrama-sequencia-notificar-usuario.puml>)
    - [`diagrama-classes-com-metodos.puml`](<./Entregas/Atividade%20-%20Diagrama%20de%20Sequencias/diagrama-classes-com-metodos.puml>)
    - [`diagrama-atividades-comprar-passagem.puml`](<./Entregas/Atividade%20-%20Diagrama%20de%20Sequencias/diagrama-atividades-comprar-passagem.puml>) *(versão ajustada para coerência com FE02)*
- **Atividades Previstas no Cronograma (Aula 12):**
  - *Em dupla:* Diagrama de sequências e definição de métodos de classes.
  - *Extra-aula:* Diagrama de sequência ao código.

---

## 📖 Síntese Teórica para Estudo e Projeto

### 1. O Papel do Diagrama de Sequência no Processo de APOO
- Faz a ponte entre os **Casos de Uso** (comportamento funcional esperado) e o **Diagrama de Classes** (estrutura estática).
- Enquanto o modelo conceitual/classes inicial foca em **atributos e associações**, o Diagrama de Sequência revela **quais métodos cada classe precisa expor** para atender um fluxo de negócio.

### 2. Elementos Fundamentais da Notação UML
- **Participantes / Objetos:** Retângulos no topo no formato `nomeObjeto : NomeClasse` (ou `:NomeClasse` quando anônimo) e atores externos.
- **Linha de Vida (*Lifeline*):** Linha vertical tracejada que representa a existência do objeto ao longo do tempo (de cima para baixo).
- **Barra de Ativação (*Focus of Control*):** Retângulo vertical fino sobre a lifeline indicando o período em que o objeto está executando uma operação.
- **Portão (*Gate*):** Mensagem que entra ou sai pela borda do quadro do diagrama (`[->` / `[<--`), representando comunicação recebida de um chamador externo ao diagrama (ex.: na interação referenciada por `ref`).
- **Tipos de Mensagens:**
  - `->` **Síncrona (seta cheia contínua):** O chamador aguarda o processamento e o retorno antes de prosseguir.
  - `->>` **Assíncrona (seta aberta):** Dispara a ação sem bloquear o chamador (comum para filas/notificações).
  - `-->` **Retorno (seta tracejada):** Devolução do resultado da chamada ao objeto invocador.
  - **Auto-chamada (*Self-message*):** Objeto invocando um método privado/auxiliar nele mesmo.
  - `<<create>>` / `<<destroy>>`: Instanciação dinâmica de objetos durante o fluxo e encerramento (`X` na lifeline).

### 3. Fragmentos Combinados (Estruturas de Controle)
- **`alt` (Alternativa):** Equivale a `if / else` (múltiplos operandos com condições de guarda `[condição]`).
- **`opt` (Opcional):** Equivale a `if` simples (executa apenas se a condição `[guarda]` for verdadeira).
- **`loop` (Repetição):** Equivale a `for / while` (ex.: `loop [para cada poltrona selecionada]`).
- **`ref` (Uso de Interação):** Referencia outro diagrama de sequência (sub-rotina ou caso de uso incluído via `<<include>>`).
- **`par` (Paralelo):** Execução concorrente de blocos (ex.: exibir tela de confirmação enquanto envia notificação).
- **Restrições de Interação (`[condição]`):** Guardas entre colchetes que delimitam quando cada ramo executa.

### 4. Do Diagrama de Sequência aos Métodos e ao Código
1. Toda seta de mensagem que chega na *lifeline* de um objeto `:ClasseB` torna-se um **método público** em `ClasseB` (com nome, parâmetros e retorno compatíveis).
2. A camada **Model** inclui, além das classes de domínio, a classe de persistência/banco de dados (ex.: `VendasDatabase`, análogo a `UsuárioDatabase` na Aula 10).
3. Fragmentos `alt`/`opt`/`loop` traduzem-se diretamente em desvios condicionais e laços na camada `Controller` / `Model`.

---

## 💻 Entrega Aplicada (Plataforma Rodoviária — Caso de Uso `Comprar Passagem`)

A modelagem completa em **PlantUML** (alinhada às classes reais do modelo conceitual do **Tópico 5** e aos fluxos do **Tópico 4**) encontra-se em [`./Entregas/Atividade - Diagrama de Sequencias/`](./Entregas/Atividade%20-%20Diagrama%20de%20Sequencias/):

- **View:** `CompraPassagemView` *(componente `ViewPassageiro`)*
- **Controller:** `CompraPassagemController` *(componente `ControllerVendas`)*
- **Model:** `VendasDatabase`, `Viagem`, `ReservaPoltrona`, `CompraPassagem`, `Pagamento`, `BilhetePassagem`, `Passageiro`, `NotificacaoEmbarque`
- **Externos:** `GatewayPagamento`, `ServicoNotificacao`

Consulte [`RESPOSTAS_ATIVIDADE_SEQUENCIA.md`](<./Entregas/Atividade%20-%20Diagrama%20de%20Sequencias/RESPOSTAS_ATIVIDADE_SEQUENCIA.md>) para a tabela completa de rastreabilidade (*mensagem → classe → método*) e instruções de importação no [diagrams.net](https://app.diagrams.net/).
