def receber_tarefas_e_notas():
    """Função que recebe as tarefas e as respectivas notas das tarefas
    e devolve uma matriz de notas e tarefas relacionadas
    """

    tarefas_e_notas = input().split()
    matriz = []
    elemento = 0
    while elemento < len(tarefas_e_notas):
        notas_agrupadas = [tarefas_e_notas[elemento], tarefas_e_notas[elemento + 1]]
        matriz.append(notas_agrupadas)
        elemento += 2
    return matriz

def listar_presenca():
    """Função que recebe os valores das presenças
    e retorna em uma saída com uma lista desses valores
    """
    lista_presenca = []
    while True:
        try:
            presenca = input()
            if presenca != "":    
                lista_presenca.append(presenca)
        except EOFError:
            break
    return lista_presenca

def aprovacao_por_nota(matriz_notas):
    """Verifica na lista de notas se há alguma nota "D"
    assim, devolvendo uma saída verdadeira se não houver nenhuma
    e falsa
    """
    for lista in matriz_notas:
        for nota in lista[1]:
            if nota == "D": 
                return False
    return True

def aprovacao_por_presenca(lista_presenca):
    """Faz a contagem de vezes que presente está na lista de presença
    e após isso faz a verificação se essa frequência é maior do que 75%,
    devolvendo verdadeiro se for maior e falso se for menor.
    """
    contador = 0
    for elemento in lista_presenca:
        if elemento == "presente":
            contador += 1

    if (contador/ len(lista_presenca)) >= 0.75:
        return True
    else:
        return False

def aprovado_no_total(aprovado_nota, aprovado_presenca):
    """Recebe os parâmetros se foi aprovado por nota e por presença,
    assim, se for aprovado por ambos, esse aluno estará aprovadx na disciplina.
    Se reprovar em algum dos dois ou em ambas as "aprovações", esse aluno está
    reprovadx na disciplina.
    """
    if aprovado_nota and aprovado_presenca:
        print("Aprovadx")
    else:
        print("Reprovadx")

def main():
    matriz_notas = receber_tarefas_e_notas()
    lista_presenca = listar_presenca()
    aprovado_nota = aprovacao_por_nota(matriz_notas)
    aprovado_presenca = aprovacao_por_presenca(lista_presenca)
    aprovado_no_total(aprovado_nota, aprovado_presenca)

main()