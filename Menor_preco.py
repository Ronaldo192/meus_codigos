#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
# é sempre pelo mais barato.

produto_1 = float(input('Qual o valor do produto "A"?\n'))
produto_2 = float(input('Qual o valor do produto "B"?\n'))
produto_3 = float(input('Qual o valor do produto "C"?\n'))

if  produto_1 < produto_2 and produto_1 < produto_3:
    print('O primeiro Produto digitado é menor.')
elif produto_2 < produto_1 and produto_2 < produto_3:
    print("O segundo produto é menor.")
elif produto_3 < produto_1 and produto_3 < produto_2:
    print("O terceiro produto é menor")
