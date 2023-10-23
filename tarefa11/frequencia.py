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

def retirar_stopwords_texto(lista_texto, lista_stopwords):
    """Retira as stopwords da lista do texto a partir de uma lista das stopwords
    que deseja-se retirar e retorna esse texto sem stopwords."""
    set_stopwords = transformar_lista_set(lista_stopwords)
    lista_texto_sem_stopwords = []
    for elemento in lista_texto:
        if elemento not in set_stopwords:
            lista_texto_sem_stopwords.append(elemento)
    
    return lista_texto_sem_stopwords

def transformar_lista_set(lista_stopwords):
    """A partir da lista de stopwords, transforma ela em um set com os
    mesmos stopwords e retorna esse set."""
    set_stopwords = set()
    for elemento in lista_stopwords:
        set_stopwords.add(elemento)

    return set_stopwords

def obter_frequencia_palavras(lista_texto_sem_stopwords):
    """A partir do texto filtrado, sem stopwords e pontuações indesejadas, cria-se
    um dicionário com a frequência de cada uma dessas palavras e retorna esse dict."""
    dict_frequencia_palavras = dict()
    for elemento in lista_texto_sem_stopwords:
        if elemento not in dict_frequencia_palavras:
            dict_frequencia_palavras[elemento] = 1
        else:
            dict_frequencia_palavras[elemento] += 1
    
    return dict_frequencia_palavras

def obter_tres_palavras_mais_frequentes(dict_frequencia_palavras):
    """A partir do dicionario da frequencia das palavras, realiza operações e retorna
    uma lista com tuplas da forma(dicionario[valor],valor) e também retorna uma lista
    com as três palavras mais frequentes. """
    lista_tuplas = []
    for valor in dict_frequencia_palavras:
        lista_tuplas.append((dict_frequencia_palavras[valor], valor))
    lista_tuplas_ordenada = sorted(lista_tuplas)

    lista_tres_mais_frequentes = []
    for quantidade_maiores_quartil in range(3):
        valor_palavra = 0
        for i, tupla in enumerate(lista_tuplas_ordenada):
            if tupla[0] > valor_palavra:
                valor_palavra = tupla[0]
                indice_tupla = i
        lista_tres_mais_frequentes.append(lista_tuplas_ordenada[indice_tupla][1])
        lista_tuplas_ordenada.pop(indice_tupla)

    return lista_tuplas, lista_tres_mais_frequentes

def obter_quantidade_maiores_quartil(lista_tuplas):
    """A partir da lista de tuplas, retorna a quantidade de tuplas com o primeiro
    elemento maior do que o primeiro elemento do primeiro quartil"""
    lista_tuplas.sort(reverse=True)

    lista_maiores_cinco = []
    for tupla in lista_tuplas:
        if tupla[0] >= 5:
            lista_maiores_cinco.append(tupla)
    
    i_quartil = (len(lista_maiores_cinco))//4 - 1

    quantidade_maiores_quartil = 0
    for tupla in lista_maiores_cinco:
        if (tupla[0] >= lista_maiores_cinco[i_quartil][0]):
            quantidade_maiores_quartil += 1
    
    return quantidade_maiores_quartil

def obter_frequentes_nao_incluidas(lista_tuplas, quantidade_maiores_quartil):
    """Obtém, a partir da lista de tuplas e da quantidade de tuplas com frequência
    maior que a do quartil as três palavras frequentes que não foram incluidas na
    contagem do quartil."""

    lista_tuplas.sort()
    frequencia_quartil = lista_tuplas[-quantidade_maiores_quartil][0]
    lista_tres_nao_incluidas = []
    for _ in range(3):    
        contador_frequencia = 0
        for i, tupla in enumerate(lista_tuplas):
            if tupla[0] > contador_frequencia and tupla[0] < frequencia_quartil:
                contador_frequencia = lista_tuplas[i][0]
                indice_tupla = i

        lista_tres_nao_incluidas.append(lista_tuplas[indice_tupla][1])
        lista_tuplas.pop(indice_tupla)

    return lista_tres_nao_incluidas

def escrever_saida(lista_tres_palavras_mais_frequentes, quantidade_maiores_quartil, tres_frequentes_nao_incluidas):
    """Escreve a saída do modo desejado pelo problema."""
    print(' '.join(lista_tres_palavras_mais_frequentes))
    print(quantidade_maiores_quartil)
    print(' '.join(tres_frequentes_nao_incluidas))

def main():
    caminho_arquivo = input()
    lista_stopwords = input().split()
    lista_texto = ler_texto_caminho(caminho_arquivo)
    lista_texto_sem_stopwords = retirar_stopwords_texto(lista_texto, lista_stopwords)
    dict_frequencia_palavras = obter_frequencia_palavras(lista_texto_sem_stopwords)
    lista_tuplas, lista_tres_palavras_mais_frequentes=obter_tres_palavras_mais_frequentes(dict_frequencia_palavras)
    quantidade_maiores_quartil = obter_quantidade_maiores_quartil(lista_tuplas)
    tres_frequentes_nao_incluidas = obter_frequentes_nao_incluidas(lista_tuplas, quantidade_maiores_quartil)
    escrever_saida(lista_tres_palavras_mais_frequentes, quantidade_maiores_quartil, tres_frequentes_nao_incluidas)

main()