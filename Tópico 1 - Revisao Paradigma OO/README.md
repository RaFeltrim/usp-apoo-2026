# Semana 01 — Revisão: O Paradigma Orientado a Objetos

## 🔗 Links e Recursos do e-Disciplinas
- **Seção Moodle:** [Revisão - Programação Orientada a Objetos](https://edisciplinas.usp.br/course/section.php?id=6991976) & [O Paradigma Orientado a Objetos](https://edisciplinas.usp.br/course/section.php?id=6991978)
- **Arquivo da Aula:** [`Aula 01 - O paradigma de orientação a objetos.pdf`](./Material%20de%20Apoio/Aula%2001%20-%20O%20paradigma%20de%20orienta%C3%A7%C3%A3o%20a%20objetos.pdf)

---

## 📖 Estrutura de Tópicos do Módulo

### 1. Paradigma Orientado a Objetos
- Transição do modelo procedural para o modelo baseado em objetos e troca de mensagens.
- Princípio da Abstração e modelagem de entidades do domínio do problema.

### 2. Classes e Objetos
- **Classe:** Molde/estrutura que define atributos (estado) e métodos (comportamento).
- **Objeto:** Instância concreta em memória com identidade e ciclo de vida próprios.

### 3. Encapsulamento
- Ocultamento de detalhes internos de implementação e blindagem de estado.
- Modificadores de visibilidade (`public`, `protected`, `private`, `package-private`).
- Preservação de invariantes de classe através de métodos de acesso e mutação controlados.

### 4. Herança e Polimorfismo — Parte 1
- **Herança:** Reuso e extensão de atributos e métodos entre superclasses e subclasses.
- **Polimorfismo:** Sobrescrita (*method overriding*) e despacho dinâmico de métodos em tempo de execução.

### 5. Herança e Polimorfismo — Parte 2: Interfaces e Classes Abstratas
- **Classes Abstratas:** Classes que não podem ser instanciadas diretamente e servem de base conceitual para subclasses especializadas.
- **Interfaces:** Contratos de comportamento estritos que garantem desacoplamento e suporte a múltiplos tipos de implementação sem dependência de hierarquia rígida de herança.
- **Princípio:** *"Favoreça composição sobre herança"*.

---

## 🎯 Métricas de Qualidade de Design
- **Alta Coesão:** Cada classe deve ser focada em uma única responsabilidade.
- **Baixo Acoplamento:** Módulos devem depender de abstrações (interfaces/classes abstratas) e não de implementações concretas.
