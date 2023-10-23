lista = '1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 9, 9, 9, 9, 9'

def transformar_em_lista(lista):
    nova_lista = []
    print(len(lista))
    for i in range(len(lista)):
        if lista[i] != ',' or lista[i] != ' ':
            nova_lista.append(lista[i])
    print(nova_lista)
    return nova_lista


transformar_em_lista(lista)