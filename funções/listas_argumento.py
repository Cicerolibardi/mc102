"""
Escrever um programa que leia uma
lista de notas e devolva as notas
com um bônus de 20%
"""
def ler_lista_notas():
    """Pede que o usuário escreva uma lista de notas"""
    
    n = int(input("Quantos estudantes há? "))
    print("Digite a nota dos estudantes: ")
    lista_notas = []
    for _ in range(n):
        nota = float(input())
        lista_notas.append(nota)
    return lista_notas

def multiplica_lista_fator(lista, fator):
    """multiplica a lista de notas por um fator"""
    
    n = len(lista)
    for i in range(n):
        lista[i] *= fator


def imprimir_lista(lista):
    """imprime a lista na tela"""
    
    for indice, numero in enumerate(lista):
        print(f"O estudante {indice} tem nota {numero}")

def main():
    lista_notas = ler_lista_notas()
    multiplica_lista_fator(lista_notas, 1.2)
    imprimir_lista(lista_notas)

main()