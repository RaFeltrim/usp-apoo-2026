<div align="center">

# 🎓 SSC0124 — Análise e Projeto Orientados a Objetos

### *Estudos e entregas · ICMC USP · 2026*

[![USP ICMC](https://img.shields.io/badge/USP-ICMC-00529B?style=for-the-badge)](https://www.icmc.usp.br/)
[![Disciplina SSC0124](https://img.shields.io/badge/Disciplina-SSC0124-2ea44f?style=for-the-badge)](https://edisciplinas.usp.br/course/view.php?id=143121)
[![Conteúdo acadêmico](https://img.shields.io/badge/Conteúdo-Acadêmico-8A2BE2?style=for-the-badge)](#-estrutura-oficial-do-repositório-por-módulos--semanas)
[![Autor Rafael Feltrim](https://img.shields.io/badge/Autor-Rafael%20Feltrim-0A66C2?style=for-the-badge)](https://github.com/RaFeltrim)

<p align="center">
  <strong>Repositório de estudos, anotações, trabalhos práticos, resumos teóricos e materiais de apoio da disciplina SSC0124 — Análise e Projeto Orientados a Objetos, do Instituto de Ciências Matemáticas e de Computação da Universidade de São Paulo.</strong>
</p>

[Informações gerais](#-informações-gerais) •
[Estrutura do repositório](#-estrutura-oficial-do-repositório-por-módulos--semanas) •
[Atividades e entregas](#-mapa-geral-de-atividades--entregas-da-disciplina) •
[Como navegar](#-como-navegar) •
[Autoria](#-autor)

</div>
---

## 📌 Informações Gerais

- **Instituição:** Universidade de São Paulo (USP) - ICMC São Carlos
- **Departamento:** Departamento de Sistemas de Computação (SSC)
- **Código da Disciplina:** SSC0124
- **Semestre:** 2026.2
- **Docente Responsável:** Profa. Dra. Lina Garcés ([linagarces@usp.br](mailto:linagarces@usp.br))
  - *Gabinete:* Sala 4-107, Bloco 4 do ICMC
- **Horários e Locais:**
  - **Turma 1 (10h10):** Sala 1104, 1º Andar - Bloco 1 do ICMC
  - **Turma 2 (08h10):** Sala 1104, 1º Andar - Bloco 1 do ICMC
- **Ambiente Virtual:** [e-Disciplinas Moodle USP (SSC0124-2026)](https://edisciplinas.usp.br/course/view.php?id=143121)

---

## 🗂️ Estrutura Oficial do Repositório por Módulos & Semanas

```text
APOO - USP/
│
├── 📁 Tópico 0 - Informacoes Gerais/
│   ├── README.md                                         # Informações docentes, e-mails, horários e plano
│   └── 📁 Material de Apoio/
│       ├── Aula 0 - Apresentação da Disciplina.pdf           # Slides introdutórios da disciplina
│       └── SSC0124 - APOO - Planejamento disciplina.docx.pdf # Planejamento e cronograma do semestre
│
├── 📁 Tópico 1 - Revisao Paradigma OO/                   # (Semana 1)
│   ├── README.md                                         # Resumo: 4 Pilares da POO, Coesão & Acoplamento
│   └── 📁 Material de Apoio/
│       └── Aula 01 - O paradigma de orientação a objetos.pdf # Slides de revisão da Profa. Lina Garcés
│
├── 📁 Tópico 2 - Processos Desenvolvimento Software/     # (Semana 2)
│   ├── README.md                                         # Resumo: Processo Unificado (UP) e Ágil
│   ├── 📁 Entregas/
│   │   └── Atividade 1 - Resumo.pdf                          # [ENTREGA 1] Resumo manuscrito do Cap. 2 (Valente)
│   └── 📁 Material de Apoio/
│       └── Aula 02 - Análise e Design de Software e o Processo Unificado.pdf
│
├── 📁 Tópico 3 - Padroes de Projeto GoF/                 # (Semanas 3 e 4)
│   ├── README.md                                         # Panorama dos Padrões GoF
│   ├── 📁 Exercícios e Laboratórios/
│   │   ├── Atividade 2 -  Padrões GoF - primeira parte.pdf  # Enunciado Estudo Individual
│   │   └── Atividade 3 -  Padrões GoF - segunda parte.pdf   # Enunciado Comparativo Categorias
│   ├── 📁 Material de Apoio/
│   │   └── Aula - Jigsaw - Padrões GoF - 10h.pdf             # Slides da dinâmica Jigsaw em sala
│   └── 📁 Entregas/
│       ├── 📁 01-Padrao-Observer/
│       │   ├── README.md                                     # Ficha técnica, painel Padlet e conceitos
│       │   ├── Rafael_Feltrim_Entrega_Observer.pdf           # [ENTREGA 2] Relatório do padrão Observer
│       │   ├── Rafael_Feltrim_Atividade2_Observer.zip        # Pacote compactado da entrega individual
│       │   └── 📁 Apresentacao-Web/                          # Aplicação interativa em HTML5/CSS3/JS
│       │
│       ├── 📁 02-Atividade-Comparacao-Categorias/
│       │   ├── README.md                                     # Matriz de comparação dos padrões comportamentais
│       │   ├── Relatorio_Discussao_Comportamentais_Grupo.pdf  # [ENTREGA 3] Relatório da discussão em sala (Jigsaw)
│       │   └── relatorio-discussao.html
│       │
│       └── 📁 03-Atividade-Comparacao-Categorias-Completa/
│           ├── README.md                                     # Diretrizes da Atividade 3 (GoF Parte 2)
│           ├── Rafael_Feltrim_Atividade3_Comparacao_Categorias_GoF.pdf # [ENTREGA 4] Relatório Individual Completo
│           └── relatorio-gof-completo.html
│
├── 📁 Tópico 4 - Especificacao de Requisitos e Casos de Uso/  # (Semanas 5 e 6)
│   ├── README.md                                         # Resumo de requisitos, UC e atividades
│   ├── 📁 Material de Apoio/
│   │   ├── Aula 06 - Análise e Especificação de Requisitos e UC.pdf
│   │   ├── Aula 0 6- Anexo A - Descrição do Modelo de Qualidade ISO_IEC 25010 - SQUARE.pdf
│   │   ├── Aula 07 - Casos de Uso - relações.pdf
│   │   ├── Aula 8 - Casos de uso - prática.pdf
│   │   └── Aula 8 - Material Complementar - Diagrama de Atividades.pdf
│   └── 📁 Entregas/
│       ├── 📁 Atividade - Casos de Uso/
│       │   ├── Atividade - casos de uso.docx.pdf             # [ENTREGA 5] Modelagem de Casos de Uso (Plataforma Rodoviária)
│       │   ├── Atividade – Diagrama de Casos de Uso.drawio.pdf
│       │   └── RESPOSTAS.md
│       │
│       └── 📁 Atividade - Descricao Textual e Diagrama de Atividades/
│           ├── Descrição Textual de Casos de Uso e Diagrama de Atividades - Rafael Feltrim.pdf # [ENTREGA 6] Documento consolidado
│           ├── Comprar Passagem.pdf                          # Diagrama de UC refinado
│           ├── Diagrama de Atividades.pdf                    # Diagrama de atividades (Swimlanes)
│           ├── Atividade – Descrição Textual de Casos de Uso e Diagrama de Atividades.docx.pdf
│           └── RESPOSTAS_ATIVIDADE_2.md
│
├── 📁 Tópico 5 - Componentes, Modelo Conceitual e Classes/    # (Semanas 7 a 9)
│   ├── README.md                                         # Análise & Design, Padrões Arquiteturais e Classes
│   ├── 📁 Material de Apoio/
│   │   ├── Aula 09 - parte 1 - Elementos de projeto de Software (Arquitetura, componentes, classes, objetos).pdf
│   │   └── modelo-conceitual-biblioteca.puml             # Código PlantUML oficial decodificado do Moodle
│   ├── 📁 Entregas/
│   │   └── 📁 Atividade - Identificacao de Componentes e Classes/
│   │       ├── Atividade – Identificação de Componentes e Classes do Sistema.pdf # [ENTREGA 7] Documento consolidado
│   │       ├── Atividade – Identificação de componentes e classes do sistema.docx-1.pdf # Enunciado oficial
│   │       ├── UML-Diagrama de Componentes UML seguindo o Padrão Arquitetural MVC.drawio.png # Diagrama MVC
│   │       ├── UML-Atividade_ Plataforma de Venda de Passagens Rodoviárias Integrada .drawio.png # Modelo Conceitual
│   │       └── RESPOSTAS_ATIVIDADE_3.md                  # Resolução técnica completa e scripts PlantUML
│   └── 📁 Exercícios e Laboratórios/
│
├── 📁 Tópico 6 - Diagrama de Sequencias/                 # (Semana 12 — 26/10)
│   ├── README.md                                         # Síntese teórica, métodos de classes e exemplo PlantUML
│   ├── 📁 Material de Apoio/                             # Local para Diagramas de interação - sequência.pdf
│   ├── 📁 Exercícios e Laboratórios/
│   └── 📁 Entregas/
│
├── 📁 Tópico 7 - Projeto Final/                          # (Semanas 15 a 17 — 16/11 a 30/11)
│   ├── README.md                                         # Pipeline completo, cronograma e checklist do projeto (35%)
│   ├── 📁 Material de Apoio/
│   └── 📁 Entregas/
│
├── 📁 graphify-out/                                      # Grafo de conhecimento navegável da disciplina
│   ├── GRAPH_REPORT.md                                   # Relatório analítico e God Nodes
│   ├── graph.html                                        # Visualização interativa
│   └── graph.json                                        # Base estruturada GraphRAG
│
├── .gitignore                                            # Filtro de dependências e arquivos temporários
└── README.md                                             # Portal central de navegação
```

---

## 📚 Mapa Geral de Atividades & Entregas da Disciplina

| Atividade | Módulo / Tópico | Prazo | Status | Arquivo Final de Entrega |
| :--- | :--- | :---: | :---: | :--- |
| **Atividade 1** | Resumo Cap. 2 Eng. Software Moderna (Processos de Software) | 17/08/2026 | ✅ **Entregue** | [`Atividade 1 - Resumo.pdf`](./Tópico%202%20-%20Processos%20Desenvolvimento%20Software/Entregas/Atividade%201%20-%20Resumo.pdf) |
| **Atividade 2** | Estudo Individual de Padrão (Padrão Observer) | 24/08/2026 | ✅ **Entregue** | [`Rafael_Feltrim_Entrega_Observer.pdf`](./Tópico%203%20-%20Padroes%20de%20Projeto%20GoF/Entregas/01-Padrao-Observer/Rafael_Feltrim_Entrega_Observer.pdf) |
| **Atividade em Sala (Jigsaw)** | Comparação de Padrões Comportamentais (Mediator, Observer, CoR) | 24/08/2026 | ✅ **Entregue** | [`Relatorio_Discussao_Comportamentais_Grupo.pdf`](./Tópico%203%20-%20Padroes%20de%20Projeto%20GoF/Entregas/02-Atividade-Comparacao-Categorias/Relatorio_Discussao_Comportamentais_Grupo.pdf) |
| **Atividade 3 (GoF Parte 2)** | Estudo Comparativo Completo: 3 Categorias, 9 Padrões e 3 Tabelas | 31/08/2026 | ✅ **Entregue** | [`Rafael_Feltrim_Atividade3_Comparacao_Categorias_GoF.pdf`](./Tópico%203%20-%20Padroes%20de%20Projeto%20GoF/Entregas/03-Atividade-Comparacao-Categorias-Completa/Rafael_Feltrim_Atividade3_Comparacao_Categorias_GoF.pdf) |
| **Atividade 4 (Casos de Uso)** | Diagrama Geral de Casos de Uso (Sistema Rodoviário / ClickBus) | 21/09/2026 | ✅ **Entregue** | [`Atividade - casos de uso.docx.pdf`](./Tópico%204%20-%20Especificacao%20de%20Requisitos%20e%20Casos%20de%20Uso/Entregas/Atividade%20-%20Casos%20de%20Uso/Atividade%20-%20casos%20de%20uso.docx.pdf) |
| **Atividade 5 (Texto & Atividades)** | Descrição Textual de Casos de Uso e Diagrama de Atividades | 28/09/2026 | ✅ **Entregue** | [`Descrição Textual de Casos de Uso e Diagrama de Atividades - Rafael Feltrim.pdf`](./Tópico%204%20-%20Especificacao%20de%20Requisitos%20e%20Casos%20de%20Uso/Entregas/Atividade%20-%20Descricao%20Textual%20e%20Diagrama%20de%20Atividades/Descrição%20Textual%20de%20Casos%20de%20Uso%20e%20Diagrama%20de%20Atividades%20-%20Rafael%20Feltrim.pdf) |
| **Atividade 6 (Componentes & Classes)** | Identificação de Componentes, MVC e Modelo Conceitual de Classes | 14/10/2026 | ✅ **Entregue** | [`Atividade – Identificação de Componentes e Classes do Sistema.pdf`](./Tópico%205%20-%20Componentes,%20Modelo%20Conceitual%20e%20Classes/Entregas/Atividade%20-%20Identificacao%20de%20Componentes%20e%20Classes/Atividade%20–%20Identificação%20de%20Componentes%20e%20Classes%20do%20Sistema.pdf) |
| **Aula 12 (Diagrama de Sequências)** | Diagramas de interação — sequência e mapeamento para código | 26/10/2026 | 📘 **Em Estudo** | [`Tópico 6 - Diagrama de Sequencias`](./Tópico%206%20-%20Diagrama%20de%20Sequencias/README.md) |
| **Projeto Final (35% da Média)** | Desenvolvimento orientado a objetos integrado (Semanas 15 a 17) | 16/11 – 30/11 | 🎯 **Inicia em 16/11** | [`Tópico 7 - Projeto Final`](./Tópico%207%20-%20Projeto%20Final/README.md) |
| **Prova Final (40% da Média)** | Avaliação geral de APOO *(Sub em 14/12 com justificativa)* | 07/12/2026 | ⏳ **Prevista** | [`Cronograma e Critérios`](./Tópico%200%20-%20Informacoes%20Gerais/README.md) |

---

## 👥 Autor

- **Rafael Feltrim** ([GitHub](https://github.com/RaFeltrim)) — ICMC USP

---

## 🧭 Como navegar

| Objetivo | Onde encontrar |
| :--- | :--- |
| Consultar dados da disciplina | Seção **Informações Gerais** e pasta **Tópico 0** |
| Revisar conceitos | README de cada tópico e respectiva pasta **Material de Apoio** |
| Localizar trabalhos | Tabela **Mapa Geral de Atividades & Entregas** e pastas **Entregas** |
| Consultar exemplos e relatórios web | Arquivos HTML e pasta **Apresentacao-Web** nas entregas de padrões GoF |

Este repositório reúne materiais acadêmicos; não possui um comando único de instalação, execução ou testes documentado. Cada entrega deve ser consultada em seu contexto.

### Verificação e responsabilidade

- As datas e situações de entrega acima foram preservadas do README anterior; não representam uma nova confirmação de submissão no ambiente da disciplina.
- Não são declarados resultados de testes, cobertura ou auditorias sem execução verificável.
- Materiais de terceiros permanecem sujeitos aos direitos de seus respectivos autores. A presença no repositório não implica autorização de redistribuição.