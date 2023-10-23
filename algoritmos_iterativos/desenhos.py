def absoluto(valor):
    if valor < 0:
        return -valor
    else:
        return valor

def desenhar_disco():
    raio = 10
    for linha in range(1,21):
        num_espaco = absoluto(10 - linha)
        num_asteriscos = (10 - num_espaco)*2 -1
        str_espaco = " " *  num_espaco
        str_asteriscos = "*" * num_asteriscos
        print(str_espaco, end="")
        print(str_asteriscos, end="")
        print()

def esta_no_disco(i, j, n):
    return i**2 + j**2 <= 3**2

def desenhar_disco2():
    for i in range(-7, 8):
        for j in range(-7, 8):
            no_disco = esta_no_disco(i,j)
            if no_disco:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def main():
    desenhar_disco2()

main()