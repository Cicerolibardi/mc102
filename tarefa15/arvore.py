from modulo import *
import re

def receber_html(link_atual):
    """Recebe o link atual que deseja-se obter o html e retorna uma
    lista com esses urls"""
    
    str_html = obter_html(link_atual)
    regex = r'href="(.*?)"'
    lista_url = re.findall(regex, str_html)

    return lista_url

def validar_itens_lista_url(lista_url, url_raiz, url_base):
    """Recebe uma lista de urls com suas strings sem href=" e devolve uma lista
    os urls váidos para a árvore"""

    lista_validos = []
    for i in range(len(lista_url)):
        url_resolvido_parcial = resolver_url(lista_url[i], url_base)
        if eh_url_valida(url_resolvido_parcial, url_raiz):
            lista_validos.append(lista_url[i])
    
    return lista_validos

def obter_e_escrever_arvore(url_raiz, link_atual, url_base, espacamento_atual='', lista_arvore=[]):
    """Recebe o url_raiz, o link atual e o url_base e escreve na tela o link com sua
    respectiva indentação na árvore."""

    lista_url = receber_html(link_atual)
    lista_validos = validar_itens_lista_url(lista_url, url_raiz, url_base)

    if link_atual not in lista_arvore:
        print(espacamento_atual + link_atual)
        espacamento_atual += '  '
        lista_arvore.append(link_atual)
        for i in range(len(lista_validos)):
            url_resolvida = resolver_url(lista_validos[i], link_atual)
            if len(lista_validos) > 0 and url_resolvida not in lista_arvore:
                (obter_e_escrever_arvore(url_raiz, url_resolvida, link_atual,
                 espacamento_atual, lista_arvore))

def main():
    url_raiz = input()
    obter_e_escrever_arvore(url_raiz, url_raiz, url_raiz)

main()