# Faça um Programa que leia três números e mostre o maior e o menor deles

num1 = int(input('Digite o primeiro numero.\n'))
num2 = int(input('Digite o segundo numero.\n'))
num3 = int(input('Digite o terceiro numero.\n'))

if num1 > num2 and num1 > num3:
    print('O primeiro numero digitado é maior.')
elif num2 > num1 and num2 > num3:
    print("O segundo numero é maior.")
elif num3 > num2 and num3 > num1:
    print("O terceiro numero é maior")

if num1 < num2 and num1 < num3:
    print('O primeiro numero digitado é menor.')
elif num2 < num1 and num2 < num3:
    print("O segundo numero é menor.")
elif num3 < num1 and num3 < num2:
    print("O terceiro numero é menor")
