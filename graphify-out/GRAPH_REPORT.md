# Graph Report - APOO - USP  (2026-11-10)

## Corpus Check
- 52 files · ~55,909 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 89 nodes · 103 edges · 10 communities
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 6 edges (avg confidence: 0.92)
- Token cost: 1,800 input · 1,400 output

## Community Hubs (Navigation)
- Bibliotecas de Geração PDF
- Sequência, Projeto Final & MVC
- Padrões de Projeto GoF e Coesão
- Requisitos, Casos de Uso e Atividades
- Processo Unificado e Design de Software
- Pilares da OO e Cronograma Geral
- Interface Interativa dos Slides
- Compilador PDF Apresentação Observer
- Compiladores PDF (8)
- Compiladores PDF (9)

## God Nodes (most connected - your core abstractions)
1. `Catálogo de Padrões de Projeto GoF` - 7 edges
2. `Diagrama de Casos de Uso (UML)` - 7 edges
3. `Pilares da Orientação a Objetos` - 6 edges
4. `Processo Unificado (UP / RUP)` - 6 edges
5. `Classes de Domínio & Conceitos Canônicos` - 6 edges
6. `Diagrama de Sequência (UML Interação)` - 6 edges
7. `Projeto Final Integrado (16/11 a 30/11 - 35%)` - 6 edges
8. `Tópico 4: Requisitos, Casos de Uso e Atividades` - 5 edges
9. `Padrões Comportamentais (GoF)` - 5 edges
10. `Identificação de Componentes Arquiteturais` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Projeto Final Integrado (16/11 a 30/11 - 35%)` --conceptually_related_to--> `Fase de Construção`  [INFERRED]
  Tópico 7 - Projeto Final/README.md → Tópico 2 - Processos Desenvolvimento Software/Material de Apoio/Aula 02 - Análise e Design de Software e o Processo Unificado.pdf
- `Diagrama de Sequência (UML Interação)` --references--> `Especificação Textual de Casos de Uso`  [INFERRED]
  Tópico 6 - Diagrama de Sequencias/README.md → Tópico 4 - Especificacao de Requisitos e Casos de Uso/Material de Apoio/Aula 8 - Casos de uso - prática.pdf
- `Agregação vs Composição (Todo-Parte)` --rationale_for--> `Alta Coesão e Baixo Acoplamento`  [INFERRED]
  Tópico 5 - Componentes, Modelo Conceitual e Classes/Material de Apoio/Aula 09 - parte 1 - Elementos de projeto de Software (Arquitetura, componentes, classes, objetos).pdf → Tópico 1 - Revisao Paradigma OO/README.md
- `Projeto Final Integrado (16/11 a 30/11 - 35%)` --references--> `Diagrama de Casos de Uso (UML)`  [EXTRACTED]
  Tópico 7 - Projeto Final/README.md → Tópico 4 - Especificacao de Requisitos e Casos de Uso/Material de Apoio/Aula 07 - Casos de Uso - relações.pdf
- `Derivação de Métodos de Classe e Código` --conceptually_related_to--> `Classes de Domínio & Conceitos Canônicos`  [EXTRACTED]
  Tópico 6 - Diagrama de Sequencias/README.md → Tópico 5 - Componentes, Modelo Conceitual e Classes/Material de Apoio/Aula 09 - parte 1 - Elementos de projeto de Software (Arquitetura, componentes, classes, objetos).pdf

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Do Requisito ao Código: UC -> Atividades -> Componentes -> Classes -> Sequência -> Projeto** — diagrama_casos_de_uso, diagrama_de_atividades, elementos_arquiteturais_componentes, classes_dominio_conceitos_canonicos, diagrama_de_sequencia, projeto_final_apoo [INFERRED 0.95]

## Communities (10 total, 0 thin omitted)

### Community 0 - "Bibliotecas de Geração PDF"
Cohesion: 0.12
Nodes (15): pdf-lib, puppeteer-core, author, dependencies, pdf-lib, puppeteer-core, description, keywords (+7 more)

### Community 1 - "Sequência, Projeto Final & MVC"
Cohesion: 0.18
Nodes (15): Associação e Multiplicidade de Classes, Entrega 7: Componentes MVC e Modelo Conceitual ClickBus, Classes de Domínio & Conceitos Canônicos, Herança e Generalização, Derivação de Métodos de Classe e Código, Diagrama de Componentes (<<utiliza>>), Diagrama de Sequência (UML Interação), Identificação de Componentes Arquiteturais (+7 more)

### Community 2 - "Padrões de Projeto GoF e Coesão"
Cohesion: 0.17
Nodes (12): Agregação vs Composição (Todo-Parte), Entrega 2: Estudo Individual Padrão Observer, Entrega 4: Comparativo Completo Categorias GoF, Entrega 3: Comparação Comportamentais Jigsaw, Catálogo de Padrões de Projeto GoF, Alta Coesão e Baixo Acoplamento, Padrões Comportamentais (GoF), Padrões Criacionais (GoF) (+4 more)

### Community 3 - "Requisitos, Casos de Uso e Atividades"
Cohesion: 0.20
Nodes (11): Entrega 5: Modelagem Casos de Uso Plataforma Rodoviária, Entrega 6: Descrição Textual e Diagrama de Atividades, Diagrama de Casos de Uso (UML), Diagrama de Atividades (UML), Engenharia e Especificação de Requisitos, Especificação Textual de Casos de Uso, Modelo de Qualidade ISO/IEC 25010 (SQUARE), Relacionamento <<extend>> (+3 more)

### Community 4 - "Processo Unificado e Design de Software"
Cohesion: 0.25
Nodes (9): Processo Unificado (UP / RUP), Subprocesso de Análise e Projeto (Design), Tópico 2: Processos de Desenvolvimento de Software, Tópico 3: Padrões de Projeto GoF, Tópico 5: Componentes, Modelo Conceitual e Classes, Entrega 1: Resumo Processos de Software (Valente Cap 2), Fase de Elaboração, Fase de Incepção (+1 more)

### Community 5 - "Pilares da OO e Cronograma Geral"
Cohesion: 0.29
Nodes (7): Abstração, Encapsulamento, Pilares da Orientação a Objetos, Polimorfismo, Prova Final da Disciplina (07/12 - 40%), Tópico 0: Informações Gerais & Cronograma, Tópico 1: Revisão do Paradigma OO

### Community 6 - "Interface Interativa dos Slides"
Cohesion: 0.53
Nodes (4): changeSlide(), goToSlide(), updateCounter(), updateProgress()

### Community 7 - "Compilador PDF Apresentação Observer"
Cohesion: 0.40
Nodes (4): fs, path, { PDFDocument }, puppeteer

### Community 8 - "Compiladores PDF (8)"
Cohesion: 0.50
Nodes (3): fs, path, puppeteer

### Community 9 - "Compiladores PDF (9)"
Cohesion: 0.50
Nodes (3): fs, path, puppeteer

## Knowledge Gaps
- **40 isolated node(s):** `puppeteer`, `{ PDFDocument }`, `fs`, `path`, `name` (+35 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Catálogo de Padrões de Projeto GoF` connect `Padrões de Projeto GoF e Coesão` to `Sequência, Projeto Final & MVC`, `Processo Unificado e Design de Software`?**
  _High betweenness centrality (0.135) - this node is a cross-community bridge._
- **Why does `Projeto Final Integrado (16/11 a 30/11 - 35%)` connect `Sequência, Projeto Final & MVC` to `Padrões de Projeto GoF e Coesão`, `Requisitos, Casos de Uso e Atividades`?**
  _High betweenness centrality (0.094) - this node is a cross-community bridge._
- **Why does `Diagrama de Casos de Uso (UML)` connect `Requisitos, Casos de Uso e Atividades` to `Sequência, Projeto Final & MVC`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Catálogo de Padrões de Projeto GoF` (e.g. with `Alta Coesão e Baixo Acoplamento` and `Projeto Final Integrado (16/11 a 30/11 - 35%)`) actually correct?**
  _`Catálogo de Padrões de Projeto GoF` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `puppeteer`, `{ PDFDocument }`, `fs` to the rest of the system?**
  _40 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Bibliotecas de Geração PDF` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._