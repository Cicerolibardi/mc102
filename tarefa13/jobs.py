def diferenca_trabalhos(lista_entrada):
    inicio = 0
    acumulado = 0
    lista_comparacao = []
    for i in range(1, len(lista_entrada), 2):
        for valor in lista_entrada[i]:
            acumulado = acumulado + int(valor)
        for valor in lista_entrada[i]:
            inicio += int(valor)
            acumulado -= int(valor)
            lista_comparacao.append(abs(inicio - acumulado))
        valor_inicial = lista_comparacao[0]
        for valor in lista_comparacao:
            if valor < valor_inicial:
                valor_inicial = valor
        print(valor_inicial)
        
        acumulado = 0
        inicio = 0
        lista_comparacao = []
    
def ler_entrada():
    lista_entrada = []
    while True:
        try:
            quantidade = int(input())
            pesos = input().split()
            lista_entrada.append(quantidade)
            lista_entrada.append(pesos)
        except EOFError:
            return lista_entrada

def main():
    lista_entrada = ler_entrada()
    diferenca_trabalhos(lista_entrada)

main()