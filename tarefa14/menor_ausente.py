def verificar_menor_ausente(lista_sequencia, menor_ausente):
    if menor_ausente != int(lista_sequencia[0]):
        return menor_ausente
    else:
        menor_ausente += 1
        menor = verificar_menor_ausente(lista_sequencia[1:], menor_ausente)
        return menor

def main():
    lista_sequencia = input().split()
    menor_ausente = verificar_menor_ausente(lista_sequencia, 0)
    print(menor_ausente)

main()