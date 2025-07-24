#Refazer o exe 35 dos triangulos acrescentando o recurso de mostrar que tipo de triângulo será formado

#equilatero: todos os lados iguais
#isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

#Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas
#podem ou não formar um triângulo



#Para saber se três segmentos de reta podem formar um triângulo, você deve usar a Regra da Desigualdade Triangular, que diz:
#A soma dos comprimentos de dois lados de um triângulo deve ser sempre maior que o comprimento do terceiro lado.
#Ou seja, para três segmentos com medidas
#eles formam um triângulo se e somente se:

#a + b > c
#a + c > b
#b + c > a


retaA = int(input('Digite o comprimento da primeira reta: '))
retaB = int(input('Digite o comprimento da segunda reta: '))
retaC = int(input('Digite o comprimento da terceira reta: '))


if (retaA + retaB > retaC) and (retaA + retaC > retaB) and (retaB + retaC > retaA):
    print('Podem formar um triângulo')
    if retaA == retaB == retaC:
        print('Triângulo equilátero')
    elif (retaA == retaB) or (retaA == retaC) or (retaB == retaA) or (retaB == retaC) or (retaC == retaA) or (retaC == retaB):
        print('Triângulo isósceles')
    elif retaA != retaB != retaC:
        print('Triângulo escaleno')
else:
   print('Não podem formar um triângulo')

