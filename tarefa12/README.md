# Funções de uso para a agenda.py:

## Primeiramente, deve-se destacar que há 5 funções principais:

**Inicializar** - inicializa a agenda.csv.

**Criar** - cria um evento dentro da agenda.csv, sendo passados no terminal os parâmetros que deseja-se criar.

**Alterar** - altera um evento na agenda.csv, sendo passado no terminal o número do evento e o que deseja-se alterar.

**Remover** - remove um evento dentro da agenda.csv, sendo passado no terminal o número do evento.

**Listar** - lista os eventos para determinada data dentro da agenda.csv, sendo passado no terminal a data.

## Os parâmetros informados acima são:
> **--evento** - número do evento;

> **--data** - data do evento;

> **--nome** - nome do evento;

> **--hora** - hora do evento;

> **--descricao** - descrição do evento.

# Exemplos de uso da agenda.py:

##### **Nota:** A agenda deve-se sempre ser acessada por: **python3 agenda.py -a agenda.csv** e ser passado os parâmetros para cada função posteriormente.

> **Inicializar** - python3 agenda.py -a agenda.csv inicializar

> **Criar** - python3 agenda.py -a agenda.csv criar --nome "MC102" --descricao "Aula de laboratório" --data "01/06/2020" --hora "14:00"

> **Alterar** - python3 agenda.py -a agenda.csv alterar --evento 1 --hora "16:00"

> **Remover** - python3 agenda.py -a agenda.csv remover --evento 1

> **Listar** - python3 agenda.py -a agenda.csv listar --data "13/06/2020"

**Após tais ações serão dadas mensagens sobre tal realização.**

# Estrutura de dados utilizada:
Para a realização da tarefa, foi utilizada para armazenar os dados que são passados pelo terminal e serem trabalhados foi uma lista de dicionários, pois relaciona os valores que foram passados pelo usuário às chaves, dessa forma, sendo facilitado o trabalho de manipulação dos dados por palavras chave. Os dados, para meu arquivo, que representam um evento são: O evento, o nome dele, a descrição do evento, sua data e sua hora, sendo esses os valores das chaves no dicionário.

# Formato do arquivo.csv:
Para meu arquivo.csv foram utilizadas 5 colunas, dispostas de tal forma:

> Evento,Nome,Descrição,Data,Hora.

O separador utilizado em tal arquivo foi o elemento ",", sendo acessado, quando necessária a listagem, pelo método do delimitador sendo o caractere vírgula, que facilita a manipulação desses dados.
