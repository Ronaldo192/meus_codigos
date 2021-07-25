# Faça um Programa que leia três números e mostre-os em ordem decrescente.
lista = []

for num in range(3):
    num = int(input(f'Digite um numero {num+1}:\n'))
    lista.append(num)

print(lista)
lista.sort(reverse=True)
