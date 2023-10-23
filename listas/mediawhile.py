n = int(input())
lista = []
i = 0
while i < n:
    numero = float(input())
    i += 1
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