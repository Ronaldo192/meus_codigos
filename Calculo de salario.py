#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

hora_dia = float(input('Qual o valor da sua hora?\nR: '))
hora_mes = float(input('Quantas horas você trabalha por mês?\nR:'))


print(f'Este mês seu salario vai ser R$ {hora_dia * hora_mes}')