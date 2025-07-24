#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre
#seu status, de acordo com a tabela abaixo
from queue import PriorityQueue

#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: sobrepeso
#Acima de 40: Obesidade mórbida

#peso / (altura ** 2)

print('---CALCULADORA IMC---')
altura = float(input('\033[1;97mDigite sua altura: '))
peso = float(input('Digite seu peso: \033[m'))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('\033[1;31mAbaixo do peso\033[m')
elif (imc > 18.5) and (imc < 25):
    print('\033[1;32mPeso ideal\033[m')
elif (imc > 25) and (imc < 30):
    print('\033[1;33mSobrepeso\033[m')
elif imc > 40:
    print('\033[1;31mObesidade\033[m')
