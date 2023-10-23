def eh_primo(primo):
    encontrei_divisor = False
    for i in range(2,primo):
        if primo % i == 0:
            encontrei_divisor = True
            break
    if not encontrei_divisor and primo > 1:
        numero_eh_primo = True
    else:
        numero_eh_primo = False
    return numero_eh_primo

def eh_numero_composto(n):
    eh_composto = False
    for q in range(2, n):
        if n % q == 0:
            r = n // q
            if eh_primo(q) and eh_primo(r):
                eh_composto = True
                break
    return eh_composto

def main():
    n = int(input())

    if eh_numero_composto(n):
        print(f"O número {n} é um número composto especial")
    else:
        print(f"O número {n} não é um número composto especial")

main()