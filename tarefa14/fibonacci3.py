def achar_fibonacci(dicionario_conhecidos, valor):
    if valor in dicionario_conhecidos:
        return dicionario_conhecidos[valor]
    else:
        fibo = (achar_fibonacci(dicionario_conhecidos, valor - 1) + achar_fibonacci(dicionario_conhecidos, valor -2)
        + achar_fibonacci(dicionario_conhecidos, valor - 3))
        dicionario_conhecidos[valor] = fibo
        return fibo
        

def criar_dicionario_012():
    dicionario_conhecidos = dict()
    dicionario_conhecidos[0] = 0
    dicionario_conhecidos[1] = 1
    dicionario_conhecidos[2] = 2

    return dicionario_conhecidos

def main():
    valor_fibonacci = int(input())
    dicionario_conhecidos = criar_dicionario_012()
    fibonacci = achar_fibonacci(dicionario_conhecidos, valor_fibonacci)
    print(fibonacci)

main()