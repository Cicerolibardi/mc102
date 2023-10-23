def conjec_collatz(valor, dicionario_collatz):
    contador = 0
    if valor == 1:
        dicionario_collatz[valor] = 0
        return dicionario_collatz[valor]
    else:
        if valor not in dicionario_collatz:
            while valor > 1:
                if valor % 2 == 0:
                    contador += 1
                    dicionario_collatz[int(valor)] = contador
                    valor = valor / 2
                else:
                    contador += 1
                    dicionario_collatz[int(valor)] = contador
                    valor = ((valor * 3) + 1) / 2
                    conjec_collatz(valor, dicionario_collatz)
            dicionario_collatz[1] = dicionario_collatz[valor + 1]
            return dicionario_collatz[int(valor)]
        else:
            dicionario_collatz[int(valor)] = contador

def main():
    valor_entrada = int(input())
    collatz = conjec_collatz(valor_entrada, dict())
    print(collatz)

main()