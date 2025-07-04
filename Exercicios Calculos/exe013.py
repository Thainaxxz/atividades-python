#Programa que le o preço de um produto e mostra seu novo preço,
#com 5 % DE DESCONTO

valor  = float(input('Digite o valor do produto (em real): '))
desc = (valor * 5) / 100

final = valor - desc
print('O valor do produto com o desconto de 5% ficará: {:.2f}'.format(final))