# Registro de Prompts — Etapa 4a: Diagrama de Classes Preliminar (`PUML`)

> **Diretriz seguida:** Figura 5 (Passos 1 a 4) de [`Diretrizes - APOO apoiado por LLM.docx.pdf`](<../../../../Material%20de%20Apoio/Diretrizes%20-%20APOO%20apoiado%20por%20LLM.docx.pdf>) (págs. 7–9).  
> **Artefatos de entrada no Gem `APOO`:** [`01-casos-de-uso-final.puml`](<../../Desenvolvimento/PUML/01-casos-de-uso-final.puml>) e [`02-componentes-final.puml`](<../../Desenvolvimento/PUML/02-componentes-final.puml>).

---

## Iteração 1 — Declaração Isolada das Classes (`Antes`)
### Prompt Enviado
> `"Implemente apenas classes no código PUML de diagrama de classes, sem multiplicidades, relações, atributos e métodos. Faça a implementação baseado no código de casos de uso. Código: <código do casos de uso>"`

### Resposta da IA (`Gem APOO`)
Declarou as 18 classes do domínio (`Usuario`, `Passageiro`, `EmpresaViacao`, `Motorista`, `Administrador`, `Rota`, `Onibus`, `Assento`, `Viagem`, `Reserva`, `Bilhete`, `Pagamento`, `SolicitacaoPosVenda`, `Notificacao`, `Relatorio`, `ConfiguracaoIntegracao`, `GatewayPagamento`, `ServicoNotificacoes`), sem relações, multiplicidades, atributos ou métodos.
- **Artefato salvo (Antes):** [`03-classes-preliminar-v1.puml`](<../../Desenvolvimento/PUML/03-classes-preliminar-v1.puml>) → [`03-classes-antes.png`](<../../Desenvolvimento/Iteracoes-Antes-Depois/03-classes-antes.png>).

---

## Iteração 2 — Heranças entre Classes
### Prompt Enviado
> `"No código anterior, implemente apenas as relações de heranças que ocorrem entre as classes, considerando a semântica de casos de uso e componentes"`

### Resposta da IA (`Gem APOO`)
Adicionou `Passageiro --|> Usuario`, `EmpresaViacao --|> Usuario`, `Motorista --|> Usuario` e `Administrador --|> Usuario`.

---

## Iteração 3 — Relacionamentos e Multiplicidades
### Prompt Enviado
> `"No código anterior, implemente apenas os relacionamentos e multiplicidades (usando skinparam linetype polyline para evitar setas cruzando classes): ..."` *(detalhando as multiplicidades entre EmpresaViacao, Rota, Onibus, Assento, Viagem, Motorista, Passageiro, Reserva, Pagamento, GatewayPagamento, Bilhete, SolicitacaoPosVenda, Notificacao, ServicoNotificacoes, Administrador, ConfiguracaoIntegracao e Relatorio)*

### Resposta da IA (`Gem APOO`)
Adicionou todas as associações, composição (`Onibus *-- Assento`), dependências (`..>`) e multiplicidades coerentes com o domínio.

---

## Iteração 4 — Atributos sem Métodos (`Depois`)
### Prompt Enviado
> `"Implemente no código anterior apenas os atributos de cada classe, considerando características reais da classe"`

### Resultado Final Validado
- **Artefato final:** [`03-classes-preliminar-final.puml`](<../../Desenvolvimento/PUML/03-classes-preliminar-final.puml>)
- **Comparação (Depois):** [`03-classes-depois.png`](<../../Desenvolvimento/Iteracoes-Antes-Depois/03-classes-depois.png>)
- **Entregável ZIP:** [`03-diagrama-classes-preliminar.png`](<../Diagramas/03-diagrama-classes-preliminar.png>)
- **Validação PlantUML (`-checkonly`):** Exit 0. Nenhuma classe possui métodos nesta etapa (conforme Diretriz pág. 9).
