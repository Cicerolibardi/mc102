"""
Escreva um programa que leia a nota de 10
exercícios de 3 alunos:

a) calcule a média da TURMA de cada exercício
b) descubra o exercício com menor média
c) calcule a média de cada ALUNO, excluindo-se o exercício de menor média
"""

NUMERO_EXERCICIOS = 10
NUMERO_ALUNOS = 3

def ler_notas_exercicios(n):
    """Lê uma n de 10 números e devolve"""
    lista = []
    for _ in range(n):
        lista.append(float(input()))
    return lista

def ler_notas_alunos(m):
    """Lê a lista de notas de cada aluno e devolve"""
    pass

def calcular_media_aluno(notas, idx):
    """Calcula a média de um aluno excluindo a nota de índice idx"""
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

def calcular_media_dos_exercicios(notas_alunos):
    pass

def calcular_media_turma():
    pass

def main():
    notas_turma = ler_notas_alunos(NUMERO_ALUNOS)
    media_exercicios = calcular_media_dos_exercicios(notas_alunos)
    idx_pior_exercicio = obter_pior_exercício(medias_exercicios)
    media_turma = calcular_medias_turma()

main()
