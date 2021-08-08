"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter
14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e
uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o
usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""

def converção (hora, minuto):
    hh = hora / 12
    if hh <= 1:
        print(f'Sua hora é {hora} : {minuto} A.M')
    elif hh > 1 and hh < 2 :
        print(f'Sua hora é {int(hora) - 12} : {minuto} P.M')
    else:
        print("Forma de dado de entrada invalido.")

while True:
    hora = int(input("Qual é a hora?"))
    if hora == 'sair':
        break
    minuto = int(input("Quantos minutos ?"))
    if minuto == 'sair':
        break
    converção(hora, minuto)
    res = input("Se deseja continuar precione 'ENTER', se não desejar continuar digite 'X'")
    res = res.lower()
    if res == 'x':
        break
