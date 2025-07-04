#programa que leia a largura e a altura de uma parede em metros
#calcule a sua area e a quantidade de tinta necessaria
#sabendo que cada litro de tinta pinta uma area de 2m²

larg = float(input('Qual a altura da parede (em metros)? '))
alt = float(input('Qual a largura da parece (em metros)? '))

total = larg * alt
tinta = total / 2
print('Será necessário {:.0f} litros de tinta'.format(tinta))