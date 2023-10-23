"""
Programa que recebe um número
inteiro e decide se ele é um
produto de dois primos

Entrada = n
para cada numero q = 2, 3 ... n-1:
    se n for divisivel por q:
        r = n / q
        verifique se q é primo
        verifique se r é primo
        se ambos forem responda SIM
    se não:
        Respondo NÃO
"""


def eh_primo(numero):
    encontrei_divisor = False
    for i in range(2,numero):
            if numero % i == 0:
                encontrei_divisor = True
                break
    if not encontrei_divisor and numero > 1:     
        numero_eh_primo = True
    else:
        numero_eh_primo = False
    return numero_eh_primo

def eh_composto_especial(n):
    composto_especial = False
    for q in range(2,n):
        if n % q == 0:
            r = n // q
            if eh_primo(r) and eh_primo(q):
                composto_especial = True
                break
    return composto_especial
       
def main():   
    n = int(input('Escreva aqui o número que deseja verificar: '))
    
    if eh_composto_especial(n):
        print(f"{n} é um produto de dois primos")
    else:
        print(f"{n} não é um produto de dois primos")

main()