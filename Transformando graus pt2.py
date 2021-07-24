# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = C x 1,8 + 32

print('=' * 36)
celsius = float(input('Qual a sua temperatura em Celsius?\n R:'))
celsius = celsius * 1.8 + 32
print('=' * 36)
print(f'\nR: Sua temperatura em é {celsius} Fahrenheit.\n ')
print(('=' * 14), 'FIM', ('=' * 14))
