# Tópico 7 — Projeto Final da Disciplina & Revisão para Prova

Módulo reservado para o **Projeto Prático Final** da disciplina **SSC0124 — Análise e Projeto Orientados a Objetos** (peso **35%** da média final): **APOO assistido por LLM**, modelo de processo iterativo com **Gemini** + **PlantUML** sobre a plataforma de passagens rodoviárias (estilo ClickBus).

---

## 🔗 Links e Materiais Oficiais (`16/11/2026`)

- **Seção Moodle:** [Projeto Final (e-Disciplinas)](https://edisciplinas.usp.br/course/section.php?id=6991985)
- **Enunciado Oficial:** [`Projeto Final - APOO assistido por LLM.docx.pdf`](<./Material%20de%20Apoio/Projeto%20Final%20-%20APOO%20assistido%20por%20LLM.docx.pdf>) *([Google Docs original](https://docs.google.com/document/d/1UUVIc4oWDYsyYFCBsev1jw4y_SDMWTcv/edit?usp=sharing&ouid=102633812852574880163&rtpof=true&sd=true))*
- **Diretrizes de Modelagem com IA:** [`Diretrizes - APOO apoiado por LLM.docx.pdf`](<./Material%20de%20Apoio/Diretrizes%20-%20APOO%20apoiado%20por%20LLM.docx.pdf>) *([Google Docs original](https://docs.google.com/document/d/1lIo5g93lLTASKmpFHf1u_NcnYI1Ht4AU/edit?usp=sharing&ouid=102633812852574880163&rtpof=true&sd=true) — etapas 3, 4 e 5 marcadas como `(em breve)` em 16/11)*
- **Template do Relatório:** [`Estrutura de relatório.docx.pdf`](<./Material%20de%20Apoio/Estrutura%20de%20relat%C3%B3rio.docx.pdf>) *([Google Docs original](https://docs.google.com/document/d/1P4UoUzytTpJgtZeA1xpXu-RUjvCkQ-ev/edit?usp=sharing&ouid=102633812852574880163&rtpof=true&sd=true))*
- **Área de Trabalho / Entrega:** [`./Entregas/Projeto Final - APOO assistido por LLM/`](<./Entregas/Projeto%20Final%20-%20APOO%20assistido%20por%20LLM/README.md>)

---

## 📅 Cronograma Oficial Atualizado (Referência: 16/11/2026)

| Marco | Data | Peso / Regras | Status |
| :--- | :---: | :---: | :---: |
| **Publicação do Projeto Final (Aula 15)** | **16/11/2026** | **35%** (`Individual`) | 🚀 Enunciado publicado |
| **Desenvolvimento Assistido por LLM** | **16/11 a 14/12** | **Gemini + PlantUML** | 📝 Em preparação |
| **Prova Final (Aula 18)** | **07/12/2026** | **40%** | 📝 Revisão teórica/prática |
| **Entrega do Projeto Final (`.zip` no Moodle)** | **14/12/2026** | **Individual** | ⏳ Prazo oficial no enunciado |
| **Prova Substitutiva / Recuperação** | **14/12/2026** | — | *(Falta justificada / `3 <= MF < 5`)* |

> **Regra Crítica de Aprovação:** É necessário obter **nota >= 5,0 em cada componente** (`MProva`, `MExercícios`, `MProjeto`) e frequência >= 70%. Caso contrário, a média final será igual ao **menor valor** entre os três componentes.
>
> *Nota de cronograma:* O planejamento inicial do semestre previa encerramento do projeto em `30/11`, mas o enunciado oficial publicado em `16/11` definiu o prazo final em **14 de dezembro de 2026**.

---

## 🔄 Fluxo do Processo APOO Assistido por LLM & Estrutura do `.zip`

O projeto aplica de ponta a ponta o conhecimento dos Tópicos 4 a 6 com apoio do assistente **Gem `APOO`** no **Gemini** e avaliação crítica humana (semântica, sintaxe, completude e corretude):

1. **Histórias de Usuário (`HU01..HUn`):** formato `Como [persona], eu quero [ação], para que [benefício]`.
2. **Diagrama de Casos de Uso (`PUML`):** construção incremental no Gemini (atores/heranças → UCs por ator → `<<include>>`/`<<extend>>`) + Seção de Reflexão (*antes/depois*).
3. **Descrições Textuais Estendidas:** geração para **todos** os casos de uso + validação contra o `.puml` + Seção de Reflexão.
4. **Diagrama de Componentes (`PUML`):** + Seção de Reflexão (*aguardando diretriz §3*).
5. **Diagrama de Classes Preliminar (atributos):** + Seção de Reflexão (*aguardando diretriz §4*).
6. **Diagramas de Sequência (1 por caso de uso):** + Seção de Reflexão (*aguardando diretriz §5*).
7. **Diagrama de Classes Completo (atributos + métodos):** + Seção de Reflexão (*aguardando diretriz §4*).

### Pacote `.zip` Único Exigido no e-Disciplinas
```text
Entrega_Projeto_Final.zip
├── Relatorio.pdf      # Capa + Capítulos 1–7 (com Reflexões antes/depois) + Apêndices 1–5 (códigos .puml)
├── Diagramas/         # Diagramas finais gerados via PlantUML em .png / .jpg
└── Prompts/           # Prompts e registros de interações com o Gemini
```

---

## ✅ Checklist de Execução (Prazo: 14/12/2026)

- [x] Salvar enunciado, diretrizes e estrutura de relatório em `./Material de Apoio/`.
- [x] Estruturar pasta de entrega espelhando `.zip` (`Relatorio.pdf`, `Diagramas/`, `Prompts/`) e `Desenvolvimento/`.
- [ ] Revisar rascunho [`Historias-de-Usuario.md`](<./Entregas/Projeto%20Final%20-%20APOO%20assistido%20por%20LLM/Desenvolvimento/Historias-de-Usuario.md>) e configurar Gem `APOO` no Gemini.
- [ ] Executar Etapas 1 e 2 (`Diretrizes`) registrando `.puml`, imagens *antes/depois* e prompts.
- [ ] Baixar versão atualizada de `Diretrizes - APOO apoiado por LLM.docx` quando as seções 3, 4 e 5 (`(em breve)`) forem publicadas.
- [ ] Executar Etapas 3, 4 e 5, compilar `Relatorio.pdf` (Capítulos 1–7 + Apêndices 1–5) e enviar `.zip` único até **14/12/2026**.

---

## 📝 Preparação para a Prova Final (07/12/2026)

- Consulte [`Exemplos de Prova`](../Exemplos%20de%20Prova/README.md) com as provas anteriores publicadas no e-Disciplinas (`2024-2` e `2026`) e o mapa de temas para revisão.
- **Atenção:** As provas anteriores cobram diretamente **exemplos e decisões de abstração do projeto desenvolvido em aula** — manter os artefatos e as Seções de Reflexão deste módulo bem documentados ajuda diretamente na Prova Final.
