#escreva um programa que leia um valor em metros
#e exiba convertido em centimetros e milimetros

# 100 centimetros = 1 metros
# 1000 milimetros = 1 metros

metros = float(input('Digite o valor em metros: '))
cm = metros * 100
mm = metros * 1000

print(' {} convertido em centimetros é {} e em milimetros é {} '.format(metros, cm, mm))
