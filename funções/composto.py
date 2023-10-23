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

n = int(input())
composto_especial = False
for q in range(2,n):
    if n % q == 0:
        r = n // q

        encontrei_divisor = False
        for i in range(2,q):
            if q % i == 0:
                encontrei_divisor = True
                break

        if not encontrei_divisor and q > 1:
            q_eh_primo = True
        else:
            q_eh_primo = False
        
        encontrei_divisor = False
        for i in range(2,r):
            if r % i == 0:
                encontrei_divisor = True
                break

        if not encontrei_divisor and r > 1:
            r_eh_primo = True
        else:
            r_eh_primo = False
        
        if q_eh_primo and r_eh_primo:
            composto_especial = True
            break

if composto_especial:
    print(f"{n} é um produto de dois primos")  
else:
    print(f"{n} não é um produto de dois primos")