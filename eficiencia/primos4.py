import math

def eh_primo(numero):
    '''Devolve True se o número for primo,e, caso não seja, devolve False.'''
    if numero == 0 or numero == 1:
        return False
    
    if numero%2 == 0 and numero > 2:
        return False

    raiz = math.ceil(math.sqrt(numero)) + 1

    for d in range(3,raiz, 2):
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

def contar_crivo_eratostenes(n):
    contador = 0
    riscados = [False] * n

    riscados[0] = True
    riscados[1] = True

    for i in range(n):
        if not riscados[i]:
            contador += 1
            for j in range(2*i, n, i):
                riscados[j] = True
    
    return contador

def main():
    #n = int(input('Digite n: '))
    n = 20000000
    m = contar_crivo_eratostenes(n)
    print(f'Há {m} numeros primeiros entre 0 e {n - 1}')

main()