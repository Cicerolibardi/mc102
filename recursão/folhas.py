def descobrir_tipo(w_folha, h_folha, tipo_folha, w_retangulo, h_retangulo):
    """Devolve o tipo da menor folha em que cabe o retângulo ou None se não couber."""
    if w_retangulo > w_folha or h_retangulo > h_folha:  #se o retângulo não cabe na folha
        return None

    else: #se o retângulo cabe, caso geral
        #achar o caso menor
        w_menor = h_folha // 2
        h_menor = w_folha
        tipo_menor = tipo_folha + 1

        #chamar recursivamente
        tipo_minimo_menor = descobrir_tipo(w_menor, h_menor, tipo_menor, w_retangulo, h_retangulo)

        #combinar a resposta da recursão
        if tipo_minimo_menor is None:
            return tipo_folha
        else:
            return tipo_minimo_menor


def main():
    w_retangulo = int(input("Digite a largura do retângulo: "))
    h_retangulo = int(input("Digite a altura do retângulo: "))

    tipo = descobrir_tipo(841, 1189, 0, w_retangulo, h_retangulo)

    print(f'Utilize um papel do tipo A{tipo}.')

main()