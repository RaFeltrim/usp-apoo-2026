# Graph Report - APOO - USP  (2026-11-23)

## Corpus Check
- 104 files · ~55,241 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 36 file(s) not represented in the graph (top: .puml 28, (none) 4, .css 2)
- WARNING: 36 of 140 files seen (26%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 110 nodes · 161 edges · 9 communities
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 6 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Projeto Final APOO LLM, UC & Sequência
- Bibliotecas de Geração PDF
- Processo Unificado & Requisitos
- Compilador PDF Apresentação Observer
- Classes, MVC & Modelo Conceitual
- Módulo Auxiliar (5)
- Pilares OO, Cronograma & Provas
- Padrões de Projeto GoF e Coesão
- Interface Interativa dos Slides

## God Nodes (most connected - your core abstractions)
1. `Projeto Final: APOO assistido por LLM (14/12 - 35%)` - 18 edges
2. `Diagrama de Sequência (UML Interação)` - 11 edges
3. `Diagrama de Casos de Uso (UML)` - 9 edges
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
- `Prova APOO 2026 (UP, Análise vs Projeto, Coesão, GoF, Modelagem)` --references--> `Diagrama de Sequência (UML Interação)`  [INFERRED]
  Exemplos de Prova/Material de Apoio/Cópia de Prova APOO 2026.docx.pdf → Tópico 6 - Diagrama de Sequencias/README.md
- `Agregação vs Composição (Todo-Parte)` --rationale_for--> `Alta Coesão e Baixo Acoplamento`  [INFERRED]
  Tópico 5 - Componentes, Modelo Conceitual e Classes/Material de Apoio/Aula 09 - parte 1 - Elementos de projeto de Software (Arquitetura, componentes, classes, objetos).pdf → Tópico 1 - Revisao Paradigma OO/README.md
- `PF Etapa 1: Diagrama de Casos de Uso Final (14 UCs, 6 atores)` --implements--> `Diagrama de Casos de Uso (UML)`  [EXTRACTED]
  Tópico 7 - Projeto Final/Entregas/Projeto Final - APOO assistido por LLM/Desenvolvimento/PUML/01-casos-de-uso-final.puml → Tópico 4 - Especificacao de Requisitos e Casos de Uso/Material de Apoio/Aula 07 - Casos de Uso - relações.pdf
- `Projeto Final: APOO assistido por LLM (14/12 - 35%)` --references--> `Diagrama de Casos de Uso (UML)`  [EXTRACTED]
  Tópico 7 - Projeto Final/README.md → Tópico 4 - Especificacao de Requisitos e Casos de Uso/Material de Apoio/Aula 07 - Casos de Uso - relações.pdf

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **APOO Assistido por LLM: HUs -> UC (.puml) -> Texto UC -> Componentes -> Classes -> Sequência -> Relatório (.zip)** — historias_usuario_clickbus, diretrizes_apoo_llm, diagrama_casos_de_uso, especificacao_textual_uc, diagrama_de_componentes, modelo_conceitual_sistema, diagrama_de_sequencia, estrutura_relatorio_llm [EXTRACTED 1.00]
- **Do Requisito ao Código: UC -> Atividades -> Componentes -> Classes -> Sequência -> Projeto** — diagrama_casos_de_uso, diagrama_de_atividades, elementos_arquiteturais_componentes, classes_dominio_conceitos_canonicos, diagrama_de_sequencia, projeto_final_apoo [INFERRED 0.95]

## Communities (9 total, 0 thin omitted)

### Community 0 - "Projeto Final APOO LLM, UC & Sequência"
Cohesion: 0.15
Nodes (20): Associação e Multiplicidade de Classes, Navegabilidade, Classe Associativa, Ternária & {unique}/{readOnly}, Entrega 7: Componentes MVC e Modelo Conceitual ClickBus, Classes de Domínio & Conceitos Canônicos, Herança e Generalização, Diagrama de Componentes (<<utiliza>>), Diretrizes APOO Apoiado por LLM (Gem APOO em 5 Etapas), Enunciado Projeto Final APOO LLM (Individual, .zip) (+12 more)

### Community 1 - "Bibliotecas de Geração PDF"
Cohesion: 0.14
Nodes (15): pdf-lib, puppeteer-core, author, dependencies, pdf-lib@^1.17.1, puppeteer-core@^25.8.0, description, keywords (+7 more)

### Community 2 - "Processo Unificado & Requisitos"
Cohesion: 0.18
Nodes (12): Entrega 4: Comparativo Completo Categorias GoF, Catálogo de Padrões de Projeto GoF, Padrões Criacionais (GoF), Padrões Estruturais (GoF), Processo Unificado (UP / RUP), Prova APOO 2026 (UP, Análise vs Projeto, Coesão, GoF, Modelagem), Tópico 2: Processos de Desenvolvimento de Software, Tópico 3: Padrões de Projeto GoF (+4 more)

### Community 3 - "Compilador PDF Apresentação Observer"
Cohesion: 0.18
Nodes (8): fs, path, { PDFDocument }, puppeteer, fs, path, fs, path

### Community 4 - "Classes, MVC & Modelo Conceitual"
Cohesion: 0.17
Nodes (12): Entrega 5: Modelagem Casos de Uso Plataforma Rodoviária, Diagrama de Casos de Uso (UML), Identificação de Componentes Arquiteturais, Engenharia e Especificação de Requisitos, PF Etapa 1: Diagrama de Casos de Uso Final (14 UCs, 6 atores), Relacionamento <<extend>>, Relacionamento <<include>>, Subprocesso de Análise e Projeto (Design) (+4 more)

### Community 5 - "Módulo Auxiliar (5)"
Cohesion: 0.27
Nodes (9): Entrega 6: Descrição Textual e Diagrama de Atividades, Entrega 8: Diagrama de Sequências e Classes com Métodos (PDF), Diagrama de Atividades (UML), Diagrama de Sequência (UML Interação), Especificação Textual de Casos de Uso, Fragmentos Combinados (alt, opt, loop, par), Gate, Ref Frame e Persistência MVC (VendasDatabase), PF Etapa 2: Descrições Textuais Estendidas (UC01..UC14) (+1 more)

### Community 6 - "Pilares OO, Cronograma & Provas"
Cohesion: 0.22
Nodes (10): Abstração, Encapsulamento, Pilares da Orientação a Objetos, Polimorfismo, Banco de Provas Anteriores e Mapa de Revisão, Prova APOO 2024-2 (Subprocesso Design, Diagramas UML, Abstração), Prova Final da Disciplina (07/12 - 40%), Tópico 0: Informações Gerais & Cronograma (+2 more)

### Community 7 - "Padrões de Projeto GoF e Coesão"
Cohesion: 0.33
Nodes (6): Entrega 2: Estudo Individual Padrão Observer, Entrega 3: Comparação Comportamentais Jigsaw, Padrões Comportamentais (GoF), Padrão Chain of Responsibility, Padrão Mediator, Padrão Observer

### Community 8 - "Interface Interativa dos Slides"
Cohesion: 0.53
Nodes (4): changeSlide(), goToSlide(), updateCounter(), updateProgress()

## Knowledge Gaps
- **18 isolated node(s):** `Encapsulamento`, `Polimorfismo`, `Fase de Incepção`, `Fase de Transição`, `Padrões Criacionais (GoF)` (+13 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 37 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Projeto Final: APOO assistido por LLM (14/12 - 35%)` connect `Projeto Final APOO LLM, UC & Sequência` to `Processo Unificado & Requisitos`, `Classes, MVC & Modelo Conceitual`, `Módulo Auxiliar (5)`, `Pilares OO, Cronograma & Provas`?**
  _High betweenness centrality (0.121) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Diagrama de Sequência (UML Interação)` (e.g. with `Especificação Textual de Casos de Uso` and `Prova APOO 2026 (UP, Análise vs Projeto, Coesão, GoF, Modelagem)`) actually correct?**
  _`Diagrama de Sequência (UML Interação)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Encapsulamento`, `Polimorfismo`, `Fase de Incepção` to the rest of the system?**
  _18 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Projeto Final APOO LLM, UC & Sequência` be split into smaller, more focused modules?**
  _Cohesion score 0.14761904761904762 - nodes in this community are weakly interconnected._
- **Why does `Catálogo de Padrões de Projeto GoF` connect `Processo Unificado & Requisitos` to `Padrões de Projeto GoF e Coesão`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **Should `Bibliotecas de Geração PDF` be split into smaller, more focused modules?**
  _Cohesion score 0.14166666666666666 - nodes in this community are weakly interconnected._
- **Why does `Diagrama de Sequência (UML Interação)` connect `Módulo Auxiliar (5)` to `Projeto Final APOO LLM, UC & Sequência`, `Processo Unificado & Requisitos`, `Classes, MVC & Modelo Conceitual`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._