
import random

def jogar(n):
    '''Joga e devolve o valor ganho'''
    numero_dina = random.randint(1,n)
    
    paguei = 0
    acertou = False
    recebido = 0
    while not acertou:
        chute = int(input('Qual é o seu chute? '))
        if chute == numero_dina:
            recebido = 10
            print(f'Você acertou o {numero_dina}')
            break
        else:
            paguei += 1
            print('Você errou, tente outra vez.')

    return recebido - paguei

def jogar_sacola(n):

    lista_bolas = []
    
    for _ in range(n):
        lista.append(random.randin(1,1000000))
    
    print('Diná, escolha um número entre: ', lista_bolas)

    numero = random.choice(lista_bolas)

    for i in range(n):
        chute = lista[i]
        if chute == numero:



def main():
    n = int(input('Digite o maior número: '))
    ganho = jogar(n)
    print(f"Ganhei {ganho} reais!!!!!!")

main()