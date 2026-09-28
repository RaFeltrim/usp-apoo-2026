# Tópico 5 — Componentes, Modelo Conceitual e Classes

Módulo focado na transição da etapa de requisitos para o projeto (design) de software, abordando identificação de elementos arquiteturais, modelagem de componentes, padrões arquiteturais (ênfase em MVC), diagrama de classes de domínio, relacionamentos estruturais e elaboração do modelo conceitual integrado.

---

## 🔗 Links e Recursos do e-Disciplinas

- **Seção Moodle:** [Diagrama de Componentes, Diagrama de modelo conceitual, Diagrama de Classes e Associações entre Classes](https://edisciplinas.usp.br/course/section.php?id=6991982)
- **Arquivo da Aula:** [`Aula 09 - parte 1 - Elementos de projeto de Software (Arquitetura, componentes, classes, objetos).pdf`](./Material%20de%20Apoio/Aula%2009%20-%20parte%201%20-%20Elementos%20de%20projeto%20de%20Software%20(Arquitetura,%20componentes,%20classes,%20objetos).pdf)
- **Atividades Cadastradas:** Nenhuma atividade avaliativa publicada até o momento nesta seção.

---

## 📖 Síntese do Conteúdo Programático (Aula 09)

### 1. O Subprocesso de Análise e Projeto (Design)
- **Objetivo Central:** Transformar os requisitos em um projeto técnico robusto e sustentável.
- **Ciclo Iterativo de Design:**
  1. *Identificar elementos* (componentes, módulos, serviços, classes, objetos).
  2. *Definir relações entre os elementos*.
  3. *Definir colaborações entre os elementos*.
  4. *Definir a semântica dos elementos*.
  5. *Gerar especificações do design para a codificação*.

### 2. Elementos no Nível Arquitetural (Componentes & Padrões)
- **Abstração Arquitetural:** Agrupamento de casos de uso correlatos em componentes coesos (princípio da responsabilidade única).
- **Elementos Implícitos:** Bancos de dados, serviços em nuvem, middlewares, brokers de mensageria e APIs externas.
- **Diagrama de Componentes (UML):** Representação do relacionamento `<<utiliza>>` / `<<use>>`.
- **Padrões Arquiteturais:** Camadas (*Layers*), Microsserviços, *Publish-Subscribe*, *Pipes and Filters* e **MVC (Model-View-Controller)**.

### 3. Elementos Concretos (Classes e Objetos do Domínio)
- **Identificação de Classes:** A partir das responsabilidades do componente (coisas tangíveis, perfis, eventos, lugares, conceitos canônicos, transações).
- **Conceitos Canônicos e Refinamento:** Unificação de termos e sinônimos para evitar duplicidade de modelos.
- **Atributos e Tipagem:** Levantamento das propriedades que as entidades devem reter.

### 4. Relacionamentos entre Classes
- **Associação:** Conexão semântica direta com especificação de **multiplicidade** (`1`, `1..*`, `0..*`).
- **Herança (Generalização/Especialização):** Reuso de estrutura e polimorfismo. Discussão sobre herança simples e múltipla.
- **Agregação (`◇` losango vazio):** Vínculo fraco ("todo-parte"), onde a parte pode existir independentemente do todo.
- **Composição (`◆` losango preenchido):** Vínculo forte ("todo-parte"), onde a parte não existe ou não tem significado sem o todo.

### 5. Modelo Conceitual do Sistema
- União dos modelos de classes de todos os componentes mantendo integridade conceitual.
- Serve de subsídio direto para o Modelo Entidade-Relacionamento (MER) e abordagens MDD (*Model Driven Development*).
