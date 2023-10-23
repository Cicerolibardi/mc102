"""
Algoritmo do insertion sort

i <-- 1  (representa o início da lista preta)

para i do índice 1 até o último:
    chave <-- lista[i]
    j <-- posição de inserção da chave na lista
    desloque os elementos de j até i - 1 para frente
    lista[j] <-- chave

"""

def achar_posicao(lista, i, chave):
    """
    devolve a posição de inserção da chave
    na lista ordenada que vai de 0 até i-1
    """
    j = 0
    while j != i and chave > lista[j]:
        j += 1
    
    return j

def deslocar_lista(lista, i, j):
    """desloque os elementos da lista
    da posição j até i - 1 para frente"""
    k = i
    while k > j:
        lista[k] = lista [k-1]
        k -= 1

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = achar_posicao(lista, i, chave)
        deslocar_lista(lista, i, j)
        lista[j] = chave

def main():
    lista = [7, 3, 2, 5, 6, 1, 4]
    insertion_sort(lista)
    print(lista)

main()