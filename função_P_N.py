"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
 se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""


def nummero(x):
    if x > 0:
        print("P")
    elif x < 0:
        print("N")
    else:
        print("Zero")


nummero(0)
