def calcular_mmc(a, b, mdc):    
   
   return int(a/mdc) * b

def calcular_mdc(a, b):
    if a < b:
        return calcular_mdc(b,a)
    if b == 0:
        return a
    resto = a % b
    return calcular_mdc(b, resto)

def main():
    entrada = input().split()
    a = int(entrada[0])
    b = int(entrada[1])
    mdc = calcular_mdc(a, b)
    mmc = calcular_mmc(a, b, mdc)
    print(int(mmc))

main()