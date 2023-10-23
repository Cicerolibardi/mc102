def codificar(largura, altura, imagem):
    """Recebe a altura e largura da imagem e a imagem e retorna uma lista com a codificação
    do modo run-length modificado"""
    codificacao = []
    contador_repeticoes_padrao = 0

    for i in range(0, altura, 2):
        for j in range(largura):
            padrao = (imagem[i][j] + imagem[i+1][j])
            if i == 0:
                if j == 0:
                    contador_repeticoes_padrao += 1
                elif j > 0 and (padrao == imagem[i][j-1] + imagem[i+1][j-1]):
                    contador_repeticoes_padrao += 1
                else:
                    codificacao.append(contador_repeticoes_padrao)
                    codificacao.append(imagem[i][j-1] + imagem[i+1][j-1])
                    contador_repeticoes_padrao = 1
            else:
                if j == 0 and (padrao == imagem[i-2][largura-1] + imagem[i-1][largura-1]):
                    contador_repeticoes_padrao += 1
                elif j > 0 and (padrao == imagem[i][j-1] + imagem[i+1][j-1]):
                    contador_repeticoes_padrao += 1
                elif j == 0 and (padrao != imagem[i-2][largura-1] + imagem[i-1][largura-1]):
                    codificacao.append(contador_repeticoes_padrao)
                    codificacao.append(imagem[i-2][largura - 1] + imagem[i-1][largura-1])
                    contador_repeticoes_padrao = 1
                elif j > 0 and (padrao != imagem[i][j-1] + imagem[i+1][j-1]):
                    codificacao.append(contador_repeticoes_padrao)
                    codificacao.append(imagem[i][j-1] + imagem[i+1][j-1])
                    contador_repeticoes_padrao = 1

    codificacao.append(contador_repeticoes_padrao)
    codificacao.append(imagem[altura-2][largura-1] + imagem[altura-1][largura-1])

    return codificacao

def decodificar(largura, altura, codificacao):
    """Recebe a largura e a altura da imagem e uma lista com a codificação no modo run-length
    modificado e retorna uma matriz com a imagem decodificada."""
    imagem = []
    for _ in range(altura):
        imagem.append(list('0' * largura))

    posicao_repeticoes = 0
    posicao_padrao = 1
    contador_repeticoes_padrao = int(codificacao[posicao_repeticoes])

    for i in range(0, altura, 2):
        for j in range(largura):
            imagem[i][j] = codificacao[posicao_padrao][0]
            imagem[i+1][j] = codificacao[posicao_padrao][1]
            contador_repeticoes_padrao -= 1
            if contador_repeticoes_padrao == 0:
                posicao_repeticoes += 2
                posicao_padrao += 2
                if i == altura - 2 and j == largura - 1:
                    return imagem
                
                contador_repeticoes_padrao = int(codificacao[posicao_repeticoes])


def carregar_imagem_codificada(nome_arquivo):
    """A partir do nome do arquivo lê a imagem codificada e retorna a largura, altura
    e a codificação em formato de lista."""
    with open(nome_arquivo) as arquivo:
        formato_do_arquivo = arquivo.readline().strip()
        altura_largura = arquivo.readline().strip().split()
        
        largura = int(altura_largura[0])
        altura = int(altura_largura[1])
        
        codificacao = arquivo.readline().strip().split()
    
    return largura, altura, codificacao

def carregar_imagem_decodificada(nome_arquivo):
    """A partir do nome do arquivo lê a imagem decodificada e retorna a largura, altura
    e a imagem no formato de uma matriz."""
    with open(nome_arquivo) as arquivo:
        formato_do_arquivo = arquivo.readline().strip()
        altura_largura = arquivo.readline().strip().split()
        
        largura = int(altura_largura[0])
        altura = int(altura_largura[1])
        
        imagem = []
        for linha in arquivo:
            lista_linha = list(linha.strip())
            imagem.append(lista_linha)

    return largura, altura, imagem

def escrever_imagem_codificada(largura, altura, lista_codificacao, nome_arquivo):
    """Escreve no arquivo desejado a imagem codificada com o molde desejado"""
    with open(nome_arquivo,"w") as arquivo:
        arquivo.write('P1C''\n')
        arquivo.write(f'{str(largura)} {str(altura)}\n')
        linha_codificada = str()
        for elemento in lista_codificacao:
            linha_codificada += str(elemento) + ' '
        arquivo.write(linha_codificada.strip())
        

def escrever_imagem_decodificada(largura, altura, imagem, nome_arquivo):
    """Escreve no arquivo desejado a imagem decodificada com o molde desejado"""
    with open(nome_arquivo,"w") as arquivo:
        arquivo.write('P1''\n')
        arquivo.write(f'{str(largura)} {str(altura)}\n')
        for linha in imagem:
            for elemento in linha:
                arquivo.write(str(elemento))
            arquivo.write('\n')
