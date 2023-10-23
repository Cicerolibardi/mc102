"Algoritmo para a soma de dias em uma data"

Instruções elementares para a produção do algoritmo:
	O computador deve ser hábil de fazer:
		- Soma
		- Subtração
		- Divisão
		- Multiplicação
		- Identificação de números inteiros
		- Tomar nota de números inteiros

Definição para se o ano é bissexto ou não:
	Se Ano/4 não for inteiro:
		Defina Ano como não-bissexto
	Se Ano/4 for um número inteiro e Ano/100 não for inteiro:
		Defina Ano como bissexto
	Se Ano/4 for um número inteiro e Ano/400 for inteiro:
		Defina Ano como bissexto
	Se Ano/4 for um número inteiro e Ano/100 for inteiro e Ano/400 não for inteiro:
		Defina Ano como não-bissexto

Definição para o número de dias em cada mês:
	Se o valor do Mês for = (1,3,5,7,8,10,12):
		Defina o valor máximo da entrada Dia para 31
	Se o valor do Mês digitado for = (4,6,9,11):
		Defina o valor máximo da entrada Dia para 30
	Se o valor do Mês digitado for = (2) e Ano for não-bissexto:
		Defina o valor máximo da entrada Dia para 28
	Se o valor do Mês digitado for = (2) e Ano for bissexto:
		Defina o valor máximo da entrada Dia para 29

Intervalo da entrada Mês = [0,12]

Tome nota do valor Dia
Tome nota do valor Mês
Tome nota do valor Ano
Some o valor Dias soma ao Dia;
	Se (Dias soma + Dia) for menor que o valor máximo de dias definido para o Mês:
		Tome nota do novo valor Dia
	Se (Dias soma + Dia) for maior que o valor máximo de dias definido para o Mês e Mês é diferente de 12:
		Subtraia o valor máximo de Dia para o Mês de (Dias soma + Dia) e some 1 ao Mês
			Tome nota do novo valor Dia e Mês
	Se (Dias soma + Dia) for maior que o valor máximo de dias definido para o Mês e Mês é igual a 12:
		Subtraia 31 de (Dias soma + Dia) e defina novo valor Mês para 1 e some 1 ao Ano
			Tome nota dos novos valores Dia, Mês e Ano

Devolva como saída: Dia/Mês/Ano
