#Programa que le o comprimento do cateto oposto e do cateto
#adjacente de um triangulo retangulo, calcule e mostre o comprimento da
#hipotenusa

from math import pow, sqrt

CatOp = float(input('Digite o comprimento do cateto oposto: '))
CatAdj = float(input('Digite o comprimento do cateto adjacente: '))

n1 = pow(CatOp, 2)
n2 = pow(CatAdj, 2)
hip = n1 + n2
n3 = sqrt(hip)

print('{}'.format(n3))