def multiplicar_iterativo(lista):
    """
    Devolve o produto de todos os valores da lista.
    """
    produto = 1
    for fator in lista:
        produto *= fator
    
    return fator

def multiplicar_recursivo1(lista, n):
    """
    Devolve o produto dos n primeiros fatores da lista.
    """
    if n == 1:
        return lista[0]
    else:
        return multiplicar_recursivo(lista, n-1) * lista[n-1]

def multiplicar_recursivo2(lista, inicio, fim):

    if inicio == fim:
        return lista[inicio]
    else:
        meio = (inicio + fim) // 2
        subproduto1 = multiplicar_recursivo2(lista, inicio, meio)
        subproduto2 = multiplicar_recursivo2(lista, meio + 1, fim)
        produto = subproduto1 * subproduto2
        return produto

def main():
    lista = [1, 2, 3, 5]
    produto = multiplicar_recursivo2(lista, 0, len(lista) - 1)
    print(produto)

main()