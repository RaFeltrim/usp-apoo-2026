# Graph Report - APOO - USP  (2026-11-16)

## Corpus Check
- Corpus is ~49,058 words - fits in a single context window. You may not need a graph.

## Summary
- 101 nodes · 142 edges · 8 communities
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 6 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Projeto Final APOO LLM, UC & Sequência
- Bibliotecas de Geração PDF
- Pilares OO, Cronograma & Provas
- Compilador PDF Apresentação Observer
- Padrões de Projeto GoF e Coesão
- Classes, MVC & Modelo Conceitual
- Processo Unificado & Requisitos
- Interface Interativa dos Slides

## God Nodes (most connected - your core abstractions)
1. `Diagrama de Sequência (UML Interação)` - 10 edges
2. `Projeto Final: APOO assistido por LLM (14/12 - 35%)` - 9 edges
3. `Diagrama de Casos de Uso (UML)` - 8 edges
4. `Processo Unificado (UP / RUP)` - 7 edges
5. `Catálogo de Padrões de Projeto GoF` - 7 edges
6. `Classes de Domínio & Conceitos Canônicos` - 7 edges
7. `Diretrizes APOO Apoiado por LLM (Gem APOO em 5 Etapas)` - 7 edges
8. `Pilares da Orientação a Objetos` - 6 edges
9. `Tópico 4: Requisitos, Casos de Uso e Atividades` - 5 edges
10. `Padrões Comportamentais (GoF)` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Projeto Final: APOO assistido por LLM (14/12 - 35%)` --conceptually_related_to--> `Fase de Construção`  [INFERRED]
  Tópico 7 - Projeto Final/README.md → Tópico 2 - Processos Desenvolvimento Software/Material de Apoio/Aula 02 - Análise e Design de Software e o Processo Unificado.pdf
- `Agregação vs Composição (Todo-Parte)` --rationale_for--> `Alta Coesão e Baixo Acoplamento`  [INFERRED]
  Tópico 5 - Componentes, Modelo Conceitual e Classes/Material de Apoio/Aula 09 - parte 1 - Elementos de projeto de Software (Arquitetura, componentes, classes, objetos).pdf → Tópico 1 - Revisao Paradigma OO/README.md
- `Prova APOO 2026 (UP, Análise vs Projeto, Coesão, GoF, Modelagem)` --references--> `Diagrama de Sequência (UML Interação)`  [INFERRED]
  Exemplos de Prova/Material de Apoio/Cópia de Prova APOO 2026.docx.pdf → Tópico 6 - Diagrama de Sequencias/README.md
- `Diagrama de Sequência (UML Interação)` --references--> `Especificação Textual de Casos de Uso`  [INFERRED]
  Tópico 6 - Diagrama de Sequencias/README.md → Tópico 4 - Especificacao de Requisitos e Casos de Uso/Material de Apoio/Aula 8 - Casos de uso - prática.pdf
- `Diagrama de Sequência (UML Interação)` --references--> `Padrão Arquitetural MVC`  [EXTRACTED]
  Tópico 6 - Diagrama de Sequencias/README.md → Tópico 5 - Componentes, Modelo Conceitual e Classes/Material de Apoio/Aula 09 - parte 1 - Elementos de projeto de Software (Arquitetura, componentes, classes, objetos).pdf

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **APOO Assistido por LLM: HUs -> UC (.puml) -> Texto UC -> Componentes -> Classes -> Sequência -> Relatório (.zip)** — historias_usuario_clickbus, diretrizes_apoo_llm, diagrama_casos_de_uso, especificacao_textual_uc, diagrama_de_componentes, modelo_conceitual_sistema, diagrama_de_sequencia, estrutura_relatorio_llm [EXTRACTED 1.00]
- **Do Requisito ao Código: UC -> Atividades -> Componentes -> Classes -> Sequência -> Projeto** — diagrama_casos_de_uso, diagrama_de_atividades, elementos_arquiteturais_componentes, classes_dominio_conceitos_canonicos, diagrama_de_sequencia, projeto_final_apoo [INFERRED 0.95]

## Communities (8 total, 0 thin omitted)

### Community 0 - "Projeto Final APOO LLM, UC & Sequência"
Cohesion: 0.17
Nodes (17): Entrega 5: Modelagem Casos de Uso Plataforma Rodoviária, Entrega 6: Descrição Textual e Diagrama de Atividades, Entrega 8: Diagrama de Sequências e Classes com Métodos (PDF), Diagrama de Casos de Uso (UML), Diagrama de Atividades (UML), Diagrama de Sequência (UML Interação), Diretrizes APOO Apoiado por LLM (Gem APOO em 5 Etapas), Enunciado Projeto Final APOO LLM (Individual, .zip) (+9 more)

### Community 1 - "Bibliotecas de Geração PDF"
Cohesion: 0.14
Nodes (15): pdf-lib, puppeteer-core, author, dependencies, pdf-lib@^1.17.1, puppeteer-core@^25.8.0, description, keywords (+7 more)

### Community 2 - "Pilares OO, Cronograma & Provas"
Cohesion: 0.16
Nodes (14): Abstração, Encapsulamento, Pilares da Orientação a Objetos, Polimorfismo, Banco de Provas Anteriores e Mapa de Revisão, Prova APOO 2024-2 (Subprocesso Design, Diagramas UML, Abstração), Prova Final da Disciplina (07/12 - 40%), Subprocesso de Análise e Projeto (Design) (+6 more)

### Community 3 - "Compilador PDF Apresentação Observer"
Cohesion: 0.18
Nodes (8): fs, path, { PDFDocument }, puppeteer, fs, path, fs, path

### Community 4 - "Padrões de Projeto GoF e Coesão"
Cohesion: 0.18
Nodes (11): Entrega 2: Estudo Individual Padrão Observer, Entrega 4: Comparativo Completo Categorias GoF, Entrega 3: Comparação Comportamentais Jigsaw, Catálogo de Padrões de Projeto GoF, Padrões Comportamentais (GoF), Padrões Criacionais (GoF), Padrões Estruturais (GoF), Padrão Chain of Responsibility (+3 more)

### Community 5 - "Classes, MVC & Modelo Conceitual"
Cohesion: 0.25
Nodes (10): Associação e Multiplicidade de Classes, Navegabilidade, Classe Associativa, Ternária & {unique}/{readOnly}, Entrega 7: Componentes MVC e Modelo Conceitual ClickBus, Classes de Domínio & Conceitos Canônicos, Herança e Generalização, Diagrama de Componentes (<<utiliza>>), Identificação de Componentes Arquiteturais, Modelo Conceitual Integrado do Sistema (+2 more)

### Community 6 - "Processo Unificado & Requisitos"
Cohesion: 0.22
Nodes (9): Engenharia e Especificação de Requisitos, Processo Unificado (UP / RUP), Tópico 2: Processos de Desenvolvimento de Software, Tópico 3: Padrões de Projeto GoF, Tópico 4: Requisitos, Casos de Uso e Atividades, Entrega 1: Resumo Processos de Software (Valente Cap 2), Fase de Construção, Fase de Incepção (+1 more)

### Community 7 - "Interface Interativa dos Slides"
Cohesion: 0.53
Nodes (4): changeSlide(), goToSlide(), updateCounter(), updateProgress()

## Knowledge Gaps
- **19 isolated node(s):** `Encapsulamento`, `Polimorfismo`, `Fase de Incepção`, `Fase de Transição`, `Padrões Criacionais (GoF)` (+14 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 38 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Catálogo de Padrões de Projeto GoF` connect `Padrões de Projeto GoF e Coesão` to `Processo Unificado & Requisitos`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Diagrama de Sequência (UML Interação)` (e.g. with `Especificação Textual de Casos de Uso` and `Prova APOO 2026 (UP, Análise vs Projeto, Coesão, GoF, Modelagem)`) actually correct?**
  _`Diagrama de Sequência (UML Interação)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Encapsulamento`, `Polimorfismo`, `Fase de Incepção` to the rest of the system?**
  _19 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Bibliotecas de Geração PDF` be split into smaller, more focused modules?**
  _Cohesion score 0.14166666666666666 - nodes in this community are weakly interconnected._
- **Why does `Prova APOO 2026 (UP, Análise vs Projeto, Coesão, GoF, Modelagem)` connect `Padrões de Projeto GoF e Coesão` to `Projeto Final APOO LLM, UC & Sequência`, `Pilares OO, Cronograma & Provas`, `Processo Unificado & Requisitos`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Why does `Diagrama de Sequência (UML Interação)` connect `Projeto Final APOO LLM, UC & Sequência` to `Pilares OO, Cronograma & Provas`, `Padrões de Projeto GoF e Coesão`, `Classes, MVC & Modelo Conceitual`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._