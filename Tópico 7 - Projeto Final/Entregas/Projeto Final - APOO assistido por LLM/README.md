# Projeto Final — APOO Assistido por LLM

- **Disciplina:** SSC0124 — Análise e Projeto Orientados a Objetos (`Profa. Dra. Lina Garcés`)
- **Aluno:** Rafael Feltrim · **N° USP:** `15942812`
- **Modalidade / Ferramentas:** Trabalho **Individual** · LLM **Gemini** (Gem `APOO`) · Diagramas em **PlantUML**
- **Prazo oficial de entrega:** **14 de dezembro de 2026** (arquivo `.zip` único no e-Disciplinas)

---

## Organização desta pasta

Para evitar misturar códigos `.puml`, rascunhos e comparativos *antes/depois* no pacote final enviado à professora, a pasta está dividida em duas áreas:

- [`./Pacote-ZIP/`](./Pacote-ZIP/) — **espelho limpo** do arquivo `.zip` único exigido no e-Disciplinas:
  - `Relatorio.pdf` *(a ser gerado ao concluir os Capítulos 1–7 + Apêndices 1–5)*
  - `Diagramas/` *(apenas os diagramas finais em `.png`/`.jpg`)*
  - `Prompts/` *(prompts e interações com o Gemini; já contém [`00-Gem-APOO-Config.md`](./Pacote-ZIP/Prompts/00-Gem-APOO-Config.md))*
- [`./Desenvolvimento/`](./Desenvolvimento/) — insumos e histórico de iterações usados para montar o relatório e as **Seções de Reflexão**:
  - [`Historias-de-Usuario.md`](./Desenvolvimento/Historias-de-Usuario.md) (`HU01..HU16`, rascunho inicial para revisão antes de subir no Gem `APOO`)
  - `PUML/` (códigos `.puml` por iteração → alimentam os **Apêndices 1 a 5**)
  - `Iteracoes-Antes-Depois/` (imagens de iterações iniciais vs. corrigidas → alimentam as **Seções de Reflexão**)

---

## Checklist de Execução (`Diretrizes` + `Estrutura de relatório`)

| Capítulo / Artefato | Regra Oficial | Diretriz Docente | Status |
| :--- | :--- | :---: | :---: |
| **Capa** | Nome completo + N° USP | [`Estrutura de relatório`](<../../Material%20de%20Apoio/Estrutura%20de%20relat%C3%B3rio.docx.pdf>) | ⏳ Aguardando geração |
| **Cap. 1 — Histórias de Usuário** | Formato *Como / eu quero / para que* (`HU01..HUn`) | [`Projeto Final`](<../../Material%20de%20Apoio/Projeto%20Final%20-%20APOO%20assistido%20por%20LLM.docx.pdf>) | 📝 Rascunho inicial criado ([HUs](./Desenvolvimento/Historias-de-Usuario.md)) |
| **Cap. 2 — Diagrama de Casos de Uso** | Diagrama final (`.png`) + Reflexão antes/depois + Apêndice 1 (`.puml`) | [`Diretrizes §1`](<../../Material%20de%20Apoio/Diretrizes%20-%20APOO%20apoiado%20por%20LLM.docx.pdf>) | ⏳ A fazer no Gemini |
| **Cap. 3 — Descrições Textuais Estendidas** | Todas as descrições de todos os UCs + Reflexão | `Diretrizes §2` | ⏳ A fazer após Cap. 2 |
| **Cap. 4 — Diagrama de Componentes** | Diagrama final (`.png`) + Reflexão antes/depois + Apêndice 2 (`.puml`) | *Diretriz §3 marcada como `(em breve)` em 16/11* | ⏳ Aguardando diretriz §3 |
| **Cap. 5 — Diagrama de Classes Preliminar** | Apenas atributos + Reflexão antes/depois + Apêndice 3 (`.puml`) | *Diretriz §4 marcada como `(em breve)` em 16/11* | ⏳ Aguardando diretriz §4 |
| **Cap. 6 — Diagramas de Sequência** | **1 diagrama por caso de uso** + Reflexão antes/depois + Apêndice 4 (`.puml`) | *Diretriz §5 marcada como `(em breve)` em 16/11* | ⏳ Aguardando diretriz §5 |
| **Cap. 7 — Diagrama de Classes Completo** | Atributos **E** métodos + Reflexão antes/depois + Apêndice 5 (`.puml`) | *Diretriz §4 marcada como `(em breve)` em 16/11* | ⏳ Aguardando diretriz §4 |
| **Empacotamento Final (`.zip`)** | Compactar `Relatorio.pdf`, `Diagramas/` e `Prompts/` até **14/12** | [`Projeto Final`](<../../Material%20de%20Apoio/Projeto%20Final%20-%20APOO%20assistido%20por%20LLM.docx.pdf>) | ⏳ Pendente |
