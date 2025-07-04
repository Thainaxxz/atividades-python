#crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dolares ela pode comprar
#valor do dolar atual 5.41 Brazilian Real

real = float(input('Quanto voçe tem em real brasileiro? '))


if real < 5.41:
    print('Você não tem dinheiro suficiente' )
    exit()
else:
    us = real / 5.41
    print('Então você tem U${:.2f}'.format(us))
