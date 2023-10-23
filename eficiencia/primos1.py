"""
Mostra e conta todos os números primos de 0 até n - 1, com n lido do teclado.
"""
def eh_primo(numero):
    '''Devolve True se o número for primo,e, caso não seja, devolve False.'''
    if numero == 0 or numero == 1:
        return False
    for d in range(2,numero):
        if numero%d == 0:
            return False
    else:
        return True

def contar_primos(n):
    '''Mostra na tela todos os números primos de 0 até n-1
    e devolve o número de primos que foram mostrados'''
    m = 0
    for i in range(n):
        if eh_primo(i):
            print(i)
            m += 1
    return m

def main():
    #n = int(input('Digite n: '))
    n = 40000
    m = contar_primos(n)
    print(f'Há {m} numeros primeiros entre 0 e {n - 1}')

main()