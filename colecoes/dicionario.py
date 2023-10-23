def criar_dicionario():
    '''
    Cria um dicionário vazio
    '''
    return []

def adicionar_verbete(dicionario, verbete):
    '''adiciona um novo verbete ao dicionário'''
    idx = procurar_indice(dicionario, verbete[0])
    if idx is None:    
        dicionario.append(verbete)
    else:
        raise Exception(f'Palavra verbete{verbete[0]} já existe')

def procurar_verbete(dicionario, palavra):
    '''procura um verbete no dicionario ou none de a palavra não existir no dicionario'''
    for verbete in dicionario:
        if verbete[0] == palavra:
            return verbete
    return None

def atualizar_verbete(dicionario, verbete_atualizado):
    '''altera o verbete correspondente a uma palavra'''
    idx = procurar_indice(dicionario, verbete_atualizado[0])
    dicionario[idx] = verbete_atualizado

def procurar_indice(dicionario, palavra):
    '''Devolve o índice de uma palavra no dicionário'''
    idx = None
    for i, verbete in enumerate(dicionario):
        if verbete[0] == palavra:
            idx = i
            break
    return idx

def atualizar_definicao(dicionario, palavra, nova_definicao):
    """Atualiza a definição de uma palavra"""
    idx = procurar_indice(dicionario, palavra)
    verbete_anterior = dicionario[idx]
    verbete_atualizado = (palavra, nova_definicao, verbete_anterior[2])
    dicionario[idx] = verbete_atualizado

def main():
    # o dicionarista é o autor da função main()
    # ele vai criar e operar sobre o dicionário

    # criar um dicionário
    dicionario = criar_dicionario()
    verbete = ('amor', 'é fogo que arde sem se ver', 1540)
    adicionar_verbete(dicionario, verbete)
    verbete2 = ('arder','é algo que doi pra caramba', 2039)
    adicionar_verbete(dicionario, verbete2)
    fogo = procurar_verbete(dicionario, 'fogo')
    if fogo is None:
        print("A palavra fogo não está no dicionário")
    else:
        print(f'Fogo significa {fogo[1]}')
    palavra, definicao, ano = procurar_verbete(dicionario, 'arder')
    print(f'{palavra} significa {definicao}')
    nova_definicao = input('O que você acha que é o amor?\n')
    verbete_atualizado = (verbete[0], nova_definicao, verbete[2])
    atualizar_verbete(dicionario, verbete_atualizado)
    atualizar_definicao(dicionario, palavra, nova_definicao)
    palavra, definicao, ano = procurar_verbete(dicionario, 'amor')
    print(f'{palavra} significa {definicao}')
main()