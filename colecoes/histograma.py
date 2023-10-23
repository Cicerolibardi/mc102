"""
Crie um programa que calcule o histograma de um conjunto
de números inteiros.
"""

def ler_arquivo(nome_arquivo):
    lista = []
    with open(nome_arquivo) as arquivo:
        for linha in arquivo:
            lista.append(int(linha.strip()))
    
    return lista

def calcular_histograma2(lista):
    histograma = dict()

    for elemento in lista:
        if elemento not in histograma:
            histograma[elemento] = 0
        
        histograma[elemento] += 1

    return histograma

def calcular_histograma(lista):
    histograma = []
    
    for item in lista:
        for par in histograma:
            if par[0] == item:
                break
        else:
            par = [item,0]
            histograma.append(par)
        
        par[1] += 1

    return histograma

def main():
    A = ler_arquivo('muitos.txt')
    histograma = calcular_histograma2(A)
    print(histograma)

main()