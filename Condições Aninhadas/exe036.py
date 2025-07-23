#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
#ou então o empréstimo será negado

casa = float(input('Digite o valor da casa que você deseja comprar: '))
sal = float(input('Digite o valor do seu salário mensal: '))
parc = float(input('Em quantos anos você pretende pagar? '))

soma1 = casa / parc
soma2 = (sal * 30) / 100

if soma1 <= soma2:
    print('\033[0;32mEmpréstimo aprovado')
else:
    print('\033[0;31mEmpréstimo negado')