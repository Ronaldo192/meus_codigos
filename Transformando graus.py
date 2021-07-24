# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#     C = 5 * ((F-32) / 9).


def grau(numero):
    return 5 * ((numero - 32) / 9)


fahrenheit = float(input('Qual a sua temperatura em Fahrenheit?\n'))
numero = fahrenheit

print(f'Sua temperatura é {grau(numero)} em Celsius.')
