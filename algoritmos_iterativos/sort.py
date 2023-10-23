"""Algoritmo de ordenação por bolha

Repita n-1 vezes:
    Para cada índice i do primeiro ao penúltimo:
        Compare o elemento i ao i+1
            Se estiverem fora de ordem troque as posições 

"""

def bubble_sort(lista):
    for _ in range(len(lista) - 1):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux

"""Algoritmo de seleção

A lista preta é a lista do índice i até o ultimo

Para cada índice i do primeiro até o penúltimo
Encontrar o menor na lista preta
Troca com o primeiro da lista preta

"""

def indice_menor_lista_preta(lista, i):
    indice_menor = i
    for j in range(i, len(lista)):
        if lista[j] < lista[indice_menor]:
            indice_menor = j
    
    return indice_menor

def selection_sort(lista):
    for i in range(len(lista)):
        indice_menor = indice_menor_lista_preta(lista, i)
        aux = lista[i]
        lista[i] = lista[indice_menor]
        lista[indice_menor] = aux

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
