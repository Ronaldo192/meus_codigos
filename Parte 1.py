""""
# Print Ola mundo na tela.
print("Ola mundo")


# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = input('Digite um numero!\n')
print(f'O numero que você digitou foi {numero}')


# Faça um Programa que peça dois números e imprima a soma.
num1 = int(input('Digite o 1º numero\n'))
num2 = int(input('Digite o 2º numero \n'))

print(f" O resultado é { num1 + num2}")


# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota_1 = float(input('Digite a nota do 1º bimestre\n'))
nota_2 = float(input('Digite a nota do 2º bimestre\n'))
nota_3 = float(input('Digite a nota do 3º bimestre\n'))
nota_4 = float(input('Digite a nota do 4º bimestre\n'))


print(f' Sua media é {(nota_1 + nota_2 + nota_3 + nota_4) / 4}')


# Faça um Programa que converta metros para centímetros.

media_metros = float(input('Digite a sua medida em metros\n'))

print(f'Sua medida em centímetor é {media_metros * 100} cm.')


# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input('Qual o raio do seu circulo\n'))
print(f'Sua aréa é de {raio ** 2 * 3.14}')

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

base = float(input('Diga o tamanho da sua base do seu quadrado.\n'))
altura = float(input('Digite o tamanho a altura do seu quadrado.\n'))


def area():
    return base * altura * 2


print(f'Sua area é {base * altura}\n')
print(f'O dobro da sua area é {area()}.')


#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.

hora_dia = float(input('Qual o valor da dua hora?\nR: '))
hora_mes = float(input('Quantas horas você trabalha por mês?\nR:'))


print(f'Este mês seu salario vai ser R$ {hora_dia * hora_mes}')


# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#     C = 5 * ((F-32) / 9).


def grau(numero):
    return 5 * ((numero - 32) / 9)


fahrenheit = float(input('Qual a sua temperatura em Fahrenheit?\n'))
numero = fahrenheit

print(f'Sua temperatura é {grau(numero)} em Celsius\n')

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = C x 1,8 + 32

print('=' * 36)
celsius = float(input('Qual a sua temperatura em Celsius?\n R:'))
celsius = celsius * 1.8 + 32
print('=' * 36)
print(f'\nR: Sua temperatura em é {celsius} Fahrenheit.\n ')
print(('=' * 14), 'FIM', ('=' * 14))



Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. 
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
print('*FIM*' * 10)
    


Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 


"""""


