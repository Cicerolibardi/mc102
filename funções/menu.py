#vamos proibir o uso de math e o de **
#import math

#criando função sqrt
def minha_sqrt(radiando):
    """recebe um número pelo argumento radiando
    e devolve a raiz quadrada de radiando"""
    raiz = radiando / 2
    return raiz 

def operacao_raiz_cubica():
    pass

def operacao_soma():
    num1 = int(input())
    num2 = int(input())
    soma = num1 + num2
    print(soma)

def operacao_diferenca():
    num1 = int(input())
    num2 = int(input())
    diferenca = num1 - num2
    print(diferenca)

def operacao_produto():
    num1 = int(input())
    num2 = int(input())
    produto = num1 * num2
    print(produto)

def operacao_raiz():
    num1 = int(input())
    raiz = int(minha_sqrt(num1))
    print(raiz)

def main():
    while True:
        operador = input()
        if operador == "+":
            operacao_soma()
        elif operador == "-":
            operacao_diferenca()
        elif operador == "*":
            operacao_produto()
        elif operador == "raiz":
            operacao_raiz()
        elif operador == "cubica":
            operacao_raiz_cubica()
        elif operador == "F":
            break
        else:
            print("Operação inválida")

main()
