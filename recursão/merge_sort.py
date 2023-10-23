'''def intercalar(lista, inicio, meio, fim):
    """
    Ordena a lista supondo que:
    1) lista[inicio] ... lista[meio] está ordenada
    2) lista[meio + 1] ... lista[fim] está ordenada
    """
    lista_esquerda = lista[inicio:meio]
    lista_direita = lista[meio:fim]
    i_esquerda = 0
    j_direita = 0
    
    for contador in range(inicio, fim):
        


def merge_sort(lista, inicio, fim):
    """
    Ordena a parte da lista do índice inicio até o índice fim.
    """

    if inicio == fim:
        pass
    else:
        meio = (inicio + fim) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio + 1, fim)
        intercalar(lista, inicio, meio, fim)
'''

def merge_sort(lista):
    if len(lista) > 1:
        meio = (len(lista)) // 2
        lista_esquerda = lista[:meio]
        lista_direita = lista[meio:]
        merge_sort(lista_esquerda)
        merge_sort(lista_direita)

        i_esquerda = 0
        i_direita = 0
        contador = 0

        while i_esquerda < len(lista_esquerda) and i_direita < len(lista_direita):

            if lista_esquerda[i_esquerda] < lista_direita[i_direita]:
                lista[contador]=lista_esquerda[i_esquerda]
                i_esquerda += 1
            else:
                lista[contador]=lista_direita[i_direita]
                i_direita += 1
            contador += 1

        while i_direita < len(lista_direita):
            lista[contador]=lista_direita[i_direita]
            i_direita += 1
            contador += 1

        while i_esquerda < len(lista_esquerda):
            lista[contador]=lista_esquerda[i_esquerda]
            i_esquerda += 1
            contador += 1

def main():
    lista = [3, 2, 1, 6, 10, 8, 19, 9, 12, 8, 5]
    merge_sort(lista)
    print(lista)

main()