frase1 = input().split()
frase2 = input().split()

for i in range(len(frase1)):
    frase3 = frase1[i] + frase2[i]
    print(frase3, end = " ")