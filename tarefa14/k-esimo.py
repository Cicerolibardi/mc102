def encontrar_k_esimo_menor(lista_sequencia, k):
    menor = lista_sequencia[0]
    index_menor = 0
    for i in range(len(lista_sequencia)):
        if lista_sequencia[i] < menor:
            menor = lista_sequencia[i]
            index_menor = i
    lista_sequencia.pop(index_menor)
    
    if k == 1:
        return menor
    else:
        k -= 1
        k_esimo_menor = encontrar_k_esimo_menor(lista_sequencia, k)
        return k_esimo_menor

def main():
    lista_sequencia = input().split()
    k = int(input())
    for i in range(len(lista_sequencia)):
        lista_sequencia[i] = int(lista_sequencia[i])
    k_esimo_menor = encontrar_k_esimo_menor(lista_sequencia, k)
    print(k_esimo_menor)

main()

