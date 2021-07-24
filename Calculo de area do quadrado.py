# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

base = float(input('Qual o tamanho da sua base do seu quadrado.\n'))
altura = float(input('Qual o tamanho a altura do seu quadrado.\n'))


def area():
    return base * altura * 2


print(f'Sua area é {base * altura}\n')
print(f'O dobro da sua area é {area()}.')


