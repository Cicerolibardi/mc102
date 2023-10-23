from modulo import *


def destacar_bordas(largura, altura, imagem):
    """A partir da largura, altura e a imagem, modifica os valores da imagem que são iguais
    a '1', em que nenhum dos 8 elementos vizinhos (cima, baixo, esquerda, direita e
    as 4 diagonais) seja igual a '0', para '0', retornando a nova imagem modificada."""

    nova_imagem = []
    for m in range(altura):
        lista_provisoria = []
        for n in range(largura):
            lista_provisoria.append(imagem[m][n])
        nova_imagem.append(lista_provisoria)

    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            if ((imagem[i][j] == '1') and ((imagem[i-1][j-1] == '0') or (imagem[i-1][j] == '0') 
                or (imagem[i-1][j+1] == '0') or (imagem[i][j-1] == '0') or (imagem[i][j+1] == '0') 
                or (imagem[i+1][j-1] == '0') or (imagem[i+1][j] == '0') or (imagem[i+1][j+1] == '0'))):
                
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
