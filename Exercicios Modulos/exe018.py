#Programa que lê um angulo qualquer e mostra na tela o valor do seno, cosseno e tangente
import math
from math import sqrt, sin, cos, tan

ang = float(input('Digite o valor do angulo: '))

n1 = math.cos(ang)
n2 = math.sin(ang)

print("o seno é {} e o cosseno é {}".format(n2, n1))