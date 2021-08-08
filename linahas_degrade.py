"""
Faça um programa para imprimir:

        1
        2   2
        3   3   3
        .....
        n   n   n   n   n   n  ... n

    para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.


linhas(4)
"""



def linhas(n):
    for i in range(n):
        i += 1
        return print(str(i) * i)

linhas(6)


