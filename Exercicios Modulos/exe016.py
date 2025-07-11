#Programa que ler um número real qualquer pelo teclado e mostra
#na tela a sua porção inteira

from math import ceil, trunc

n1 = float(input('Digite um numero: '))

print('A parte inteira de {} é {}'.format(n1, trunc(n1) ))