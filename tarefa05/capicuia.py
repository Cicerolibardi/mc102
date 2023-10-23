entrada = input()
entradaint = int(entrada)

if entradaint < 100 and entrada[0] == entrada[-1]:
    print('sim')
elif entradaint >= 100 and entradaint < 1000 and entrada[0] == entrada[-1]:
    print('sim')
elif entradaint >= 100 and entradaint < 10000 and entrada[0] == entrada [-1] and entrada[1] == entrada[-2]:
    print('sim')
else:
    print('não')

#ou pode ser feito de tal maneira

"""entrada = input()
if entrada [::-1] == entrada:
    print('sim')
else:
    print('não')"""

