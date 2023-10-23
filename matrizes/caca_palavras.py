"""
Lê uma palavra do teclado e em seguida lê um caça palavras, linha por linha até o fim,
depois imprime o número de ocorrências da palavra.
"""

def verificar_horizontal(palavra, matriz, i, j):
    """
    Devolve True se a palavra ocorre horizontalmente
    na matriz a partir da coluna j na linha i
    """

    # para cada k de 0 até len(palavra) - 1:
    #   comparo palavra[k] com matriz [i][j+k]
    #   se forem diferentes, respondo False
    # respondo True

    for k in range(len(palavra)):
        if j + k >= len(matriz[i]):
            return False
        if palavra[k] != matriz[i][j + k]:
            return False
    return True

def verificar_vertical(palavra, matriz, i, j):
    for k in range(len(palavra)):
        if i + k >= len(matriz):
            return False
        if palavra[k] != matriz[i + k][j]:
            return False
    return True

def encontrar_ocorrencias(palavra, matriz):
    """
    para cada linha i:
        para cada coluna j:
            se a palavra começa na coluna j horizontalmente:
                conta uma ocorrencia
            se a palavra começa na coluna j verticalmente:
                conta uma ocorrencia
    """
    m = len(matriz)
    n = len(matriz[0])
    ocorrencias = 0
    for i in range(m):
        for j in range(n):
            if verificar_horizontal(palavra, matriz, i, j):
                ocorrencias += 1
            if verificar_vertical(palavra, matriz, i, j):
                ocorrencias += 1
    return ocorrencias


def ler_matriz_teclado():
    palavra = input()
    matriz = []
    while True:
        try:
            linha = input()
            matriz.append(linha)
        except EOFError:
            break
    return palavra, matriz

def main():
    palavra, matriz = ler_matriz_teclado()
    ocorrencias = encontrar_ocorrencias(palavra, matriz)
    print(f"Há {ocorrencias} ocorrências da palavra {palavra}")

main()

