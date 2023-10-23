def ler_texto_caminho(caminho_arquivo):
    """Lê o texto a partir do caminho dado pelo terminal, retira os caracteres indesejados
    desse texto e transforma as palavras para uma lista com cada elemento sendo uma palavra,
    retornando essa lista."""
    with open(caminho_arquivo) as arquivo:
        texto_sem_pontuacoes = ''
        set_pontuacoes = ({'8', '1', '9',';', '$', '(', '2', '&', '=', '#', '3', ')', '>', '/',
                         '+', '?', ',', '7', ':', "'", '!', '6', '*', '<', '"', '4', '.', '@', 
                         '0', '%', '5', '[', ']'})
        for linha in arquivo:
            for letra in linha:
                letra = letra.lower()
                if letra not in set_pontuacoes:
                    if letra == '\n':
                        texto_sem_pontuacoes += ' '
                    else:
                        texto_sem_pontuacoes += letra
        
    lista_texto = texto_sem_pontuacoes.split()

    return lista_texto

def ler_pares():
    """Lê a entrada e retorna uma lista de tuplas com os pares dados pelo input"""
    lista_tuplas_pares = []
    while True:
        try:
            par = input().split()
            tupla_par = (par[0], par[1])
            lista_tuplas_pares.append(tupla_par)
        except EOFError:
            break

    return lista_tuplas_pares

def identificar_palavras_apos_pares(lista_texto, lista_tuplas_pares):
    """Recebe uma lista com as palavras do texto e uma lista com os pares da entrada em tuplas
    e retorna uma lista com dicionarios com as possíveis sugestões para cada um dos pares."""
    lista_dicionario_pares = []
    for tupla in lista_tuplas_pares:
        dicionario_frequencia_par = dict()
        for i in range(len(lista_texto)):
            if (tupla[0] == lista_texto[i] and tupla[1] == lista_texto[i+1]):
                if lista_texto[i+2] not in dicionario_frequencia_par:
                    dicionario_frequencia_par[lista_texto[i+2]] = 1
                else:
                    dicionario_frequencia_par[lista_texto[i+2]] += 1
        lista_dicionario_pares.append(dicionario_frequencia_par)

    return lista_dicionario_pares
            
def transformar_dict_em_tupla(lista_dicionario_correspondecia_pares):
    """Transforma o dicionário com as possíveis sugestões para os pares da entrada e
    retorna uma lista de lista com tuplas da forma (dicionario[valor], valor)"""
    lista_tuplas_correspondencia_pares = []
    for dicionario in lista_dicionario_correspondecia_pares:
        lista_tupla_par = []
        for valor in dicionario:
            lista_tupla_par.append((dicionario[valor], valor))
        lista_tuplas_correspondencia_pares.append(lista_tupla_par)

    return lista_tuplas_correspondencia_pares

def identificar_sugestao_pares(lista_tuplas_correspondecia_pares):
    """Recebe uma lista de lista de tuplas com as possíveis sugestões para os pares da entrada,
    realiza operações para definir a com maior frequência e menor escala na ordem alfabética e
    retorna uma lista com as palavras sugeridas para cada par."""
    lista_palavras_sugestao = []
    for lista_tupla in lista_tuplas_correspondecia_pares:
        frequencia_sugestao = 0
        sugestao = ''
        for i in range(len(lista_tupla)):
            if lista_tupla[i][0] >= frequencia_sugestao:
                if (((lista_tupla[i][0] == frequencia_sugestao) and lista_tupla[i][1] < sugestao) or
                    lista_tupla[i][0] > frequencia_sugestao):
                    frequencia_sugestao = lista_tupla[i][0]
                    sugestao = lista_tupla[i][1]
        
        lista_palavras_sugestao.append(sugestao)

    return lista_palavras_sugestao

def escrever_saida(lista_palavras_sugestao, lista_tuplas_pares):
    """Escreve a saída do modo desejado pelo problema."""
    for i in range(len(lista_tuplas_pares)):
        print(f'{lista_tuplas_pares[i][0]} {lista_tuplas_pares[i][1]} {lista_palavras_sugestao[i]}')

def main():
    caminho_arquivo = input()
    lista_tuplas_pares = ler_pares()
    lista_texto = ler_texto_caminho(caminho_arquivo)
    lista_dicionario_correspondecia_pares = identificar_palavras_apos_pares(lista_texto, lista_tuplas_pares)
    lista_tuplas_correspondecia_pares = transformar_dict_em_tupla(lista_dicionario_correspondecia_pares)
    lista_palavras_sugestao = identificar_sugestao_pares(lista_tuplas_correspondecia_pares)
    escrever_saida(lista_palavras_sugestao, lista_tuplas_pares)

main()