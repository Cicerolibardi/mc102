"""Mostra uma tabela de número de triângulos.
    0   0
    1   1
    2   4
    3   10
    4   20
"""
#recursão: Chamada de uma função dentro dela mesma

def triangulos_internos(n):
    """Devolve o número de triângulos (em pé)
    de um castelo de cartas de altura n."""
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        tn1 = triangulos_internos(n-1) #recursão
        tn2 = triangulos_internos(n-2) #recursão
        return (2 * tn1) - tn2 + n
    
def main():
    print('n    t(n)')
    for i in range(35):
        print(f't({i})    {triangulos_internos(i)}')


main()