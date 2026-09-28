# Tópico 4 — Especificação de Requisitos, Casos de Uso e Diagramas de Atividades

Módulo dedicado ao levantamento de requisitos, modelagem comportamental com Diagramas de Casos de Uso (UML), especificação textual detalhada (fluxo principal, alternativo e de exceção) e modelagem de fluxos com Diagramas de Atividades.

---

## 🔗 Links e Recursos do e-Disciplinas

- **Seções Moodle:**
  - [Especificação de Requisitos - Casos de Uso](https://edisciplinas.usp.br/course/section.php?id=6991980)
  - [Especificação textual de casos de uso e diagramas de atividades](https://edisciplinas.usp.br/course/section.php?id=6991981)

- **Materiais de Apoio da Docente:**
  - [`Aula 06 - Análise e Especificação de Requisitos e UC.pdf`](./Material%20de%20Apoio/Aula%2006%20-%20Análise%20e%20Especificação%20de%20Requisitos%20e%20UC.pdf)
  - [`Aula 0 6- Anexo A - Descrição do Modelo de Qualidade ISO_IEC 25010 - SQUARE.pdf`](./Material%20de%20Apoio/Aula%200%206-%20Anexo%20A%20-%20Descrição%20do%20Modelo%20de%20Qualidade%20ISO_IEC%2025010%20-%20SQUARE.pdf)
  - [`Aula 07 - Casos de Uso - relações.pdf`](./Material%20de%20Apoio/Aula%2007%20-%20Casos%20de%20Uso%20-%20relações.pdf)
  - [`Aula 8 - Casos de uso - prática.pdf`](./Material%20de%20Apoio/Aula%208%20-%20Casos%20de%20uso%20-%20prática.pdf)
  - [`Aula 8 - Material Complementar - Diagrama de Atividades.pdf`](./Material%20de%20Apoio/Aula%208%20-%20Material%20Complementar%20-%20Diagrama%20de%20Atividades.pdf)

---

## 📝 Atividades Práticas e Entregas

### 1. [Entrega 1] Tarefa Individual — Diagrama de Casos de Uso
- **Pasta:** [`./Entregas/Atividade - Casos de Uso/`](./Entregas/Atividade%20-%20Casos%20de%20Uso/)
- **Período:** 15 de setembro de 2026 a 21 de setembro de 2026, 08:00
- **Escopo:** Modelagem do sistema de plataforma rodoviária integrada (estilo ClickBus).
- **Entregáveis:**
  - [`Atividade - casos de uso.docx.pdf`](./Entregas/Atividade%20-%20Casos%20de%20Uso/Atividade%20-%20casos%20de%20uso.docx.pdf) (Documento formal final)
  - [`Atividade – Diagrama de Casos de Uso.drawio.pdf`](./Entregas/Atividade%20-%20Casos%20de%20Uso/Atividade%20–%20Diagrama%20de%20Casos%20de%20Uso.drawio.pdf) (Diagrama exportado do diagrams.net)
  - [`RESPOSTAS.md`](./Entregas/Atividade%20-%20Casos%20de%20Uso/RESPOSTAS.md) (Especificação textual e código PlantUML)

### 2. [Entrega 2] Atividade — Descrição Textual de Casos de Uso e Diagrama de Atividades
- **Pasta:** [`./Entregas/Atividade - Descricao Textual e Diagrama de Atividades/`](./Entregas/Atividade%20-%20Descricao%20Textual%20e%20Diagrama%20de%20Atividades/)
- **Período:** 20 de setembro de 2026 a 28 de setembro de 2026, 08:00
- **Escopo:** Detalhamento formal do Caso de Uso *Comprar Passagem*, cenários alternativos e de exceção, diagrama reduzido de UC e diagrama de atividades particionado (*swimlanes*).
- **Entregáveis:**
  - [`Descrição Textual de Casos de Uso e Diagrama de Atividades - Rafael Feltrim.pdf`](./Entregas/Atividade%20-%20Descricao%20Textual%20e%20Diagrama%20de%20Atividades/Descrição%20Textual%20de%20Casos%20de%20Uso%20e%20Diagrama%20de%20Atividades%20-%20Rafael%20Feltrim.pdf) (Documento consolidado de entrega final com N° USP)
  - [`Comprar Passagem.pdf`](./Entregas/Atividade%20-%20Descricao%20Textual%20e%20Diagrama%20de%20Atividades/Comprar%20Passagem.pdf) (Diagrama de Caso de Uso focado no diagrams.net)
  - [`Diagrama de Atividades.pdf`](./Entregas/Atividade%20-%20Descricao%20Textual%20e%20Diagrama%20de%20Atividades/Diagrama%20de%20Atividades.pdf) (Diagrama de Atividades com raias do diagrams.net)
  - [`RESPOSTAS_ATIVIDADE_2.md`](./Entregas/Atividade%20-%20Descricao%20Textual%20e%20Diagrama%20de%20Atividades/RESPOSTAS_ATIVIDADE_2.md) (Rascunho técnico e scripts PlantUML)

---

## 📖 Síntese Teórica do Módulo

1. **Requisitos de Software:**
   - Funcionais (o que o sistema faz) vs. Não-funcionais (como o sistema se comporta, baseado na ISO/IEC 25010 - SQUARE: usabilidade, segurança, confiabilidade, eficiência).
2. **Diagramas de Casos de Uso (UML):**
   - **Atores:** Primários (iniciam ações) e Secundários (fornecem serviços/apoio, ex.: gateways de pagamento, serviços de mensageria).
   - **Relacionamentos:**
     - `<<include>>`: Comportamento obrigatório compartilhado (baixo acoplamento / alta coesão).
     - `<<extend>>`: Comportamento opcional ou condicional que estende o fluxo base em pontos de extensão.
     - `Generalização/Especialização`: Herança entre atores ou casos de uso.
3. **Diagramas de Atividades (UML):**
   - Modelagem do fluxo de controle e fluxo de dados de um caso de uso.
   - Particionamento por **raias (swimlanes)** para indicar responsabilidades claras de cada ator e componente do sistema.
   - Nós de decisão (`decision node`), mesclagem (`merge node`), bifurcação paralela (`fork`) e junção (`join`).
