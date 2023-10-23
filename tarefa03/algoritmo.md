"Algoritmo para descobrir qual número tem mais divisores"

Definindo as entradas:
	As entradas devem ser estritamente números naturais;

Entradas:
	Quantidade de números para se analisar = n
	Número 1 = a1
	Número 2 = a2
	.	
	.	
	.	
	Número n = an

Saída:
	A saída deve ser o número com maior quantidade de divisores

Dizendo as ações que devem ser elementares para se fazer esse algoritmo:
	Divisão por número inteiro
	Tomar nota de números
	Somar
	Divisão
	Subtração
	Crie e analise listas
	Correlacione itens de mesmo índice

Algoritmo:

a = {a1, a2, ..., an}

b = {b1, b2, ..., bn}

x = 1

Aponte para o primeiro valor da lista "a"
Aponte para o primeiro valor da lista "b"	
	f: Divida o valor de a que foi apontado por x
		Se o resto de a/x for igual a 0
			Some 1 ao valor de b
			Some 1 ao valor de x	
				Se x < (n+1)/2
					Realize novamente "f:"
				Se não
					Some 1 ao valor de b atual	
						Aponte para o próximo valor da lista a
						Aponte para o próximo valor da lista b
						Defina o valor de x para 1		
						Realize novamente "f:"
		
		Se não
			Some 1 ao valor de x
			Realize novamente "f"


Correlacione os índices da lista "a" e lista "b" (a1 com b1, a2 com b2, ..., an com bn)
Verifique o maior valor entre os elementos da lista "b" e chame-o de c
Verifique a quantidade de vezes que esse valor aparece e anote como z
Aponte para o primeiro valor c na lista "b"
		Faça z vezes:
			Verifique o índice desse elemento da lista "b"
				Escreva como saída o valor do ítem da lista "a" correlacionado à esse índice
					Aponte para o próximo valor c na lista "b"
