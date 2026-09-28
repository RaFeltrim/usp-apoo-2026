# Graph Report - APOO - USP  (2026-09-28)

## Corpus Check
- Corpus is ~35,337 words - fits in a single context window. You may not need a graph.

## Summary
- 81 nodes · 85 edges · 10 communities
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.95)
- Token cost: 1,500 input · 1,200 output

## Community Hubs (Navigation)
- Requisitos, Casos de Uso e Componentes
- Configura??o Web e Depend?ncias
- Pilares da OO, Classes e Associa??es
- Padr?es de Projeto GoF e Entregas
- Processo Unificado e M?dulos do Curso
- Interface Interativa dos Slides
- Bibliotecas de Gera??o PDF
- Compilador PDF Apresenta??o Observer
- Compilador PDF Relat?rio Jigsaw
- Compilador PDF GoF Completo

## God Nodes (most connected - your core abstractions)
1. `Pilares da Orientação a Objetos` - 6 edges
2. `Processo Unificado (UP / RUP)` - 6 edges
3. `Catálogo de Padrões de Projeto GoF` - 6 edges
4. `Diagrama de Casos de Uso (UML)` - 6 edges
5. `Tópico 4: Requisitos, Casos de Uso e Diagramas de Atividades` - 5 edges
6. `Padrões Comportamentais (GoF)` - 5 edges
7. `Identificação de Componentes Arquiteturais` - 5 edges
8. `Classes de Domínio & Conceitos Canônicos` - 5 edges
9. `goToSlide()` - 4 edges
10. `Tópico 2: Processos de Desenvolvimento de Software` - 4 edges

## Surprising Connections (you probably didn't know these)
- `Agregação vs Composição (Todo-Parte)` --rationale_for--> `Alta Coesão e Baixo Acoplamento`  [INFERRED]
  Tópico 5 - Componentes, Modelo Conceitual e Classes/Material de Apoio/Aula 09 - parte 1 - Elementos de projeto de Software (Arquitetura, componentes, classes, objetos).pdf → Tópico 1 - Revisao Paradigma OO/README.md
- `Catálogo de Padrões de Projeto GoF` --rationale_for--> `Alta Coesão e Baixo Acoplamento`  [INFERRED]
  Tópico 3 - Padroes de Projeto GoF/README.md → Tópico 1 - Revisao Paradigma OO/README.md
- `Tópico 1: Revisão do Paradigma OO` --references--> `Pilares da Orientação a Objetos`  [EXTRACTED]
  Tópico 1 - Revisao Paradigma OO/README.md → Tópico 1 - Revisao Paradigma OO/Material de Apoio/Aula 01 - O paradigma de orientação a objetos.pdf
- `Tópico 3: Padrões de Projeto GoF` --references--> `Tópico 4: Requisitos, Casos de Uso e Diagramas de Atividades`  [EXTRACTED]
  Tópico 3 - Padroes de Projeto GoF/README.md → Tópico 4 - Especificacao de Requisitos e Casos de Uso/README.md
- `Tópico 4: Requisitos, Casos de Uso e Diagramas de Atividades` --references--> `Engenharia e Especificação de Requisitos`  [EXTRACTED]
  Tópico 4 - Especificacao de Requisitos e Casos de Uso/README.md → Tópico 4 - Especificacao de Requisitos e Casos de Uso/Material de Apoio/Aula 06 - Análise e Especificação de Requisitos.pdf

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Do Requisito ao Design: UC -> Atividades -> Componentes -> Classes** — diagrama_casos_de_uso, diagrama_de_atividades, elementos_arquiteturais_componentes, classes_dominio_conceitos_canonicos, modelo_conceitual_sistema [INFERRED 0.95]

## Communities (10 total, 0 thin omitted)

### Community 0 - "Requisitos, Casos de Uso e Componentes"
Cohesion: 0.13
Nodes (17): Entrega 5: Modelagem Casos de Uso Plataforma Rodoviária, Entrega 6: Descrição Textual e Diagrama de Atividades, Diagrama de Casos de Uso (UML), Diagrama de Atividades (UML), Diagrama de Componentes (<<utiliza>>), Identificação de Componentes Arquiteturais, Engenharia e Especificação de Requisitos, Especificação Textual de Casos de Uso (+9 more)

### Community 1 - "Configura??o Web e Depend?ncias"
Cohesion: 0.18
Nodes (10): author, description, keywords, license, main, name, scripts, test (+2 more)

### Community 2 - "Pilares da OO, Classes e Associa??es"
Cohesion: 0.22
Nodes (10): Agregação vs Composição (Todo-Parte), Associação e Multiplicidade de Classes, Classes de Domínio & Conceitos Canônicos, Abstração, Alta Coesão e Baixo Acoplamento, Encapsulamento, Herança e Generalização, Pilares da Orientação a Objetos (+2 more)

### Community 3 - "Padr?es de Projeto GoF e Entregas"
Cohesion: 0.20
Nodes (10): Entrega 2: Estudo Individual Padrão Observer, Entrega 4: Comparativo Completo Categorias GoF, Entrega 3: Comparação Comportamentais Jigsaw, Catálogo de Padrões de Projeto GoF, Padrões Comportamentais (GoF), Padrões Criacionais (GoF), Padrões Estruturais (GoF), Padrão Chain of Responsibility (+2 more)

### Community 4 - "Processo Unificado e M?dulos do Curso"
Cohesion: 0.25
Nodes (9): Processo Unificado (UP / RUP), Tópico 0: Informações Gerais & Planejamento, Tópico 1: Revisão do Paradigma OO, Tópico 2: Processos de Desenvolvimento de Software, Tópico 3: Padrões de Projeto GoF, Entrega 1: Resumo Processos de Software (Valente Cap 2), Fase de Construção, Fase de Incepção (+1 more)

### Community 5 - "Interface Interativa dos Slides"
Cohesion: 0.53
Nodes (4): changeSlide(), goToSlide(), updateCounter(), updateProgress()

### Community 6 - "Bibliotecas de Gera??o PDF"
Cohesion: 0.40
Nodes (5): pdf-lib, puppeteer-core, dependencies, pdf-lib, puppeteer-core

### Community 7 - "Compilador PDF Apresenta??o Observer"
Cohesion: 0.40
Nodes (4): fs, path, { PDFDocument }, puppeteer

### Community 8 - "Compilador PDF Relat?rio Jigsaw"
Cohesion: 0.50
Nodes (3): fs, path, puppeteer

### Community 9 - "Compilador PDF GoF Completo"
Cohesion: 0.50
Nodes (3): fs, path, puppeteer

## Knowledge Gaps
- **43 isolated node(s):** `puppeteer`, `{ PDFDocument }`, `fs`, `path`, `name` (+38 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Catálogo de Padrões de Projeto GoF` connect `Padr?es de Projeto GoF e Entregas` to `Pilares da OO, Classes e Associa??es`, `Processo Unificado e M?dulos do Curso`?**
  _High betweenness centrality (0.121) - this node is a cross-community bridge._
- **Why does `Tópico 3: Padrões de Projeto GoF` connect `Processo Unificado e M?dulos do Curso` to `Requisitos, Casos de Uso e Componentes`, `Padr?es de Projeto GoF e Entregas`?**
  _High betweenness centrality (0.111) - this node is a cross-community bridge._
- **Why does `Tópico 4: Requisitos, Casos de Uso e Diagramas de Atividades` connect `Requisitos, Casos de Uso e Componentes` to `Processo Unificado e M?dulos do Curso`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **What connects `puppeteer`, `{ PDFDocument }`, `fs` to the rest of the system?**
  _43 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Requisitos, Casos de Uso e Componentes` be split into smaller, more focused modules?**
  _Cohesion score 0.1323529411764706 - nodes in this community are weakly interconnected._