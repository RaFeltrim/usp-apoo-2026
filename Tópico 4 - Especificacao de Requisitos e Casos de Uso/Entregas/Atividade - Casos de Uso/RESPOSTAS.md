# Atividade – Diagrama de Casos de Uso (Plataforma Rodoviária)

## 1. Identificação dos Atores

Os atores representam papéis interagindo com o sistema, podendo ser usuários humanos ou sistemas externos.

- **Passageiro:** Usuário principal que utiliza a plataforma para pesquisar viagens, efetuar a compra de passagens e gerenciar suas reservas online.
- **Empresa de Viação:** Parceira da plataforma. Responsável por fornecer e cadastrar informações de viagens (rotas, horários, preços, ônibus) e gerenciar os cancelamentos, reembolsos e o acompanhamento de vendas.
- **Motorista:** Funcionário da viação. Seu papel é consultar informações sobre as viagens alocadas a ele e visualizar a lista de passageiros.
- **Administrador da Plataforma:** Responsável pela visão macro do negócio. Cuida do gerenciamento geral do sistema, do monitoramento das operações e da geração de relatórios (financeiros e operacionais).
- **Sistema de Pagamento (Ator Externo):** Plataforma terceira responsável por processar as transações financeiras das passagens online.
- **Sistema de Notificações (Ator Externo):** Serviço terceiro (E-mail ou WhatsApp) responsável por enviar alertas, comprovantes e atualizações aos usuários.

---

## 2. Identificação dos Casos de Uso

Abaixo estão listados os principais Casos de Uso agrupados por Atores primários (aqueles que iniciam a ação):

- **Passageiro:**
  - `Pesquisar Viagens`
  - `Comparar Preços e Horários`
  - `Comprar Passagem`
  - `Gerenciar Passagem` (Base para Cancelar, Alterar e Solicitar Reembolso)
  
- **Empresa de Viação:**
  - `Manter Catálogo de Viagens` (inclui cadastro de rotas, horários, preços e ônibus disponíveis)
  - `Acompanhar Vendas`
  - `Gerenciar Cancelamentos e Reembolsos`
  
- **Motorista:**
  - `Consultar Escala de Viagens`
  - `Consultar Lista de Passageiros`
  
- **Administrador da Plataforma:**
  - `Monitorar Operações do Sistema`
  - `Gerar Relatórios` (Base para Relatórios Financeiros e Operacionais)

- **Sistema de Pagamento e Sistema de Notificações** interagem de forma secundária com casos de uso já iniciados (ex: `Efetuar Pagamento Online`).

---

## 3. Relacionamentos (Baixo Acoplamento e Alta Coesão)

Os seguintes relacionamentos de *include*, *extend* e *generalização* foram aplicados para garantir modularidade (coesão) e reaproveitamento de fluxo:

- **Inclusão (`<<include>>`):**
  - **`Comprar Passagem` <<include>> `Efetuar Pagamento Online`**: Não há como finalizar a compra sem passar pelo processamento da plataforma de pagamento.
  - **`Comprar Passagem` <<include>> `Notificar Usuário`**: O fluxo de compra obrigatoriamente aciona o serviço de e-mail/whatsapp.
  - **`Gerenciar Cancelamentos e Reembolsos` <<include>> `Efetuar Reembolso`**: A aprovação do cancelamento por parte da viação aciona o processo financeiro de estorno.

- **Extensão (`<<extend>>`):**
  - **`Comparar Preços e Horários` <<extend>> `Pesquisar Viagens`**: O passageiro pode pesquisar de forma direta, mas tem a *opção* de comparar diferentes viações (cometa, 1001, catarinense) caso deseje.
  - **`Solicitar Reembolso` <<extend>> `Cancelar Passagem`**: É um fluxo condicional, pois nem sempre o passageiro que cancela solicita reembolso via sistema (depende das políticas da passagem).

- **Herança (Generalização):**
  - **Casos de Uso de Gerenciamento de Passagem:** `Cancelar Passagem` e `Alterar Passagem` são casos específicos que herdam de um caso de uso genérico `Gerenciar Passagem`.
  - **Casos de Uso de Relatórios:** `Gerar Relatório Financeiro` e `Gerar Relatório Operacional` herdam do caso genérico `Gerar Relatórios` (ação exclusiva do Administrador).

---

## 4. Diagrama de Casos de Uso (Código-fonte)

Abaixo está o código-fonte UML estruturado em `PlantUML` que representa graficamente a modelagem acima.
*(Instruções para renderizar no diagrams.net: Vá em **Organizar > Inserir > Avançado > PlantUML** e cole o código abaixo).*

```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle

actor Passageiro
actor "Empresa de Viação" as Viacao
actor Motorista
actor "Administrador" as Admin
actor "Sistema de Pagamento" as Pagamento <<System>>
actor "Sistema de Notificações" as Notificacao <<System>>

rectangle "Plataforma Rodoviária" {
  
  ' Casos do Passageiro
  usecase "Pesquisar Viagens" as UC1
  usecase "Comparar Preços e Horários" as UC2
  usecase "Comprar Passagem" as UC3
  usecase "Gerenciar Passagem" as UC4
  usecase "Cancelar Passagem" as UC5
  usecase "Alterar Passagem" as UC6
  usecase "Solicitar Reembolso" as UC7
  
  ' Casos da Empresa
  usecase "Manter Catálogo de Viagens" as UC8
  usecase "Acompanhar Vendas" as UC9
  usecase "Gerenciar Cancelamentos/Reembolsos" as UC10
  usecase "Efetuar Reembolso" as UC11
  
  ' Casos do Motorista
  usecase "Consultar Escala de Viagens" as UC12
  usecase "Consultar Lista de Passageiros" as UC13
  
  ' Casos do Admin
  usecase "Monitorar Operações do Sistema" as UC14
  usecase "Gerar Relatórios" as UC15
  usecase "Gerar Relatório Financeiro" as UC16
  usecase "Gerar Relatório Operacional" as UC17
  
  ' Casos Intermediários de Integração Externa
  usecase "Efetuar Pagamento Online" as UC18
  usecase "Notificar Usuário" as UC19
}

' Ligações Passageiro
Passageiro --> UC1
Passageiro --> UC3
Passageiro --> UC4

' Ligações Empresa
Viacao --> UC8
Viacao --> UC9
Viacao --> UC10

' Ligações Motorista
Motorista --> UC12
Motorista --> UC13

' Ligações Admin
Admin --> UC14
Admin --> UC15

' Relacionamentos Extend e Include
UC2 .> UC1 : <<extend>>
UC7 .> UC5 : <<extend>>

UC3 ..> UC18 : <<include>>
UC3 ..> UC19 : <<include>>
UC10 ..> UC11 : <<include>>

' Heranças
UC5 -up-|> UC4
UC6 -up-|> UC4

UC16 -up-|> UC15
UC17 -up-|> UC15

' Ligações Atores Externos
UC18 <-- Pagamento
UC19 <-- Notificacao

@enduml
```
