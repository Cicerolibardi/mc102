def filtra(lista_operar, funcao_aplicar):
    """Percorre todos os elementos da lista e de acordo com o retorno booleano de
    funcao_aplicar filtra essa lista, para devolver uma lista com os casos em que 
    esse valor booleano seja True."""
    lista_primos = []
    for i in range(len(lista_operar)):
        condicao = funcao_aplicar(lista_operar[i])
        if condicao == True:
            lista_primos.append(lista_operar[i])

    return lista_primos

def mapear(lista_operar, funcao_aplicar):
    """Aplica a uma lista a funcao 'funcao_aplicar' e retorna a lista com a função aplicada
    a todos os elementos da lista inicial."""
    lista_operar = [funcao_aplicar(elemento) for elemento in lista_operar]

    return lista_operar

def reduz(lista_operar, funcao_aplicar):
    """Aplica a função 'funcao_aplicar' na lista e retorna o valor da operação
    feita pela funcao_aplicar"""
    valor_reduzido = 0
    if len(lista_operar) > 0:
        for i in range(len(lista_operar)):
            valor_reduzido = funcao_aplicar(valor_reduzido, lista_operar[i])
    
    return valor_reduzido

def eh_primo(valor):
    """Verifica se o valor é primo. Caso seja, retorna True e caso não, retorna False"""
    primo = False

    if valor == 1:
        return primo

    elif valor > 1:
        for i in range(2, valor):
            if valor % i == 0:
                return primo
    
    return not primo


def potenciacao(elemento):
    """Retorna o quadrado do elemento"""
    return elemento * elemento

def somar(a, b):
    """Soma os elementos a e b e retorna a soma"""
    return a + b

def main():
    lista_entrada = input().split()
    lista_entrada = mapear(lista_entrada, int)

    lista_filtrada = filtra(lista_entrada, eh_primo)
    lista_mapeada = mapear(lista_filtrada, potenciacao)
    valor_reduzido = reduz(lista_mapeada, somar)
    print(valor_reduzido)

main()