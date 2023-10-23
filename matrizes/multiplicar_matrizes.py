def calcular_produto_interno(A, B, i, j):
    prod_interno = 0
    for z in range(len(A[i])):
        c_ij = A[i][z] * B[z][j]
        prod_interno += c_ij
    return prod_interno

def multiplicar_matrizes(A,B):
    m = len(A)
    l = len(B)
    n = len(B[0])
    C = [ [0 for _ in range(n)]
             for _ in range(m)
        ]
    for i in range(m):
        for j in range(n):
            prod_interno = calcular_produto_interno(A, B, i, j)
            C[i][j] = prod_interno
    return C


def main():
    A = [
         [6,7, 8, -7,-4],
         [6,1, 3, 4, -2],
         [2,8, 1, 5, -1],
         [4,13,-7,-3,-1],
         [2, 6, 1, 3, 4]
         ]

    B = [
         [1, 4, 1],
         [2, 3, 7],
         [5, 6,-4],
         [-2,4, 6],
         [-1,-1,0]
         ]

    multiplicacao = multiplicar_matrizes(A,B)
    for i in multiplicacao:
        print(i)

main()