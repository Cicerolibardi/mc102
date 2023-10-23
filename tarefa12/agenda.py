import argparse

def adicionar_argumentos():
    """Função que cria os argumentos do parser e devolve eles"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help='inicializador de processos no arquivo que deseja-se criar ou modificar.',
                         required=True)

    parser.add_argument('operacao', help='''operação que deseja-se utilizar, que são: inicializar, criar, alterar,
                        remover e listar.''')

    parser.add_argument('--nome', help='nome do evento que deseja-se criar.', default = "")
    parser.add_argument('--descricao', help='descrição do evento de deseja-se criar.', default = "")
    parser.add_argument('--data', help='data do evento que deseja-se criar.', default = "")
    parser.add_argument('--hora', help='hora do evento que deseja-se criar.', default = "")
    parser.add_argument('--evento', help='evento que deseja-se modificar, sendo essa mudança qualquer dos parâmetros.')

    args = parser.parse_args()
    return args

def atualizar_contagem(valor_ultimo_evento):
    """Atualiza o número do último evento no arquivo numero_eventos.txt"""
    with open(".numero_eventos.txt", 'a') as arquivo:
        arquivo.write(f'{valor_ultimo_evento + 1}\n')

def ler_arquivo_csv(nome_do_arquivo):
    """Lê o arquivo.csv dado pelo nome_do_arquivo e devolve uma lista
    com dicionário das informações contidas no arquivo"""
    agenda = []
    with open(nome_do_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha_lida = linha.strip().split(',')
            evento, nome, descricao = linha_lida[0], linha_lida[1], linha_lida[2]
            data, hora = linha_lida[3], linha_lida[4]
            dict_evento = {"evento": evento, "nome": nome, "descricao": descricao, "data": data, "hora": hora}
            agenda.append(dict_evento)

    return agenda

def identificar_ultimo_evento():
    """Lê o arquivo que contabiliza os eventos e retorna o último evento criado"""
    with open(".numero_eventos.txt", 'r') as arquivo:
        eventos = arquivo.readlines()
    
    return int(eventos[-1])

def escrever_arquivo_csv(nome_arquivo, agenda):
    with open(nome_arquivo, "w") as arquivo:
        for evento in agenda:
            arquivo.write(f'{evento["evento"]},{evento["nome"]},{evento["descricao"]},{evento["data"]},{evento["hora"]}\n')

def operacao_inicializar(nome_arquivo):
    """Inicializa um arquivo csv com o nome passado ao digitar no terminal e um arquivo txt para a contagem
    do número de eventos em tal agenda"""
    
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write('')

    with open('.numero_eventos.txt', 'w') as arquivo:
        arquivo.write('0\n')

def operacao_criar(nome_arquivo, nome, descricao, data, hora):
    """Cria um evento no nome_arquivo com os parâmetros nome, descrição, data, hora
    e evento."""
    lista_dict_eventos = ler_arquivo_csv(nome_arquivo)
    ultimo_evento = identificar_ultimo_evento()
    atualizar_contagem(ultimo_evento)
    evento_criado = {"evento": ultimo_evento + 1, "nome": nome, "descricao": descricao, "data": data, "hora": hora}
    lista_dict_eventos.append(evento_criado)
    escrever_arquivo_csv(nome_arquivo, lista_dict_eventos)

    return ultimo_evento + 1

def operacao_alterar(nome_arquivo, nome, descricao, data, hora, evento):
    """Altera um evento no nome_arquivo com os parâmetros que foram dados pelo terminal, caso esse
    evento exista."""
    lista_dict_eventos = ler_arquivo_csv(nome_arquivo)
    i_evento = None
    for i, dicionario in enumerate(lista_dict_eventos):
        if dicionario["evento"] == evento:
            i_evento = i
            break
    if i_evento is None:
        return None

    if nome != "":
        lista_dict_eventos[i_evento]["nome"] = nome
    if descricao != "":
        lista_dict_eventos[i_evento]["descricao"] = descricao
    if data != "":
        lista_dict_eventos[i_evento]["data"] = data
    if hora != "":
        lista_dict_eventos[i_evento]["hora"] = hora
    
    escrever_arquivo_csv(nome_arquivo, lista_dict_eventos)
    
    return True
    
def operacao_remover(nome_arquivo, evento):
    """Remove o evento desejado no arquivo nome_arquivo, caso ele exista."""
    lista_dict_eventos = ler_arquivo_csv(nome_arquivo)
    i_evento = None
    for i, dicionario in enumerate(lista_dict_eventos):
        if dicionario["evento"] == evento:
            i_evento = i

    lista_dict_eventos.pop(i_evento)
    escrever_arquivo_csv(nome_arquivo, lista_dict_eventos)

    return i_evento

def operacao_listar(nome_arquivo, data):
    """Lista os eventos existentes no arquivo nome_arquivo na data passada pelo temrinal, para caso existam
    eventos nessa data."""
    lista_dict_eventos = ler_arquivo_csv(nome_arquivo)
    contador = 0
    if len(lista_dict_eventos) > 0:
        for evento in lista_dict_eventos:
            if evento["data"] == data:
                if contador == 0:
                    print(f'Eventos do dia {data}')
                    print('-' * 47)
                print(f'Evento {evento["evento"]} - {evento["nome"]}')
                print(f'Descrição: {evento["descricao"]}')
                print(f'Data: {evento["data"]}')
                print(f'Hora: {evento["hora"]}')
                print('-' * 47)
                contador += 1 
    if contador == 0:
        print(f'Não existem eventos para o dia {data}!')

def identificar_evento_a_realizar(argumentos_terminal):
    """Chama as funções operacao_(argumentos_terminal.operacao) dependendo do valor
    que foi obtido do valor operacao de argumentos e escreve na tela
    dizendo que a operação foi realizada"""

    if argumentos_terminal.operacao == 'inicializar':
        operacao_inicializar(argumentos_terminal.a)
        print(f'Uma agenda vazia "{argumentos_terminal.a}" foi inicializada com sucesso!')
    
    elif argumentos_terminal.operacao == 'criar':
        evento_criado = operacao_criar(argumentos_terminal.a, argumentos_terminal.nome, argumentos_terminal.descricao, argumentos_terminal.data, argumentos_terminal.hora)
        print(f'O evento {evento_criado} foi adicionado à {argumentos_terminal.a}.')
    
    elif argumentos_terminal.operacao == 'alterar':
        alteracao = operacao_alterar(argumentos_terminal.a, argumentos_terminal.nome, argumentos_terminal.descricao, argumentos_terminal.data, argumentos_terminal.hora, argumentos_terminal.evento)
        if alteracao is None:
            print(f"Não existe o evento {argumentos_terminal.evento} na {argumentos_terminal.a}.")
        else:
            print(f'O evento {argumentos_terminal.evento} foi alterado na {argumentos_terminal.a}.')
    
    elif argumentos_terminal.operacao == 'remover':
        evento_removido = operacao_remover(argumentos_terminal.a, argumentos_terminal.evento)
        if evento_removido is None:
            print(f"Não existe o evento {argumentos_terminal.evento} na {argumentos_terminal.a}.")
        else:
            print(f'O evento {evento_removido} foi removido da {argumentos_terminal.a}')
    
    elif argumentos_terminal.operacao == 'listar':
        operacao_listar(argumentos_terminal.a, argumentos_terminal.data)

def main():
    argumentos_terminal = adicionar_argumentos()
    chamada = identificar_evento_a_realizar(argumentos_terminal)

main()