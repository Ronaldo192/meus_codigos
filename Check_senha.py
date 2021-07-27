#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
# uma mensagem de erro e voltando a pedir as informações.

usuario = str(input('Nome usuario?\n')) #Faça um programa que leia um nome de usuário e a sua senha
senha = str(input('Digite sua senha!\n'))

while senha == usuario:
    print('Erro 007 # Senha invalida. Tente novamento')
    usuario = str(input('Nome usuario?\n'))
    senha = str(input('Digite sua senha!\n'))
