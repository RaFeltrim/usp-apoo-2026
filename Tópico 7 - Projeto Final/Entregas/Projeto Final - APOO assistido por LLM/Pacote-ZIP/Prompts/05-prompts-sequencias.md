# Registro de Prompts — Etapa 5: Diagramas de Sequência (`PUML`)

> **Diretriz seguida:** Figura 6 e Tabela de Validação em 5 Níveis de [`Diretrizes - APOO apoiado por LLM.docx.pdf`](<../../../../Material%20de%20Apoio/Diretrizes%20-%20APOO%20apoiado%20por%20LLM.docx.pdf>) (págs. 9–12).  
> **Artefatos de entrada no Gem `APOO`:** `Historias-de-Usuario.md`, `01-casos-de-uso-final.puml`, `02-componentes-final.puml` e `03-classes-preliminar-final.puml`.

---

## Iteração 1 — Identificação das Unidades Comportamentais (Passo 1)
### Prompt Enviado
> `"Para o sistema Plataforma ClickBus, identifique as unidades de comportamento que devem ser representadas nos diagramas de sequência. A especificação comportamental pode ser dividida em unidades que não precisam corresponder a casos de uso independentes, podendo representar etapas internas de um único cenário. Considere estritamente os requisitos (HUs) e o código PUML de casos de uso"`

### Resposta da IA (`Gem APOO`)
Identificou **14 unidades comportamentais (`SD-UC01` a `SD-UC14`)** correspondendo 1-a-1 aos casos de uso `UC01..UC14`, com `SD-UC04` modelada como sub-interação reutilizável (`ref` com `gate`) invocada por `SD-UC03` e `SD-UC09`.

---

## Iteração 2 — Participantes Candidatos e Mapeamento de Responsabilidades (Passos 2 e 3)
### Prompts Enviados
> 1. `"Neste sistema, baseado na especificação comportamental estruturada e nos diagramas PUML de componentes e classes, identifique os elementos que colaboram para realizar cada unidade comportamental, mapeando o conjunto de participantes candidatos para cada unidade comportamental"`
> 2. `"Baseado nas unidades comportamentais, participantes candidatos, diagrama de classes e responsabilidades dos componentes, determine quais participantes possuem as responsabilidades necessárias para executar cada unidade comportamental, gerando um mapeamento entre comportamentos, classes, métodos e componentes. Seja restrito à semântica que foi passada anteriormente"`

### Resposta da IA (`Gem APOO`)
Mapeou todas as 14 unidades às 18 classes do modelo preliminar, especificando os métodos e parâmetros em cada classe receptora.

---

## Iteração 3 — Colaborações, Sequência Temporal e Código PUML em Lotes (Passos 4, 5 e 6)
### Prompts Enviados (4 lotes: `UC01–UC04`, `UC05–UC08`, `UC09–UC11`, `UC12–UC14`)
> `"Estrito na especificação comportamental, nos participantes identificados e no mapeamento de responsabilidades e operações, determine como os participantes devem colaborar em cada unidade comportamental, estabeleça a sequência temporal das interações e as condições que controlam sua execução, e produza um diagrama de sequência em código PUML validado considerando diferentes níveis."`

---

## Iteração 4 — Diagnóstico e Correção na Validação em 5 Níveis
### Diagnóstico Real
1. **Nível Comportamental/Sintático em `SD-UC04`:** Na primeira versão (`seq-UC04-v1.puml`), o participante `u : Usuario` era ativado sem mensagem de entrada e enviava o resultado de volta a `n : Notificacao` sem um ponto de entrada (`gate`) claro para o `ref`.
2. **Ação Corretiva:** Adicionado o `gate` de entrada `[-> Notificacao : dispararNotificacao(usuario, canal, conteudo)` e retorno `[<-- Notificacao : resultadoEnvio`, com `Notificacao` consultando `Usuario.obterContatoPreferencial()`.
3. **Verificação nos 5 Níveis (pág. 11):**
   - **Sintático:** 14/14 arquivos `.puml` aprovados em `plantuml.jar -checkonly -charset UTF-8` (exit 0) e zero colchetes `[...]` manuais em `alt`/`opt`/`loop`/`else`.
   - **Estrutural:** Todos os objetos pertencem às 18 classes modeladas e todas as chamadas correspondem aos métodos consolidados para a Etapa 4b.
   - **Arquitetural:** Fluxos respeitam os limites dos 8 componentes e integrações externas (`GatewayPagamento`, `ServicoNotificacoes`).
   - **Comportamental:** Condições `alt`/`opt`/`loop` e `ref` refletem os fluxos principais, alternativos e de exceção de `Descricoes-Textuais-UC.md`.
   - **Rastreabilidade:** Cobertura 100% de `HU01..HU16` e `UC01..UC14`.

- **Comparação Antes/Depois:** [`05-seq-UC04-antes.png`](<../../Desenvolvimento/Iteracoes-Antes-Depois/05-seq-UC04-antes.png>) vs [`05-seq-UC04-depois.png`](<../../Desenvolvimento/Iteracoes-Antes-Depois/05-seq-UC04-depois.png>).
- **Entregáveis ZIP:** `Pacote-ZIP/Diagramas/05-seq-UC01..UC14-*.png`.
