"""
Exercício 7. Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de
uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes
valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor
de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa
deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
Para calcular os juros compostos, utiliza-se a expressão:

M = C (1+i)t

Onde,

M: montante
C: capital
i: taxa fixa
t: período de tempo
"""

def valorPagamento(valor_prestação, dias_atraso):
    if dias_atraso == 0:
        print(f'Sua parcela é de R$ {valor_prestação}.')
    elif dias_atraso > 0:
        soma_1 = valor_prestação * 1.03
        soma_2 = valor_prestação * (1.01 ** dias_atraso)
        res = (soma_1 - valor_prestação) + soma_2
        return print(f'O total a pagar é R$ {round(res,2)}.')




valor_prestação = float(input('Valor da Prestação\n='))
dias_atraso = int(input('Quantos dias de atraso?\n='))

valorPagamento(valor_prestação, dias_atraso)
