def buscar_posicao(lista_entrada, numero_desejado, primeiro, ultimo):
    meio = (primeiro + ultimo) // 2

    if primeiro == ultimo and numero_desejado == lista_entrada[primeiro]:
        return primeiro
    elif primeiro == ultimo and numero_desejado != lista_entrada[ultimo]:
        return -1
    elif primeiro != ultimo:
        if numero_desejado == int(lista_entrada[meio]):
            return meio
        elif numero_desejado < int(lista_entrada[meio]):
            posicao = buscar_posicao(lista_entrada, numero_desejado, primeiro, meio)
            return posicao
        elif numero_desejado > int(lista_entrada[meio]):
            posicao = buscar_posicao(lista_entrada, numero_desejado, meio + 1, ultimo)
            return posicao

def main():
    lista_entrada = input().split()
    numero_desejado = int(input())
    posicao = buscar_posicao(lista_entrada, numero_desejado, 0, (len(lista_entrada) -1))
    print(posicao)

main()