'''def redução_listas(lista):
    lista_reduzida = []
    for i in lista:
        if i in lista and i not in lista_reduzida:
            lista_reduzida.append(i)
    return lista_reduzida

def inteiros(lista):
    lista_convertida = []
    for elemento in lista:
        lista_convertida.append(int(elemento))
    return lista_convertida

def ordenacao(lista_inteiros_unsorted, lista_reduzida):
    lista_ordenada = []
    
    lista_ordenada.append(lista_reduzida[0])
    lista_reduzida.remove(lista_reduzida[0])
    
    while lista_reduzida:
        for i in lista_reduzida:
            n = 0
            for j in lista_ordenada:
                if lista_inteiros_unsorted.count(i) > lista_inteiros_unsorted.count(j):
                    n += 1
                elif (lista_inteiros_unsorted.count(i) == lista_inteiros_unsorted.count(j)) and (i > j):
                    n += 1

            lista_ordenada.insert(n, i)
            lista_reduzida.remove(i)
    
    return lista_ordenada

def entregar_saída(lista_ordenada):
    for i in lista_ordenada:
        print(i, end = " ")

def main():
    lista_entrada = input().split()
    lista_inteiros_unsorted = inteiros(lista_entrada)
    lista_reduzida = redução_listas(lista_inteiros_unsorted)
    lista_ordenada = ordenacao(lista_inteiros_unsorted, lista_reduzida)
    entregar_saída(lista_ordenada)

main()'''

'''def inteiros(lista):
    lista_convertida = []
    for elemento in lista:
        lista_convertida.append(int(elemento))
    return lista_convertida

def maximo_lista(lista_inteiros):
    n = 0
    for i in lista_inteiros:
        if i >= n:
            n = i
    return n

def frequencias(lista_entrada):
    lista_inteiros = inteiros(lista_entrada)
    maximo = maximo_lista(lista_inteiros)
    lista_frequencias = [0] * (maximo+1)
    
    for i in lista_inteiros:
            lista_frequencias[i] += 1
    
    return lista_frequencias

def main():
    lista_entrada = input().split()
    lista_frequencias = frequencias(lista_entrada)
    print(lista_frequencias)

main()'''