"""
Escreva um programa que leia uma lista
de números e some a cada um deles um número 1
"""

from util_listas import ler_lista_numeros, imprimir_lista_numeros, incrementar_termo_lista_numeros


def main():
    lista_numeros = ler_lista_numeros()
    incrementar_termo_lista_numeros(lista_numeros, 1)
    imprimir_lista_numeros(lista_numeros)

main()