#Escreva um programa que leia dois números inteiros e compare-os
#Mostrando na tela uma mensagem

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O número {} é maior que o {}'.format(num1, num2))
elif num1 < num2:
    print('O número {} é menor que o {}'.format(num1, num2))
elif num1 == num2:
    print('O número {} é igual ao número {}'.format(num1, num2))

