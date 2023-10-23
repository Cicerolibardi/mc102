n = int(input())
lista = []
for i in range(n):
    numero = float(input())
    lista.append(numero)

notas_maiores = []
for nota in lista:
    if nota >= 5:
        notas_maiores.append(nota)

soma = 0
for nota in notas_maiores:
    soma += nota

media = soma / len(notas_maiores)

print(f'{media:.1f}')
