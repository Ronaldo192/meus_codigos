"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.

"""
print(f'PROGRAMA DE CALCULOS\n')

num_1 = int(input('Digite o 1º numero inteiro.\n- '))
num_2 = int(input('Digite o 2º numero inteiro.\n-'))
num_3 = float(input('Digite o 3º numero inteiro.\n-'))
print('\n')

print(f'O produto do dobro do primeiro com metade do segundo é \nR- {(num_1 * 2) + (num_2 / 2)} \n')

print('A soma do triplo do primeiro com o terceiro é.')

soma_2 = num_1 * 3 + num_3

if soma_2 % int(soma_2) == 0:
    print('R-', int(soma_2))
else:
    print('R-', soma_2)
print('\n')
print(f'O terceiro elevado ao cubo é. \nR-{num_3 ** 3}')
print('\n' + '***' * 10)