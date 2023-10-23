def merge_sort(lista):
    if len(lista) > 1:
        meio = (len(lista)) // 2
        lista_esquerda = lista[:meio]
        lista_direita = lista[meio:]
        merge_sort(lista_esquerda)
        merge_sort(lista_direita)

        i_esquerda = 0
        i_direita = 0

        for k in range(len(lista)):
            if i_esquerda < len(lista_esquerda) and i_direita < len(lista_direita):

                if lista_esquerda[i_esquerda] < lista_direita[i_direita]:
                    lista[k] = lista_esquerda[i_esquerda]
                    i_esquerda += 1
                else:
                    lista[k] = lista_direita[i_direita]
                    i_direita += 1

            elif i_direita < len(lista_direita):
                lista[k] = lista_direita[i_direita]
                i_direita += 1

            else:
                lista[k] = lista_esquerda[i_esquerda]
                i_esquerda += 1

def main():
    lista = input().split()
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    merge_sort(lista)
    
    for j in range(len(lista)):
        print(lista[j], end=' ')

main()