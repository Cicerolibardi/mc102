def criar_dicionario():
    '''
    Cria um dicionário vazio
    '''
    return []

def adicionar_verbete(dicionario, verbete):
    '''adiciona um novo verbete ao dicionário'''

    palavra = verbete["palavra"]
    idx = procurar_indice(dicionario, palavra)
    if idx is None:    
        dicionario.append(verbete)
    else:
        raise Exception(f'Palavra verbete{palavra} já existe')

def procurar_verbete(dicionario, palavra):
    '''procura um verbete no dicionario ou none de a palavra não existir no dicionario'''
    for verbete in dicionario:
        if verbete['palavra'] == palavra:
            return verbete
    return None

def atualizar_verbete(dicionario, verbete_atualizado):
    '''altera o verbete correspondente a uma palavra'''
    idx = procurar_indice(dicionario, verbete_atualizado['palavra'])
    dicionario[idx] = verbete_atualizado

def procurar_indice(dicionario, palavra):
    '''Devolve o índice de uma palavra no dicionário'''
    idx = None
    for i, verbete in enumerate(dicionario):
        if verbete['palavra'] == palavra:
            idx = i
            break
    return idx

def atualizar_definicao(dicionario, palavra, nova_definicao):
    """Atualiza a definição de uma palavra"""
    idx = procurar_indice(dicionario, palavra)
    verbete_anterior = dicionario[idx]
    verbete_atualizado = {
        'palavra': verbete_anterior['palavra'],
        'classe': verbete_anterior['classe'],
        'definicao': nova_definicao,
        'ano': verbete_anterior['ano']
    }
    dicionario[idx] = verbete_atualizado

def main():
    # o dicionarista é o autor da função main()
    # ele vai criar e operar sobre o dicionário

    # criar um dicionário
    dicionario = criar_dicionario()
    verbete = {
        'palavra': 'amor', 
        'definicao':'é fogo que arde sem se ver', 
        'classe': 'substantivo',
        'ano': 1540
        }
    adicionar_verbete(dicionario, verbete)
    fogo = procurar_verbete(dicionario, 'fogo')
    if fogo is None:
        print("A palavra fogo não está no dicionário")
    else:
        print(f'Fogo significa {fogo[1]}')
    palavra, classe, definicao, ano = procurar_verbete(dicionario, 'arder')
    print(f"{verbete['palavra']} significa {verbete['definicao']}")
    nova_definicao = input('O que você acha que é o amor?\n')
    verbete_atualizado = (verbete[0], nova_definicao, verbete[2])
    atualizar_verbete(dicionario, verbete_atualizado)
    atualizar_definicao(dicionario, palavra, nova_definicao)
    palavra, definicao, ano = procurar_verbete(dicionario, 'amor')
    print(f'{palavra} significa {definicao}')
main()