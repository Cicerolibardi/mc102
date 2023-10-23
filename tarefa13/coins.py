

def calcular_notas(valor_monetario):
    notas = [100, 50, 20, 10, 5, 2]
    print('NOTAS:')
    for valor in notas:
        frequencia_nota = valor_monetario // valor
        valor_monetario -= frequencia_nota * valor
        if frequencia_nota >= 1:    
            print(f'{int(frequencia_nota)} nota(s) de R$ {valor:.2f}')
    
    return valor_monetario

def calcular_moedas(valor_restante):
    moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
    print('MOEDAS:')
    for valor in moedas:
        frequencia_moeda = valor_restante // valor
        valor_restante -= frequencia_moeda * valor
        if frequencia_moeda >= 1:
            print(f'{int(frequencia_moeda)} moeda(s) de R$ {valor:.2f}')

def main():
    valor_monetario = float(input())
    restante_notas = calcular_notas(valor_monetario)
    if restante_notas > 0:
        calcular_moedas(restante_notas)

main()