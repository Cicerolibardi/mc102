"""
Escreva um programa que dadas duas listas de strings,
escreva como saída a diferença simétrica das duas listas.
"""
def calcular_diferenca_simetrica(lista1,lista2):
    diferenca = []
    for item in lista1:
        if item not in lista2:
            diferenca.append(item)
        
    for item in lista2:
        if item not in lista1:
            diferenca.append(item)
    return diferenca

def main():
    A = set(['ana', 'daniel'])
    B = set(['gabriel','daniel'])
    C = calcular_diferenca_simetrica(A,B)
    print(C)

main()