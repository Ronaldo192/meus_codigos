# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

numero = int(input('Qual a nota do seu dia de zero a dez?\n'))

while numero > 10:
    print('Valor é invalido, tente novamente.')
    numero = int(input('Qual a nota do seu dia de zero a dez?\n'))
    numero = numero + 0
print('fim do processo')
