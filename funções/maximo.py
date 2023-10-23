"""
Calcula o valor máximo de uma lista
"""

def obter_maximo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

def ler_lista_numeros():
    n = int(input())
    lista_numeros = []
    for _ in range(n):
        numero = int(input())
        lista_numeros.append(numero)
    return lista_numeros

def produto_soma_maximos(lista1, lista2):
    maximo1 = obter_maximo(lista1)
    maximo2 = obter_maximo(lista2)
    produto = maximo1 * maximo2
    soma = maximo1 + maximo2
    return produto, soma


def main():
    print('Digite uma lista de números: ')
    lista1 = ler_lista_numeros()
    print('Digite outra lista de números: ')
    lista2 = ler_lista_numeros()

    produto, soma = produto_soma_maximos(lista1, lista2)
    print(produto)
    print(soma)
main()