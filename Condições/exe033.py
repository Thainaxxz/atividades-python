#Faça um programa que leia 3 números e diga qual o maior e qual o menor


num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o primeiro numero: '))
num3 = int(input('Digite o primeiro numero: '))

if (num1 > num2) and (num1 > num3):
    print('Maior {}'.format(num1))
elif (num2 > num1) and (num2 > num3):
    print('Maior {}'.format(num2))
else:
    print('Maior {}'.format(num3))
