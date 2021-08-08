"""
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a
quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

taxaimposto = int(input('taxa'))
custo = float(input('custo'))

def soma_Imposto (taxaimposto = taxaimposto, custo = custo):
    soma = (0.01 * taxaimposto) * custo + custo
    return print(soma)

soma_Imposto()
