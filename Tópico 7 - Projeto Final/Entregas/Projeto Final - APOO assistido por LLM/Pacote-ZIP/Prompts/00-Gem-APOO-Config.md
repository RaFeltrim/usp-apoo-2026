# Configuração do Gem `APOO` no Gemini e Roteiro de Prompts

> **Referência oficial:** [`Diretrizes - APOO apoiado por LLM.docx.pdf`](<../../../../Material%20de%20Apoio/Diretrizes%20-%20APOO%20apoiado%20por%20LLM.docx.pdf>) (págs. 3–6)

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

### Etapas 3, 4 e 5 *(aguardando publicação das diretrizes `(em breve)` pela docente)*
- **Etapa 3:** Diagrama de Componentes (`PUML`)
- **Etapa 4:** Diagrama de Classes Preliminar (atributos) e Diagrama de Classes Completo (atributos + métodos)
- **Etapa 5:** Diagramas de Sequência (1 por caso de uso)
