"""
Escreva um programa que leia a nota de 10
exercícios e calcule a média dos 9 exercícios
com maiores notas.
"""

NUMERO_ALUNOS = 10

def ler_notas(n):
    """Lê uma n de 10 números e devolve"""
    lista = []
    for _ in range(n):
        lista.append(float(input()))
    return lista

def calcular_media(notas, idx):
    """Calcula a média excluindo a nota de índice idx"""
    soma = 0.0
    for i, nota in enumerate(notas):
        if i != idx:
            soma += nota
    media = soma / (len(notas) - 1)
    return media

def obter_pior_exercício(notas):
    """Devolve o índice da pior nota"""
    idx_menor = 0
    menor_nota = notas[0]
    for i, nota in enumerate(notas):
        if nota < menor_nota:
            menor_nota = nota
            idx_menor = i
    return idx_menor

def main():
    notas = ler_notas(NUMERO_ALUNOS)
    pior_exercicio = obter_pior_exercício(notas)
    media = calcular_media(notas, pior_exercicio)
    print(f"A média é {media}")

main()