# Configuração do Gem `APOO` no Gemini e Roteiro de Prompts

> **Referência oficial:** [`Diretrizes - APOO apoiado por LLM.docx.pdf`](<../../../../Material%20de%20Apoio/Diretrizes%20-%20APOO%20apoiado%20por%20LLM.docx.pdf>) (págs. 1–12)

## 1. Configuração do Assistente (Gemini → Gems)

- **Nome:** `APOO`
- **Descrição:** `Assistente para a execução do processo de APOO`
- **Instruções:**
  ```text
  Você é um engenheiro de software que precisa realizar atividades de APOO para a modelagem UML em plantuml de um sistema de software.
  ```
- **Ferramenta padrão:** `Nenhuma ferramenta padrão`
- **Base de Conhecimento:** subir o arquivo de Histórias de Usuário (`Desenvolvimento/Historias-de-Usuario.md` ou exportado em `.txt`/`.pdf`), clicar em **Salvar** e em **Iniciar Conversa**.

---

## 2. Prompts Oficiais por Etapa (para registrar as interações nesta pasta)

Salve nesta pasta os registros reais das conversas/prompts enviados ao Gemini em cada etapa (ex.: `01-prompts-casos-de-uso.md`, `02-prompts-descricao-textual.md`, etc.) para compor o pacote `.zip`.

### Etapa 1 — Diagrama de Casos de Uso (`PUML`)
1. **Atores e heranças iniciais:**
   > `"Gere um código PUML de casos de uso implementando apenas atores, com as relações de herança se houver, considerando as seguintes HUs: <lista de HUs>"`
2. **Corretivo de ator ausente:**
   > `"Implemente o ator W"`
3. **Corretivo de herança entre atores:**
   > `"Ator X herda do ator Y; Ator Z herda de ..."`
4. **Casos de uso por ator (um ator de cada vez):**
   > `"No código PUML anterior implemente apenas os casos de uso do ator X, baseado estritamente nas seguintes HUs: <lista de HUs do ator X>"`
5. **Relacionamentos `<<include>>` e `<<extend>>`:**
   > `"Caso de uso A ocorre apenas se B ocorrer; Caso de uso C pode ocorrer se ..."`

### Etapa 2 — Descrições Textuais Estendidas de Casos de Uso
*(Incluir no projeto do Gemini o arquivo `.puml` final dos casos de uso)*
1. **Geração inicial:**
   > `"Considere trechos do código PUML. A especificação textual de casos de uso deve contemplar estritamente todos os atores e relacionamentos."` + `<código PUML dos atores, casos de uso e relacionamentos>`
2. **Revisão / prompt corretivo único:**
   > `"Revise a especificação textual dos casos de uso, garantindo estritamente que todos os atores e funcionalidades presentes nos códigos PUML fornecido sejam contemplados. Considerar atores primários e secundários, pré-condições, pós-condições e fluxos alternativos."`

### Etapa 3 — Diagrama de Componentes (`PUML` — Fig. 4)
*(Usar o código PlantUML final do diagrama de casos de uso)*
1. **Listar possíveis componentes (apenas nomes):**
   > `"A partir do código PlantUML de casos de uso, liste os possíveis componentes (apenas nomes, sem código): <código final do caso de uso>"`
2. **Agrupar componentes semelhantes (se não estiverem coesos):**
   > `"Agrupe componentes semelhantes e retorne uma nova lista"`
3. **Gerar código PUML de componentes (sem relações):**
   > `"Baseado da lista de componentes anterior e no código de casos de uso, gere um diagrama de componentes em PUML contendo somente componentes (sem relações)"`
4. **Corretivo de componente (se semântica dos casos de uso não for mantida):**
   > `"Implemente o componente X, respeitando a semântica de casos de uso"`
5. **Implementar relações entre componentes:**
   > `"Implemente as relações entre componentes no código PUML de componentes. As relações devem seguir exatamente a mesma semântica dos casos de uso"`

### Etapa 4 — Diagrama de Classes (`PUML` — Fig. 5)
*(Passos 1–4 geram o Diagrama de Classes Preliminar; Passo 5 ocorre após os Diagramas de Sequência para gerar o Diagrama de Classes Completo)*
1. **Implementar apenas as classes:**
   > `"Implemente apenas classes no código PUML de diagrama de classes, sem multiplicidades, relações, atributos e métodos. Faça a implementação baseado no código de casos de uso. Código: <código do casos de uso>"`
   - **Corretivo de classe ausente:** `"Gere a classe X, mantendo a semântica do código de componentes: <código de componentes>"`
2. **Implementar apenas as heranças entre classes:**
   > `"No código anterior, implemente apenas as relações de heranças que ocorrem entre as classes, considerando a semântica de casos de uso e componentes"`
   - **Corretivo de herança:** `"Classe Y herda características da classe Z"`
3. **Implementar apenas os relacionamentos e multiplicidades:**
   > `"No código anterior, <classe G> <relacionamento entre classe G e classe H> <classe H>. <Classe I> se relaciona com <quantidade de instâncias da classe J>. etc."`
   - **Corretivo de relacionamento/multiplicidade:** `"<quantidade classe A> Classe A se relaciona com <quantidade classe B> classe B"`
4. **Implementar apenas os atributos de cada classe:**
   > `"Implemente no código anterior apenas os atributos de cada classe, considerando características reais da classe"`
   - **Corretivo de atributos:** `"Implemente os atributos P, Q e R na classe C"`
5. **Implementar os métodos de cada classe (após os Diagramas de Sequência):**
   > `"Implemente agora no código PUML anterior os métodos de cada classe, considerando características reais e semântica da classe."` *(fornecendo o código PUML preliminar + lista consolidada de métodos por classe extraída das mensagens dos diagramas de sequência)*
   - **Corretivo de métodos:** `"Implemente os métodos P, Q e R na classe C"`

### Etapa 5 — Diagramas de Sequência (`PUML` — Fig. 6)
*(1 diagrama de sequência por caso de uso, utilizando referências `ref` para unidades compartilhadas quando aplicável)*
1. **Identificação das unidades comportamentais:**
   > `"Para o sistema X, identifique as unidades de comportamento que devem ser representadas nos diagramas de sequência. A especificação comportamental pode ser dividida em unidades que não precisam corresponder a casos de uso independentes, podendo representar etapas internas de um único cenário. Considere estritamente os requisitos (HUs) e o código PUML de casos de uso <HU e UC>"`
2. **Elementos colaborativos para cada unidade comportamental:**
   > `"Neste sistema, baseado na especificação comportamental estruturada e nos diagramas PUML de componentes e classes, identifique os elementos que colaboram para realizar cada unidade comportamental, mapeando o conjunto de participantes candidatos para cada unidade comportamental <PUML de componentes e classes>"`
3. **Determinação dos participantes responsáveis:**
   > `"Baseado nas unidades comportamentais, participantes candidatos, diagrama de classes e responsabilidades dos componentes, determine quais participantes possuem as responsabilidades necessárias para executar cada unidade comportamental, gerando um mapeamento entre comportamentos, classes, métodos e componentes. Seja restrito à semântica que foi passada anteriormente"`
4. **Identificação das colaborações:**
   > `"Estrito na especificação comportamental, nos participantes identificados e no mapeamento de responsabilidades e operações, determine como os participantes devem colaborar em cada unidade comportamental, resultando na especificação das colaborações entre os participantes"`
5. **Estabelecer sequência temporal das interações:**
   > `"Baseado estritamente na especificação comportamental, nas colaborações identificadas e nas regras de negócio e restrições, estabeleça a sequência temporal das interações e as condições que controlam sua execução, gerando um fluxo de interações estruturado"`
6. **Produção do diagrama de sequência em código PUML:**
   > `"Produza um diagrama de sequência em código PUML validado considerando diferentes níveis. Considere estritamente os requisitos, modelo de classes, componentes, casos de uso e demais representações e fluxos previamente estruturados. Condense tudo em um único PUML"`

#### Critérios de Validação em 5 Níveis (Diretrizes, pág. 11)
| Nível | Pergunta de Verificação (Fig. 6) | O que verificar (Tabela pág. 11) |
| :--- | :--- | :--- |
| **Sintático** | `"O diagrama está bem formado?"` | O código está bem formado e pode ser renderizado pelo PlantUML? |
| **Estrutural** | `"Os participantes e as operações são compatíveis com o modelo de classes?"` | Os objetos participantes correspondem às classes modeladas? As operações são coerentes com as responsabilidades das classes receptoras? |
| **Arquitetural** | `"As interações respeitam os componentes e suas interfaces?"` | As interações respeitam as responsabilidades dos componentes e suas interfaces? |
| **Comportamental** | `"O fluxo representa os cenários e as regras de negócio?"` | A ordem das mensagens e as condições de execução representam os cenários e as regras de negócio? |
| **Rastreabilidade** | `"É possível relacionar o comportamento representado aos requisitos de origem?"` | É possível relacionar o comportamento representado aos requisitos de origem? |
