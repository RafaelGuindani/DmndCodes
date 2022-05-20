duvida01 = input("Defina Modelagem Conceitual\n>:")
print("\nEste é o modelo de mais alto nível, ou seja, que está mais próximo dos usuários."
     "\nO nível conceitual é desenvolvido com alto nível de abstração, a partir dos requisitos"
     "\ndo sistema, extraídos na fase de levantamento de requisitos pelos analista de sistemas."
     "\nEsse modelo pode ser elaborado de forma textual ou por meio de dois diagramas: "
     "\nDiagramade Entidade e Relacionamento e/ou Diagrama de Classes*.")

duvida02 = input("Defina Modelagem Lógica\n>:")
print("\nEste modelo descreve como os dados serão armazenados no banco de dados e"
      "\ntambém seus relacionamentos. Neste modelo ainda pode ser definida a tecnologia"
      "\nque será utilizada para armazenagem dos dados:"
      "\nBancos de Dados Relacionais ou Bancos de Dados Não Relacionais")

duvida03 = input("Defina Modelagem Física\n:>")
print("\nTambém chamado de Modelo de Implementação, descreve, por meio de alguma"
      "\nlinguagem(comumente SQL), como será feita a armazenagem do banco. "
      "\nNeste nível se escolhe qual Sistema Gerenciador de Banco de Dados (SGBD)"
      "\nserá utilizado,levando em consideração o modelo lógico adotado.")

duvida04 = input("Explique a Cardinalidade Máxima e Mínima entre relações\n>:")
print("\nCardinalidade (Máxima):"
      "\nDefine a quantidade máxima de ocorrências de uma entidade que poderá"
      "\nestar associada a outra entidade."
      "\nPor exemplo: - Um vendedor pode vender apenas um tipo de produto? Ou dois? Ou três?"
      "\nUm produto pode ser vendido por apenas um vendedor? Ou por todos?")

print("\nCardinalidade (Mínima):"
      "\nDefine a quantidade mínima de ocorrências de uma entidade que precisa"
      "\nestar associada a outra entidade (em caráter obrigatório)."
      "\nSão consideradas como cardinalidades mínimas: 0 e 1"
      "\nSão presentadas por: 0..1, 1..1, 0..n, 1..n, o..*, 1..*, etc ")

print("\nDefine a quantidade mínima de ocorrências de uma entidade que precisa"
      "\nestar associadaaoutra entidade (em caráter obrigatório).")

print("\nModelagem Conceitual, Lógica e Física Se fossemos resumir..."
      "\nDo Negócio:"
      "\nModelo de tarefa do usuário - Definição de regras e tecnologia:"
      "\nRelatório descritivo do processo da tarefa do ponto de vista do usuário"
      "\nModelo Conceitual - Regras de negócio:"
      "\nFerramentas ou objetos, propriedades técnicas, processos, mapeamento do dominio do usuário."
      "\nModelo lógico - Definição de regras e tecnologia:"
      "\nDefinição de dados, funções e projeto de regras."
      "\nModelo Físico - Implementação:"
      "\nPode representar tanto o projeto como a própria interface gráfica,"
      "\no banco de dados e os programas.")

duvida05 = input("O que é a Normalização de Dados?\n>:")
print("\nNormalização de Dados"
      "\nChamamos de normalização de dados o processo formal e passo a passo"
      "\nque examina o documento descritivo gerado pelos analistas de sistemas"
      "\ndurante a análise de requisitos em busca de definir as"
      "\nentidades, atributos, relacionamentos, chaves primárias e chaveses trangeiras"
      "\ndo banco de dados a ser modelado."
      "\nEste processo é realizado utilizando regras bem estabelecidas "
      "\nconhecidas como Formas Normais definidas por Edgar Frank Codd em seu artigo."
      "\nUm dos objetivos principais da normalização é evitar ou pelo menos amenizar"
      "\nanomalias e inconsistências que podem ocorrer durante a"
      "\ninclusão, exclusão, alteração e consulta de registros em um banco de dados."
      "\nUm banco de dados normalizado dentro dos padrões reduz o trabalho de manutenção e ajuda"
      "\na evitar o desperdício do espaço de armazenamento, dentre outros benefícios.")

duvida06 = input("Defina a Primeira Forma Normal:\n:>")
print("\nPrimeira Forma Normal (1FN)"
      "\nNesta forma os atributos precisam ser atômicos, o que significa que as tabelas"
      "\nnão podem ter valores repetidos e nem atributos possuindo mais de um valor."
      "\nExemplo: CLIENTE = {ID + ENDEREÇO + TELEFONES}."
      "\nPorém, uma pessoa poderá ter mais de um número de telefone, sendo assim"
      "\no atributo |TELEFONES| é multivalorado."
      "\nPara normalizar, é necessário:"
      "\nIdentificar a chave primária e também a coluna que possui dados repetidos"
      "\nnesse exemplo |TELEFONES| e removê-los;"
      "\nConstruir uma outra tabela com o atributo em questão, no caso |TELEFONES|."
      "\nMas não se esquecendo de fazer uma relação entre as duas tabelas:"
      "\nCLIENTE = {ID + ENDEREÇO} e TELEFONE (nova tabela) = {CLIENTE_ID (chave estrangeira) + TELEFONE}.")

duvida07 = input("Defina a Segunda Forma Normal\n>:")
print("\nSegunda Forma Normal (ou 2FN)."
      "\nPrimeiramente, para estar na 2FN é preciso estar também na 1FN."
      "\n2FN define que os atributos normais, ou seja, os não chave, devem depender"
      "\nunicamente da chave primária da tabela."
      "\nAssim como as colunas da tabela que não são dependentes dessa chave devem ser removidas"
      "\nda tabela principal e cria-se uma nova tabela utilizando esses dados."
      "\nExemplo: PROFESSOR_CURSO = {ID_PROF + ID_CURSO + SALARIO + DESCRICAO_CURSO}"
      "\nComo podemos observar, o atributo |DESCRICAO_CURSO| não depende unicamente da chave primária"
      "\nID_PROF, mas sim somente da chave ID_CURSO."
      "\nPara normalizar, é necessário:"
      "\nIdentificar os dados não dependentes da chave primária (nesse exemplo DESCRICAO_CURSO)"
      "\ne removê-los."
      "\nConstruir uma nova tabela com os dados em questão:"
      "\nPROFESSOR_CURSO = {ID_PROF + ID_CURSO + SALARIO} e"
      "\nCURSOS (nova tabela) = {ID_CURSO + DESCRICAO_CURSO}.")

duvida08 = input("Defina a Terceira Forma Normal\n>:")
print("\nTerceira Forma Normal (ou 3FN)."
      "\nssim como para estar na 2FN é preciso estar na 1FN,"
      "\npara estar na 3FN é preciso estar também na 2FN."
      "\n3FN define que todos os atributos dessa tabela devem ser funcionalmente independentes"
      "\nuns dos outros, ao mesmo tempo que devem ser dependentes exclusivamente da chave primária"
      "\nda tabela. 3FN foi projetada para melhorar o desempenho de processamento dos banco de dados"
      "\ne minimizar os custos de armazenamento."
      "\nExemplo: FUNCIONARIO = {ID + NOME + VALOR_SALARIO + VALOR_FGTS}."
      "\nComo sabemos o valor do FGTS é proporcional ao salário,"
      "\nlogo o atributo normal VALOR_FGTS é dependente do também atributo normal VALOR_SALARIO."
      "\nPara normalizar, é necessário: Identificar os dados dependentes de outros"
      "\n(nesse exemplo VALOR_FGTS)"
      "\nRemovê-los da tabela. Esses atributos poderiam ser definitivamente excluídos --"
      "\ne deixando para a camada de negócio a responsabilidade pelo seu cálculo --"
      "\nou até ser movidos para uma nova tabela e referenciar a principal (FUNCIONARIO).")

duvida09 = input("O que é o MER - Modelo de Entidade e Relacionamento?\n>:")
print("\nO Modelo Entidade Relacionamento (também chamado Modelo ER, ou simplesmente MER),"
      "\ncomo o nome sugere, é um modelo conceitual utilizado na Engenharia de Software para"
      "\ndescrever os objetos (entidades) envolvidos em um domínio de negócios, com suas"
      "\ncaracterísticas (atributos) e como elas se relacionam entre si (relacionamentos)."
      "\nm geral, este modelo representa de forma abstrata a estrutura que possuirá"
      "\no banco de dados da aplicação. Obviamente, o banco de dados poderá conter"
      "\nvárias outras entidades, tais como chaves e tabelas intermediárias, que "
      "\npodem só fazer sentido no contexto de bases de dados relacionais.")

duvida10 = input("O que é o DER - Diagrama de Entidade e Relacionamento?\n>:")
print("\nEnquanto o MER é um modelo conceitual,"
      "\no Diagrama Entidade Relacionamento (Diagrama ER ou ainda DER)"
      "\né a sua representação gráfica e principal ferramenta."
      "\nEm situações práticas, o diagrama é tido muitas vezes como sinônimo de modelo,"
      "\numa vez que sem uma forma de visualizar as informações, o modelo pode ficar abstrato"
      "\ndemais para auxiliar no desenvolvimento do sistema."
      "\nDessa forma, quando se está modelando um domínio, o mais comum é já criar"
      "\nsua representação gráfica, seguindo algumas regras."
      "\nO diagrama facilita ainda a comunicação entre os integrantes da equipe,"
      "\npois oferece uma linguagem comum utilizada tanto pelo analista,"
      "\nresponsável por levantar os requisitos, e os desenvolvedores,"
      "\nresponsáveis por implementar aquilo que foi modelado.")

duvida11 = input("O que é a linguagem SQL?\n>:")
print("\nStructured Query Language, ou Linguagemde Consulta Estruturada."
      "\né a linguagem padrão* dos Bancos de DadosRelacionais.")

duvida12 = input("A linguagem SQL se divide em quantos subgrupos? E quais são eles?\n>:")
print("\n linguagem SQL se divide em 5 subgrupos:"
      "\nData Query Language - (Linguagem de Consulta de Dados)"
      "\nData Manipulation Language - (Linguagem de Manipulação de Dados)"
      "\nData Definition Language - (Linguagem de Definição de Dados)"
      "\nData Control Language - (Linguagem de Controle de Dados)"
      "\nData Transaction Language - (Linguagem de Transação de Dados)")

duvida13 = input("Quais os comandos do Data Query Language e qual sua utilização?")
print("\nNo grupo DQL nós temos apenas 1 comando SQL: Select"
      "\nEste comando é utilizado para realizar consultas no banco de dados."
      "\nEmbora tenha apenas um comando, a DQL é a parte da SQL mais utilizada."
      "\nO comando SELECT permite ao usuário espeficicar uma consulta (query)"
      "\ncomo uma descrição do resultadoesperado."
      "\nEste comando é composto de várias cláusulas e opções, possibilitando eleborar"
      "\nconsultas das mais simples às mais complexas.")

duvida14 = input("Quais os comandos do Data Manipulation Language e qual sua utilização?\n>:")
print("No subgrupo DML nós temos 3 comandos SQL: Insert, Update e Delete"
      "Este subgrupo da linguagem SQL é utilizado para realizar"
      "inclusões, alterações eexclusões de dados presentes em registros do banco de dados.")

print("INSERT - Usado para inserir um registro a uma tabela existente;"
      "UPDATE - Usado para alterar valores de dados em um ou mais registros de umatabela;"
      "DELETE - Usado para remover registros de uma tabela;")

duvida15 = input("Quais os comandos do Data Definition Language e qual sua utilização?\n>:")
print("No subgrupo DDL nós temos 3 comandos SQL: Create, Alter e Drop"
      "Este subgrupo da linguagem SQL é utilizado para criar, alterar e excluir bancos de dados,"
      "tabelas,e elementos associados como índice e visão.")

print("CREATE - Usado para criar um banco de dados, tabela e outros objetos emumbancodedados;"
      "ALTER - Usado para alterar a estrutura de tabelas ou outro objeto emumbancodedados;"
      "DROP - Usado para apagar bancos de dados, tabelas e outros objetos;")

duvida16 = input("Quais os comandos do Data Control Language e qual sua utilização?\n\n")
print("No subgrupo DCL nós temos 2 comandos SQL: Grant e Revoke"
      "Este subgrupo da linguagem SQL é utilizado para controlar os aspectos de"
      "autorização de dados e licenças de usuários para controlar quem tem acesso"
      "para manipular dados dentro do banco de dados.")

print("GRANT - Usado para autorizar um usuário a executar ou setar operações no bancodedados;"
      "REVOKE - Usado para remover ou restringir a capacidade de um usuário de executar operações;")

duvida19 = input("Quais os comandos do Data Transaction Language e qual sua utilização?\n>:")
print("No subgrupo DTL nós temos 3 comandos SQL: Begin, Commit e Rollback")

print("BEGIN (ou STARTTRANSACTION*) - Usado para marcar o começo de uma transação que pode ser completada ou não."
      "COMMIT - Finaliza uma transação."
      "ROLLBACK - Faz com que as mudanças nos dados existentes deste o último COMMIT sejam descartadas.")

duvida20 = input("Qual a necessidade de se utilizar a cláusula WHERE em uma consulta?\n>:")
print("A cláusula WHERE no SQL funciona como um filtro da consulta,"
      "ao usá-la a query irá extrair apenas os registros que obedecerem à determinada condição."
      "A sintaxe básica do WHERE é a seguinte:"
      "SELECT coluna1, coluna2, coluna3"
      "FROM nome_tabela"
      "WHERE coluna1 = condicao"
      "Na primeira linha da query acima selecionamos as colunas que desejamos que apareçam na tabela"
      "que será formada com o resultado da query, na segunda linha ,em “FROM”, especificamos de qual"
      "tabelas estamos extraindo a informação e na terceira linha especificamos a condição"
      "para filtrar os registros que irão aparecer no resultado."
      "Os seguintes operadores podem ser usados com o comando WHERE:"
      "=	Igual"
      ">	Maior que"
      "<	Menor que"
      ">=	Maior ou igual"
      "<=	Menor ou igual"
      "<> ou !=	Diferente de"
      "IN	Incluindo (múltiplos valores)"
      "NOT IN	Excluindo (múltiplos valores)"
      "BETWEEN	Entre dois valores"
      "LIKE	Busca um padrão parecido"
      "IS NULL	Traz todos os valores nulos"
      "IS NOT NULL	Traz todos os valores que não são nulos")

duvida21 = input("Por que as vezes precisamos fazer consultas em múltiplas tabelas?\n>:")
print("Quando temos relacionamentos entre tabelas significa que os dados estão espalhados"
      "entre estas tabelas, e ao precisarmos realizar consultas as vezes precisamos consultar"
      "nestas múltiplas tabelas.")

duvida22 = input("O que é a junção de tabelas?\n>: ")
print("Em um banco de dados podemos ter duas ou mais tabelas relacionadas."
      "É bastante comum que ao elaborarmos uma consulta termos a necessidade de"
      "trazer dados de diferentes tabelas. Para criarmos esta seleção de dados devemos"
      "definir os critérios de agrupamento para trazer estes dados."
      "Estes critérios são chamados de Junções. Uma junção de tabelas cria uma"
      "pseudo-tabela derivada de duas ou mais tabelas de acordo com as regras especificadas,"
      "e que são parecidas com as regras da Teoria dos Conjuntos.")

duvida23 = input("O que são funções de agregação? Cite 3 que você ache mais importantes.\n>:")
print("Uma função de agregação processa um conjunto de valores contidos em uma única coluna"
      "de uma tabela e retorna um único valor como resultado."
      "Sua síntaxe é semelhante aquela utilizada em funções encontradas nas linguagens de programação,"
      "contudo o parâmetro de entrada é sempre a coluna cujos valores desejamos processar."
      "Exemplo:"
      "nome-da-funcao(coluna)"
      "Podemos informar no comando SELECT uma ou mais funções de agregação, deacordocoma necessidade.")

print("Comando DDL para criar o banco de dados."
      "Comando DML para utilizar o banco de dados.")

print("A função max analisa um conjunto de valores e retorna o maior entre eles."
      "A função min analisa um conjunto de valores e retorna o menor entre eles."
      "A função sum() realiza a soma dos valores em uma única coluna e retorna esseresultado."
      "Com a função avg() podemos calcular a média aritmética dos valores emumaúnicacoluna."
      "Utilizamos a função round() para arredondar valores e desta forma especificar quantascasasdecimais queremos apresentar o valor."
      "A função count() retorna o total de linhas selecionadas.")


duvida24 = input("Por que as vezes precisamos agrupar resultados?\n>:")
print(" É muito raro que uma base de dados tenha todos os seus dados em uma única tabela."
      "Os dados tendem a estar espalhados por diversas tabelas de modo a otimizar o armazenamento e"
      "assegurar a coerência e integridade. Parte do seu trabalho ao escrever uma consulta é de implantar e"
      "interligar as operações de T-SQL que podem operar através de tabelas, a fim de gerar resultados de negócio necessários."
      "Uma característica muito importante do SQL é o poder de agrupar linhas com base em valores de determinadas colunas."
      "Dessa forma, não estaremos trabalhando na pesquisa em todas as linhas da tabela, em grupos menores.")

duvida25 = input("Qual é a forma padrão de ordenação de resultados em uma consulta?\n>:")
print("A cláusula ORDER BY organiza os dados em ordem alfabética ou numérica."
      "A ordenação pode ser ASC (Ascendente) ou DESC (Descendente)"
      "Por padrão, a ordenação é ascendente, ou seja, do menor para o maior.")

duvida26 = input("Cite 3 funções de dada e hora. 8) O que são subconsultas?\n>:")
print("CURDATE()... Função que retorna a data atual no formato aaaa-mm-dd"
      "CURTIME()... Retorna a hora atual no formato hh:mm:ss"
      "DATE_ADD(data, intervalo)... Adiciona um intervalo à data."
      "O intervalo pode ser uma data seguida de um horário."
      "O intervalo a ser somado pode ser em dias, dias e horas e minutos, dias e segundos, minutosesegundos e etc."
      "DATE_SUB(data, intervalo)... Subtrai um intervalo à data. A data pode ser uma data seguida de umhorário."
      "O intervalo a ser subtraído pode ser em dias, dias e horas e minutos, dias e segundos, minutos e segundos,etc."
      "DATEDIFF(expressão1, expressão2)... Retorna o valor da diferença entre 'expressão1' e 'expressão2',"
      "podendo ambos ser em uma data ou data e horário."
      "DATE_FORMAT(data, formato)... Retorna a data no formato especificado."
      "DAYNAME(data)... Retorna o dia da semana para a data."
      "DAYOFMONTH(data)... Retorna o dia do mês para a data."
      "DAYOFWEEK(data)... Retorna o dia da semana em que a data cai."
      "DAYOFYEAR(data)... Retorna o dia do ano para a data."
      "FROM_DAYS(n)... Retorna a data real referente a um número 'n' em dias."
      "NOW()... Retorna a data e hora atuais."
      "CURRENT_TIMESTAMP()... Esta função faz o mesmo que NOW()."
      "TIME()... Esta função serve para extrair a hora de uma data."
      "SEC_TO_TIME(segundos)... Função recebe um valor em segundos e retorna esse valor convertido emhoras, minutosesegundos."
      "TIME_TO_SEC(hora)... A função acima converte a hora recebida em segundos."
      "HOUR(hora), MINUTE(hora), SECOND(hora)... As funções acima retornam a hora, minuto e segundo da hora recebida comoparâmetro."
      "PERIOD_DIFF(periodo1, periodo2)... Retorna o número de meses entre os dois período, que devem estar no formato AA MM ou AAAA MM."
      "TIME_DIFF(hora1, hora2)... A função acima calcula a diferença entre a hora 1 e hora 2."
      "QUARTER(data)... Retorna o trimestre do ano para a data."
      "WEEK(data)... Retorna a semana do ano para a data."
      "WEEKDAY(data)... Retorna o dia da semana que inicia com segunda-feira para uma data."
      "YEAR(data)... Retorna o ano de uma data"
      "MONTH(data)... Retorna o mês de uma data."
      "DAY(data)... Retorna o dia de uma data."
      "Contextualizando... De forma geral, grande parte das consultas realizadas em bancos de dados"
      "podem ser resolvidas de forma simples. Toda via, existem casos que é necessário aumentar a"
      "complexidade destas consultas,até mesmo para facilitar o resultado final e melhorar a leitura"
      "destas consultas. É aqui que entram as Subconsultas, conhecidas também como Subqueries."
      "Uma subconsulta nada mais é do que uma instrução SELECT dentro de outro SELECT que"
      "retorna algumas colunas específicas que são usadas em algumas funções como INSERT e UPDATE e DELETE por exemplo.")

