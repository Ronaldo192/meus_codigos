# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print(24 * '*')
print(f'{8 * "*"} Medias {8 * "*"}')
print(24 * '*')
nota_1 = float(input('Digite a nota do 1º bimestre\n'))
nota_2 = float(input('Digite a nota do 2º bimestre\n'))
nota_3 = float(input('Digite a nota do 3º bimestre\n'))
nota_4 = float(input('Digite a nota do 4º bimestre\n'))
soma = ((nota_1 + nota_2 + nota_3 + nota_4)/ 4)

print(f'Sua media é {soma}')

if soma >= 7.0:
    print('Parabens você esta aprovado.')
else:print('Quem pena você esta reprovado, tente novamente.')