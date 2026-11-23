# Registro de Prompts — Etapa 1: Diagrama de Casos de Uso (`PUML`)

> **Diretriz seguida:** Figura 2 de [`Diretrizes - APOO apoiado por LLM.docx.pdf`](<../../../../Material%20de%20Apoio/Diretrizes%20-%20APOO%20apoiado%20por%20LLM.docx.pdf>) (págs. 2–5).  
> **Base de Conhecimento carregada no Gem `APOO`:** [`Historias-de-Usuario.md`](<../../Desenvolvimento/Historias-de-Usuario.md>) (`HU01` a `HU16`).

---

## Iteração 1 — Atores e Heranças Iniciais
### Prompt Enviado
> `"Gere um código PUML de casos de uso implementando apenas atores, com as relações de herança se houver, considerando as seguintes HUs: HU01, HU02, HU03, HU04, HU05, HU06, HU07, HU08, HU09, HU10, HU11, HU12, HU13, HU14, HU15, HU16"`

### Resposta da IA (`Gem APOO`)
Gerou os atores humanos/organizacionais (`Passageiro`, `Empresa de Viação`, `Motorista`, `Administrador da Plataforma`) herdando de `Usuário`, além dos dois atores externos (`Plataforma de Pagamento <<Sistema Externo>>` e `Serviço de Notificações <<Sistema Externo>>`).

### Verificação
Todos os atores das `HU01..HU16` e suas generalizações foram contemplados corretamente. Nenhum corretivo de ator ausente ou herança foi necessário.

---

## Iteração 2 — Casos de Uso por Ator (Um de Cada Vez)
### 2.1 Ator `Passageiro` (`HU01..HU07`)
> `"No código PUML anterior implemente apenas os casos de uso do ator Passageiro, baseado estritamente nas seguintes HUs: HU01, HU02, HU03, HU04, HU05, HU06, HU07"`

**Resposta da IA:** Adicionou `UC01` (Pesquisar e Comparar Viagens), `UC02` (Selecionar e Reservar Assentos), `UC03` (Efetuar Pagamento Online), `UC04` (Receber Bilhete e Notificações) e `UC05` (Solicitar Cancelamento, Alteração ou Reembolso).

### 2.2 Ator `Empresa de Viação` (`HU08..HU11`)
> `"No código PUML anterior implemente apenas os casos de uso do ator Empresa de Viação, baseado estritamente nas seguintes HUs: HU08, HU09, HU10, HU11"`

**Resposta da IA:** Adicionou `UC06` (Cadastrar e Atualizar Rotas e Horários), `UC07` (Definir Preços e Vincular Ônibus), `UC08` (Acompanhar Vendas de Viagens) e `UC09` (Gerenciar Cancelamentos, Reembolsos e Alterações).

### 2.3 Ator `Motorista` (`HU12..HU13`)
> `"No código PUML anterior implemente apenas os casos de uso do ator Motorista, baseado estritamente nas seguintes HUs: HU12, HU13"`

**Resposta da IA:** Adicionou `UC10` (Consultar Viagens Alocadas) e `UC11` (Consultar Lista de Passageiros).

### 2.4 Ator `Administrador da Plataforma` (`HU14..HU16`)
> `"No código PUML anterior implemente apenas os casos de uso do ator Administrador da Plataforma, baseado estritamente nas seguintes HUs: HU14, HU15, HU16"`

**Resposta da IA:** Adicionou `UC12` (Gerenciar Cadastros e Configurações Globais), `UC13` (Monitorar Operações em Andamento) e `UC14` (Gerar Relatórios Financeiros e Operacionais).

**Artefato salvo (Antes):** [`01-casos-de-uso-v1.puml`](<../../Desenvolvimento/PUML/01-casos-de-uso-v1.puml>) → [`01-uc-antes.png`](<../../Desenvolvimento/Iteracoes-Antes-Depois/01-uc-antes.png>).

---

## Iteração 3 — Diagnóstico e Correção de Relacionamentos (`<<include>>`, `<<extend>>` e Atores Externos)
### Diagnóstico Real
Na versão `v1`:
1. Os atores externos `PlataformaPagamento` e `ServicoNotificacoes` estavam declarados, porém **desconectados** de qualquer caso de uso.
2. Faltavam os relacionamentos `<<include>>` e `<<extend>>` entre os casos de uso (`UC02` estendendo `UC01`, `UC03` incluindo `UC04`, `UC09` incluindo `UC04`).

### Prompt Corretivo Enviado
> `"No código PUML anterior, adicione os relacionamentos de inclusão, extensão e associações com atores externos: UC03 inclui UC04 (pois após o pagamento aprovado o sistema envia o bilhete e notificações via ServicoNotificacoes); UC02 pode estender UC01 (quando o passageiro decide selecionar e reservar assentos após pesquisar viagens); UC09 pode incluir UC04 (quando o processamento de cancelamento/reembolso/alteração notifica o passageiro); além disso, associe PlataformaPagamento a UC03 e UC09 (estorno), e associe ServicoNotificacoes a UC04."`

### Resultado Final Validado
- **Artefato final:** [`01-casos-de-uso-final.puml`](<../../Desenvolvimento/PUML/01-casos-de-uso-final.puml>)
- **Comparação (Depois):** [`01-uc-depois.png`](<../../Desenvolvimento/Iteracoes-Antes-Depois/01-uc-depois.png>)
- **Entregável ZIP:** [`01-diagrama-casos-de-uso.png`](<../Diagramas/01-diagrama-casos-de-uso.png>)
- **Validação PlantUML (`-checkonly`):** Exit 0, 14 casos de uso (`UC01..UC14`) cobrindo `HU01..HU16`.
