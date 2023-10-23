def calcular_potencia(base, expoente):
    if expoente == 1:
        return base
    elif expoente == 0:
        return 1
    else:
        resultado = calcular_potencia(base, (expoente - 1))
        return resultado * base

def main():
    entrada = input().split()
    base = int(entrada[0])
    expoente = int(entrada[1])
    potencia = calcular_potencia(base, expoente)
    print(potencia)

main()