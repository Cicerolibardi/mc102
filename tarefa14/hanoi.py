
def achar_quantidade_hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * achar_quantidade_hanoi(n-1) + 1

def main():
    n = int(input())
    numero_movimentos = achar_quantidade_hanoi(n)
    print(numero_movimentos)


main()