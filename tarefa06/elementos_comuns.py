a = input().split()
b = input().split()

lista_comum = []

for i in a:
    if i in b and i not in lista_comum:
        lista_comum.append(i)

for j in lista_comum:
    print(j, end = " ")