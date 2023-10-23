def tempo_gasto_tartaruga():
    numero_passo = 0
    distancia = 0.0
    proximo_passo = 1.0

    while distancia < 15:
        numero_passo += 1
        distancia += proximo_passo
        proximo_passo = 1.0/ (numero_passo + 1)

    return numero_passo

def tempo_gasto_coelho():
    numero_saltos = 0
    distancia = 0.0
    proximo_salto = 1.0

    while distancia < 2.0:
        numero_saltos += 1
        distancia += proximo_salto
        proximo_salto = proximo_salto / 2

    return numero_saltos

def main():
    tempo_coelho = tempo_gasto_coelho()
    print(f"O coelho gasta {tempo_coelho} minutos")
    tempo_tartaruga = tempo_gasto_tartaruga()
    print(f"A tartaruga gasta {tempo_tartaruga} minutos")

main()