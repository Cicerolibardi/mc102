def ler_lista_numeros():
    """Lê uma lista de números de ponto flutuante do teclado e devolve essa lista"""
    lista_numeros = []
    n = int(input("Digite quantos elementos: "))
    for i in range(n):
        numero = float(input())
        lista_numeros.append(numero)
    return lista_numeros
    

def imprimir_lista_numeros(lista_numeros):
    """Imprime uma lista de números recebida na tela, um por linha"""
    for valor in lista_numeros:
        print(valor)

def incrementar_termo_lista_numeros(lista_numeros, termo):
    """Altera a lista passada incrementando 5 a cada elemento da lista anterior e devolve a lista incrementada"""
    for i in range(len(lista_numeros)):
        lista_numeros[i] += termo
    return lista_numeros