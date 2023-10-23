

def achar_maximo(lista_entrada):
    if len(lista_entrada) == 1:
        maximo = int(lista_entrada[0])
    else:
        if int(lista_entrada[1]) >= int(lista_entrada[0]):
            maximo = achar_maximo(lista_entrada[1:])
        else:
            lista_entrada.pop(1)
            maximo = achar_maximo(lista_entrada)
    
    return maximo

def main():
    lista_entrada = input().split()
    maximo = achar_maximo(lista_entrada)
    print(maximo)

main()