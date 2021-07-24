"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""
nome = input('Qual é o seu nome?\nR:')
altura = float(input('Qual a sua altura?\nR:'))
peso = float(input('Qual é o seu peso?\nR:'))
sexo = input('Qual é o seu sexo, F ou H ?\nR:')

if sexo in sexo == "H":
    print(f'Ola {nome} seu IMC é {peso / (altura * 2)}')
else:
    print(f'Ola {nome.capitalize()} seu IMC é {peso / (altura * 2)}')
