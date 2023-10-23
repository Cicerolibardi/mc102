"""
Escreva um programa que leia uma lista
de números e some a cada um deles um número 5
"""

import util_listas

def main():
    lista_numeros = util_listas.ler_lista_numeros()
    util_listas.incrementar_termo_lista_numeros(lista_numeros, 5)
    util_listas.imprimir_lista_numeros(lista_numeros)

main()