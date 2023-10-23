"""
Lê um arquivo chamado palavras.txt e cria outros dois:
- um arquivo plural.txt com as palavras que terminam em s
- um arquivo singular.txt com as demais
"""

def ler_palavras(nome_arquivo):
    """ Lê o arquivo e devolve uma lista das palavras contidas nele"""
    
    """arquivo = open(nome_arquivo)
    palavras = []
    for linha in arquivo:
        palavra = linha.strip()
        palavras.append(palavra)
    arquivo.close()"""
    
    # Significa a mesma coisa que a funçõa acima
    with open(nome_arquivo) as arquivo:
        palavras = []
        for linha in arquivo:
            palavra = linha.strip()
            palavras.append(palavra)
    return palavras

def criar_arquivo_palavras(nome_arquivo, lista_palavras):
    """ Cria um arquivo com nome de nome_arquivo com as palavras de lista_palavras"""
    with open(nome_arquivo, "w") as arquivo:
        for elemento in lista_palavras:
            arquivo.write(elemento)
            arquivo.write("\n")

def separar_plurais(palavras):
    """ Devolve uma lista de palavras terminadas com s"""
    plurais = []
    for palavra in palavras:
        if palavra[-1] == "s":
            plurais.append(palavra)
    return plurais

def calcular_diferenca(lista_palavras, lista_plurais):
    """ Devolve os elementos de lista_palavras que não estão em lista_plurais"""
    diferenca = []
    for valor in lista_palavras:
        if valor not in lista_plurais:
            diferenca.append(valor)
    return diferenca

def main():
    # Lê as palavras do arquivo de entrada
    palavras = ler_palavras("palavras.txt")
    # separar as que terminam em s
    plurais = separar_plurais(palavras)
    # separar as demais
    singulares = calcular_diferenca(palavras, plurais)
    # criar um arquivo plural.txt com as primeiras
    criar_arquivo_palavras("plural.txt", plurais)
    # criar um arquivo singular.txt com as demais
    criar_arquivo_palavras("singular.txt", singulares)

main()