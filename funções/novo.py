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
    imagem_codificada = codificacao.split()
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

from modulo import *


def destacar_bordas(largura, altura, imagem):
    nova_imagem = []
    for linha in imagem:
        inserir_nova_imagem = []
        for elemento in linha:
            inserir_nova_imagem.append(str(elemento))
        nova_imagem.append(inserir_nova_imagem)

    for i in range(altura):
        for j in range(largura):
            if (i == 0) or (i == altura -1):
                nova_imagem[i][j] = imagem[i][j]
            elif (j == 0) or (j == largura - 1):
                nova_imagem[i][j] = imagem[i][j]
            else:
                if imagem[i][j] == '1':
                    fronteira = False
                    for i_linha in range(i-1,i+2):
                        for j_coluna in range(j-1,j+2):
                            if imagem[i_linha][j_coluna] == '0':
                                fronteira = True
                    if fronteira == True:
                        nova_imagem[i][j] = '1'
                    else:
                        nova_imagem[i][j] = '0'

    return nova_imagem

def main():

    arquivo_entrada = input()
    arquivo_saida = input()

    largura, altura, codificacao = carregar_imagem_codificada(arquivo_entrada)
    imagem = decodificar(largura, altura, codificacao)
    nova_imagem = destacar_bordas(largura, altura, imagem)

    codificacao = codificar(largura, altura, nova_imagem)
    escrever_imagem_codificada(largura, altura, codificacao, arquivo_saida)


if __name__ == '__main__':
    main()
