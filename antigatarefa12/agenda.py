import argparse

def adicionar_argumentos():
    """Função que cria os argumentos do parser e devolve eles"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help='inicializador de processos no arquivo que deseja-se criar ou modificar.',
                         required=True)

    parser.add_argument('operacao', help='''operação que deseja-se utilizar, que são: inicializar, criar, alterar,
                        remover e listar.''')

    parser.add_argument('--nome', help='nome do evento que deseja-se criar.')
    parser.add_argument('--descricao', help='descrição do evento de deseja-se criar.')
    parser.add_argument('--data', help='data do evento que deseja-se criar.')
    parser.add_argument('--hora', help='hora do evento que deseja-se criar.')
    parser.add_argument('--evento', help='evento que deseja-se modificar, sendo essa mudança qualquer dos parâmetros.',
                        type=int)

    args = parser.parse_args()
    return args

def ler_arquivo(nome_arquivo, modo_leitura):
    """Lê os dados do arquivo que foi fornecido"""
    with open(nome_arquivo, modo_leitura) as arquivo:
        arquivo_lido = arquivo.readlines()

    return arquivo_lido

def adicionar_evento_agenda(nome_arquivo, modo_escrita, dict_evento, valor_ultimo_evento):
    """Escreve na agenda o novo evento que foi desejado criar"""
    with open(nome_arquivo, modo_escrita) as arquivo:
        arquivo.write(f"evento {valor_ultimo_evento + 1}, {dict_evento['nome']}, {dict_evento['descricao']}, {dict_evento['data']}, {dict_evento['hora']}\n")

def atualizar_contagem(nome_arquivo, valor_ultimo_evento):
    """Atualiza o número do último evento no arquivo numero_eventos.txt"""
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(f'{valor_ultimo_evento + 1}\n')

def escrever_agenda_modificada(nome_arquivo, modo_escrita, lista_evento):
    """Escreve no arquivo a saída, no caso, os eventos da agenda após a operação desejada"""
    with open(nome_arquivo, modo_escrita) as arquivo:
        for elemento in lista_evento:
            arquivo.write(elemento)

def operacao_inicializar(nome_arquivo):
    """Inicializa um arquivo csv com o nome passado ao digitar no terminal e um arquivo txt para a contagem
    do número de eventos em tal agenda"""
    
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write('')

    with open('numero_eventos.txt', 'w') as arquivo:
        arquivo.write('0\n')

def operacao_criar(nome_arquivo, nome, descricao, data, hora, evento):
    """Cria eventos por meio da obtenção dos valores em um dicionário
    e armazena na agenda.csv um evento por linha. Também utiliza um arquivo
    numero_eventos.txt para armazenar o número de eventos que foram criados. Devolve
    o número do evento criado."""

    dict_evento = criar_dicionario(evento, nome, descricao, data, hora)

    arquivo_lido = ler_arquivo('numero_eventos.txt', 'r')
    valor_ultimo_evento = int(arquivo_lido[-1])
    atualizar_contagem('numero_eventos.txt', valor_ultimo_evento)
    adicionar_evento_agenda(nome_arquivo, 'a', dict_evento, valor_ultimo_evento)
    
    return valor_ultimo_evento + 1

def operacao_alterar(nome_arquivo, nome, descricao, data, hora, evento):
    """Recebe como argumento os dados passados no terminal e devolve para o arquivo csv
    a agenda com os fatores alterados. Caso o evento não existe retorna False."""
    dict_evento = criar_dicionario(evento, nome, descricao, data, hora)
    arquivo_lido = ler_arquivo(nome_arquivo, 'r')
    lista_arquivo_modificada = localizar_evento_modificado(nome_arquivo, evento, dict_evento, arquivo_lido)

    if lista_arquivo_modificada == None:
        return False

    escrever_agenda_modificada(nome_arquivo, 'w', lista_arquivo_modificada)

    return dict_evento['evento']

def localizar_evento_modificado(nome_arquivo, evento, dict_evento, arquivo_lido):
    """Recebe o arquivo em formato de listas, e modifica o índice da lista
    correspondente ao evento que foi desejado pelo usuário. Retorna None se o evento não existir"""
    existe = False
    for i, linha in enumerate(arquivo_lido):
        lista_linha = linha.strip().split(', ')
        if lista_linha[0] == f'evento {dict_evento["evento"]}':
            existe = True
            dict_evento_atualizado = modificar_linha_arquivo(dict_evento, lista_linha)
            evento_atualizado = (f"evento {dict_evento_atualizado['evento']}, {dict_evento_atualizado['nome']}, {dict_evento_atualizado['descricao']}, {dict_evento_atualizado['data']}, {dict_evento_atualizado['hora']}"'\n')
            arquivo_lido[i] = evento_atualizado
    
    if not existe:
        print(f'O evento {evento} não pode ser modificado pois ele não existe na {nome_arquivo}.')
        return None
    
    return arquivo_lido 

def modificar_linha_arquivo(dict_evento, lista_linha):
    """Recebe o dicionário de eventos que foi digitado no terminal para operacao_criar e devolve um dicionario
    de eventos que deve substituir na linha que deseja-se modificar o evento."""
    novo_dicionario = dict()
    for elemento in dict_evento:
        novo_dicionario[elemento] = dict_evento[elemento]

    for i, elemento in enumerate(novo_dicionario):
        if novo_dicionario[elemento] == None:
            novo_dicionario[elemento] = lista_linha[i]
    
    return novo_dicionario

def operacao_remover(nome_arquivo, evento):
    """Recebe como argumento os dados passados no terminal e devolve para o arquivo csv
    a agenda com o evento removido. Caso o evento não exista, retorna None."""
    arquivo_lido = ler_arquivo(nome_arquivo, 'r')

    lista_evento_removido = remover_evento(arquivo_lido, nome_arquivo, evento)
    
    escrever_agenda_modificada(nome_arquivo, 'w', lista_evento_removido)

    if lista_evento_removido == None:
        return False
    
    return evento

def remover_evento(lista_arquivo, nome_arquivo, evento):
    """Remove o evento da lista_arquivo caso ele exista e retorna uma lista sem esse evento.
    Caso não exista retorna None"""
    existe = False
    numero_evento = ''
    for i, linha in enumerate(lista_arquivo):
        for letra in linha:
            if letra == ',':
                break
            else:
                numero_evento += letra
        if numero_evento == f'evento {evento}':
            lista_arquivo[i] = ''
            existe = True
            return lista_arquivo
        else:
            numero_evento = ''
    
    if not existe:
        print(f'O evento {evento} não pode ser removido pois ele não existe na {nome_arquivo}.')
        return None

def operacao_listar(nome_arquivo, data):
    """Lista os eventos da data fornecida pelo usuário no terminal. Caso não existam eventos
    para esse dia, escreve-se uma mensagem de não existencia de eventos em tal data."""
    lista_arquivo = ler_arquivo(nome_arquivo, 'r')

    existe = False
    for linha in lista_arquivo:
        lista_linha = linha.split(',')
        if lista_linha[-2].strip() == data:
            if not existe:
                print(f'Eventos do dia {data}')
                print('-' * 47)
            existe = True
            print(f'{lista_linha[0].capitalize()} -{lista_linha[1]}')
            print(f'Descrição:{lista_linha[2]}')
            print(f'Data:{lista_linha[3]}')
            print(f'Hora:{lista_linha[-1]}')
            print('-' * 47)

    if not existe:
        print(f'Não existem eventos para o dia {data}!')

def criar_dicionario(evento, nome, descricao, data, hora):
    """Cria um dicionário de acordo com os argumentos que foram dados no terminal"""
    dicionario = dict()
    
    dicionario['evento']= evento
    dicionario['nome'] = nome
    dicionario['descricao'] = descricao
    dicionario['data'] = data
    dicionario['hora'] = hora

    return dicionario

def chamar_funcoes_operacao(argumentos_terminal):
    '''Chama as funções operacao_(argumentos_terminal.operacao) dependendo do valor
    que foi obtido do valor operacao de argumentos e escreve na tela
    dizendo que a operação foi realizada'''

    if argumentos_terminal.operacao == 'inicializar':
        operacao_inicializar(argumentos_terminal.a)
        print(f'Uma agenda vazia "{argumentos_terminal.a}" foi inicializada com sucesso!')
    
    elif argumentos_terminal.operacao == 'criar':
        evento_criado = operacao_criar(argumentos_terminal.a, argumentos_terminal.nome, argumentos_terminal.descricao, argumentos_terminal.data, argumentos_terminal.hora, argumentos_terminal.evento)
        if evento_criado:
            print(f'O evento {evento_criado} foi adicionado à {argumentos_terminal.a}.')
    
    elif argumentos_terminal.operacao == 'alterar':
        evento_alterado = operacao_alterar(argumentos_terminal.a, argumentos_terminal.nome, argumentos_terminal.descricao, argumentos_terminal.data, argumentos_terminal.hora, argumentos_terminal.evento)
        if evento_alterado != False:
            print(f'O evento {evento_alterado} foi alterado na {argumentos_terminal.a}.')
    
    elif argumentos_terminal.operacao == 'remover':
        evento_removido = operacao_remover(argumentos_terminal.a, argumentos_terminal.evento)
        if evento_removido != False:
            print(f'O evento {evento_removido} foi removido da {argumentos_terminal.a}')
    
    elif argumentos_terminal.operacao == 'listar':
        operacao_listar(argumentos_terminal.a, argumentos_terminal.data)

def main():
    argumentos_terminal = adicionar_argumentos()
    chamada = chamar_funcoes_operacao(argumentos_terminal)

main()