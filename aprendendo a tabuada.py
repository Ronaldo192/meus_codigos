from random import randint

valor = int(input('Digite o número para gerar a tabuada.\nR:'))
valor2 = randint(0, 10)

print(f'Antes de gerar a tabuada você tem que acertar esta pergunta: {valor} x {valor2}')
soma = valor * valor2
aux = soma
resultado = int(input("Qual a dua resposta\nR:"))

if resultado == soma:
    print('Parabens você acertou')
else:print(f"Que pena você errou, a resposta correta é {soma}, sua tabuada esta abaixo.")


aux = 1
print('X' * 18)
print(f'Tabuada de {valor}')
print('X' * 18)

while(aux <= 10):
    print(f'{aux} x {valor} = {aux * valor}')
    #print('{0} x {1} = {2}'.format(aux, valor, (aux * valor)))
    aux = aux + 1