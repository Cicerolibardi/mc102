
def achar_fatorial(valor):
    if valor == 0:
        return 1
    elif valor == 1:
        return 1
    else:
        return valor * achar_fatorial(valor - 1)

def main():
    valor_fatorial = int(input())
    fatorial = achar_fatorial(valor_fatorial)
    print(fatorial)

main()