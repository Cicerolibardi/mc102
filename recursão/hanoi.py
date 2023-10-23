
def hanoi(n, origem, auxiliar, destino):
    """Mostra as instruções para mover n discos de origem até o destino, usando auxiliar como apoio."""
    if n > 0:
        hanoi(n-1, origem, destino, auxiliar)
        print(f'mova 1 disco de {origem} para {destino}')
        hanoi(n-1, auxiliar, origem, destino)

def main():
    n = int(input('Digite o valor de n: '))
    hanoi(n, 'A', 'B', 'C')

main()