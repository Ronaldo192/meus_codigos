#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra.\nR:")).lower()

if letra == 'a':
    print('Vogal')
if letra == 'e':
    print('Vogal')
if letra == 'i':
    print('Vogal')
if letra == 'o':
    print('Vogal')
if letra == 'u':
    print('Vogal')
elif letra == '':
    print('Digite uma letra por favor.'
          '')
else:print('Consoalte')

print('Fim!')