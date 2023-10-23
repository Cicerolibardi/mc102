def codificar(largura, altura, imagem):
    codificacao = []
    contagem_vezes = 0
    for i in range(0, altura,2):
        for j in range(largura):
            padrao = str(imagem[i][j]) + str(imagem[i+1][j])
            if j == 0 and i == 0:
                contagem_vezes += 1
            elif j > 0 and (padrao == str(imagem[i][j-1]) + str(imagem[i+1][j-1])):
                contagem_vezes += 1
            elif j == 0 and i >= 2 and (padrao == str(imagem[i-2][largura-1]) + str(imagem[i-1][largura-1])):
                contagem_vezes += 1
            elif padrao != (str(imagem[i][j-1]) + str(imagem[i+1][j-1])):
                codificacao.append(contagem_vezes)
                codificacao.append(str(imagem[i][j-1]) + str(imagem[i+1][j-1]))
                contagem_vezes = 0
                contagem_vezes += 1
            elif j == 0 and i >= 2 and (padrao != str(imagem[i-2][largura-1]) + str(imagem[i-1][largura-1])):
                codificacao.append(contagem_vezes)
                codificacao.append(str(imagem[i-2][largura - 1]) + str(imagem[i-1][largura -1]))
                contagem_vezes = 0
                contagem_vezes += 1
    
    codificacao.append(contagem_vezes)
    codificacao.append(str(imagem[altura-2][largura-1]) + str(imagem[altura-2][largura-1]))
    return codificacao
    
def decodificar(largura, altura, codificacao):
    imagem_codificada = codificacao
    imagem = []
    for _ in range(altura):
        imagem.append(list('0' * largura))
    
    incremento_fator = 0
    incremento_linhas = 1
    fator_adicao = int(imagem_codificada[incremento_fator])

    for i in range(0, altura, 2):
        for j in range(largura):
            linha_impar = int(imagem_codificada[incremento_linhas][0])
            linha_par = int(imagem_codificada[incremento_linhas][1])
            
            imagem[i][j] = linha_impar
            imagem[i+1][j] = linha_par
            fator_adicao = fator_adicao - 1

            if fator_adicao == 0:
                if (i == altura -2) and (j == largura -1):
                    return imagem
                else:
                    incremento_fator += 2
                    incremento_linhas += 2
                    fator_adicao = int(imagem_codificada[incremento_fator])

def carregar_imagem_codificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        tipo_arquivo = arquivo.readline().strip()
        dimensoes = arquivo.readline().strip().split()
        
        largura = int(dimensoes[0])
        altura = int(dimensoes[1])
        codificacao = arquivo.readline().strip()

    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        tipo_arquivo = arquivo.readline().strip()
        dimensoes = arquivo.readline().strip().split()
        largura = int(dimensoes[0])
        altura = int(dimensoes[1])
        
        imagem = []
        for linha in arquivo:
            linha_imagem = list(linha.strip())
            imagem.append(linha_imagem)
    
    return largura, altura, imagem


def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    with open(nome_do_arquivo,"w") as arquivo:
        arquivo.write('P1C''\n')
        arquivo.write(str(largura) + ' ' + str(altura) +'\n')
        linha_codificada = ''
        for elemento in codificacao:
            linha_codificada += str(elemento) + ' '
        arquivo.write(linha_codificada.strip())
        

def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo,"w") as arquivo:
        arquivo.write('P1''\n')
        arquivo.write(str(largura) + ' ' + str(altura) + '\n')
        for linha in imagem:
            for indice in range(len(linha)):
                arquivo.write(str(linha[indice]))
            arquivo.write('\n')
