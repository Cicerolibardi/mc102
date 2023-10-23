# lê uma string com três partes
a, b, c = input().split()

# converte strings em números
a = float(a)
b = float(b)
c = float(c)

# termine esse programa aqui...
# sendo "a" o maior lado do triângulo, pode se dizer que caso a² == b² + c² é retângulo
# caso a² < b² + c² esse triângulo é acutângulo e se a² > b² + c² esse triângulo é obtusângulo
# isso não importando a ordem de a, b e c.

lados =[a, b, c]
if lados[0] < lados[1] + lados[2] and lados[1] < lados[0] + lados[2] and lados[2] < lados[1] + lados[0]:
    if lados [0] > lados[1] and lados [0] > lados[2]:
        if lados[0]**2 == lados[1]**2 + lados[2]**2:
            print('retângulo')
        elif lados[0]**2 < lados[1]**2 + lados[2]**2:
            print('acutângulo')
        else:
            print('obtusângulo')
    elif lados[1] > lados[0] and lados[1] > lados[2]:
        if lados[1]**2 == lados[2]**2 + lados[0]**2:
            print('retângulo')
        elif lados[1]**2 < lados[2]**2 + lados[0]**2:
            print('acutângulo')
        else:
            print('obtusângulo')
    else:
        if lados[2]**2 == lados[1]**2 + lados[0]**2:
            print('retângulo')
        elif lados[2]**2 < lados[1]**2 + lados[0]**2:
            print('acutângulo')
        else:
            print('obtusângulo')
else:
    print("não forma triângulo")

# maneira mais extensa
'''lados =[a, b, c]
if lados [0] > lados[1] and lados [0] > lados[2]:
    if lados[0] < lados[1] + lados[2] and lados[1] < lados[0] + lados[2] and lados[2] < lados[1] + lados[0]:
        if lados[0]**2 == lados[1]**2 + lados[2]**2:
            print('retângulo')
        elif lados[0]**2 < lados[1]**2 + lados[2]**2:
            print('acutângulo')
        else:
            print('obtusângulo')
    else:
        print("não forma triângulo")
elif lados[1] > lados[0] and lados[1] > lados[2]:
    if lados[0] < lados[1] + lados[2] and lados[1] < lados[0] + lados[2] and lados[2] < lados[1] + lados[0]:
        if lados[1]**2 == lados[2]**2 + lados[0]**2:
            print('retângulo')
        elif lados[1]**2 < lados[2]**2 + lados[0]**2:
            print('acutângulo')
        else:
            print('obtusângulo')
    else:
        print("não forma triângulo")
else:
    if lados[0] < lados[1] + lados[2] and lados[1] < lados[0] + lados[2] and lados[2] < lados[1] + lados[0]:
        if lados[2]**2 == lados[1]**2 + lados[0]**2:
            print('retângulo')
        elif lados[2]**2 < lados[1]**2 + lados[0]**2:
            print('acutângulo')
        else:
            print('obtusângulo')
    else:
        print("não forma triângulo")'''

# Outra forma de fazer, sendo utilizado o lados.sort() para ordenar os elementos
# da lista "lados" para que assim seja realizado o processo somente uma vez
'''lados = [a, b, c]
lados.sort()
if lados[0] < lados[1] + lados[2] and lados[1] < lados[0] + lados[2] and lados[2] < lados[1] + lados[0]:
    if lados[2]**2 == lados[1]**2 + lados[0]**2:
        print('retângulo')
    elif lados[2]**2 < lados[1]**2 + lados[0]**2:
        print('acutângulo')
    else:
        print('obtusângulo')
else:
    print("não forma triângulo")'''