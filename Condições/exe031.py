#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50  por km para viagens de até 200km
#e R$0,45 para viagens mais longe


dist = float(input('Qual a distância da viagem? '))

if dist <= 200:
    valor1 = dist * 0.50
    print('O valor da sua passagem será de R${}'.format(valor1))
else:
    valor2 = dist * 0.45
    print('O valor da sua passagem sera de R${}'.format(valor2))
