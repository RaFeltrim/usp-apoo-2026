# Tópico 7 — Projeto Final da Disciplina & Revisão para Prova

Módulo reservado para o **Projeto Prático Final** da disciplina **SSC0124 — Análise e Projeto Orientados a Objetos** (peso **35%** da média final), conforme o cronograma oficial.

---

## 📅 Cronograma da Reta Final (Referência: 10/11/2026)

| Etapa | Data | Peso na Média | Status |
| :--- | :---: | :---: | :---: |
| **Aula 15 — PROJETO (Semana 1)** | **16/11/2026** *(próxima segunda)* | **35%** | ⏳ Aguardando início |
| **Aula 16 — PROJETO (Semana 2)** | **23/11/2026** | *(contínuo)* | ⏳ Planejado |
| **Aula 17 — PROJETO (Semana 3 — Encerramento)** | **30/11/2026** | *(entrega)* | ⏳ Planejado |
| **Aula 18 — PROVA FINAL** | **07/12/2026** | **40%** | 📝 Revisão teórica/prática |
| **Aula 19 — PROVA SUBSTITUTIVA / RECUPERAÇÃO** | **14/12/2026** | — | *(Apenas falta justificada / `3 <= MF < 5`)* |

> **Regra Crítica de Aprovação:** É necessário obter **nota >= 5,0 em cada componente** (`MProva`, `MExercícios`, `MProjeto`) e frequência >= 70%. Caso contrário, a média final será igual ao **menor valor** entre os três componentes.

---

## 🔗 Pipeline Completo de Artefatos (Do Requisito ao Código)

O projeto final consolida todo o ciclo do Processo Unificado e APOO trabalhado ao longo do semestre:

1. **Especificação de Requisitos e Casos de Uso** ([Tópico 4](../T%C3%B3pico%204%20-%20Especificacao%20de%20Requisitos%20e%20Casos%20de%20Uso/))
   - Identificação de atores primários/secundários, cenários principal/alternativo/exceção e relacionamentos `<<include>>`, `<<extend>>` e generalização.
   - Fluxos detalhados com Diagramas de Atividades (*swimlanes* e paralelismo).
2. **Arquitetura e Componentes (MVC)** ([Tópico 5](../T%C3%B3pico%205%20-%20Componentes,%20Modelo%20Conceitual%20e%20Classes/))
   - Separação em camadas (`<<view>>`, `<<controller>>`, `<<model>>`, `<<data>>`) com alta coesão e baixo acoplamento.
3. **Modelo Conceitual e Diagrama de Classes** ([Tópico 5](../T%C3%B3pico%205%20-%20Componentes,%20Modelo%20Conceitual%20e%20Classes/))
   - Conceitos canônicos, atributos tipados, multiplicidades, herança, agregação (`◇`) e composição (`◆`).
4. **Diagramas de Sequência e Métodos** ([Tópico 6](../T%C3%B3pico%206%20-%20Diagrama%20de%20Sequencias/))
   - Rastreamento temporal das mensagens entre objetos e definição precisa das assinaturas de métodos.
5. **Implementação + Padrões GoF + Persistência** ([Tópico 3](../T%C3%B3pico%203%20-%20Padroes%20de%20Projeto%20GoF/) + Aulas 9 e 12)
   - Aplicação de padrões GoF pertinentes ao domínio, implementação orientada a objetos e mapeamento para modelo relacional/banco de dados.

---

## ✅ Checklist de Preparação (16/11/2026)

- [ ] Receber enunciado oficial / escopo do projeto em aula (`16/11`) e salvar em `./Material de Apoio/`.
- [ ] Definir stack de implementação e persistência (conforme diretriz da professora).
- [ ] Consolidar diagramas UML atualizados (Casos de Uso, Atividades, Componentes MVC, Classes e Sequência).
- [ ] Implementar código-fonte mantendo rastreabilidade direta com os diagramas de classes e sequência.
- [ ] Validar requisitos funcionais, não-funcionais (ISO/IEC 25010) e entregar dentro do prazo (`30/11`).
