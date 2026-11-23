# Projeto Final — APOO Assistido por LLM

- **Disciplina:** SSC0124 — Análise e Projeto Orientados a Objetos (`Profa. Dra. Lina Garcés`)
- **Aluno:** Rafael Feltrim · **N° USP:** `15942812`
- **Modalidade / Ferramentas:** Trabalho **Individual** · LLM **Gemini** (Gem `APOO`) · Diagramas em **PlantUML**
- **Prazo oficial de entrega:** **14 de dezembro de 2026** (arquivo `.zip` único no e-Disciplinas)

---

## Organização desta pasta

Para evitar misturar códigos `.puml`, rascunhos e comparativos *antes/depois* no pacote final enviado à professora, a pasta está dividida em duas áreas:

- [`./Pacote-ZIP/`](./Pacote-ZIP/) — **espelho limpo** do arquivo `.zip` único exigido no e-Disciplinas:
  - [`Relatorio.pdf`](./Pacote-ZIP/Relatorio.pdf) *(39 páginas: Capa + Capítulos 1–7 com Reflexões antes/depois + Apêndices 1–5)*
  - [`Diagramas/`](./Pacote-ZIP/Diagramas/) *(18 diagramas finais em `.png`)*
  - [`Prompts/`](./Pacote-ZIP/Prompts/) *([`00-Gem-APOO-Config.md`](./Pacote-ZIP/Prompts/00-Gem-APOO-Config.md) + `01..06-prompts-*.md`)*
- [`./Projeto_Final_APOO_LLM_Rafael_Feltrim.zip`](./Projeto_Final_APOO_LLM_Rafael_Feltrim.zip) — **pacote `.zip` único** pronto para envio no e-Disciplinas (`3,75 MB`, 26 entradas).
- [`./Desenvolvimento/`](./Desenvolvimento/) — insumos e histórico de iterações usados para montar o relatório e as **Seções de Reflexão**:
  - [`Historias-de-Usuario.md`](./Desenvolvimento/Historias-de-Usuario.md) (`HU01..HU16`) e [`Descricoes-Textuais-UC.md`](./Desenvolvimento/Descricoes-Textuais-UC.md) (`UC01..UC14`)
  - [`PUML/`](./Desenvolvimento/PUML/) (23 arquivos `.puml` validados com `-checkonly`, incluindo [`sequencias/`](./Desenvolvimento/PUML/sequencias/))
  - [`Iteracoes-Antes-Depois/`](./Desenvolvimento/Iteracoes-Antes-Depois/) (imagens *antes/depois* das iterações corretivas)

---

## Checklist de Execução (`Diretrizes` + `Estrutura de relatório`)

| Capítulo / Artefato | Regra Oficial | Diretriz Docente | Status |
| :--- | :--- | :---: | :---: |
| **Capa** | Nome completo + N° USP (`15942812`) | [`Estrutura de relatório`](<../../Material%20de%20Apoio/Estrutura%20de%20relat%C3%B3rio.docx.pdf>) | ✅ Concluído ([`Relatorio.pdf`](./Pacote-ZIP/Relatorio.pdf)) |
| **Cap. 1 — Histórias de Usuário** | Formato *Como / eu quero / para que* (`HU01..HU16`) | [`Projeto Final`](<../../Material%20de%20Apoio/Projeto%20Final%20-%20APOO%20assistido%20por%20LLM.docx.pdf>) | ✅ Concluído ([HUs](./Desenvolvimento/Historias-de-Usuario.md)) |
| **Cap. 2 — Diagrama de Casos de Uso** | Diagrama final + Reflexão antes/depois + Apêndice 1 (`.puml`) | [`Diretrizes §1`](<../../Material%20de%20Apoio/Diretrizes%20-%20APOO%20apoiado%20por%20LLM.docx.pdf>) | ✅ Concluído (`14 UCs · 6 atores`) |
| **Cap. 3 — Descrições Textuais Estendidas** | Todas as descrições (`UC01..UC14`) + Reflexão | `Diretrizes §2` | ✅ Concluído ([Descrições](./Desenvolvimento/Descricoes-Textuais-UC.md)) |
| **Cap. 4 — Diagrama de Componentes** | Diagrama final + Reflexão antes/depois + Apêndice 2 (`.puml`) | `Diretrizes §3` | ✅ Concluído (`8 componentes coesos`) |
| **Cap. 5 — Diagrama de Classes Preliminar** | Apenas atributos (A4 paisagem) + Reflexão + Apêndice 3 (`.puml`) | `Diretrizes §4a` | ✅ Concluído (`18 classes · 0 métodos`) |
| **Cap. 6 — Diagramas de Sequência** | **14 diagramas (1 por UC)** + Auditoria 5 níveis + Apêndice 4 (`.puml`) | `Diretrizes §5` | ✅ Concluído (`70 chamadas · 0 divergências`) |
| **Cap. 7 — Diagrama de Classes Completo** | Atributos **E** métodos (A4 paisagem) + Reflexão + Apêndice 5 (`.puml`) | `Diretrizes §4b` | ✅ Concluído (`18 classes + métodos`) |
| **Empacotamento Final (`.zip`)** | Compactar `Relatorio.pdf`, `Diagramas/*.png` e `Prompts/*.md` até **14/12** | [`Projeto Final`](<../../Material%20de%20Apoio/Projeto%20Final%20-%20APOO%20assistido%20por%20LLM.docx.pdf>) | 📦 Pronto ([`.zip`](./Projeto_Final_APOO_LLM_Rafael_Feltrim.zip)) |
| **Item 4 — Questionário de Esforço/Riscos** | Responder formulário sobre esforço, produtividade e riscos com LLM | [`Projeto Final`](<../../Material%20de%20Apoio/Projeto%20Final%20-%20APOO%20assistido%20por%20LLM.docx.pdf>) | ⏳ Aguardando URL da docente |
