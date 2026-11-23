# Registro de Prompts — Etapa 2: Descrições Textuais Estendidas de Casos de Uso

> **Diretriz seguida:** Figura 3 de [`Diretrizes - APOO apoiado por LLM.docx.pdf`](<../../../../Material%20de%20Apoio/Diretrizes%20-%20APOO%20apoiado%20por%20LLM.docx.pdf>) (págs. 5–6).  
> **Artefato de entrada no Gem `APOO`:** [`01-casos-de-uso-final.puml`](<../../Desenvolvimento/PUML/01-casos-de-uso-final.puml>).

---

## Iteração 1 — Lote 1 (`UC01` a `UC07`)
### Prompt Enviado
> `"Considere trechos do código PUML. A especificação textual de casos de uso deve contemplar estritamente todos os atores e relacionamentos."` *(com o trecho PUML de `UC01`–`UC07`, atores e relacionamentos `<<include>>`/`<<extend>>`)*

### Resposta da IA (`Gem APOO`)
Gerou as descrições textuais estendidas de `UC01` a `UC07` com rastreabilidade (`HU01..HU09`), atores primários/secundários, relacionamentos, pré-condições, pós-condições, fluxo principal, fluxos alternativos e fluxos de exceção.

---

## Iteração 2 — Lote 2 (`UC08` a `UC14`)
### Prompt Enviado
> `"Considere trechos do código PUML. A especificação textual de casos de uso deve contemplar estritamente todos os atores e relacionamentos."` *(com o trecho PUML de `UC08`–`UC14`, atores e relacionamentos `<<include>>`/`<<extend>>`)*

### Resposta da IA (`Gem APOO`)
Gerou as descrições textuais estendidas de `UC08` a `UC14` com rastreabilidade (`HU10..HU16`), atores primários/secundários (`Plataforma de Pagamento` em `UC09`), relacionamentos (`UC09 <<include>> UC04`), pré-condições, pós-condições, fluxo principal, fluxos alternativos e fluxos de exceção.

---

## Verificação (Fig. 3 — Cobertura e Coerência)
- Todos os **14 casos de uso (`UC01..UC14`)** foram especificados sem truncamento.
- Todos os atores primários (`Passageiro`, `Empresa de Viação`, `Motorista`, `Administrador da Plataforma`) e secundários (`Plataforma de Pagamento`, `Serviço de Notificações`) estão contemplados.
- Todos os relacionamentos (`UC02 ..> UC01 : <<extend>>`, `UC03 ..> UC04 : <<include>>`, `UC09 ..> UC04 : <<include>>`) estão refletidos nos fluxos.
- **Artefato final:** [`Descricoes-Textuais-UC.md`](<../../Desenvolvimento/Descricoes-Textuais-UC.md>).
