#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('Qual sua prefência sexual? Escolha uma das opções:\n* F = Feminino;\n* M = Masculino \n* S/I = Sexo Indefinido\nR:')).upper()
print(sexo)

if sexo == "F":
    print('Sua preferência é pessoas do sexo feminino.')
elif sexo == "M":
    print('Sua preferência é pessoas do sexo masculino')
else:print('Sua opção de sexo é indefinida.')