def encontrar_combinacoes(numero_digitos, soma, lista_combinação, indice):
    if soma < 0:
        return None
    if indice + 1 == numero_digitos:
        if soma == 0:
            lista_devolver = map(str, lista_combinação)
            print(''.join(lista_devolver))
    else:
        indice += 1
        for i in range(10):
            lista_combinação[indice] = i
            encontrou = encontrar_combinacoes(numero_digitos, soma - i, lista_combinação, indice)

def definir_primeiro_elemento(numero_digitos, soma):
    for i in range(1,10):
        lista_combinação = [""] * numero_digitos
        lista_combinação[0] = i
        indice = 0
        encontrou = encontrar_combinacoes(numero_digitos, soma - i, lista_combinação, indice)

def main():
    entrada = input().split()
    numero_digitos = int(entrada[0])
    soma = int(entrada[1])
    encontrar_n_digitos = definir_primeiro_elemento(numero_digitos, soma)


main()