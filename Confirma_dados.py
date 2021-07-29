"""
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""
nome = input('Qual é o seu nome:\n')

while len(nome) <= 3:
    print('O nome tem que ter nmais de 3 caracteres')
    nome = input('Qual o seu nome?\n')

idade = int(input('Qual a sua idade:\n'))

while idade > 150 or idade < 0:
    print('Algo de errado com sua idade, tente novamente.')
    idade = int(input('Qual a sua idade:\n'))

salario = float(input('Qual seu salario?\n'))

while salario < 1:
    print('Algo de errado com seu salario, tente novamente.')
    salario = float(input('Qual seu salario?\n'))

sexo = input('Digite sexo: [M ou F] \n')

while sexo != "F" and sexo != "f" and sexo != "M" and sexo != "m":
    print('Algo deu errado, tente novamete')
    sexo = str(input('Digite seu sexo: [M ou F]\n'))

estado_civil = input('Qual estdo civil?\n *Casado; \n *Solteiro; \n *Viúvo; \n *Divorciado; \n')
estado_civil = estado_civil[0].lower()

while estado_civil != 'c' and estado_civil != 's' and estado_civil != 'v' and estado_civil != 'd':
    print('Algo deu errado, tente novamente.')
    estado_civil = input('Qual estdo civil?\n')

print(f' Ola {nome}, você tem {idade} anos do sexo {sexo}, seu estado civil é {estado_civil} e teo salário e de  '
      f'R${salario}.\nConfirme por favor que os dados inseridos são verdadeiros digitando "Sim".')
fim = input('Você confirma?\n').lower()

while fim != 'sim':
    nome = input('Qual é o seu nome:\n')
    while len(nome) <= 3:
        print('O nome tem que ter nmais de 3 caracteres')
        nome = input('Qual o seu nome?\n')

    idade = int(input('Qual a sua idade:\n'))

    while idade > 150 or idade < 0:
        print('Algo de errado com sua idade, tente novamente.')
        idade = int(input('Qual a sua idade:\n'))

    salario = float(input('Qual seu salario?\n'))

    while salario < 1:
        print('Algo de errado com seu salario, tente novamente.')
        salario = float(input('Qual seu salario?\n'))

    sexo = input('Digite sexo: [M ou F] \n')

    while sexo != "F" and sexo != "f" and sexo != "M" and sexo != "m":
        print('Algo deu errado, tente novamete')
        sexo = str(input('Digite seu sexo: [M ou F]\n'))

    estado_civil = input('Qual estdo civil?\n *Casado; \n *Solteiro; \n *Viúvo; \n *Divorciado; \n')
    estado_civil = estado_civil[0].lower()

    while estado_civil != 'c' and estado_civil != 's' and estado_civil != 'v' and estado_civil != 'd':
        print('Algo deu errado, tente novamente.')
        estado_civil = input('Qual estdo civil?\n')

    print(f' Ola {nome}, você tem {idade} anos do sexo {sexo}, seu estado civil é {estado_civil} e teo salário e de  '
          f'R${salario}.\nConfirme por favor que os dados inseridos são verdadeiros digotando fim')
    fim = input('Você confirma?').lower()

print('Fim do processo.')
