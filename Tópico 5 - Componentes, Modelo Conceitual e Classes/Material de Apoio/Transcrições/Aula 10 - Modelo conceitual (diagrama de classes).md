# Aula 10 - Modelo conceitual (diagrama de classes)

> **Fonte:** `Aula 10 - Modelo conceitual (diagrama de classes).mp4` (mantido localmente em `../Vídeos/`, fora do git)  
> **Duração:** 15m12s (`912s`)  
> **Nota metodológica:** Transcrição automática gerada com `faster-whisper` (modelo `small`, `beam_size=1`, CPU). Pode conter ruídos de reconhecimento de fala (ASR). As seções de análise abaixo identificam explicitamente as interpretações e correções de termos ASR (ex.: *"sequiele"* → SQL; *"desenvolvimento oriental modelos"* → Desenvolvimento Orientado a Modelos / MDD; *"adquisição"* → aquisição); a seção final preserva a transcrição bruta **verbatim**.  
> **Limitação visual:** Esta transcrição cobre apenas a faixa de áudio. Diagramas de classes completos, cores de fronteira entre componentes, multiplicidades e setas desenhadas em tela sem leitura verbal integral podem não estar detalhados no áudio — complemente o estudo com [`modelo-conceitual-biblioteca.puml`](../modelo-conceitual-biblioteca.puml) e [`codigo-modelo-conceitual-biblioteca.pdf`](../codigo-modelo-conceitual-biblioteca.pdf).

---

## Resumo executivo

A videoaula consolida o conceito de **Modelo Conceitual** do sistema como a integração e o refinamento dos diagramas de classes derivados de cada componente arquitetural (como *Acervo*, *Empréstimo* e *Usuários* no estudo de caso da Biblioteca). Mais do que registrar classes, atributos e relacionamentos de domínio, o modelo conceitual cumpre papel estratégico na engenharia de software: fornece vocabulário comum entre stakeholders e desenvolvedores, permite estimar tamanho, complexidade e esforço de implementação, subsidia a divisão de tarefas entre equipes, serve de base para derivar o esquema relacional de banco de dados (SQL) e sustenta abordagens de Desenvolvimento Orientado a Modelos (MDD). Ao unir os diagramas parciais de componentes, classes compartilhadas nas interseções confirmam e refinam as dependências arquiteturais no diagrama de componentes.

---

## Conceitos-chave (definição + exemplo citado na aula)

| Conceito | Definição / Papel | Exemplo citado na aula (Sistema de Biblioteca) |
| :--- | :--- | :--- |
| **Modelo Conceitual** | Visão integrada dos conceitos do domínio (classes, atributos, relacionamentos e multiplicidades) obtida pela união e refinamento dos diagramas dos componentes. | União dos submodelos de *Acervo*, *Empréstimo* e *Usuários* em um único diagrama global da Biblioteca. |
| **Herança Simples e Múltipla** *(ASR: "herança múltiple", "Herdan")* | Subclasses herdam **não apenas atributos**, mas **também todos os relacionamentos** definidos na superclasse. Na herança múltipla, uma subclasse especializa mais de uma superclasse. | `Livro` e `Artigo` especializam `PublicacaoSeriada`, herdando suas ligações com `Autor`, `Localizacao`, `Estado` e `RegistroEmprestimo`; `Professor` e `Estudante` envolvendo `Usuario` / `UsuarioUSP`. |
| **Composição (`◆─`)** | Todo-parte forte com dependência de ciclo de vida: a existência/significado da parte está acoplado ao todo. | `Biblioteca` ◆─ `Acervo`; `Aquisicao` ◆─ `TipoAquisicao` (Doação/Compra); relação forte entre `PublicacaoSeriada` e `Autor` destacada na modelagem do exemplo. |
| **Agregação (`◇─`)** | Todo-parte mais fraca na qual as partes podem existir ou ser referenciadas independentemente do agrupador. | `Acervo` ◇─ `PublicacaoSeriada`; `Aquisicao` ◇─ `Usuario`; `RegistroEmprestimo` ◇─ `Usuario`. |
| **Associação Simples e Múltiplos Relacionamentos** | Ligação estrutural entre classes independentes; um mesmo par de classes pode possuir mais de uma associação com papéis distintos. | Associação entre `Atendente` e `RegistroEmprestimo`; múltiplos vínculos no domínio entre usuários, registros e publicações. |
| **Derivação para Banco de Dados (SQL / ER)** *(ASR: "sequiele")* | Tradução estrutural do modelo conceitual orientado a objetos para modelo entidade-relacionamento e tabelas SQL (classes → tabelas, atributos → colunas, associações → chaves/tabelas de ligação). | Mapeamento das classes e relacionamentos da Biblioteca para o esquema relacional de persistência. |
| **Desenvolvimento Orientado a Modelos (MDD)** *(ASR: "desenvolvimento oriental modelos")* | Uso do modelo conceitual rigoroso como artefato primário para geração semiautomática ou automática de esqueletos de código e persistência. | Geração de estrutura inicial de classes e tabelas a partir do diagrama unificado da Biblioteca. |
| **Retroalimentação Arquitetural (Classes de Interseção)** | Classes usadas por mais de um componente evidenciam acoplamentos que precisam estar refletidos como dependências no diagrama de componentes. | `Usuario` (pertencente a *Usuários*, usado em *Empréstimo* e *Acervo*) e `PublicacaoSeriada` (de *Acervo*, usada em *Empréstimo*). |

---

## Passo a passo / método ensinado

1. **Partir dos diagramas de classes locais de cada componente:** após identificar as classes internas de cada componente (tema da videoaula 1), reunir os fragmentos em uma visão única.
2. **Unificar classes repetidas (interseções entre componentes):** identificar entidades que aparecem em múltiplos componentes (ex.: `Usuario`, `PublicacaoSeriada`) para evitar duplicação conceitual.
3. **Refinar associações e hierarquias:**
   - Verificar **herança** (inclusive múltipla quando cabível) garantindo que associações comuns fiquem na superclasse para serem herdadas pelas subclasses.
   - Distinguir **associação simples**, **agregação** e **composição** conforme a dependência de ciclo de vida no domínio.
   - Checar **multiplicidades** e eventuais **múltiplos relacionamentos** entre o mesmo par de classes.
4. **Retroalimentar o Diagrama de Componentes:** ao observar classes de um componente referenciadas por outro, confirmar se as interfaces/dependências no diagrama arquitetural de componentes estão consistentes.
5. **Usar o Modelo Conceitual como artefato de projeto:** derivar estimativas de esforço, particionar módulos entre membros da equipe, projetar o esquema de banco de dados (ER/SQL) e preparar a base para detalhamento dinâmico (Diagrama de Sequências com métodos).

---

## Pontos que impactam o projeto e a prova

- **Herança propaga relacionamentos (pegadinha clássica de prova):** em questões de leitura de diagrama de classes ou modelo conceitual, lembre-se de que uma subclasse (`Livro`, `Artigo`) **herda todas as associações da superclasse** (`PublicacaoSeriada`), não devendo redesenhar ligações redundantes na subclasse sem motivo de especialização.
- **Conexão direta com Arquitetura de Componentes:** modelo conceitual não nasce isolado; classes compartilhadas entre submodelos são a justificativa técnica para setas de dependência entre componentes na arquitetura.
- **Conexão com Persistência e Entrega de Sequências:** assim como a aula mostra classes conceituais servindo de base para tabelas SQL, na atividade de Diagrama de Sequências o modelo ganha classes de controle, interface e acesso a banco (como `VendasDatabase`), além das operações/métodos nas classes de domínio.
- **Terminologia rigorosa:** saber distinguir graficamente e semanticamente associação simples, agregação (`◇─`), composição (`◆─`), generalização/especialização (`▷─`) e os propósitos gerenciais/técnicos do modelo conceitual (vocabulário comum, estimativa, divisão de trabalho, mapeamento relacional, MDD).

> *Nota de interpretação ASR:* Na transcrição bruta abaixo, expressões como *"sequiele"* correspondem a **SQL**, *"desenvolvimento oriental modelos"* / *"basada em modelos"* correspondem a **Desenvolvimento Orientado a Modelos (MDD)**, *"adquisição"* corresponde a **aquisição**, *"modelo conceitado"* corresponde a **modelo conceitual**, *"Herdan"*/*“herdada”* correspondem a **herdam**/**herdar de**, e *"intersetados"* corresponde a **intersectados**.

---

## Transcrição completa (com timestamps)

```text
[00:00:01] Já definimos os elementos internos dos componentes,
[00:00:07] do componente especificamente o componente de acervo,
[00:00:11] mas como vimos na definição da arquitetura,
[00:00:15] do elemento da arquitetura,
[00:00:17] componente de acervo não é o único componente que vai ser parte da arquitetura,
[00:00:22] então é necessário trabalharmos também os outros componentes
[00:00:28] e começar a identificar as classes que vão estar envolvidas nesses componentes,
[00:00:34] as relações entre as classes, os atributos dessas classes,
[00:00:38] o tipo de relacionamento, se vai ser agregação, composição, etc.
[00:00:43] E a junção de todas essas classes,
[00:00:48] esse elemento de todos os componentes,
[00:00:51] ela vai ser considerada o modelo conceitual do nosso sistema, por quê?
[00:00:56] Porque vai modelar o nosso sistema em termos de conceitos interrelacionados entre eles.
[00:01:03] Então conceitos são classes, conceitos são atributos,
[00:01:06] conceitos são as relações entre eles, as multiplicidades entre eles.
[00:01:13] Então a gente, juntando esses modelos de classes,
[00:01:20] de todos os componentes, vamos ter uma visão geral
[00:01:24] do modelo conceitado no nosso sistema,
[00:01:28] vamos ter uma visão geral do tamanho do sistema,
[00:01:33] da complexidade do sistema,
[00:01:35] porque quantas classes vão ser necessárias para se envolver,
[00:01:39] quantas relações, interações entre elas vão ser necessárias
[00:01:43] e considerar o tamanho também de cada classe,
[00:01:49] dependendo da quanta de atributos de cada classe,
[00:01:53] também entra em jogo quando a gente está tentando estimar
[00:01:57] a complexidade e o tempo de desenvolvimento do sistema.
[00:02:02] Então, além de ajudar com isso o modelo conceitual,
[00:02:06] nos ajuda a ter uma terminologia comum
[00:02:11] em relação a que todos os stakeholders vão entender
[00:02:17] os conceitos que envolvem o sistema, como tudo,
[00:02:20] baseado nesse modelo conceitual,
[00:02:23] já a gente vai ter essa maneira como aceitou,
[00:02:27] como base para discutirmos a evolução do sistema,
[00:02:32] a estrutura do sistema, a divisão,
[00:02:37] por exemplo, a divisão de grupos de classes
[00:02:42] para ser desenvolvidos pelos desenvolvedores,
[00:02:46] etc.
[00:02:49] Esse modelo conceitual também pode ser utilizado
[00:02:52] como base para definição do modelo entidade e relacionamento
[00:02:57] antes de começarmos a codificar toda a partir base de dados do sistema.
[00:03:03] Então, muitas das entidades,
[00:03:07] muitos dos elementos tipo das classes que a gente identificou
[00:03:13] para cada componente, muitas delas vão virar
[00:03:18] tabelas na base de dados,
[00:03:22] a gente está falando de uma linguagem sequiele,
[00:03:25] de um modelo sequiele.
[00:03:29] Os atributos dessas classes
[00:03:33] também vão virar atributos das tabelas
[00:03:36] no modelo sequiele, etc.
[00:03:38] Então, esse modelo conceitual é muito importante,
[00:03:43] porque já estamos estruturando os dados do nosso sistema.
[00:03:51] E também, se, por exemplo, a empresa ou a equipe de desenvolvimento
[00:03:56] tem uma pegada de desenvolvimento oriental modelos,
[00:03:59] que é uma abordagem que algum das empresas da indústria
[00:04:05] está realizando, que ajuda na automação
[00:04:08] de codificação basada em modelos,
[00:04:11] então, esse modelo conceitual também ajudará
[00:04:15] a instanciar essas classes e gerar código mais automaticamente
[00:04:21] e a se evitar ou diminuir o tempo de desenvolvimento.
[00:04:26] Então, esse conceito de desenvolvimento oriental
[00:04:30] modelo ser bem interessante e recomendo vocês dar uma olhadinha
[00:04:34] em relação, pelo menos, a definição desse conceito.
[00:04:42] Nesse caso, no caso do nosso sistema de biblioteca,
[00:04:46] esse seria o modelo conceitual.
[00:04:52] Então, vemos aqui que já temos classes que não foram identificadas,
[00:04:59] classes que vão além do componente de acervo,
[00:05:02] esse modelo conceitual já tem as classes vindas
[00:05:06] dos outros, do projeto interno dos outros componentes,
[00:05:10] do componente de empréstimo e o componente de usuários.
[00:05:16] E aqui já refinamos, refatoramos os relacionamentos,
[00:05:21] identificamos tipo de relacionamentos
[00:05:24] de associações mais específicas, como agregação,
[00:05:28] essa daqui é composição, temos a herança aqui nessa parte,
[00:05:33] aqui também é herança.
[00:05:36] Temos associações simples, que somente é tipo...
[00:05:42] diz que estão relacionados de alguma forma,
[00:05:45] mas não foi identificado, não foi especializado
[00:05:49] em algum tipo de relacionamento mais concreto
[00:05:53] com a composição, agregação, herança.
[00:05:55] Mas mantemos uma associação entre classes,
[00:06:00] também é possível manter uma associação simples entre classes.
[00:06:09] Por exemplo, aqui temos o conjunto de usuários,
[00:06:12] que têm herança múltiple,
[00:06:14] o estudante tem herança múltiple,
[00:06:16] o professor tem herança múltiple,
[00:06:18] relação aos usuários.
[00:06:20] Temos que, por exemplo, a classe adquisição,
[00:06:25] ela vai estar obrigatoriamente composta
[00:06:29] por um tipo de adquisição,
[00:06:31] esse tipo de adquisição pode ser doação ou compra,
[00:06:35] uma adquisição pode ser doação ou compra,
[00:06:39] aqui essa relação de composição,
[00:06:43] no momento em que não existe essa classe de adquisição,
[00:06:46] a classe de adquisição perde o sentido,
[00:06:50] porque ela somente faz sentido
[00:06:53] quando faz parte da classe adquisição.
[00:06:57] Então, aqui estamos aplicando o conceito de composição.
[00:07:01] Agora, adquisição tem um relacionamento de agregação
[00:07:07] com a classe usuária, ou seja,
[00:07:11] adquisição precisa de informações vindas
[00:07:16] da classe de usuário,
[00:07:18] mas no caso da classe adquisição não existir,
[00:07:21] a classe usuária faz sentido-se e é necessária,
[00:07:24] pois ela é uma classe mãe,
[00:07:28] vamos falar de uma superclase,
[00:07:30] do estudante e professor, o usuário externo,
[00:07:34] e ao mesmo tempo, o usuário, a classe usuária,
[00:07:38] agrega informações para a classe de registro de empréstimos.
[00:07:44] Então, aqui é uma coisa interessante da classe adquisição,
[00:07:48] é que ela tem dois tipos de relacionamentos,
[00:07:53] que ela tem um relacionamento de composição
[00:07:56] com a classe tipo de adquisição
[00:07:58] e tem um relacionamento de agregação
[00:08:00] com a classe de usuário.
[00:08:03] Então, também é impossível
[00:08:06] uma classe estar relacionada
[00:08:10] com outra de diferentes formas.
[00:08:13] Aqui temos a relação de herança entre livro, artigo
[00:08:21] e publicação seriada.
[00:08:23] A publicação seriada,
[00:08:25] a superclase é uma classe mãe,
[00:08:29] ou seja, o livro e o artigo,
[00:08:32] além de ter essas características,
[00:08:34] essas propriedades específicas da classe,
[00:08:37] eles também vão herdar,
[00:08:39] ou seja, eles também vão ter por obrigação
[00:08:42] essas propriedades da classe de publicação seriada.
[00:08:46] A publicação seriada,
[00:08:48] igualmente ela vai ter relacionamentos
[00:08:52] com outras classes como autor.
[00:08:56] Uma publicação vai ter um autor,
[00:08:59] no mínimo um autor.
[00:09:04] E, aqui é interessante, porque o autor,
[00:09:09] se não existir a publicação seriada,
[00:09:12] o autor não faz sentido existir,
[00:09:14] pois não contesta o sistema,
[00:09:16] porque ele não vai ser utilizado por outras classes.
[00:09:20] Por isso que foi definido
[00:09:23] o relacionamento de composição entre autor
[00:09:27] e publicação seriada.
[00:09:29] Agora, localização,
[00:09:32] ele faz sentido,
[00:09:38] ele existe na publicação seriada,
[00:09:45] uma publicação seriada tem uma localização
[00:09:50] especificamente,
[00:09:52] uma publicação seriada tem um estado,
[00:09:55] esse estado é emprestado,
[00:09:58] ou é reservado,
[00:10:00] ou é disponível, por exemplo.
[00:10:05] Essa publicação seriada,
[00:10:08] ela complementa informações do acervo.
[00:10:13] O acervo faz parte da biblioteca,
[00:10:16] uma biblioteca,
[00:10:18] um acervo simibiloteca não faz sentido,
[00:10:21] por isso é composição.
[00:10:24] E, aqui, ao mesmo tempo,
[00:10:26] uma coisa interessante,
[00:10:28] que quando as classes,
[00:10:33] quando as classes estão herdando,
[00:10:39] aqui, o livro artigo Herdan da publicação seriada,
[00:10:43] ela não somente está herdando os atributos,
[00:10:46] mas está meio relacionamento
[00:10:48] com as outras classes.
[00:10:50] Então, o livro, por herdada publicação seriada,
[00:10:53] o livro também vai herdar
[00:10:55] esse relacionamento com o autor.
[00:10:59] Então, o livro vai ter, pelo menos,
[00:11:02] um ou muitos autores.
[00:11:06] O livro vai ter um estado,
[00:11:09] o livro vai ter uma localização.
[00:11:12] Então, a herança,
[00:11:14] não é herança somente de esquerda,
[00:11:16] são as que estão aqui,
[00:11:18] ou as propriedades que estão na classe mãe,
[00:11:20] mas também herda
[00:11:22] o relacionamento da classe mãe
[00:11:25] com outras classes.
[00:11:28] O livro, por herdada publicação seriada,
[00:11:30] também vai ser parte do registro de empréstimo,
[00:11:34] igualmente o artigo,
[00:11:36] vai ser parte do registro de empréstimo.
[00:11:39] E o atendente realiza o registro,
[00:11:46] e aqui o atendente é uma relação simples,
[00:11:49] uma associação simples.
[00:11:54] Não tem uma relação mais específica,
[00:11:56] tipo herança, agregação,
[00:11:58] composição, porque não faz sentido
[00:12:00] para o tipo de relacionamento entre essas duas classes.
[00:12:04] Então, de forma geral,
[00:12:06] essa seria a nossa primeira versão do modelo
[00:12:09] conceitado no nosso sistema.
[00:12:13] E uma coisa importante
[00:12:16] é que as classes
[00:12:21] têm classes que vão ser utilizadas
[00:12:25] por diversas componentes,
[00:12:30] vai ser parte do modelo de diversos componentes.
[00:12:36] E essas interseções, por exemplo,
[00:12:40] essas classes em azul,
[00:12:42] que são subconjunto de classes em azul,
[00:12:45] são da responsabilidade
[00:12:48] do componente de usuário.
[00:12:53] Mas o componente de empréstimo
[00:12:56] vai ter que considerar algumas classes de usuário.
[00:13:02] Então, nesse sentido,
[00:13:05] é necessário, ou se faz um relacionamento
[00:13:11] entre componentes de empréstimo e componentes de usuário,
[00:13:15] que no nosso modelo da arquitetura já existia.
[00:13:18] Então, o relacionamento já se faz mais concreto aqui,
[00:13:21] entre esses dois componentes,
[00:13:23] pois vai ser em relação as informações relacionadas aos usuários,
[00:13:28] que o componente de empréstimo
[00:13:30] vai ter que utilizar.
[00:13:34] Igualmente, para a parte do modelo
[00:13:39] de classes internos do componente de acervo,
[00:13:43] que está em verde, então temos duas partes aqui,
[00:13:46] vamos ter classes que intersectam
[00:13:51] entre componentes.
[00:13:54] Então, por exemplo, para componentes de acervo,
[00:13:58] vamos precisar informações da publicação
[00:14:03] de empréstimo, vamos precisar informações da publicação seriada,
[00:14:08] mas essa publicação seriada está baixa a responsabilidade do acervo.
[00:14:14] Então, vai ter que ter um relacionamento entre acervo e empréstimo
[00:14:20] na nossa arquitetura,
[00:14:24] que vai ser informações sobre a publicação seriada.
[00:14:27] É igualmente aqui.
[00:14:29] Então, os componentes acervo e empréstimo,
[00:14:36] pelo fato de estar intersetados aqui com essas classes de usuário,
[00:14:41] vai ter que ter uma relação,
[00:14:45] os componentes de empréstimo e acervo
[00:14:47] vão ter que ter uma relação com o componente de usuário
[00:14:49] na nossa arquitetura também.
[00:14:51] Então, esse modelo de conceitual também ajuda a identificar
[00:14:55] algumas relações que a gente estava e esqueceu
[00:14:58] ou não percebeu no momento de definir a arquitetura
[00:15:01] e que podem ser refinadas
[00:15:04] assim que a gente tiver mais estruturado os conceitos do nosso sistema.
```
