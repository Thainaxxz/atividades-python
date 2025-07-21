#Escreva um programa que faça o computador "pensar" em um número inteiro
#entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador
#O programa devera escrever na tela se o usuario venceu ou perdeu.

import random
num1 = random.randint(0,5)
print(num1)

num2 = int(input('Escolha um número de 0 a 5: '))
if num2 > 5:
    print('Numeros acima de 5 não sao aceitos')
    exit()
if num1 == num2:
    print('Parabens! Você acertou')
else:
    print('Você perdeu :(')

