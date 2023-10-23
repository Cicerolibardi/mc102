def buscar_posicao(lista_entrada, numero_desejado, primeiro, ultimo):
    meio = (primeiro + ultimo) // 2

    if primeiro == ultimo and numero_desejado == lista_entrada[primeiro]:
        return primeiro
    elif primeiro == ultimo and numero_desejado != lista_entrada[ultimo]:
        return -1
    elif primeiro != ultimo:
        if numero_desejado == lista_entrada[meio]:
            return meio
        elif numero_desejado < lista_entrada[meio]:
            posicao = buscar_posicao(lista_entrada, numero_desejado, primeiro, meio)
            return posicao
        elif numero_desejado > lista_entrada[meio]:
            posicao = buscar_posicao(lista_entrada, numero_desejado, meio + 1, ultimo)
            return posicao

def main():
    with open('testes/busca_binaria4.in') as arquivo:
        lista1 = arquivo.readline().split()
        numero = arquivo.readline()
    posicao = buscar_posicao(lista1, numero, 0, (len(lista1) -1))
    print(posicao)

main()