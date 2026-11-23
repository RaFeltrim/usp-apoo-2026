# Registro de Prompts — Etapa 3: Diagrama de Componentes (`PUML`)

> **Diretriz seguida:** Figura 4 de [`Diretrizes - APOO apoiado por LLM.docx.pdf`](<../../../../Material%20de%20Apoio/Diretrizes%20-%20APOO%20apoiado%20por%20LLM.docx.pdf>) (págs. 6–7).  
> **Artefato de entrada no Gem `APOO`:** [`01-casos-de-uso-final.puml`](<../../Desenvolvimento/PUML/01-casos-de-uso-final.puml>).

---

## Iteração 1 — Listagem Inicial de Componentes Candidatos
### Prompt Enviado
> `"A partir do código PlantUML de casos de uso, liste os possíveis componentes (apenas nomes, sem código): <código final do caso de uso>"`

### Resposta da IA (`Gem APOO`)
Listou 10 componentes candidatos, separando `Serviço de Notificações (Integração E-mail/WhatsApp)` e `Adaptador Serviço de Notificações (Sistema Externo)` como dois itens distintos.

---

## Iteração 2 — Diagnóstico e Agrupamento por Coesão
### Diagnóstico Real
Os itens 7 e 10 sobrepunham a mesma responsabilidade de notificações externas, reduzindo a coesão da lista.

### Prompt Corretivo Enviado (Fig. 4)
> `"Agrupe componentes semelhantes e retorne uma nova lista"`

### Resposta da IA (`Gem APOO`)
Consolidou em **8 componentes coesos**: `Portal Web / Interface do Usuário`, `Gestão de Usuários e Autenticação`, `Catálogo de Viagens, Rotas e Frota`, `Reservas, Assentos e Bilhetes`, `Pagamentos e Pós-Venda`, `Monitoramento e Relatórios Gerenciais`, `Plataforma de Pagamento (Sistema Externo)` e `Serviço de Notificações (Sistema Externo)`.

---

## Iteração 3 — Geração do Código PUML sem Relações (`Antes`)
### Prompt Enviado
> `"Baseado da lista de componentes anterior e no código de casos de uso, gere um diagrama de componentes em PUML contendo somente componentes (sem relações)"`

- **Artefato salvo (Antes):** [`02-componentes-v1.puml`](<../../Desenvolvimento/PUML/02-componentes-v1.puml>) → [`02-componentes-antes.png`](<../../Desenvolvimento/Iteracoes-Antes-Depois/02-componentes-antes.png>).

---

## Iteração 4 — Inclusão das Relações entre Componentes (`Depois`)
### Prompt Enviado
> `"Implemente as relações entre componentes no código PUML de componentes. As relações devem seguir exatamente a mesma semântica dos casos de uso"`

### Resultado Final Validado
- **Artefato final:** [`02-componentes-final.puml`](<../../Desenvolvimento/PUML/02-componentes-final.puml>)
- **Comparação (Depois):** [`02-componentes-depois.png`](<../../Desenvolvimento/Iteracoes-Antes-Depois/02-componentes-depois.png>)
- **Entregável ZIP:** [`02-diagrama-componentes.png`](<../Diagramas/02-diagrama-componentes.png>)
- **Validação PlantUML (`-checkonly`):** Exit 0.
